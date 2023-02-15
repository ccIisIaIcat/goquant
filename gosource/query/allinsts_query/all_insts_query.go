package allinsts_query

import (
	ctp "ctpapi"
	gl "global"
	"log"
	"time"
)

type InstrumentsUseField struct {
	InstrumentID      string
	ExchangeID        string
	ExchangeInstID    string
	ProductID         string
	UnderlyingInstrID string
	Volume            float64
	Turnover          float64
	OpenInterest      float64
	PreOpenInterest   float64
}

type ATConfig struct {
	// Public
	User_config gl.ConfigUser
	Port_config gl.ConfigPort

	// Private
	tradeFront string
	quoteFront string
	brokerID   string
	userID     string
	password   string
	appID      string
	authCode   string

	t            *ctp.Trade
	login_record map[string]bool // 用于判断登录回执是否齐全
}

func sortoi(inst_arr []InstrumentsUseField) []InstrumentsUseField {
	for i := range inst_arr {
		for j := i + 1; j < len(inst_arr); j++ {
			if inst_arr[j].PreOpenInterest > inst_arr[i].PreOpenInterest {
				tmpi := inst_arr[i]
				inst_arr[i] = inst_arr[j]
				inst_arr[j] = tmpi
			}
		}
	}
	return inst_arr
}

