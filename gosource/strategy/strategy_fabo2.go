package strategy

import (
	"fabo"
	"fmt"
	"genbar"
	"global"
	"log"
	"os"
	"sync"
	"time"
	"zigzag"
)

// 写一个基于网格的demo交易，用来重排一下部署流程
type FaboStrategy2 struct {
	Strategy
	// Private
	zigzag_map   map[string]*zigzag.Zigzag   // 为每一个合约创建一个zigzag对象
	fabo_map     map[string]*fabo.FaboSignal // 为每一个合约创建一个fabo对象
	signal_loger *log.Logger                 // 用于记录本地的全部信号信息
	Last_p3_time map[string]string           // 每一个品种最新fabo特征的时间
	// 用于生成bar数据
	genbar_obj       genbar.Genbar
	genbar_tick_chan chan global.Tick_info
	genbar_min_chan  chan global.Price_dic
	// 记录不同品种最新的买一价和卖一价
	temp_ask sync.Map
	temp_bid sync.Map
}

func (G *FaboStrategy2) Init() {
	// 用于产生分钟数据
	G.genbar_tick_chan = make(chan global.Tick_info, 200)
	G.genbar_min_chan = make(chan global.Price_dic, 200)
	G.genbar_obj = genbar.Genbar{Tick_info_channel: G.genbar_tick_chan, Bar_chan: G.genbar_min_chan}
	G.genbar_obj.Init()
	go G.genbar_obj.GenbarByStream()
	// 最新卖一价和买一价
	G.temp_ask = sync.Map{}
	G.temp_bid = sync.Map{}

	file := "./log_record/" + time.Now().Format("2006-01-02") + "_signal_log" + ".txt"
	logFile, err := os.OpenFile(file, os.O_RDWR|os.O_CREATE|os.O_APPEND, 0766)
	if err != nil {
		panic(err)
	}
	G.signal_loger = log.New(logFile, "[signal]", log.Ldate|log.Ltime|log.Lmicroseconds)

	G.Last_p3_time = make(map[string]string, 0)
	G.zigzag_map = make(map[string]*zigzag.Zigzag, 0)
	G.fabo_map = make(map[string]*fabo.FaboSignal, 0)
	if len(G.Ins_id_list) == 0 {
		panic("策略需要至少指定一个交易合约,但Ins_id_list为空")
	}
	// 为每一个合约创建一个zigzag对象，实时计算zigzag指标
	for i := 0; i < len(G.Ins_id_list); i++ {
		temp_zigzag := zigzag.Zigzag{Bar_count: 30}
		temp_zigzag.Init()
		G.zigzag_map[G.Ins_id_list[i]] = &temp_zigzag
	}
	// 为每一个合约创建一个fabo对象，实时计算fabo指标
	for i := 0; i < len(G.Ins_id_list); i++ {
		temp_fabo := fabo.FaboSignal{}
		temp_fabo.Init()
		G.fabo_map[G.Ins_id_list[i]] = &temp_fabo
	}

	G.SignalCallBack = G.Signal
	G.Strategy.Init()

	global.Never_stop_direct()
}

func (G *FaboStrategy2) LocalGenBar(t_price global.Tick_info) global.Price_dic {
	bar_dic := global.Price_dic{}

	return bar_dic
}

// 在Strategy每有新的tick信息该函数都会被回调
func (G *FaboStrategy2) Signal(t_price global.Tick_info) (bool, string, string, float64, float64, float64, int) {
	// 生成分钟数据
	G.genbar_tick_chan <- t_price
	G.temp_ask.Store(t_price.Ins_id, t_price.AskPrice1)
	G.temp_bid.Store(t_price.Ins_id, t_price.BidPrice1)

	// 判断是否有分钟数据生成，若有计算指标
	for len(G.genbar_min_chan) != 0 {
		bar_price := <-G.genbar_min_chan
		G.zigzag_map[bar_price.Ins_id].Compute(bar_price)
		cur_zigzag := G.zigzag_map[bar_price.Ins_id].Current_zigzag()
		// S.test_loger.Println("[生成zigzag信号]", bar_price.Ins_id, cur_zigzag)
		G.fabo_map[bar_price.Ins_id].Recognize(cur_zigzag, bar_price)
		cur_signal := G.fabo_map[bar_price.Ins_id].Current_signal()
		fmt.Println(cur_signal)
		if cur_signal.P3_time != "" && cur_signal.P3_time != G.Last_p3_time[bar_price.Ins_id] {
			G.fabo_map[bar_price.Ins_id].Shrunk_size(30)
			G.zigzag_map[bar_price.Ins_id].Shrunk_size(30)
			temp_winprice, temp_loseprice := G.win_lose_price(cur_signal)
			G.Last_p3_time[bar_price.Ins_id] = cur_signal.P3_time
			fmt.Println("/////", cur_signal.Type)
			if cur_signal.Type == 1 {
				temp_price, _ := G.temp_ask.Load(bar_price.Ins_id)
				G.signal_loger.Println(true, bar_price.Ins_id, "买", temp_price.(float64), temp_winprice, temp_loseprice, 1)
				return true, bar_price.Ins_id, "买", temp_price.(float64), temp_winprice, temp_loseprice, 1
			} else {
				temp_price, _ := G.temp_bid.Load(bar_price.Ins_id)
				G.signal_loger.Println(true, bar_price.Ins_id, "卖", temp_price.(float64), temp_winprice, temp_loseprice, 1)
				return true, bar_price.Ins_id, "卖", temp_price.(float64), temp_winprice, temp_loseprice, 1
			}

		}

	}

	return false, "", "", 0, 0, 0, 0
}

func (F *FaboStrategy2) win_lose_price(signal_dict global.Signal_obj) (float64, float64) {
	cur_signal := signal_dict
	hl0 := cur_signal.P1_price
	hl1 := cur_signal.P2_price
	hl2 := cur_signal.P3_price
	delta0 := hl1 - hl0 // 当信号状态表示上升时，为正数；当信号状态表示下降时，为负数。
	delta1 := hl2 - hl1 // 当信号状态表示上升时，为负数；当信号状态表示下降时，为正数。
	tp := 0.382
	sl := 0.618
	win_price, lose_price := 0., 0.
	// 计算止盈价格
	lose_price = hl1 - sl*delta0
	win_price = hl2 - tp*delta1
	return win_price, lose_price

}
