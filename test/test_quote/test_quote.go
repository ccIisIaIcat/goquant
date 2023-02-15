package main

import (
	ctp "ctpapi"
	"fmt"
	"log"
	"path"
	"runtime"
	"sync"
	"time"

	"gopkg.in/ini.v1"
)

type InstrumentsUseField struct {
	InstrumentID   string
	InstrumentName string
	InstLifePhase  string
	ExchangeInstID string
	ExchangeID     string
}

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

func QryInstsInfo() map[string]InstrumentsUseField {
	conf := new(ATConfig)
	_, curFile, _, _ := runtime.Caller(0)
	conf.LoadConf(path.Join(curFile, "../../conf_test/GlobalConfTest.ini"))
	// Instrument Info
	// var InstrumentsInfo sync.Map
	InstrumentsInfo := make(map[string]InstrumentsUseField, 0)
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

	// Response Qryinfo
	t.OnRspQryInstrument(func(pInstrument *ctp.CThostFtdcInstrumentField, pRspInfo *ctp.CThostFtdcRspInfoField, nRequestID int, bIsLast bool) {
		// fmt.Println("OnRspQryInstrument:", ctp.Bytes2String(pRspInfo.ErrorMsg[:]))
		InstrumentsInfo[ctp.Bytes2String(pInstrument.InstrumentID[:])] =
			InstrumentsUseField{
				InstrumentID:   ctp.Bytes2String(pInstrument.InstrumentID[:]),
				InstrumentName: ctp.Bytes2String(pInstrument.InstrumentName[:]),
				InstLifePhase:  string(pInstrument.InstLifePhase),
				ExchangeInstID: ctp.Bytes2String(pInstrument.ExchangeInstID[:]),
				ExchangeID:     ctp.Bytes2String(pInstrument.ExchangeID[:]),
			}
		if bIsLast == true {
			wait <- true
		}
	})

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
	select {
	case <-wait:
		return InstrumentsInfo
	}
}

func QryMarketData() {
	conf := new(ATConfig)
	_, curFile, _, _ := runtime.Caller(0)
	conf.LoadConf(path.Join(curFile, "../../conf_test/GlobalConfTest.ini"))

	var Ticks sync.Map

	q := ctp.InitQuote()
	q.RegisterSpi()
	bQuoteFront := []byte(conf.QuoteFront)
	q.RegisterFront(bQuoteFront)
	q.Init()

	// Callback Function Initialization
	q.OnFrontConnected(func() {
		log.Println("Quote OnFrontConnected")
	})
	q.OnRspUserLogin(func(login *ctp.CThostFtdcRspUserLoginField, info *ctp.CThostFtdcRspInfoField, nRequestID int, bIsLast bool) {
		log.Println("Quote OnRspUserLogin", string(info.ErrorMsg[:]))
	})
	q.OnRtnDepthMarketData(func(dataField *ctp.CThostFtdcDepthMarketDataField) {
		tick := ctp.TickField{
			TradingDay:      ctp.Bytes2String(dataField.TradingDay[:]),
			InstrumentID:    ctp.Bytes2String(dataField.InstrumentID[:]),
			ExchangeID:      ctp.Bytes2String(dataField.ExchangeID[:]),
			LastPrice:       float64(dataField.LastPrice),
			OpenPrice:       float64(dataField.OpenPrice),
			HighestPrice:    float64(dataField.HighestPrice),
			LowestPrice:     float64(dataField.LowestPrice),
			Volume:          int(dataField.Volume),
			Turnover:        float64(dataField.Turnover),
			OpenInterest:    float64(dataField.OpenInterest),
			ClosePrice:      float64(dataField.ClosePrice),
			SettlementPrice: float64(dataField.SettlementPrice),
			UpperLimitPrice: float64(dataField.UpperLimitPrice),
			LowerLimitPrice: float64(dataField.LowerLimitPrice),
			CurrDelta:       float64(dataField.CurrDelta),
			UpdateTime:      ctp.Bytes2String(dataField.UpdateTime[:]),
			UpdateMillisec:  int(dataField.UpdateMillisec),
			BidPrice1:       float64(dataField.BidPrice1),
			BidVolume1:      int(dataField.BidVolume1),
			AskPrice1:       float64(dataField.AskPrice1),
			AskVolume1:      int(dataField.AskVolume1),
			BidPrice2:       float64(dataField.BidPrice2),
			BidVolume2:      int(dataField.BidVolume2),
			AskPrice2:       float64(dataField.AskPrice2),
			AskVolume2:      int(dataField.AskVolume2),
			BidPrice3:       float64(dataField.BidPrice3),
			BidVolume3:      int(dataField.BidVolume3),
			AskPrice3:       float64(dataField.AskPrice3),
			AskVolume3:      int(dataField.AskVolume3),
			BidPrice4:       float64(dataField.BidPrice4),
			BidVolume4:      int(dataField.BidVolume4),
			AskPrice4:       float64(dataField.AskPrice4),
			AskVolume4:      int(dataField.AskVolume4),
			BidPrice5:       float64(dataField.BidPrice5),
			BidVolume5:      int(dataField.BidVolume5),
			AskPrice5:       float64(dataField.AskPrice5),
			AskVolume5:      int(dataField.AskVolume5),
			AveragePrice:    float64(dataField.AveragePrice),
			ActionDay:       ctp.Bytes2String(dataField.ActionDay[:]),
		}
		Ticks.Store(tick.InstrumentID, &tick)
		fmt.Printf("%+v\n", tick)
	})
	q.OnFrontDisconnected(func(nReason int) {
		log.Println("Quote OnFrontDisconnected:", nReason)
		if nReason != 0 {
			q.Release()
		}
	})

	pReqUserLoginField := ctp.CThostFtdcReqUserLoginField{}
	copy(pReqUserLoginField.UserID[:], []byte(conf.UserID))
	copy(pReqUserLoginField.BrokerID[:], []byte(conf.BrokerID))
	copy(pReqUserLoginField.Password[:], []byte(conf.Password))
	for i := 0; q.ReqUserLogin(&pReqUserLoginField, 1) != 0; i++ {
		fmt.Println("Retry Login:", i)
		time.Sleep(1 * time.Second)
	}

	instruments := make([]string, 0)
	// instruments = append(instruments, "i2305")
	instruments = append(instruments, "SA305")
	// instruments = append(instruments, "rb2305")
	ppInstrumentID := make([][]byte, len(instruments)) // [][]byte{[]byte(instrument)}
	for i := 0; i < len(instruments); i++ {
		ppInstrumentID[i] = []byte(instruments[i])
	}
	q.SubscribeMarketData(ppInstrumentID, len(ppInstrumentID))

	time.Sleep(10 * time.Second)
}

func main() {
	InstsInfo := QryInstsInfo()
	fmt.Println(InstsInfo)
	// QryMarketData()
}
