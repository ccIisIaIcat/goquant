package main

import (
	"fake"
	"flag"
	"fmt"
	"global"
	"strategy"
	"tick_query"
	"trade"
)

var (
	User_type        = "Test"
	Market_port_type = "1"
	Trade_port_type  = "1"
	Mysql_type       = "Rm"
	Database         = "tick_info"
	IniFile          = "../../gosource/conf/ExchangeConf.ini"
)

// 一个连接query=>strategy
func connect_demo(config *global.Config) error {
	// 声明相关通道
	tick_chan_root := make(chan global.Tick_info, 200) // tick数据流

	signal_chan := make(chan global.Trade_signal, 200)
	signal_backward_chan := make(chan global.Signal_backward, 200)
	tick_chan_signal := make(chan global.Tick_info, 200)

	// 声明对象
	// 声明查询对象
	q := tick_query.Query{Query_list: []string{"pp2305"}, User_config: config.UserInfo[User_type], Port_config: config.PortInfo[Market_port_type], Tick_info_channel: tick_chan_root}
	// 声明交易对象
	t := trade.TradeBySignal{Signal_backward_chan: signal_backward_chan, User_config: config.UserInfo[User_type], Port_config: config.PortInfo[Trade_port_type], Signal_chan: signal_chan}
	// 声明策略对象
	s := strategy.Strategy{Tick_price_chan: tick_chan_signal, Signal_chan: signal_chan}

	// 信息分发
	go func() {
		for {
			t_price := <-tick_chan_root
			tick_chan_signal <- t_price

		}
	}()

	// 初始化
	// 初始化策略对象,检查错误
	var err error
	err = s.Init()
	if err != nil {
		fmt.Println("s")
		return err
	}
	t.Init()
	if err != nil {
		fmt.Println("t")
		return err
	}
	q.Init()
	if err != nil {
		fmt.Println("q")
		return err
	}
	// 查看交易回执
	go func() {
		for {
			temp_signal_back := <-t.Signal_backward_chan
			fmt.Println(temp_signal_back)
		}
	}()

	// 开启服务
	go t.Start()
	info := <-t.Connection_check_chan
	fmt.Println(info)
	go q.Start()

	global.Never_stop_direct()

	return nil
}

func main() {
	// Flag
	var tmpStr string
	flag.StringVar(&tmpStr, "ini_file", "../../gosource/conf/ExchangeConf.ini", "ini file path")
	flag.Parse()
	if tmpStr != IniFile {
		IniFile = tmpStr
	}

	// 载入配置文件
	config := global.GetConfig("../../gosource/conf/ExchangeConf.ini")

	err := connect_demo(&config)
	if err != nil {
		fmt.Println(err)
	}

	fake_tick_mongo := make(chan global.Tick_info, 200)

	mongo_moudle := fake.FakeQueryMongo{Query_list: []string{"ag2302"}, Database_name: "quant_info", Tick_info_chan: fake_tick_mongo}
	mongo_moudle.Init()

	global.Never_stop_direct()
	// info := mainforce_query.QuickCheck()
	// fmt.Println(info)
	// err := q.Init()
	// if err != nil {
	// 	fmt.Println(err)
	// }

	// mysql_insert := record.Mysql_obj{Username: "root", Password: "", Database_name: "quant_info", Table_list: []string{"ag2302"}}
	// mysql_insert.Init()

	// fmt.Println(mainforce_query.QuickCheck("root", "", "quant_info"))
}
