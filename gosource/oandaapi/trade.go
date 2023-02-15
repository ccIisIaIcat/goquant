package oandaapi

import (
	"encoding/json"
	"io/ioutil"
	"net/http"
)

// 获取某个合约所有交易信息
func (O *OandaObj) GetTradeInfo(order_id string) map[string]interface{} {
	// 某个合约下的全部订单
	req, err := http.NewRequest("GET", O.base_url+"/v3/accounts/"+O.User_config.Account+"/trades?instrument="+order_id, nil)
	if err != nil {
		panic(err)
	}
	req.Header.Set("Authorization", "Bearer "+O.User_config.Authorization)
	req.Header.Set("Content-Type", "application/json")
	resp, err := O.client.Do(req)
	if err != nil {
		panic(err)
	}
	b, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()
	var p map[string]interface{}
	json.Unmarshal(b, &p)

	return p
}

// 获取某个合约所有开放交易信息
func (O *OandaObj) GetTradeInfoAll() map[string]interface{} {
	// 某个合约下的全部订单
	req, err := http.NewRequest("GET", O.base_url+"/v3/accounts/"+O.User_config.Account+"/openTrades", nil)
	if err != nil {
		panic(err)
	}
	req.Header.Set("Authorization", "Bearer "+O.User_config.Authorization)
	req.Header.Set("Content-Type", "application/json")
	resp, err := O.client.Do(req)
	if err != nil {
		panic(err)
	}
	b, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()
	var p map[string]interface{}
	json.Unmarshal(b, &p)

	return p
}
