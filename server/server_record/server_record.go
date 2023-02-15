package main

import (
	"flag"
	"fmt"
	"global"
	"log"
	"mainforce_query"
	"record"
	"tick_query"
	"time"
)

var (
	User_type        = "Test"
	Market_port_type = "1"
	Trade_port_type  = "1"
	Mysql_type       = "Local2"
	Database         = "quant_info"
	IniFile          = "../../gosource/conf/ExchangeConf.ini"
)

func Start_server(config global.Config) {
	// Flag

	log.Println("Waiting Start...")
	// atq_model := allinsts_queryATConfig{
	// 	User_config: config.UserInfo[User_type], Port_config: config.PortInfo[Trade_port_type],
	// }
	_, mainforce_list, _ := mainforce_query.QuickCheckCustom(map[string]bool{"SHFE": true})
	log.Println(mainforce_list)
	log.Println("Instrument number: ", len(mainforce_list))
	// global.Never_stop_direct()

	tick_chan_root := make(chan global.Tick_info, 400)
	// 声明query对象
	query_model := tick_query.Query{Query_list: mainforce_list, User_config: config.UserInfo[User_type], Port_config: config.PortInfo[Market_port_type], Tick_info_channel: tick_chan_root}
	query_model.Init()

	// 记录模块
	// 声明tick数据获取对象
	tick_chan_mysql := make(chan global.Tick_info, 400)
	// 声明mysql对象
	mysql_module := record.Mysql_obj{Mysql_config: config.MysqlInfo[Mysql_type], Database_name: Database, Table_list: mainforce_list, Tick_info_chan: tick_chan_mysql}
	mysql_module.Init()

	// tick信号分发
	go func() {
		for {
			t_price := <-tick_chan_root
			if t_price.Ins_id == "ag2306" {
				fmt.Println(t_price.Time)
			}
			tick_chan_mysql <- t_price
			// fmt.Println(len(tick_chan_mysql))
		}
	}()

	// 记录模组
	go mysql_module.InsertByTick()

	// 查询模组
	go query_model.Start()
	for {
		temp_time := time.Now().Format("15:04")
		fmt.Println(temp_time)
		if temp_time > "02:30" && temp_time < "02:40" {
			query_model.ReleaseQuote()
			break
		}
		if temp_time > "11:30" && temp_time < "11:35" {
			query_model.ReleaseQuote()
			break
		}
		if temp_time > "15:10" && temp_time < "15:20" {
			query_model.ReleaseQuote()
			break
		}

		time.Sleep(time.Minute)
	}
}

func main() {
	var tmpStr string
	flag.StringVar(&tmpStr, "ini_file", "../../gosource/conf/ExchangeConf.ini", "ini file path")
	flag.Parse()
	if tmpStr != IniFile {
		IniFile = tmpStr
	}

	// 载入配置文件
	config := global.GetConfig(IniFile)
	for {
		temp_time := time.Now().Format("15:04")
		fmt.Println("wair for start:", temp_time)
		if temp_time > "13:20" && temp_time < "13:25" {
			Start_server(config)
		}
		if temp_time > "08:50" && temp_time < "08:55" {
			Start_server(config)
		}
		if temp_time > "20:30" && temp_time < "20:40" {
			Start_server(config)
		}
		time.Sleep(time.Minute)
	}

}
