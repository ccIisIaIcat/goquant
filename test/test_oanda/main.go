package main

import (
	"fmt"
	"global"
	"oandaapi"
)

func main() {
	config := global.GetConfig("../../gosource/conf/ExchangeConf.ini")
	oq := oandaapi.OandaObj{User_config: config.UserInfoOanda["Test"], Port_type: "Test"}
	oq.Init()

	// fmt.Println(oq.GetAccount())

	// fmt.Println(oq.GetAccountDetail())

	// fmt.Println(oq.GetAccountSummary())

	// js, _ := json.Marshal(map[string]string{"alias": "zwj"})
	// oq.PatchAccountConfig(string(js))

	// a := oq.GetBarRecent("EUR_USD", "5", "10", "AB")
	// fmt.Println(a)

	// (to 和 from 同时声明时会返回空？)
	// para := map[string]string{"price": "AB", "granularity": "M1", "from": "2023-01-11T00:00:00Z", "count": "1000"}
	// a := oq.GetBar("EUR_TRY", para)
	// fmt.Println(a)

	// para := map[string]string{"time": "2023-01-05T03:40:00Z"}
	// a, b := oq.GetOrderbook("EUR_USD", para)
	// fmt.Println(a, b[0])
	// para := map[string]string{}
	// a, b := oq.GetOrderbook("EUR_USD", para)
	// fmt.Println(a, b[0])

	// temp_order := map[string](string){"units": "100", "instrument": "EUR_USD", "timeInForce": "FOK", "type": "MARKET", "positionFill": "DEFAULT"}
	// new_order := make(map[string](map[string]string), 0)
	// new_order["order"] = temp_order
	// js, _ := json.Marshal(new_order)
	// re := oq.PostOrder(string(js))
	// fmt.Println(string(re))

	// temp_order := map[string](string){"timeInForce": "GTC", "price": "1.7000", "type": "TAKE_PROFIT", "tradeID": "6368"}
	// new_order := make(map[string](map[string]string), 0)
	// new_order["order"] = temp_order
	// js, _ := json.Marshal(new_order)
	// fmt.Println(oq.PutOrderSpecifier("1", string(js)))

	// oq.GetTradeInfo("EUR_USD")
	// fmt.Println(oq.PutOrderCancel("1"))

	fmt.Println(oq.GetPosition())

}
