package allinsts_query

import (
	ctp "ctpapi"
	"fmt"
	gl "global"
	"log"
	"time"
)

func (conf *ATConfig) init() {
	conf.tradeFront = conf.Port_config.TradePort
	conf.quoteFront = conf.Port_config.MarketPort
	conf.brokerID = conf.User_config.BrokerID
	conf.userID = conf.User_config.UserID
	conf.password = conf.User_config.Password
	conf.appID = conf.User_config.AppID
	conf.authCode = conf.User_config.AuthCode
}

func (T *ATConfig) QryInstsInfo2() (map[string]InstrumentsUseField, []string) {
	T.init()

	// 声明trade对象
	T.t = ctp.InitTrade()
	// 注册spi
	T.t.RegisterSpi()
	// 生成前台端口byte
	bTradeFront := []byte(T.tradeFront)
	// 注册前台端口
	T.t.RegisterFront(bTradeFront)
	// 订阅
	T.t.SubscribePrivateTopic(ctp.THOST_TERT_RESUME)
	T.t.SubscribePublicTopic(ctp.THOST_TERT_RESUME)
	T.t.Init()

	T.login_record = make(map[string]bool, 0)

	// 前台连接相应(前台连接成功后进行认证)
	T.t.OnFrontConnected(func() {
		fmt.Println("OnFrontConnected")
		T.login_record["OnFrontConnected"] = true

		// 声明认证对象结构体
		pReqAuthenticateField := ctp.CThostFtdcReqAuthenticateField{}
		copy(pReqAuthenticateField.BrokerID[:], []byte(T.brokerID))
		copy(pReqAuthenticateField.UserID[:], []byte(T.userID))
		copy(pReqAuthenticateField.AppID[:], []byte(T.appID))
		copy(pReqAuthenticateField.AuthCode[:], []byte(T.authCode))
		// 发送认证请求
		nRequestID := 0
		for i := 0; T.t.ReqAuthenticate(&pReqAuthenticateField, nRequestID) != 0; i++ {
			fmt.Println("Retry ReqAuthenticate:", i)
			nRequestID += 1
			time.Sleep(1 * time.Second)
		}
	})

	// 等待认证响应接收（认证成功后进行登录）
	T.t.OnRspAuthenticate(func(pRspAuthenticateField *ctp.CThostFtdcRspAuthenticateField, pRspInfo *ctp.CThostFtdcRspInfoField, nRequestID int, bIsLast bool) {
		fmt.Println("OnRspAuthenticate:", ctp.Bytes2String(pRspInfo.ErrorMsg[:]))
		if ctp.Bytes2String(pRspInfo.ErrorMsg[:]) == "正确" {
			T.login_record["OnRspAuthenticate"] = true
		}

		// 声明用户认证结构体
		pReqUserLoginField := ctp.CThostFtdcReqUserLoginField{}
		copy(pReqUserLoginField.BrokerID[:], []byte(T.brokerID))
		copy(pReqUserLoginField.UserID[:], []byte(T.userID))
		copy(pReqUserLoginField.Password[:], []byte(T.password))
		// length := ctp.TThostFtdcSystemInfoLenType(273)

		// 用户登录请求
		nRequestID = 0
		for i := 0; T.t.ReqUserLogin(&pReqUserLoginField, nRequestID) != 0; i++ {
			fmt.Println("Retry ReqUserLogin:", i)
			nRequestID += 1
			time.Sleep(1 * time.Second)
		}

	})

	// 等待用于登录响应接收（登录成功后确认每日结算）
	T.t.OnRspUserLogin(func(pRspUserLogin *ctp.CThostFtdcRspUserLoginField, pRspInfo *ctp.CThostFtdcRspInfoField, nRequestID int, bIsLast bool) {
		fmt.Println("OnRspUserLogin:", ctp.Bytes2String(pRspInfo.ErrorMsg[:]))
		if ctp.Bytes2String(pRspInfo.ErrorMsg[:]) == "正确" {
			T.login_record["OnRspUserLogin"] = true
		}

		// 结算确认
		pSettlementInfoConfirm := ctp.CThostFtdcSettlementInfoConfirmField{}
		copy(pSettlementInfoConfirm.BrokerID[:], []byte(T.brokerID))
		copy(pSettlementInfoConfirm.InvestorID[:], []byte(T.userID))
		nRequestID = 0
		T.t.ReqSettlementInfoConfirm(&pSettlementInfoConfirm, nRequestID)
	})

	// 等待用于每日结算接受
	T.t.OnRspSettlementInfoConfirm(func(pSettlementInfoConfirm *ctp.CThostFtdcSettlementInfoConfirmField, pRspInfo *ctp.CThostFtdcRspInfoField, nRequestID int, bIsLast bool) {
		fmt.Println("OnRspSettlementInfoConfirm", ctp.Bytes2String(pRspInfo.ErrorMsg[:]))
		if ctp.Bytes2String(pRspInfo.ErrorMsg[:]) == "正确" {
			T.login_record["OnRspSettlementInfoConfirm"] = true
		}
	})

	// 等待用户结算响应
	T.waitForBackward("OnRspSettlementInfoConfirm")

	// 寻找合约对应交易所
	// T.insId_ExchangeId = T.getInsidExchange()
	log.Println("登陆成功")
	return T.GetIns()

}

