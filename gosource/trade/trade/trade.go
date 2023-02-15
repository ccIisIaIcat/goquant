package trade

import (
	ctp "ctpapi"
	"errors"
	"fmt"
	"global"
	"log"
	"os"
	"sync"
	"time"
)

// 接入Signal chan 用于输入signal信号
// 输出Trade_back_chan，用于声明交易是否完成
// 输出Connection_check_chan，用于确认连接是否成功
// 基于输入信号进行实时交易
type TradeBySignal struct {
	// Public
	Signal_chan           chan global.Trade_signal // 用于接收发单信息
	Connection_check_chan chan string              // 用于确认连接是否成功
	Trade_back_chan       chan bool
	Signal_backward_chan  chan global.Signal_backward // 用于自身的回执信息交互
	User_config           global.ConfigUser
	Port_config           global.ConfigPort
	// Private
	simulation_order_respon_loger *log.Logger // 用于记录回执信息
	investor                      string
	password                      string
	broker                        string
	appid                         string
	authcode                      string
	port                          string
	login_record                  map[string]bool               // 用于判断登录回执是否齐全
	t                             *ctp.Trade                    // 声明交易指针
	nRequestID                    int                           // 本地计数器
	order_sample_SHFE             ctp.CThostFtdcInputOrderField // 声明一份订单模板，填入必要信息(上期所期货)
	order_sample_Other            ctp.CThostFtdcInputQuoteField // 声明一份订单模板，填入必要信息(除上期所外期货)
	insId_ExchangeId              map[string]string
	communicate_map               sync.Map // 用于多个合约同时交易的线程控制
}

// 初始化
func (T *TradeBySignal) Init() {
	// 路径、账号、端口检查
	// 检查端口配置文件
	var port_judge global.ConfigPort
	if T.Port_config == port_judge {
		panic("Query:missing Port_config")
	} else {
		T.port = T.Port_config.TradePort
	}
	// 检查用户配置文件
	var user_judge global.ConfigUser
	if T.User_config == user_judge {
		panic("Query:missing User_config")
	} else {
		T.investor = T.User_config.Investor
		T.password = T.User_config.Password
		T.broker = T.User_config.BrokerID
		T.appid = T.User_config.AppID
		T.authcode = T.User_config.AuthCode
	}
	// 接口检查
	if cap(T.Signal_chan) == 0 {
		panic("missing Signal_chan")
	}
	if cap(T.Signal_backward_chan) == 0 {
		panic("missing Signal_backward_chan")
	}
	// 信号端口声明
	T.Connection_check_chan = make(chan string, 5)
	// 声明委托回执信息
	_, err := os.Stat("log_record")
	if err != nil {
		os.Mkdir("log_record", os.ModePerm)
	}
	file := "./log_record/" + "simulation_order_respon_log" + ".txt"
	logFile, err := os.OpenFile(file, os.O_CREATE|os.O_APPEND, 0766)
	if err != nil {
		panic(err)
	}
	T.simulation_order_respon_loger = log.New(logFile, "[simulation_order_respon]", log.LUTC)
	T.login_record = map[string]bool{"OnFrontConnected": false, "OnRspAuthenticate": false, "OnRspUserLogin": false, "OnRspSettlementInfoConfirm": false}

	// 一些工具变量的声明
	// 声明t
	T.t = ctp.InitTrade()
	// 声明nRequestID
	T.nRequestID = 0
	// 声明样本订单
	T.order_sample_SHFE = ctp.CThostFtdcInputOrderField{}
	T.order_sample_Other = ctp.CThostFtdcInputQuoteField{}

	// 声明合约对应交易所
	T.insId_ExchangeId = make(map[string]string, 0)

	T.makeSample()
}

// 开始服务
func (T *TradeBySignal) Start() error {
	// 登录,若十秒内未完成登录则认为登录失败
	go T.login()
	select {
	case info := <-T.Connection_check_chan:
		fmt.Println(info)
	case <-time.After(60 * time.Second):
		T.t.Release()
		return errors.New("连接超时,交易请求已断开")
	}
	go func() {
		for {
			temp_signal := <-T.Signal_chan
			// fmt.Println(temp_signal)
			T.subOrder(temp_signal.Ins_id, temp_signal.Open_Close, temp_signal.Amount, temp_signal.Direction, temp_signal.Price, 0., temp_signal.Exchange, temp_signal.Closing_type)
			// if _, ok := T.insId_ExchangeId[temp_signal.Ins_id]; ok {
			// 	temp_signal.Exchange = T.insId_ExchangeId[temp_signal.Ins_id]
			// 	T.subOrder(temp_signal.Ins_id, temp_signal.Open_Close, temp_signal.Amount, temp_signal.Direction, temp_signal.Price, 0., temp_signal.Exchange)
			// } else {
			// 	fmt.Println("信号错误,未找到合约交易所")
			// }

		}
	}()

	global.Never_stop_direct()

	return nil

}

func (T *TradeBySignal) Stop() {
	T.t.Release()
}
