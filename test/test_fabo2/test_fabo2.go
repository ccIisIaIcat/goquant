package main

import (
	"fmt"
	"global"
	"mainforce_query"
	"strategy"
	"tick_query"
	"time"
	"trade"
)

// 配置信息
var (
	User_type        = "Test1"
	Market_port_type = "1"
	Trade_port_type  = "1"
	Mysql_type       = "Local"
	Database         = "quant_info"
)

// 操作信息
var (
	period_start_1 = "08:50"
	period_end_1   = "15:05"
	period_start_2 = "20:50"
	period_end_2   = "02:50"
)

type Server struct {
	// 配置
	config global.Config
	// 合约单
	mainforce_list []string
	// 各种channel
	tick_chan_root chan global.Tick_info
	// tick_chan_genbar   chan global.Tick_info
	// tick_chan_mysql    chan global.Tick_info
	// tick_chan_mongodb  chan global.Tick_info
	tick_chan_strategy chan global.Tick_info
	// bar_chan_genbar      chan global.Price_dic
	signal_chan          chan global.Trade_signal
	signal_backward_chan chan global.Signal_backward
	// 各种模块
	query_model tick_query.Query
	// genbar_model    genbar.Genbar
	// mysql_module    record.Mysql_obj
	strategy_module strategy.FaboStrategy2 // PS:不同策略下结构体不同
	trade_module    trade.TradeBySignal
}

// 声明结构体
func (Se *Server) InitChan() {
	Se.tick_chan_root = make(chan global.Tick_info, 200)
	// Se.tick_chan_genbar = make(chan global.Tick_info, 200)
	// Se.tick_chan_mysql = make(chan global.Tick_info, 200)
	// Se.tick_chan_mongodb = make(chan global.Tick_info, 200)
	Se.tick_chan_strategy = make(chan global.Tick_info, 200)
	// Se.bar_chan_genbar = make(chan global.Price_dic, 200)
	Se.signal_chan = make(chan global.Trade_signal, 200)
	Se.signal_backward_chan = make(chan global.Signal_backward, 200)
}

// 初始化配置,和查询对象
func (Se *Server) InitConfig() {
	Se.config = global.GetConfig("../../gosource/conf/ExchangeConf.ini")
	if len(Se.mainforce_list) == 0 {
		_, mainforce_list, _ := mainforce_query.QuickCheckCustom(map[string]bool{"SHFE": true})
		fmt.Println(mainforce_list)
		Se.mainforce_list = mainforce_list
	}
}

// 初始化本地模块（可只初始化用到的)
func (Se *Server) InitLocalModeul() {
	// Se.genbar_model = genbar.Genbar{Tick_info_channel: Se.tick_chan_genbar, Bar_chan: Se.bar_chan_genbar}
	Se.strategy_module = strategy.FaboStrategy2{Strategy: strategy.Strategy{Tick_price_chan: Se.tick_chan_strategy, Signal_chan: Se.signal_chan, Signal_backward_chan: Se.signal_backward_chan, Ins_id_list: Se.mainforce_list}}
	// Se.genbar_model.Init()
	Se.strategy_module.Init()
}

// 初始化网络和数据库模块（可只初始化用到的)
func (Se *Server) InitOnlineModeul() {
	Se.query_model = tick_query.Query{Query_list: Se.mainforce_list, User_config: Se.config.UserInfo[User_type], Port_config: Se.config.PortInfo[Market_port_type], Tick_info_channel: Se.tick_chan_root}
	// Se.mysql_module = record.Mysql_obj{Mysql_config: Se.config.MysqlInfo[Mysql_type], Database_name: Database, Table_list: Se.mainforce_list, Tick_info_chan: Se.tick_chan_mysql, Table_type: "Part"}
	Se.trade_module = trade.TradeBySignal{Signal_chan: Se.signal_chan, Signal_backward_chan: Se.signal_backward_chan, User_config: Se.config.UserInfo[User_type], Port_config: Se.config.PortInfo[Trade_port_type]}
	Se.query_model.Init()
	// Se.mysql_module.Init()
	Se.trade_module.Init()
}

// 信息分发
func (Se *Server) DistributeTick() {
	for {
		t_price := <-Se.tick_chan_root
		// Se.tick_chan_genbar <- t_price
		// Se.tick_chan_mysql <- t_price
		Se.tick_chan_strategy <- t_price
	}
}

// 本地服务开启
func (Se *Server) StartLocalServer() {
	// go Se.genbar_model.GenbarByStream()
	go Se.strategy_module.Start()
	global.Never_stop_direct()
}

func (Se *Server) StartOnlineServer() {
	// go Se.mysql_module.InsertByTickPart()
	go Se.trade_module.Start()
	info := <-Se.trade_module.Connection_check_chan
	fmt.Println(info)
	go Se.query_model.Start()
}

func (Se *Server) StopOnlineServer() {
	Se.query_model.ReleaseQuote()
	//
	// Se.mysql_module.CloseStmt()
	Se.trade_module.Stop()
}

// 工作周期A：08:40 => 15:10
// 工作时间B：20:40 => 02:40
func Start() {
	MainServer := Server{}
	MainServer.InitChan()
	MainServer.InitConfig()
	go MainServer.InitLocalModeul()
	go MainServer.DistributeTick()
	go MainServer.StartLocalServer()
	Day_id := 0
	MainServer.strategy_module.Day_id = Day_id
	for {
		temp_time := time.Now().Format("15:04")
		fmt.Println(temp_time)
		if temp_time > period_start_1 && temp_time < period_end_1 {
			MainServer.InitOnlineModeul()
			MainServer.StartOnlineServer()
			for {
				time.Sleep(time.Minute)
				temp_time := time.Now().Format("15:04")
				if temp_time > period_end_1 {
					MainServer.StopOnlineServer()
					Day_id += 1
					MainServer.strategy_module.Day_id = Day_id
					break
				}
			}
		}
		temp_time = time.Now().Format("15:04")
		if temp_time > period_start_2 {
			MainServer.InitOnlineModeul()
			MainServer.StartOnlineServer()
			for {
				time.Sleep(time.Minute)
				temp_time := time.Now().Format("15:04")
				if temp_time < period_start_2 && temp_time > period_end_2 {
					MainServer.StopOnlineServer()
					break
				}
			}
		}
		time.Sleep(time.Minute)
	}

}

func main() {
	Start()
}
