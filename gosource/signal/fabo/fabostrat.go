package fabo

import (
	"global"
	"math"
)

type FaboStrat struct {
	tp          float64
	sl          float64
	tole        float64
	Signal_list []global.Signal_obj
	Profit_dict map[string]Profit_obj
}

type Profit_obj struct {
	Open_price  float64
	Close_time  string
	Close_price float64
	Profit      float64
	Profit_rate float64
	Tp_rate     float64
	Sl_rate     float64
	Type        int
}

func (F *FaboStrat) Init() {
	F.tp = 0.382
	F.sl = 0.618
	F.tole = 0.001
	F.Signal_list = make([]global.Signal_obj, 0)
	F.Profit_dict = make(map[string]Profit_obj, 0)
}

func (F *FaboStrat) Profit_tick(signal_dict global.Signal_obj, price float64, datetime string) Profit_obj {
	// fmt.Println(signal_dict)
	cur_signal := signal_dict
	hl0 := cur_signal.P1_price
	hl1 := cur_signal.P2_price
	hl2 := cur_signal.P3_price
	crtype := cur_signal.Type
	delta0 := math.Abs(hl0 - hl1)
	delta1 := math.Abs(hl1 - hl2)
	tp_rate, sl_rate := 0., 0.
	delta2 := 0.
	if crtype == 0 {
		delta2 = hl2 - price
		if delta2 < 0 {
			delta3 := hl1 - price
			sl_rate = delta3 / delta0
		} else {
			tp_rate = delta2 / delta1
		}
	} else if crtype == 1 {
		delta2 = price - hl2
		if delta2 < 0 {
			delta3 := price - hl1
			sl_rate = delta3 / delta0
		} else {
			tp_rate = delta2 / delta1
		}
	}
	if ((tp_rate > F.tp) || (-sl_rate > F.sl)) && math.Abs(hl0-hl1)/hl0 > 0.001 {
		temp_profit_obj := Profit_obj{Open_price: hl2, Close_time: datetime, Close_price: price, Profit: delta2, Profit_rate: delta2 / hl2, Tp_rate: tp_rate, Sl_rate: sl_rate, Type: crtype}

		return temp_profit_obj
	} else {
		temp_profit_obj := Profit_obj{Close_time: "-1"}
		return temp_profit_obj
	}

}

func (F *FaboStrat) Profit(signal_dict global.Signal_obj, price_dict global.Price_dic) {
	if len(F.Signal_list) != 0 {
		if F.Signal_list[len(F.Signal_list)-1].P3_time != signal_dict.P3_time {
			temp_dic := signal_dict
			if temp_dic.P3_time != "" {
				F.Signal_list = append(F.Signal_list, temp_dic)
			}
		}
		for i := 0; i < len(F.Signal_list); i++ {
			cur_signal := F.Signal_list[i]
			crtime := cur_signal.P3_time
			_, ok := F.Profit_dict[crtime]
			if ok {
				continue
			}
			hl0 := cur_signal.P1_price
			hl1 := cur_signal.P2_price
			hl2 := cur_signal.P3_price
			crtype := cur_signal.Type
			delta0 := math.Abs(hl0 - hl1)
			delta1 := math.Abs(hl1 - hl2)
			tp_rate, sl_rate := 0., 0.
			delta2 := 0.
			if crtype == 0 {
				delta2 = hl2 - price_dict.Close
				if delta2 < 0 {
					delta3 := hl1 - price_dict.Close
					sl_rate = delta3 / delta0
				} else {
					tp_rate = delta2 / delta1
				}
			} else if crtype == 1 {
				delta2 = price_dict.Close - hl2
				if delta2 < 0 {
					delta3 := price_dict.Close - hl1
					sl_rate = delta3 / delta0
				} else {
					tp_rate = delta2 / delta1
				}
			}
			if (tp_rate > F.tp) || (-sl_rate > F.sl) {
				temp_profit_obj := Profit_obj{Open_price: hl2, Close_time: price_dict.Date_time, Close_price: price_dict.Close, Profit: delta2, Profit_rate: delta2 / hl2, Tp_rate: tp_rate, Sl_rate: sl_rate, Type: crtype}
				F.Profit_dict[crtime] = temp_profit_obj
				// fmt.Println(temp_profit_obj.Profit)
			}
		}
	} else {
		temp_dic := signal_dict
		if temp_dic.P3_time != "" {
			F.Signal_list = append(F.Signal_list, temp_dic)
		}
	}
}
