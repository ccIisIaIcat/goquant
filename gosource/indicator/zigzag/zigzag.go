package zigzag

import (
	"global"
	"math"
)

type Zigzag struct {
	Bar_count    int
	Price_list   []global.Price_dic
	Zigzag_list  []global.Cur_obj
	Highlow_list []global.Cur_obj
	Status       int
	cur_high     global.Cur_obj
	cur_low      global.Cur_obj
	inv_max      float64
	inv_min      float64
	pos          int
	prev_pos     int
	preprev_pos  int
}

func (Z *Zigzag) Init() {
	Z.Price_list = make([]global.Price_dic, 0)
	Z.Zigzag_list = make([]global.Cur_obj, 0)
	Z.Highlow_list = make([]global.Cur_obj, 0)
	Z.Status = 0
	Z.cur_high = global.Cur_obj{Date_time: "1970-01-01", Price: math.Inf(-1), Close: math.Inf(-1), Dist: 1, Type: 1}
	Z.cur_low = global.Cur_obj{Date_time: "1970-01-01", Price: math.Inf(1), Close: math.Inf(1), Dist: 1, Type: 0}
	Z.inv_max = Z.cur_high.Price
	Z.inv_min = Z.cur_low.Price
	Z.pos = 0
	Z.prev_pos = 0
	Z.preprev_pos = -1
}

func (Z *Zigzag) Compute(price_dic global.Price_dic) {
	if Z.Status == 1 {
		if price_dic.High > Z.inv_max && price_dic.High > Z.cur_high.Price {
			Z.cur_high.Date_time = price_dic.Date_time
			Z.cur_high.Price = price_dic.High
			Z.cur_high.Close = price_dic.Close
			Z.cur_high.Volumn = price_dic.Volumn
			Z.cur_high.Dist = Z.pos - Z.prev_pos + 1
			Z.prev_pos = Z.pos
			temp_cur := Z.cur_high
			Z.Zigzag_list = append(Z.Zigzag_list, temp_cur)
		} else if price_dic.Low < Z.inv_min {
			Z.cur_low.Date_time = price_dic.Date_time
			Z.cur_low.Price = price_dic.Low
			Z.cur_low.Close = price_dic.Close
			Z.cur_low.Volumn = price_dic.Volumn
			Z.cur_low.Dist = Z.pos - Z.prev_pos + 1
			// 更新当前zigzag的状态为下降
			Z.Status = 0
			Z.prev_pos = Z.pos
			temp_cur := Z.cur_low
			Z.Zigzag_list = append(Z.Zigzag_list, temp_cur)
		}
	} else if Z.Status == 0 {
		if price_dic.Low < Z.inv_min && price_dic.Low < Z.cur_low.Price {
			Z.cur_low.Date_time = price_dic.Date_time
			Z.cur_low.Price = price_dic.Low
			Z.cur_low.Close = price_dic.Close
			Z.cur_low.Volumn = price_dic.Volumn
			Z.cur_low.Dist = Z.pos - Z.prev_pos + 1
			Z.prev_pos = Z.pos
			temp_cur := Z.cur_low
			Z.Zigzag_list = append(Z.Zigzag_list, temp_cur)
		} else if price_dic.High > Z.inv_max {
			Z.cur_high.Date_time = price_dic.Date_time
			Z.cur_high.Price = price_dic.High
			Z.cur_high.Close = price_dic.Close
			Z.cur_high.Volumn = price_dic.Volumn
			Z.cur_high.Dist = Z.pos - Z.prev_pos + 1
			//更新当前状态为上升
			Z.Status = 1
			Z.prev_pos = Z.pos
			temp_cur := Z.cur_high
			Z.Zigzag_list = append(Z.Zigzag_list, temp_cur)
		}
	}
	Z.pos += 1
	// 更新price_list
	if len(Z.Price_list) >= Z.Bar_count {
		Z.Price_list = append(Z.Price_list, price_dic)[1:]
	} else {
		Z.Price_list = append(Z.Price_list, price_dic)
	}
	// 更新区间最大值的最大值和最小值的最小值
	temp_max := math.Inf(-1)
	temp_min := math.Inf(1)
	for i := 0; i < len(Z.Price_list); i++ {
		if Z.Price_list[i].High > temp_max {
			temp_max = Z.Price_list[i].High
		}
		if Z.Price_list[i].Low < temp_min {
			temp_min = Z.Price_list[i].Low
		}
	}
	Z.inv_max = temp_max
	Z.inv_min = temp_min

	if Z.check_hl() {
		if len(Z.Highlow_list) != 0 {
			if Z.Highlow_list[len(Z.Highlow_list)-1] != Z.Highlow_list[len(Z.Highlow_list)-2] {
				Z.Highlow_list = append(Z.Highlow_list, Z.Highlow_list[len(Z.Highlow_list)-2])
			} else {
				Z.Highlow_list = append(Z.Highlow_list, Z.Zigzag_list[len(Z.Zigzag_list)-2])
			}
		}
	}

}

func (Z *Zigzag) check_hl() bool {
	h1_flag := false
	if len(Z.Zigzag_list) > 1 {
		h1_flag = (Z.Zigzag_list[len(Z.Zigzag_list)-1].Type != Z.Zigzag_list[len(Z.Zigzag_list)-2].Type)
	}
	return h1_flag
}

func (Z *Zigzag) Current_zigzag() global.Cur_obj {
	return Z.Zigzag_list[len(Z.Zigzag_list)-1]
}

// 防止zigzag_list 过长
func (Z *Zigzag) Shrunk_size(Max_length int) {
	if len(Z.Zigzag_list) > Max_length {
		Z.Zigzag_list = Z.Zigzag_list[len(Z.Zigzag_list)-Max_length:]
	}
}