func (T *ATConfig) waitForBackward(back string) {
	for !T.login_record[back] {
		time.Sleep(time.Second * 1)
	}
}

func (T *ATConfig) GetIns() (map[string]InstrumentsUseField, []string) {
	InstrumentsInfoN := make(map[string]InstrumentsUseField, 0)
	InstrumentsInfoV := make(map[string]InstrumentsUseField, 0)
	wait := make(chan bool, 2)
	contFlag := make(chan bool, 2)

	// 超时设置
	go func() {
		time.Sleep(time.Hour)
		wait <- true
		contFlag <- true
	}()

	// 声明合约响应函数
	T.t.OnRspQryInstrument(func(pInstrument *ctp.CThostFtdcInstrumentField, pRspInfo *ctp.CThostFtdcRspInfoField, nRequestID int, bIsLast bool) {
		if pInstrument.ProductClass == ctp.THOST_FTDC_PC_Futures {
			InstrumentsInfoN[ctp.Bytes2String(pInstrument.InstrumentID[:])] =
				InstrumentsUseField{
					InstrumentID:      ctp.Bytes2String(pInstrument.InstrumentID[:]),
					ExchangeID:        ctp.Bytes2String(pInstrument.ExchangeID[:]),
					ExchangeInstID:    ctp.Bytes2String(pInstrument.ExchangeInstID[:]),
					ProductID:         ctp.Bytes2String(pInstrument.ProductID[:]),
					UnderlyingInstrID: ctp.Bytes2String(pInstrument.UnderlyingInstrID[:]),
				}
			// fmt.Println(ctp.Bytes2String(pInstrument.InstrumentID[:]))
		}
		// fmt.Println(bIsLast)
		if bIsLast {
			wait <- true
		}
	})

	// 声明深度响应函数
	T.t.OnRspQryDepthMarketData(func(pDepthMarketData *ctp.CThostFtdcDepthMarketDataField, pRspInfo *ctp.CThostFtdcRspInfoField, nRequestID int, bIsLast bool) {
		InstrumentsInfoV[ctp.Bytes2String(pDepthMarketData.InstrumentID[:])] =
			InstrumentsUseField{
				InstrumentID:    ctp.Bytes2String(pDepthMarketData.InstrumentID[:]),
				ExchangeID:      ctp.Bytes2String(pDepthMarketData.ExchangeID[:]),
				Volume:          float64(pDepthMarketData.Volume),
				Turnover:        float64(pDepthMarketData.Turnover),
				OpenInterest:    float64(pDepthMarketData.OpenInterest),
				PreOpenInterest: float64(pDepthMarketData.PreOpenInterest),
			}
		if bIsLast {
			contFlag <- true
		}
	})

	// 订阅合约
	pQryInstrument := ctp.CThostFtdcQryInstrumentField{}
	nRequestID := 0
	repn := T.t.ReqQryInstrument(&pQryInstrument, gl.ReqID(&nRequestID))
	for i := 0; repn != 0; i++ {
		log.Println("Retry ReqQryInstrument:", i)
		time.Sleep(time.Second)
		repn = T.t.ReqQryInstrument(&pQryInstrument, gl.ReqID(&nRequestID))
	}

	if <-wait {
		fmt.Println("合约获取完成")
	}

	pQryDepthMarketData := ctp.CThostFtdcQryDepthMarketDataField{}
	repin := T.t.ReqQryDepthMarketData(&pQryDepthMarketData, gl.ReqID(&nRequestID))
	for i := 0; repin != 0; i++ {
		log.Println(repin, "Retry ReqQryDepthMarketData:", i)
		if i == -1 {
			time.Sleep(time.Second)
		} else {
			time.Sleep(time.Second * 30) //如果请求此处过多或者有未处理完的请求则等待30s
		}
		repin = T.t.ReqQryDepthMarketData(&pQryDepthMarketData, gl.ReqID(&nRequestID))
	}

	if <-contFlag {
		fmt.Println("深度获取完成")
	}

	InstsPrdMap := make(map[string][]InstrumentsUseField, 0)

	for _, v := range InstrumentsInfoN {
		tmpInsts := InstrumentsInfoN[v.InstrumentID]
		tmpInsts.ExchangeID = InstrumentsInfoV[v.InstrumentID].ExchangeID
		tmpInsts.PreOpenInterest = InstrumentsInfoV[v.InstrumentID].PreOpenInterest
		tmpInsts.Volume = InstrumentsInfoV[v.InstrumentID].Volume
		tmpInsts.Turnover = InstrumentsInfoV[v.InstrumentID].Turnover
		tmpInsts.OpenInterest = InstrumentsInfoV[v.InstrumentID].OpenInterest
		InstrumentsInfoN[v.InstrumentID] = tmpInsts
		InstsPrdMap[v.ProductID] = append(InstsPrdMap[v.ProductID], tmpInsts)
	}

	T.t.Release()

	for idx, val := range InstsPrdMap {
		if len(val) > 2 {
			InstsPrdMap[idx] = sortoi(val)[:2]
		}
	}
	InstrumentsInfoList := make([]string, 0)
	for _, v := range InstsPrdMap {
		for _, k := range v {
			InstrumentsInfoList = append(InstrumentsInfoList, k.InstrumentID)
		}
	}
	return InstrumentsInfoN, InstrumentsInfoList
}
