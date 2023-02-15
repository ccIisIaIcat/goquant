package oandaapi

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"strings"
)

// 账户相关接口

//根据当前授权码获取属于他的账户id
func (O *OandaObj) GetAccount() []map[string]string {
	req, err := http.NewRequest("GET", O.base_url+"/v3/accounts", nil)
	if err != nil {
		panic(err)
	}

	// 命名请求头
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

	var p map[string]([]map[string]string)
	json.Unmarshal(b, &p)

	return p["accounts"]
}

// 获得一个当前账户下的全量信息
func (O *OandaObj) GetAccountDetail() map[string](interface{}) {
	req, err := http.NewRequest("GET", O.base_url+"/v3/accounts/"+O.User_config.Account, nil)
	if err != nil {
		panic(err)
	}
	// 命名请求头
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

	var p map[string](map[string](interface{}))
	json.Unmarshal(b, &p)

	return p["account"]
}

// 获得一个当前账户下的全量总结
func (O *OandaObj) GetAccountSummary() map[string](interface{}) {
	req, err := http.NewRequest("GET", O.base_url+"/v3/accounts/"+O.User_config.Account+"/summary", nil)
	if err != nil {
		panic(err)
	}
	// 命名请求头
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

	var p map[string](map[string](interface{}))
	json.Unmarshal(b, &p)

	fmt.Println(p["account"])

	return p["account"]
}

// 获得当前账户下可交易的全部品种（可交易品种取决于注册时注册地的监管部门）
func (O *OandaObj) GetAccountInstuments() [](map[string]string) {
	req, err := http.NewRequest("GET", O.base_url+"/v3/accounts/"+O.User_config.Account+"/instruments", nil)
	if err != nil {
		panic(err)
	}
	// 命名请求头
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

	var p map[string]([](map[string]string))
	json.Unmarshal(b, &p)

	return p["instruments"]
}

//更改当前账户下的一些配置请求
func (O *OandaObj) PatchAccountConfig(string_json string) {
	req, err := http.NewRequest("PATCH", O.base_url+"/v3/accounts/"+O.User_config.Account+"/configuration", strings.NewReader(string_json))
	if err != nil {
		panic(err)
	}
	// 命名请求头
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
	fmt.Println("回执:", string(b))
	defer resp.Body.Close()
}

// 查看固定TransactionID节点后的全部变化
func (O *OandaObj) GetAccountChange(sinceTransactionID string) map[string]([]map[string]string) {
	req, err := http.NewRequest("GET", O.base_url+"/v3/accounts/"+O.User_config.Account+"/changes?sinceTransactionID="+sinceTransactionID, nil)
	if err != nil {
		panic(err)
	}
	// 命名请求头
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

	var p map[string](map[string]([]map[string]string))
	json.Unmarshal(b, &p)

	return p["changes"]
}

func (O *OandaObj) InsIdQuickCheck() []string {
	// 获取所有合约对应id
	id_json := O.GetAccountInstuments()
	ins_list := make([]string, 0)
	for i := 0; i < len(id_json); i++ {
		ins_list = append(ins_list, id_json[i]["displayName"])
	}

	// 依次查询每个合约对应M1bar,检查有效的bar
	useful_ins_list := make([]string, 0)
	para := map[string]string{"price": "AB", "granularity": "M1", "from": "2023-01-01T03:40:00Z", "count": "10"}
	fmt.Printf("[get instrument] processing...")
	for i := 0; i < len(ins_list); i++ {
		if i%5 == 0 {
			fmt.Printf(">")
		}
		temp_name := ""
		for j := 0; j < len(ins_list[i]); j++ {
			if string(ins_list[i][j]) == "/" {
				temp_name += "_"
			} else {
				temp_name += string(ins_list[i][j])
			}
		}
		a := O.GetBar(temp_name, para)
		if len(a) > 5 {
			useful_ins_list = append(useful_ins_list, temp_name)
		}
	}

	return useful_ins_list
}

func (O *OandaObj) InsIdQuickCheckH() []string {
	answer := []string{"NZD_CAD", "EUR_SGD", "EUR_AUD", "TRY_JPY", "USD_SGD", "EUR_SEK", "AUD_CHF", "HKD_JPY", "GBP_AUD", "USD_PLN", "CAD_HKD", "USD_CHF", "AUD_HKD", "NZD_CHF", "GBP_CHF", "USD_THB", "GBP_CAD", "EUR_HKD", "CHF_JPY", "GBP_HKD", "EUR_NZD", "AUD_SGD", "EUR_JPY", "EUR_TRY", "USD_JPY", "SGD_JPY", "GBP_ZAR", "ZAR_JPY", "EUR_HUF", "NZD_JPY", "CHF_ZAR", "AUD_JPY", "EUR_CHF", "EUR_ZAR", "USD_HKD", "NZD_HKD", "CAD_JPY", "EUR_USD", "EUR_CAD", "USD_HUF", "USD_MXN", "GBP_USD", "USD_DKK", "USD_ZAR", "USD_CZK", "CAD_CHF", "EUR_DKK", "USD_SEK", "GBP_SGD", "EUR_CZK", "CAD_SGD", "AUD_NZD", "CHF_HKD", "EUR_GBP", "EUR_NOK", "GBP_PLN", "AUD_CAD", "EUR_PLN", "GBP_NZD", "AUD_USD", "USD_CAD", "NZD_USD", "NZD_SGD", "USD_NOK", "USD_CNH", "SGD_CHF", "USD_TRY", "GBP_JPY"}
	return answer
}
