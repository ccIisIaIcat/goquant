package main

import (
	"global"
	"oandaapi"
	"record"
	"sync"
	"time"
)

func main() {
	config := global.GetConfig("../../gosource/conf/ExchangeConf.ini")
	oq := oandaapi.OandaObj{User_config: config.UserInfoOanda["Test"], Port_type: "Test"}
	oq.Init()
	query_list := oq.InsIdQuickCheck() // 若没有更改账号地址也可使用InsIdQuickCheckH()，以获得历史搜索结果
	mo := record.Mysql_obj{Table_list: query_list, Table_type: "OandaBarM1", Database_name: "oanda", Mysql_config: config.MysqlInfo["Local"]}
	mo.Init()
	start_time := "2023-01-05T15:34:00Z"
	count := "10"
	para := map[string]string{"price": "AB", "granularity": "M1", "from": start_time, "count": count}

	judge_signal := 0
	var m sync.Mutex
	for i := 0; i < len(query_list); i++ {
		temp_name := query_list[i]
		a := oq.GetBar(temp_name, para)
		go func() {
			mo.InsertByOandaBarM1(a, temp_name)
			m.Lock()
			judge_signal += 1
			m.Unlock()
		}()
	}
	for {
		time.Sleep(time.Second)
		m.Lock()
		if judge_signal == len(query_list) {
			break
		}
		m.Unlock()
	}
}
