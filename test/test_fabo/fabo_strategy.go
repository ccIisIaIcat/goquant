package main

import (
	"fmt"
	"genbar"
	"global"
	"mainforce_query"
	"record"
	"strategy"
	"tick_query"
	"time"
	"trade"
)

var (
	User_type        = "Test1"
	Market_port_type = "1"
	Trade_port_type  = "1"
	Mysql_type       = "Local"
	Database         = "quant_info"
)

// func main() {
// 	fmt.Println(GetConfig("../../gosource/conf/ExchangeConf.ini"))
// }

func Start_server(Need_close map[int]global.Position_record, Day_id int, hour_period int) (map[int]global.Position_record, int) {
	// 配置文件
	config := global.GetConfig("../../gosource/conf/ExchangeConf.ini")
	// 主力合约
	_, mainforce_list, check := mainforce_query.QuickCheckCustom(map[string]bool{"SHFE": true})
	// 检查Need_close中的合约是否在mainforce_list中，若不在加入
	for _, v := range Need_close {
		if _, ok := check[v.Ins_id]; !ok {
			mainforce_list = append(mainforce_list, v.Ins_id)
			check[v.Ins_id] = "check"
		}
	}
	// query模块
	// 声明tick数据获取对象
	tick_chan_root := make(chan global.Tick_info, 200)
	// 声明query对象
	query_model := tick_query.Query{Query_list: mainforce_list, User_config: config.UserInfo[User_type], Port_config: config.PortInfo[Market_port_type], Tick_info_channel: tick_chan_root}
	query_model.Init()
	// genbar模块
	// 声明tick数据获取对象和bar数据获取对象
	tick_chan_genbar := make(chan global.Tick_info, 200)
	bar_chan_genbar := make(chan global.Price_dic, 200)
	// 声明genbar对象
	genbar_model := genbar.Genbar{Tick_info_channel: tick_chan_genbar, Bar_chan: bar_chan_genbar}
	genbar_model.Init()
	// 声明tick数据获取对象
	tick_chan_mysql := make(chan global.Tick_info, 200)
	// tick_chan_mongodb := make(chan global.Tick_info, 200)
	// 声明mysql对象
	mysql_module := record.Mysql_obj{Mysql_config: config.MysqlInfo[Mysql_type], Database_name: Database, Table_list: mainforce_list, Tick_info_chan: tick_chan_mysql, Table_type: "Part"}
	mysql_module.Init()
	// 策略模块
	// 声明tick数据接入对象,声明信号和信号回执对象（bar数据嫁接bar模组）
	signal_chan := make(chan global.Trade_signal, 200)
	signal_backward_chan := make(chan global.Signal_backward, 200)
	tick_chan_strategy := make(chan global.Tick_info, 200)
	// 声明strategy对象
	strategyFabo_module := strategy.Strategy_fabo{Tick_price_chan: tick_chan_strategy, Bar_price_chan: bar_chan_genbar, Signal_chan: signal_chan, Signal_backward_chan: signal_backward_chan, Ins_id_list: mainforce_list, Need_close: Need_close, Day_id: Day_id}
	strategyFabo_module.Init()
	// 声明trade对象
	trade_module := trade.TradeBySignal{Signal_chan: signal_chan, Signal_backward_chan: signal_backward_chan, User_config: config.UserInfo[User_type], Port_config: config.PortInfo[Trade_port_type]}
	trade_module.Init()
	// tick信号分发
	go func() {
		for {
			t_price := <-tick_chan_root
			tick_chan_genbar <- t_price
			tick_chan_mysql <- t_price
			tick_chan_strategy <- t_price
			// tick_chan_mongodb <- t_price
		}
	}()
	// genbar模组
	go genbar_model.GenbarByStream()
	// 记录模组
	go mysql_module.InsertByTickPart()
	// go mongodb_module.InsertByTick()
	// 策略模组
	go strategyFabo_module.Start()
	// 交易模组,等待交易模组连接成功
	go trade_module.Start()
	info := <-trade_module.Connection_check_chan
	fmt.Println(info)
	// 查询模组
	query_model.Start()
	time.Sleep(time.Duration(hour_period) * time.Hour)

	// 关闭有关模组
	query_model.ReleaseQuote()
	mysql_module.CloseStmt()
	trade_module.Stop()

	return strategyFabo_module.Need_close, strategyFabo_module.Day_id

}

// 工作周期A：08:40 => 11:40
// 工作周期A：12:40 => 15:40
// 工作时间B：20:40 => 02:40
func Start() {
	nc := make(map[int]global.Position_record, 0)
	Day_id := 0
	for {
		time.Sleep(time.Minute)
		temp_time := time.Now().Format("15:04")
		if temp_time == "08:40" {
			nc, Day_id = Start_server(nc, Day_id, 3)
		}
		if temp_time == "12:40" {
			nc, Day_id = Start_server(nc, Day_id, 3)
			Day_id += 1
		}
		if temp_time == "20:40" {
			nc, Day_id = Start_server(nc, Day_id, 6)
		}
	}

}

func main() {
	Start()
}
