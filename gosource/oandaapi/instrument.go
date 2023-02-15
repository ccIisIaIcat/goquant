package oandaapi

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
)

// 行情相关

// 获取最近bar数据(指定个数和间隔秒数,price_type M:中间价，A：asks，B：bids)
func (O *OandaObj) GetBarRecent(InsId string, count string, granularity string, price_type string) []map[string](interface{}) {
	req, err := http.NewRequest("GET", O.base_url+"/v3/instruments/"+InsId+"/candles?count="+count+"&price="+price_type+"&granularity=S"+granularity, nil)
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

	var p map[string]([]map[string](interface{}))
	json.Unmarshal(b, &p)
	return p["candles"]
}

// 获取bar数据(自定义全部参数)
// instrument:	Name of the Instrument [required]
// price:	The Price component(s) to get candlestick data for. [default=M]
// granularity:	The granularity of the candlesticks to fetch [default=S5]
// count:	The number of candlesticks to return in the response. Count should not be specified if both the start and end parameters are provided, as the time range combined with the granularity will determine the number of candlesticks to return. [default=500, maximum=5000]
// from:	The start of the time range to fetch candlesticks for.
// to:	The end of the time range to fetch candlesticks for.
// smooth:	A flag that controls whether the candlestick is “smoothed” or not. A smoothed candlestick uses the previous candle’s close price as its open price, while an un-smoothed candlestick uses the first price from its time range as its open price. [default=False]
// includeFirst:	A flag that controls whether the candlestick that is covered by the from time should be included in the results. This flag enables clients to use the timestamp of the last completed candlestick received to poll for future candlesticks but avoid receiving the previous candlestick repeatedly. [default=True]
// dailyAlignment:	The hour of the day (in the specified timezone) to use for granularities that have daily alignments. [default=17, minimum=0, maximum=23]
// alignmentTimezone:	The timezone to use for the dailyAlignment parameter. Candlesticks with daily alignment will be aligned to the dailyAlignment hour within the alignmentTimezone. Note that the returned times will still be represented in UTC. [default=America/New_York]
// weeklyAlignment:	The day of the week used for granularities that have weekly alignment. [default=Friday]
func (O *OandaObj) GetBar(InsId string, parameter map[string]string) []map[string](interface{}) {
	// 生成参数部分
	para_str := ""
	for k, v := range parameter {
		para_str += k
		para_str += "="
		para_str += v
		para_str += "&"
	}
	para_str = para_str[:len(para_str)-1]
	req, err := http.NewRequest("GET", O.base_url+"/v3/instruments/"+InsId+"/candles?"+para_str, nil)
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

	var p map[string]([]map[string](interface{}))
	json.Unmarshal(b, &p)
	return p["candles"]
}

// 获得订单簿快照
// time	   The time of the snapshot to fetch. If not specified, then the most recent snapshot is fetched.
func (O *OandaObj) GetOrderbook(InsId string, parameter map[string]string) (map[string]string, []interface{}) {
	// 生成参数部分
	para_str := ""
	if len(parameter) > 0 {
		for k, v := range parameter {
			para_str += k
			para_str += "="
			para_str += v
			para_str += "&"
		}
		para_str = para_str[:len(para_str)-1]
	}
	req, err := http.NewRequest("GET", O.base_url+"/v3/instruments/"+InsId+"/orderBook?"+para_str, nil)
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
	var p map[string](map[string](interface{}))
	json.Unmarshal(b, &p)
	for k := range p["orderBook"] {
		fmt.Println(k)
	}
	info_map := map[string]string{"time": p["orderBook"]["time"].(string), "unixTime": p["orderBook"]["unixTime"].(string), "price": p["orderBook"]["price"].(string), "bucketWidth": p["orderBook"]["bucketWidth"].(string)}
	buckets := p["orderBook"]["buckets"].([]interface{})
	return info_map, buckets
}
