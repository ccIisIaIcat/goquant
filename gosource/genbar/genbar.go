package genbar

import (
	"global"
	"time"
)

// 连接一个chan输入tick信息，生成一个chan输出分钟信息
type Genbar struct {
	Tick_info_channel chan global.Tick_info
	Bar_chan          chan global.Price_dic
	bar_record        map[string]*global.Price_dic //记录不同品种最新bar的信息
}

func (G *Genbar) Init() {
	G.bar_record = make(map[string]*global.Price_dic, 0)
	if cap(G.Bar_chan) == 0 {
		panic("missing Bar_chan")
	}
}

// 根据时间信息生成bar
func (G *Genbar) GenbarByTime() {
	temp_signal := false
	for {
		time.Sleep(time.Millisecond * 10)
		temp_time := time.Now().Format("2006-01-02 15:04")
		// 判断是否有时间数据生成
		for _, v := range G.bar_record {
			if v.Date_time != temp_time {
				temp_signal = true
				break
			}
		}
		if temp_signal {
			for _, v := range G.bar_record {
				G.Bar_chan <- *v
			}
			G.bar_record = make(map[string]*global.Price_dic, 0)
			temp_signal = false
		}

		for len(G.Tick_info_channel) != 0 {
			tick_info := <-G.Tick_info_channel
			if _, ok := G.bar_record[tick_info.Ins_id]; !ok {
				G.bar_record[tick_info.Ins_id] = &global.Price_dic{Ins_id: tick_info.Ins_id, Date_time: temp_time, Open: tick_info.Last_price, High: tick_info.Last_price, Low: tick_info.Last_price, Close: tick_info.Last_price, Volumn: tick_info.Volume, Update_ask: tick_info.AskPrice1, Update_bid: tick_info.BidPrice1}
			} else {
				G.bar_record[tick_info.Ins_id].Close = tick_info.Last_price
				G.bar_record[tick_info.Ins_id].Update_ask = tick_info.AskPrice1
				G.bar_record[tick_info.Ins_id].Update_bid = tick_info.BidPrice1
				if tick_info.Last_price > G.bar_record[tick_info.Ins_id].High {
					G.bar_record[tick_info.Ins_id].High = tick_info.Last_price
				}
				if tick_info.Last_price < G.bar_record[tick_info.Ins_id].Low {
					G.bar_record[tick_info.Ins_id].Low = tick_info.Last_price
				}
				G.bar_record[tick_info.Ins_id].Volumn += tick_info.Volume
			}
		}
	}
}

// 根据数据流信息生成bar
func (G *Genbar) GenbarByStream() {
	// G.bar_record = make(map[string]*global.Price_dic, 0)
	for {
		tick_info := <-G.Tick_info_channel
		// fmt.Println(tick_info)
		temp_time := tick_info.Time[:14]

		if _, ok := G.bar_record[tick_info.Ins_id]; !ok {
			temp_bar := global.Price_dic{Ins_id: tick_info.Ins_id, Date_time: temp_time[:14], Open: tick_info.Last_price, High: tick_info.Last_price, Low: tick_info.Last_price, Close: tick_info.Last_price, Volumn: tick_info.Volume, Update_ask: tick_info.AskPrice1, Update_bid: tick_info.BidPrice1}
			G.bar_record[tick_info.Ins_id] = &temp_bar
		} else {
			if G.bar_record[tick_info.Ins_id].Date_time != temp_time {
				G.Bar_chan <- *G.bar_record[tick_info.Ins_id]
				G.bar_record[tick_info.Ins_id] = &global.Price_dic{Ins_id: tick_info.Ins_id, Date_time: temp_time[:14], Open: tick_info.Last_price, High: tick_info.Last_price, Low: tick_info.Last_price, Close: tick_info.Last_price, Volumn: tick_info.Volume, Update_ask: tick_info.AskPrice1, Update_bid: tick_info.BidPrice1}
			} else {
				G.bar_record[tick_info.Ins_id].Close = tick_info.Last_price
				G.bar_record[tick_info.Ins_id].Update_ask = tick_info.AskPrice1
				G.bar_record[tick_info.Ins_id].Update_bid = tick_info.BidPrice1
				if tick_info.Last_price > G.bar_record[tick_info.Ins_id].High {
					G.bar_record[tick_info.Ins_id].High = tick_info.Last_price
				}
				if tick_info.Last_price < G.bar_record[tick_info.Ins_id].Low {
					G.bar_record[tick_info.Ins_id].Low = tick_info.Last_price
				}
				G.bar_record[tick_info.Ins_id].Volumn += tick_info.Volume
			}
		}
	}
}
