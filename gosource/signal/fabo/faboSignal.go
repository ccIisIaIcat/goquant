package fabo

import (
	"global"
	"math"
)

type FaboSignal struct {
	Zigzag_count int                 // 计算信号所需要的高低点个数
	zigzag_list  []global.Cur_obj    // 计算信号所需要的高低点价格信息列表
	prev_zigzag  global.Cur_obj      // 上一个高低点的价格信息
	cur_price    global.Price_dic    //当前价格
	cur_state    int                 // 当前状态，0：低点；1：高点
	cur_close    float64             // 当前高低点的收盘价
	signal_list  []global.Signal_obj // 信号点列表，基础元素为字典
	start_time   string              // 信号起始时间
	signal_type  int                 //信号涨跌类型，其中取值，0：跌；1：涨
	cur_high     float64
	cur_low      float64
}

func (F *FaboSignal) Init() {
	F.zigzag_list = make([]global.Cur_obj, 0)
	F.signal_list = make([]global.Signal_obj, 0)
	F.Zigzag_count = 2
}

func (F *FaboSignal) Recognize(zigzag_dict global.Cur_obj, price_dict global.Price_dic) {
	F.cur_price = price_dict
	F.cur_high = price_dict.High
	F.cur_low = price_dict.Low
	if len(F.zigzag_list) == 0 {
		temp_dic := zigzag_dict
		F.zigzag_list = append(F.zigzag_list, temp_dic)
		F.prev_zigzag = F.zigzag_list[len(F.zigzag_list)-1]
	}
	F.cur_state = zigzag_dict.Type
	F.cur_close = F.cur_price.Close
	// 如果传入的价格信息与之前最后一个的type一致，则更新最后一个，否则，则向zigzag_list中添加该信息
	if F.prev_zigzag.Type == zigzag_dict.Type {
		temp_dic := zigzag_dict
		F.zigzag_list[len(F.zigzag_list)-1] = temp_dic
	} else if F.prev_zigzag.Type != zigzag_dict.Type {
		temp_dic := zigzag_dict
		if len(F.zigzag_list) < F.Zigzag_count {
			F.zigzag_list = append(F.zigzag_list, temp_dic)
		} else {
			F.zigzag_list = append(F.zigzag_list, temp_dic)
			F.zigzag_list = F.zigzag_list[1:]
		}

	}
	F.prev_zigzag = F.zigzag_list[len(F.zigzag_list)-1]
	if len(F.zigzag_list) == F.Zigzag_count {
		// 判断当前的zigzag_list是否为信号
		// fmt.Println("zigzag_list:", F.zigzag_list)
		gen_sig := false
		if F.cur_price.Date_time != F.zigzag_list[1].Date_time {
			gen_sig = F.rule()
		}
		if gen_sig && F.start_time != F.zigzag_list[0].Date_time {
			cur_signal := global.Signal_obj{P1_price: F.zigzag_list[0].Price, P1_time: F.zigzag_list[0].Date_time, P2_price: F.zigzag_list[1].Price, P2_time: F.zigzag_list[1].Date_time, P3_time: F.cur_price.Date_time, Type: F.signal_type}
			if F.signal_type == 0 {
				cur_signal.P3_price = F.cur_close
			} else if F.signal_type == 1 {
				cur_signal.P3_price = F.cur_close
			}
			temp_signal := cur_signal
			F.signal_list = append(F.signal_list, temp_signal)
			F.start_time = F.zigzag_list[0].Date_time
		}
	}
}

// 防止signal_list 过长
func (F *FaboSignal) Shrunk_size(Max_length int) {
	if len(F.signal_list) > Max_length {
		F.signal_list = F.signal_list[len(F.signal_list)-Max_length:]
	}
}

func (F *FaboSignal) rule() bool {
	gen_sig := false
	F.signal_type = 0
	cur_sts := F.zigzag_list[len(F.zigzag_list)-1].Type
	// fmt.Println(cur_sts)
	hl0 := F.zigzag_list[len(F.zigzag_list)-2].Price
	hl1 := F.zigzag_list[len(F.zigzag_list)-1].Price
	delta0 := math.Abs(hl0 - hl1)
	if cur_sts == 0 {
		delta1 := F.cur_close - hl1
		rate0 := delta1 / delta0
		// fmt.Println(rate0)
		if rate0 >= 0.48 && rate0 <= 0.52 {
			F.signal_type = 0
			gen_sig = true
		}
	} else {
		delta1 := hl1 - F.cur_close
		rate0 := delta1 / delta0
		// fmt.Println(rate0)
		if rate0 >= 0.48 && rate0 <= 0.52 {
			F.signal_type = 1
			gen_sig = true
		}
	}

	return gen_sig
}

func (F *FaboSignal) Current_signal() global.Signal_obj {
	if len(F.signal_list) == 0 {
		an := global.Signal_obj{}
		return an
	} else {
		return F.signal_list[len(F.signal_list)-1]
	}

}
