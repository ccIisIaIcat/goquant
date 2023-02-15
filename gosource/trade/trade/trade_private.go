package trade

import (
	ctp "ctpapi"
	"fmt"
	"global"
	"time"
)

// 获取合约对应的交易所
func (T *TradeBySignal) getInsidExchange() map[string]string {
	// Response Qryinfo
	wait := make(chan bool)
	temp_map := make(map[string]string, 0)
	T.t.OnRspQryInstrument(func(pInstrument *ctp.CThostFtdcInstrumentField, pRspInfo *ctp.CThostFtdcRspInfoField, nRequestID int, bIsLast bool) {
		// fmt.Println("OnRspQryInstrument:", ctp.Bytes2String(pRspInfo.ErrorMsg[:]))
		if len(ctp.Bytes2String(pInstrument.InstrumentID[:])) < 10 {
			temp_map[ctp.Bytes2String(pInstrument.InstrumentID[:])] = ctp.Bytes2String(pInstrument.ExchangeID[:])
		}
		if bIsLast == true {
			wait <- true
		}
	})
	pQryInstrument := ctp.CThostFtdcQryInstrumentField{}
	T.t.ReqQryInstrument(&pQryInstrument, T.ReqID(&T.nRequestID))

	select {
	case <-wait:
		fmt.Println(temp_map)
		return temp_map
	}
}

// 根据信号发单
func (T *TradeBySignal) subOrder(InsID string, OffsetFlag string, Volume int, Direction string, LimitPrice float64, stop_price float64, exchange string, closeType string) error {
	copy(T.order_sample_SHFE.InstrumentID[:], []byte(InsID))
	if OffsetFlag == "开仓" {
		T.order_sample_SHFE.CombOffsetFlag[0] = ctp.THOST_FTDC_OF_Open
	} else {
		if closeType == "平今" {
			T.order_sample_SHFE.CombOffsetFlag[0] = ctp.THOST_FTDC_OF_CloseToday
		} else {
			T.order_sample_SHFE.CombOffsetFlag[0] = ctp.THOST_FTDC_OF_CloseYesterday
		}
	}
	T.order_sample_SHFE.VolumeTotalOriginal = int32(Volume)
	if Direction == "买" {
		T.order_sample_SHFE.Direction = ctp.THOST_FTDC_D_Buy
	} else {
		T.order_sample_SHFE.Direction = ctp.THOST_FTDC_D_Sell
	}
	T.order_sample_SHFE.LimitPrice = LimitPrice
	T.order_sample_SHFE.StopPrice = stop_price

	T.t.ReqOrderInsert(&T.order_sample_SHFE, T.ReqID(&T.nRequestID))
	T.makeSample()

	return nil
}