func (conf *ATConfig) QryInstsInfo() (map[string]InstrumentsUseField, []string) {
	conf.tradeFront = conf.Port_config.TradePort
	conf.quoteFront = conf.Port_config.MarketPort
	conf.brokerID = conf.User_config.BrokerID
	conf.userID = conf.User_config.UserID
	conf.password = conf.User_config.Password
	conf.appID = conf.User_config.AppID
	conf.authCode = conf.User_config.AuthCode
	const REQSLEEP = 1 * time.Second
	// Instrument Info
	// var InstrumentsInfo sync.Map
	// InstrumentsInfo := make(map[string]InstrumentsUseField, 0)
	InstrumentsInfoN := make(map[string]InstrumentsUseField, 0)
	InstrumentsInfoV := make(map[string]InstrumentsUseField, 0)
	clogin := make(chan bool)
	wait := make(chan bool)
	contFlag := make(chan bool)
	nRequestID := 0
	repn := int32(0)

	// Init: Create Api and Spi
	t := ctp.InitTrade()
	// Register Spi
	t.RegisterSpi()
	bTradeFront := []byte(conf.tradeFront)
	// Register Front
	t.RegisterFront(bTradeFront)
	// Subscribe
	t.SubscribePrivateTopic(ctp.THOST_TERT_RESUME)
	t.SubscribePublicTopic(ctp.THOST_TERT_RESUME)
	t.Init()

	// Front connected
	t.OnFrontConnected(func() {
		log.Println("Trade OnFrontConnected:", conf.tradeFront)
		// Auth
		pReqAuthenticateField := ctp.CThostFtdcReqAuthenticateField{}
		copy(pReqAuthenticateField.BrokerID[:], []byte(conf.brokerID))
		copy(pReqAuthenticateField.UserID[:], []byte(conf.userID))
		copy(pReqAuthenticateField.AppID[:], []byte(conf.appID))
		copy(pReqAuthenticateField.AuthCode[:], []byte(conf.authCode))
		repn = t.ReqAuthenticate(&pReqAuthenticateField, gl.ReqID(&nRequestID))
		for i := 0; repn != 0; i++ {
			log.Println(repn, "Retry ReqAuthenticate:", i)
			time.Sleep(REQSLEEP)
			repn = t.ReqAuthenticate(&pReqAuthenticateField, gl.ReqID(&nRequestID))
		}
	})
	// Response Authenticate
	t.OnRspAuthenticate(func(pRspAuthenticateField *ctp.CThostFtdcRspAuthenticateField, pRspInfo *ctp.CThostFtdcRspInfoField, nRequestID int, bIsLast bool) {
		log.Println("Trade OnRspAuthenticate:", ctp.Bytes2String(pRspInfo.ErrorMsg[:]))

		// Login
		pReqUserLoginField := ctp.CThostFtdcReqUserLoginField{}
		copy(pReqUserLoginField.BrokerID[:], []byte(conf.brokerID))
		copy(pReqUserLoginField.UserID[:], []byte(conf.userID))
		copy(pReqUserLoginField.Password[:], []byte(conf.password))
		length := ctp.TThostFtdcSystemInfoLenType(273)
		systemInfo := ctp.TThostFtdcClientSystemInfoType{}
		repn = t.CTP_GetSystemInfo(&systemInfo, length)
		log.Println("Get System Return:", repn)
		repn = t.ReqUserLogin(&pReqUserLoginField, gl.ReqID(&nRequestID))
		for i := 0; repn != 0; i++ {
			log.Println(repn, "Retry ReqUserLogin:", i)
			time.Sleep(REQSLEEP)
			repn = t.ReqUserLogin(&pReqUserLoginField, gl.ReqID(&nRequestID))
		}
	})

	// Response UserLogin
	t.OnRspUserLogin(func(pRspUserLogin *ctp.CThostFtdcRspUserLoginField, pRspInfo *ctp.CThostFtdcRspInfoField, nRequestID int, bIsLast bool) {
		log.Println("Trade OnRspUserLogin:", ctp.Bytes2String(pRspInfo.ErrorMsg[:]))
		clogin <- true
	})

	// Response Qryinfo
	t.OnRspQryInstrument(func(pInstrument *ctp.CThostFtdcInstrumentField, pRspInfo *ctp.CThostFtdcRspInfoField, nRequestID int, bIsLast bool) {
		if pInstrument.ProductClass == ctp.THOST_FTDC_PC_Futures {
			InstrumentsInfoN[ctp.Bytes2String(pInstrument.InstrumentID[:])] =
				InstrumentsUseField{
					InstrumentID:      ctp.Bytes2String(pInstrument.InstrumentID[:]),
					ExchangeID:        ctp.Bytes2String(pInstrument.ExchangeID[:]),
					ExchangeInstID:    ctp.Bytes2String(pInstrument.ExchangeInstID[:]),
					ProductID:         ctp.Bytes2String(pInstrument.ProductID[:]),
					UnderlyingInstrID: ctp.Bytes2String(pInstrument.UnderlyingInstrID[:]),
				}
		}
		if bIsLast == true {
			wait <- true
		}
	})

	// Response QryDepthMarket
	t.OnRspQryDepthMarketData(func(pDepthMarketData *ctp.CThostFtdcDepthMarketDataField, pRspInfo *ctp.CThostFtdcRspInfoField, nRequestID int, bIsLast bool) {
		InstrumentsInfoV[ctp.Bytes2String(pDepthMarketData.InstrumentID[:])] =
			InstrumentsUseField{
				InstrumentID:    ctp.Bytes2String(pDepthMarketData.InstrumentID[:]),
				ExchangeID:      ctp.Bytes2String(pDepthMarketData.ExchangeID[:]),
				Volume:          float64(pDepthMarketData.Volume),
				Turnover:        float64(pDepthMarketData.Turnover),
				OpenInterest:    float64(pDepthMarketData.OpenInterest),
				PreOpenInterest: float64(pDepthMarketData.PreOpenInterest),
			}
		if bIsLast == true {
			contFlag <- true
		}
	})

	lflg, lok := <-clogin
	if !lflg || !lok {
		panic("Login Error")
	}

	// Query Insts
	pQryInstrument := ctp.CThostFtdcQryInstrumentField{}
	repn = t.ReqQryInstrument(&pQryInstrument, gl.ReqID(&nRequestID))
	for i := 0; repn != 0; i++ {
		log.Println("Retry ReqQryInstrument:", i)
		time.Sleep(REQSLEEP)
		repn = t.ReqQryInstrument(&pQryInstrument, gl.ReqID(&nRequestID))
	}

	InstsPrdMap := make(map[string][]InstrumentsUseField, 0)
	nflg, nok := <-wait
	if nok && nflg {
		log.Println("Insts List:", nok)
		pQryDepthMarketData := ctp.CThostFtdcQryDepthMarketDataField{}
		repin := t.ReqQryDepthMarketData(&pQryDepthMarketData, gl.ReqID(&nRequestID))
		for i := 0; repin != 0; i++ {
			log.Println(repin, "Retry ReqQryDepthMarketData:", i)
			if i == -1 {
				time.Sleep(REQSLEEP)
			} else {
				time.Sleep(REQSLEEP * 30) //如果请求此处过多或者有未处理完的请求则等待30s
			}
			repin = t.ReqQryDepthMarketData(&pQryDepthMarketData, gl.ReqID(&nRequestID))
		}
		vflg, vok := <-contFlag
		if vok && vflg {
			log.Println("Insts Info:", nok)
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
		}
	}

	t.Release()

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
