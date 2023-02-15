package tick_query

import (
	ctp "ctpapi"
	"fmt"
	"global"
	"strconv"
	"sync"
	"time"
)

// 编写一个使用本地ctp接口的query模组
type Query struct {
	// Public
	Query_list        []string //需要查询的指标列表
	User_config       global.ConfigUser
	Port_config       global.ConfigPort
	Tick_info_channel chan global.Tick_info

	// private
	q         *ctp.Quote // ctp查询结构体
	stop_chan chan bool
	investor  string
	password  string
	broker    string
	port      string
}

func (Q *Query) Init() {
	// 输入参数检查
	if cap(Q.Tick_info_channel) == 0 {
		panic("Query:未声明Tick_info_channel")
	}
	// 判断行情配置端口是否为空
	var port_judge global.ConfigPort
	if Q.Port_config == port_judge {
		panic("Query:未声明端口类型")
	} else {
		Q.port = Q.Port_config.MarketPort
	}
	// 判断用户数据是否为空
	var user_judge global.ConfigUser
	if Q.User_config == user_judge {
		panic("Query:未声明用户类型")
	} else {
		Q.investor = Q.User_config.Investor
		Q.password = Q.User_config.Password
		Q.broker = Q.User_config.BrokerID
	}

	// 初始化指针访问对象
	Q.q = ctp.InitQuote()

}

func (Q *Query) ReleaseQuote() {
	Q.q.Release()
	// Q.q = ctp.InitQuote()
}

func (Q *Query) Start() {
	chConnected := make(chan bool)
	Q.q.RegisterSpi()
	// 提交注册
	Q.q.OnFrontConnected(func() {
		chConnected <- true
		fmt.Println("[query] quote connected")
		f := ctp.CThostFtdcReqUserLoginField{}
		copy(f.UserID[:], []byte(Q.investor))
		copy(f.BrokerID[:], []byte(Q.broker))
		copy(f.Password[:], []byte(Q.password))
		fmt.Println(Q.investor, Q.broker, Q.password)
		Q.q.ReqUserLogin(&f, 1)
	})
	// 提交访问申请
	Q.q.OnRspUserLogin(func(login *ctp.CThostFtdcRspUserLoginField, info *ctp.CThostFtdcRspInfoField, nRequestID int, bIsLast bool) {
		fmt.Printf("[query]quote login: %+v\n", string(info.ErrorMsg[:]))
		for i := 0; i < len(Q.Query_list); i++ {
			instruments := make([]string, 0)
			instruments = append(instruments, Q.Query_list[i])
			// fmt.Println(Q.Query_list[i])
			ppInstrumentID := make([][]byte, len(instruments)) // [][]byte{[]byte(instrument)}
			for i := 0; i < len(instruments); i++ {
				ppInstrumentID[i] = []byte(instruments[i])
			}
			Q.q.SubscribeMarketData(ppInstrumentID, len(ppInstrumentID))
		}

	})
	var Ticks sync.Map
	Q.q.OnRtnDepthMarketData(func(dataField *ctp.CThostFtdcDepthMarketDataField) {
		tick := ctp.TickField{
			// 后方有//* 备注的在mysql中进行保存
			TradingDay:      ctp.Bytes2String(dataField.TradingDay[:]),   //*
			InstrumentID:    ctp.Bytes2String(dataField.InstrumentID[:]), //*
			ExchangeID:      ctp.Bytes2String(dataField.ExchangeID[:]),   //*
			LastPrice:       float64(dataField.LastPrice),                //*
			OpenPrice:       float64(dataField.OpenPrice),
			HighestPrice:    float64(dataField.HighestPrice),
			LowestPrice:     float64(dataField.LowestPrice),
			Volume:          int(dataField.Volume),           //*
			Turnover:        float64(dataField.Turnover),     //*
			OpenInterest:    float64(dataField.OpenInterest), //*
			ClosePrice:      float64(dataField.ClosePrice),
			SettlementPrice: float64(dataField.SettlementPrice),
			UpperLimitPrice: float64(dataField.UpperLimitPrice),
			LowerLimitPrice: float64(dataField.LowerLimitPrice),
			CurrDelta:       float64(dataField.CurrDelta),
			UpdateTime:      ctp.Bytes2String(dataField.UpdateTime[:]), //*
			UpdateMillisec:  int(dataField.UpdateMillisec),             //*
			BidPrice1:       float64(dataField.BidPrice1),              //*
			BidVolume1:      int(dataField.BidVolume1),                 //*
			AskPrice1:       float64(dataField.AskPrice1),              //*
			AskVolume1:      int(dataField.AskVolume1),                 //*
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
		temp_time := tick.TradingDay + " " + tick.UpdateTime + " " + strconv.Itoa(tick.UpdateMillisec)
		t_info := global.Tick_info{
			Exchange: tick.ExchangeID, Ins_id: tick.InstrumentID, Time: temp_time, Last_price: tick.LastPrice, Volume: float64(tick.Volume), Turnover: float64(tick.Turnover),
			AskPrice1: tick.AskPrice1, AskVolume1: tick.AskVolume1, BidPrice1: tick.BidPrice1, BidVolume1: tick.BidVolume1,
			AskPrice2: tick.AskPrice2, AskVolume2: tick.AskVolume2, BidPrice2: tick.BidPrice2, BidVolume2: tick.BidVolume2,
			AskPrice3: tick.AskPrice3, AskVolume3: tick.AskVolume3, BidPrice3: tick.BidPrice3, BidVolume3: tick.BidVolume3,
			AskPrice4: tick.AskPrice4, AskVolume4: tick.AskVolume4, BidPrice4: tick.BidPrice4, BidVolume4: tick.BidVolume4,
			AskPrice5: tick.AskPrice5, AskVolume5: tick.AskVolume5, BidPrice5: tick.BidPrice5, BidVolume5: tick.BidVolume5,
		}
		// if t_info.Ins_id == "ag2304" {
		// 	fmt.Println("/////", t_info)
		// }
		// fmt.Println(t_info)
		Q.Tick_info_channel <- t_info
	})
	Q.q.OnFrontDisconnected(func(reason int) {
		fmt.Println("[query]quote disconected ", reason)
		if reason != 0 {
			Q.ReleaseQuote()
		}
		Q.Start()
	})
	fmt.Println("[query]connecting to quote " + Q.port)
	bquoteFront := []byte(Q.port)
	Q.q.RegisterFront(bquoteFront)
	Q.q.Init()
	// q.RegisterSpi()
	go func() {
		// 连接超时设置
		select {
		case <-chConnected:
		case <-time.After(60 * time.Second):
			fmt.Println("连接超时")
			Q.ReleaseQuote()
		}
	}()

}
