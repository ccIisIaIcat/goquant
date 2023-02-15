package oandaapi

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"strings"
)

// 挂单相关

// 挂单
func (O *OandaObj) PostOrder(string_json string) []byte {
	req, err := http.NewRequest("POST", O.base_url+"/v3/accounts/"+O.User_config.Account+"/orders", strings.NewReader(string_json))
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

	return b
}

// 查询挂单
func (O *OandaObj) GetOrder(ins_id string) map[string]interface{} {
	req, err := http.NewRequest("GET", O.base_url+"/v3/accounts/"+O.User_config.Account+"/orders?instrument="+ins_id, nil)
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
	var p map[string]interface{}
	json.Unmarshal(b, &p)

	return p
}

// 获取特定订单的信息
func (O *OandaObj) GetOrderSpecifier(order_id string) map[string]interface{} {
	req, err := http.NewRequest("GET", O.base_url+"/v3/accounts/"+O.User_config.Account+"/orders/"+order_id, nil)
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
	var p map[string]interface{}
	json.Unmarshal(b, &p)

	return p
}

// Replace an Order in an Account by simultaneously cancelling it and creating a replacement Order
func (O *OandaObj) PutOrderSpecifier(order_id string, string_json string) string {
	fmt.Println(O.base_url + "/v3/accounts/" + O.User_config.Account + "/orders/" + order_id)
	req, err := http.NewRequest("PUT", O.base_url+"/v3/accounts/"+O.User_config.Account+"/orders/"+order_id, strings.NewReader(string_json))
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

	return string(b)
}

// 撤单
func (O *OandaObj) PutOrderCancel(order_id string) string {
	req, err := http.NewRequest("PUT", O.base_url+"/v3/accounts/"+O.User_config.Account+"/orders/"+order_id+"/cancel", nil)
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

	return string(b)
}
