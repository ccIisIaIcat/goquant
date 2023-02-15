package main

import (
	ctp "ctpapi"
	"fmt"
	"log"
	"path"
	"runtime"
	"time"

	"gopkg.in/ini.v1"
)

type ATConfig struct {
	QuoteFront string
	TradeFront string
	BrokerID   string
	UserID     string
	Password   string
	AppID      string
	AuthCode   string
}

func (conf *ATConfig) LoadConf(confPath string) {
	conf_ini, err := ini.Load(confPath)
	if err != nil {
		fmt.Println(err)
	}
	conf.QuoteFront = conf_ini.Section("UserInfo").Key("QuoteFront").String()
	conf.TradeFront = conf_ini.Section("UserInfo").Key("TradeFront").String()
	conf.BrokerID = conf_ini.Section("UserInfo").Key("BrokerID").String()
	conf.UserID = conf_ini.Section("UserInfo").Key("UserID").String()
	conf.Password = conf_ini.Section("UserInfo").Key("Password").String()
	conf.AppID = conf_ini.Section("UserInfo").Key("AppID").String()
	conf.AuthCode = conf_ini.Section("UserInfo").Key("AuthCode").String()
}

func ReqID(nRequestID *int) int {
	*nRequestID++
	return *nRequestID
}

func OrderTrade() {
	conf := new(ATConfig)
	_, curFile, _, _ := runtime.Caller(0)
	conf.LoadConf(path.Join(curFile, "../../conf_test/GlobalConfTest.ini"))
	wait := make(chan bool)
	// Init: Create Api and Spi
	t := ctp.InitTrade()
	// Register Spi
	t.RegisterSpi()
	bTradeFront := []byte(conf.TradeFront)
	// Register Front
	t.RegisterFront(bTradeFront)
	// Subscribe
	t.SubscribePrivateTopic(ctp.THOST_TERT_RESUME)
	t.SubscribePublicTopic(ctp.THOST_TERT_RESUME)
	t.Init()

	// Front connected
	t.OnFrontConnected(func() {
		log.Println("Trade OnFrontConnected")
	})
	// Response Authenticate
	t.OnRspAuthenticate(func(pRspAuthenticateField *ctp.CThostFtdcRspAuthenticateField, pRspInfo *ctp.CThostFtdcRspInfoField, nRequestID int, bIsLast bool) {
		log.Println("Trade OnRspAuthenticate:", ctp.Bytes2String(pRspInfo.ErrorMsg[:]))
	})

	// Response UserLogin
	t.OnRspUserLogin(func(pRspUserLogin *ctp.CThostFtdcRspUserLoginField, pRspInfo *ctp.CThostFtdcRspInfoField, nRequestID int, bIsLast bool) {
		log.Println("Trade OnRspUserLogin:", ctp.Bytes2String(pRspInfo.ErrorMsg[:]))
	})
	t.OnRtnOrder(func(pOrder *ctp.CThostFtdcOrderField) {
		log.Println("Trade OnRtnOrder StatusMsg:", ctp.Bytes2String(pOrder.StatusMsg[:]))
		wait <- true
	})
	t.OnRtnTrade(func(pTrade *ctp.CThostFtdcTradeField) {
		log.Println("Trade OnRtnTrade TradeType:", pTrade.TradeType)
	})

	//Auth
	pReqAuthenticateField := ctp.CThostFtdcReqAuthenticateField{}
	copy(pReqAuthenticateField.BrokerID[:], []byte(conf.BrokerID))
	copy(pReqAuthenticateField.UserID[:], []byte(conf.UserID))
	copy(pReqAuthenticateField.AppID[:], []byte(conf.AppID))
	copy(pReqAuthenticateField.AuthCode[:], []byte(conf.AuthCode))
	nRequestID := 0
	for i := 0; t.ReqAuthenticate(&pReqAuthenticateField, ReqID(&nRequestID)) != 0; i++ {
		log.Println("Retry ReqAuthenticate:", i)
		time.Sleep(1 * time.Second)
	}
	pReqUserLoginField := ctp.CThostFtdcReqUserLoginField{}
	copy(pReqUserLoginField.BrokerID[:], []byte(conf.BrokerID))
	copy(pReqUserLoginField.UserID[:], []byte(conf.UserID))
	copy(pReqUserLoginField.Password[:], []byte(conf.Password))
	length := ctp.TThostFtdcSystemInfoLenType(273)
	systemInfo := ctp.TThostFtdcClientSystemInfoType{}
	t.CTP_GetSystemInfo(&systemInfo, length)
	for i := 0; t.ReqUserLogin(&pReqUserLoginField, ReqID(&nRequestID)) != 0; i++ {
		log.Println("Retry ReqUserLogin:", i)
		time.Sleep(1 * time.Second)
	}
	pQryInstrument := ctp.CThostFtdcQryInstrumentField{}
	for i := 0; t.ReqQryInstrument(&pQryInstrument, ReqID(&nRequestID)) != 0; i++ {
		log.Println("Retry ReqQryInstrument:", i)
		time.Sleep(1 * time.Second)
	}

	pInputOrder := ctp.CThostFtdcInputOrderField{}
	copy(pInputOrder.BrokerID[:], []byte(conf.BrokerID))
	copy(pInputOrder.InvestorID[:], []byte(conf.UserID))
	copy(pInputOrder.InstrumentID[:], "p2301")
	copy(pInputOrder.UserID[:], []byte(conf.UserID))
	pInputOrder.CombOffsetFlag[0] = ctp.THOST_FTDC_OF_Open
	pInputOrder.CombHedgeFlag[0] = ctp.THOST_FTDC_HF_Speculation
	copy(pInputOrder.ExchangeID[:], "DCE")
	pInputOrder.VolumeTotalOriginal = 10
	pInputOrder.IsAutoSuspend = 0
	pInputOrder.IsSwapOrder = 0
	pInputOrder.OrderPriceType = ctp.THOST_FTDC_OPT_AnyPrice
	pInputOrder.Direction = ctp.THOST_FTDC_D_Buy
	pInputOrder.TimeCondition = ctp.THOST_FTDC_TC_IOC
	pInputOrder.VolumeCondition = ctp.THOST_FTDC_VC_AV
	pInputOrder.ContingentCondition = ctp.THOST_FTDC_CC_Immediately
	pInputOrder.ForceCloseReason = ctp.THOST_FTDC_FCC_NotForceClose
	pInputOrder.LimitPrice = 0
	pInputOrder.StopPrice = 0
	for t.ReqOrderInsert(&pInputOrder, ReqID(&nRequestID)) != 0 {
		fmt.Println("Retry Order")
		time.Sleep(1 * time.Second)
	}

	select {
	case <-wait:
		log.Println("Order")
	}
}

func main() {
	OrderTrade()
}
