package oandaapi

import (
	"encoding/json"
	"io/ioutil"
	"net/http"
)

// 获取某个账户的全部持仓
func (O *OandaObj) GetPosition() map[string]interface{} {
	// 某个合约下的全部订单
	req, err := http.NewRequest("GET", O.base_url+"/v3/accounts/"+O.User_config.Account+"/positions", nil)
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