// 登录
func (T *TradeBySignal) login() {
	// 声明trade对象
	T.t = ctp.InitTrade()
	// 注册spi
	T.t.RegisterSpi()
	// 生成前台端口byte
	bTradeFront := []byte(T.port)
	// 注册前台端口
	T.t.RegisterFront(bTradeFront)
	// 订阅
	T.t.SubscribePrivateTopic(ctp.THOST_TERT_RESUME)
	T.t.SubscribePublicTopic(ctp.THOST_TERT_RESUME)
	T.t.Init()
	// 订阅委托回执错误
	T.t.OnErrRtnOrderInsert(func(pInputOrder *ctp.CThostFtdcInputOrderField, pRspInfo *ctp.CThostFtdcRspInfoField) {
		temp_signal := global.Signal_backward{Info_type: "错误", Err_info: ctp.Bytes2String(pRspInfo.ErrorMsg[:]), Ins_id: ctp.Bytes2String(pInputOrder.InstrumentID[:])}
		T.Signal_backward_chan <- temp_signal
	})
	// T.t.OnRspOrderInsert(func(pInputOrder *ctp.CThostFtdcInputOrderField, pRspInfo *ctp.CThostFtdcRspInfoField, nRequestID int, bIsLast bool) {
	// 	temp_signal := global.Signal_backward{Info_type: "错误2", Err_info: ctp.Bytes2String(pRspInfo.ErrorMsg[:]), Ins_id: ctp.Bytes2String(pInputOrder.InstrumentID[:])}
	// 	T.Signal_backward_chan <- temp_signal
	// })

	// 订阅委托回执
	T.t.OnRtnOrder(func(pOrder *ctp.CThostFtdcOrderField) {
		temp_signal := global.Signal_backward{Info_type: "委托回执", StatusMsg: ctp.Bytes2String(pOrder.StatusMsg[:]), Limit_price: pOrder.LimitPrice, Limit_amount: int(pOrder.VolumeTotal), Ins_id: ctp.Bytes2String(pOrder.InstrumentID[:]), Exc_id: ctp.Bytes2String(pOrder.ExchangeID[:]), OrderSysID: ctp.Bytes2String(pOrder.OrderSysID[:]), Direction: string(pOrder.Direction), OrderRef: ctp.Bytes2String(pOrder.OrderRef[:]), OffsetFlag: ctp.Bytes2String(pOrder.CombOffsetFlag[:])}
		T.Signal_backward_chan <- temp_signal
	})

	// 订阅委托回执(成交)
	T.t.OnRtnTrade(func(pTrade *ctp.CThostFtdcTradeField) {
		temp_signal := global.Signal_backward{Info_type: "成交", Limit_price: pTrade.Price, Limit_amount: int(pTrade.Volume), Ins_id: ctp.Bytes2String(pTrade.InstrumentID[:]), Exc_id: ctp.Bytes2String(pTrade.ExchangeID[:]), OrderSysID: ctp.Bytes2String(pTrade.OrderSysID[:]), Direction: string(pTrade.Direction), OrderRef: ctp.Bytes2String(pTrade.OrderRef[:]), OffsetFlag: string(pTrade.OffsetFlag)}
		T.Signal_backward_chan <- temp_signal
	})
	// 前台连接相应(前台连接成功后进行认证)
	T.t.OnFrontConnected(func() {
		fmt.Println("OnFrontConnected")
		T.login_record["OnFrontConnected"] = true

		// 声明认证对象结构体
		pReqAuthenticateField := ctp.CThostFtdcReqAuthenticateField{}
		copy(pReqAuthenticateField.BrokerID[:], []byte(T.broker))
		copy(pReqAuthenticateField.UserID[:], []byte(T.investor))
		copy(pReqAuthenticateField.AppID[:], []byte(T.appid))
		copy(pReqAuthenticateField.AuthCode[:], []byte(T.authcode))
		// 发送认证请求
		nRequestID := 0
		for i := 0; T.t.ReqAuthenticate(&pReqAuthenticateField, T.ReqID(&nRequestID)) != 0; i++ {
			fmt.Println("Retry ReqAuthenticate:", i)
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
		copy(pReqUserLoginField.BrokerID[:], []byte(T.broker))
		copy(pReqUserLoginField.UserID[:], []byte(T.investor))
		copy(pReqUserLoginField.Password[:], []byte(T.password))
		// length := ctp.TThostFtdcSystemInfoLenType(273)

		// 用户登录请求
		nRequestID = 0
		for i := 0; T.t.ReqUserLogin(&pReqUserLoginField, T.ReqID(&nRequestID)) != 0; i++ {
			fmt.Println("Retry ReqUserLogin:", i)
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
		copy(pSettlementInfoConfirm.BrokerID[:], []byte(T.broker))
		copy(pSettlementInfoConfirm.InvestorID[:], []byte(T.investor))
		T.t.ReqSettlementInfoConfirm(&pSettlementInfoConfirm, T.ReqID(&T.nRequestID))
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

	T.Connection_check_chan <- "登录成功"
	T.Connection_check_chan <- "登录成功"

	global.Never_stop_direct()
}

// 生成订单模板
// 生成样本订单簿，上期所未填入信息，InstrumentID（产品代码），CombOffsetFlag（开平标志），VolumeTotalOriginal（成交量）,Direction(开仓方向)，LimitPrice（开单价格）,stop_price (止损价格)
// 其他交易所未填入信息 AskPrice（买价格），BidPrice（卖价格），AskVolume（买数量），BidVolume（卖数量），AskOffsetFlag（买开平标志），BidOffsetFlag（买开平标志）
func (T *TradeBySignal) makeSample() {
	// 上期所订单
	copy(T.order_sample_SHFE.BrokerID[:], []byte(T.broker))
	copy(T.order_sample_SHFE.UserID[:], []byte(T.investor))
	copy(T.order_sample_SHFE.ExchangeID[:], []byte("SHFE"))
	copy(T.order_sample_SHFE.InvestorID[:], []byte(T.investor))
	// copy(T.order_sample_SHFE.InvestorID[:], []byte("ag2302"))
	// T.order_sample_SHFE.CombOffsetFlag[0] = ctp.THOST_FTDC_OF_Open
	T.order_sample_SHFE.CombHedgeFlag[0] = ctp.THOST_FTDC_BHF_Speculation
	// T.order_sample_SHFE.VolumeTotalOriginal = 1
	T.order_sample_SHFE.IsAutoSuspend = 0
	T.order_sample_SHFE.IsSwapOrder = 0
	T.order_sample_SHFE.OrderPriceType = ctp.THOST_FTDC_OPT_LimitPrice
	// T.order_sample_SHFE.Direction = ctp.THOST_FTDC_D_Buy
	T.order_sample_SHFE.TimeCondition = ctp.THOST_FTDC_TC_IOC
	T.order_sample_SHFE.VolumeCondition = ctp.THOST_FTDC_VC_AV
	T.order_sample_SHFE.ContingentCondition = ctp.THOST_FTDC_CC_Immediately // 触发条件
	T.order_sample_SHFE.ForceCloseReason = ctp.THOST_FTDC_FCC_NotForceClose
	// T.order_sample_SHFE.LimitPrice = 5350
	// T.order_sample_SHFE.StopPrice = 0
	// 其他交易所订单
	copy(T.order_sample_Other.BrokerID[:], []byte(T.broker))
	copy(T.order_sample_Other.InvestorID[:], []byte(T.investor))
	// copy(T.order_sample_Other.InstrumentID[:], []byte("rb2302"))
	copy(T.order_sample_Other.UserID[:], []byte(T.investor))
	copy(T.order_sample_Other.ExchangeID[:], []byte(""))
	T.order_sample_Other.AskHedgeFlag = ctp.THOST_FTDC_HF_Speculation
	T.order_sample_Other.BidHedgeFlag = ctp.THOST_FTDC_HF_Speculation
}
