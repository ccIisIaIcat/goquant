package strategy

import (
	"errors"
	"global"
	"log"
	"os"
	"sync"
	"time"
)

// 写一个基于网格的demo交易，用来重排一下部署流程
type Strategy struct {
	// Public
	// 数据源
	Tick_price_chan chan global.Tick_info // 用于接收tick信息
	Bar_price_chan  chan global.Price_dic
	// 输出项
	Signal_chan chan global.Trade_signal
	// 回执项
	Signal_backward_chan chan global.Signal_backward // 用于接收数据回执
	// 定义一个方便继承类发出信号的回调函数
	SignalCallBack func(global.Tick_info) (bool, string, string, float64, float64, float64, int)
	// 对输出过的信号进行记录
	Ins_id_list []string                          // 进行交易的合约名称
	Need_close  map[string]global.Position_record // 持仓
	// Day_id      int                               // 日期标识符
	statues_map sync.Map    // 记录交易和持仓状态
	info_map    sync.Map    // 记录交易信息
	trade_loger *log.Logger // 交易log文件

	////////以上为每个策略的固定设置，一下是自定义的导入的结构体////////

}

func (S *Strategy) Init() error {
	// 检查信号通道
	if cap(S.Signal_chan) == 0 {
		return errors.New("missing Signal_chan")
	}
	// 检查数据源
	if cap(S.Tick_price_chan) == 0 && cap(S.Bar_price_chan) == 0 {
		return errors.New("missing bar/tick")
	}
	// 检查数据回执
	if cap(S.Signal_backward_chan) == 0 {
		panic("missing Signal_backward_chan")
	}
	// 声明log对象
	var err error
	_, err = os.Stat("log_record")
	if err != nil {
		os.Mkdir("log_record", os.ModePerm)
	}
	file := "./log_record/" + time.Now().Format("2006-01-02") + "_trade_log" + ".txt"
	logFile, err := os.OpenFile(file, os.O_RDWR|os.O_CREATE|os.O_APPEND, 0766)
	if err != nil {
		panic(err)
	}
	S.trade_loger = log.New(logFile, "[trade]", log.Ldate|log.Ltime|log.Lmicroseconds)

	S.statues_map = sync.Map{}
	for i := 0; i < len(S.Ins_id_list); i++ {
		S.statues_map.Store(S.Ins_id_list[i]+"_"+"state", "sleep")
		S.statues_map.Store(S.Ins_id_list[i]+"_"+"hold", "no")
	}
	S.info_map = sync.Map{}
	for i := 0; i < len(S.Ins_id_list); i++ {
		S.info_map.Store(S.Ins_id_list[i]+"_"+"direction", "")
		S.info_map.Store(S.Ins_id_list[i]+"_"+"win_price", 0.)
		S.info_map.Store(S.Ins_id_list[i]+"_"+"lose_price", 0.)
		S.info_map.Store(S.Ins_id_list[i]+"_"+"amount", 0)
	}

	S.Need_close = make(map[string]global.Position_record, 0)

	//自定义//////////////////////////////////////////////////////////////

	return nil

}

func (S *Strategy) CheckClose(t_price global.Tick_info) bool {
	var judge global.Position_record
	if S.Need_close[t_price.Ins_id] == judge {
		return false
	}
	direction := S.Need_close[t_price.Ins_id].Direction
	win_price := S.Need_close[t_price.Ins_id].Stop_price_win
	lose_price := S.Need_close[t_price.Ins_id].Stop_price_lose
	amount := S.Need_close[t_price.Ins_id].Amount
	// S.trade_loger.Println("止盈止损检查:")
	// S.trade_loger.Println("检查信号:", direction, win_price, lose_price, amount)
	// S.trade_loger.Println("当前价格:", "ask:", t_price.AskPrice1, "bid:", t_price.BidPrice1)
	// //若有满足，把合约状态标记为busy，写入最新价格，发单
	if direction == "买" && t_price.BidPrice1 >= win_price {
		// 最新价卖出(止盈)
		close_type := "平今"
		temp_time := time.Now().Format("2006-01-02 15:04:05")
		if !global.SameTradeDayJudge(S.Need_close[t_price.Ins_id].Day_record, temp_time) {
			close_type = "平昨"
		}
		temp_signal := global.Trade_signal{Ins_id: t_price.Ins_id, Open_Close: "平仓", Closing_type: close_type, Direction: "卖", Price: t_price.BidPrice1, Amount: amount}
		S.Signal_chan <- temp_signal
		S.trade_loger.Println("止盈", temp_signal)
		S.statues_map.Store(t_price.Ins_id+"_"+"state", "busy")
	} else if direction == "买" && t_price.BidPrice1 <= lose_price {
		// 最新价买入(止损）
		close_type := "平今"
		temp_time := time.Now().Format("2006-01-02 15:04:05")
		if !global.SameTradeDayJudge(S.Need_close[t_price.Ins_id].Day_record, temp_time) {
			close_type = "平昨"
		}
		temp_signal := global.Trade_signal{Ins_id: t_price.Ins_id, Open_Close: "平仓", Closing_type: close_type, Direction: "卖", Price: t_price.BidPrice1, Amount: amount}
		S.Signal_chan <- temp_signal
		S.trade_loger.Println("止损", temp_signal)
		S.statues_map.Store(t_price.Ins_id+"_"+"state", "busy")
	} else if direction == "卖" && t_price.AskPrice1 >= lose_price {
		// 最新价卖出(止损)
		close_type := "平今"
		temp_time := time.Now().Format("2006-01-02 15:04:05")
		if !global.SameTradeDayJudge(S.Need_close[t_price.Ins_id].Day_record, temp_time) {
			close_type = "平昨"
		}
		temp_signal := global.Trade_signal{Ins_id: t_price.Ins_id, Open_Close: "平仓", Closing_type: close_type, Direction: "买", Price: t_price.AskPrice1, Amount: amount}
		S.Signal_chan <- temp_signal
		S.trade_loger.Println("止损:", temp_signal)
		S.statues_map.Store(t_price.Ins_id+"_"+"state", "busy")
	} else if direction == "卖" && t_price.AskPrice1 <= win_price {
		// 最新价卖出(止盈)
		close_type := "平今"
		temp_time := time.Now().Format("2006-01-02 15:04:05")
		if !global.SameTradeDayJudge(S.Need_close[t_price.Ins_id].Day_record, temp_time) {
			close_type = "平昨"
		}
		temp_signal := global.Trade_signal{Ins_id: t_price.Ins_id, Open_Close: "平仓", Closing_type: close_type, Direction: "买", Price: t_price.AskPrice1, Amount: amount}
		S.Signal_chan <- temp_signal
		S.trade_loger.Println("止盈:", temp_signal)
		S.statues_map.Store(t_price.Ins_id+"_"+"state", "busy")
	}

	return true
}

func (S *Strategy) OpenSignalSend(Ins_id string, direction string, open_price float64, win_price float64, lose_price float64, amount int) {
	// // 把合约状态标记为busy
	S.statues_map.Store(Ins_id+"_"+"state", "busy")
	// // 根据openDirection(开仓方向),openPrice(开仓价格),winPrice(止盈价格),losePrice(止损价格)发单，并写入对应合约的info_map
	temp_signal := global.Trade_signal{Ins_id: Ins_id, Open_Close: "开仓", Direction: direction, Price: open_price, Amount: amount}
	S.trade_loger.Println("开仓信号:", temp_signal, "止盈:", win_price, "止损:", lose_price)
	S.Signal_chan <- temp_signal
	S.info_map.Store(Ins_id+"_"+"direction", direction)
	S.info_map.Store(Ins_id+"_"+"win_price", win_price)
	S.info_map.Store(Ins_id+"_"+"lose_price", lose_price)
	S.info_map.Store(Ins_id+"_"+"amount", amount)
}

// 判断回执信息，若类型为成交，合约状态标记为sleep
// // 若开仓成功，记录持仓为yes，记录持仓map(查询infomap填上止盈止损和方向,day_id)
// // 若平仓成功，记录持仓为no，查询对应持仓id并在持仓map中删除
// 判断回执信息，若类型为回执，且不为”报单已提交“/”全部成交报单已提交“，合约状态标记为sleep
func (S *Strategy) CheckRespon(temp_backward global.Signal_backward) {
	if temp_backward.Info_type == "成交" {
		S.statues_map.Store(temp_backward.Ins_id+"_"+"state", "sleep")
		// 若开仓成功
		// 若开仓
		if temp_backward.OffsetFlag == "0" {
			S.statues_map.Store(temp_backward.Ins_id+"_"+"hold", "yes")
			// 记录持仓
			direction, _ := S.info_map.Load(temp_backward.Ins_id + "_" + "direction")
			win_price, _ := S.info_map.Load(temp_backward.Ins_id + "_" + "win_price")
			lose_price, _ := S.info_map.Load(temp_backward.Ins_id + "_" + "lose_price")
			amount, _ := S.info_map.Load(temp_backward.Ins_id + "_" + "amount")
			temp_position := global.Position_record{Ins_id: temp_backward.Ins_id, Direction: direction.(string), Stop_price_win: win_price.(float64), Stop_price_lose: lose_price.(float64), Day_record: time.Now().Format("2006-01-02 15:04:05"), Amount: amount.(int)}
			// fmt.Println(S.Day_id)
			// S.trade_loger.Println(temp_backward)
			S.Need_close[temp_backward.Ins_id] = temp_position
		}
		// 若平仓
		if temp_backward.OffsetFlag == "3" {
			// 清空持仓
			var null_position global.Position_record
			S.Need_close[temp_backward.Ins_id] = null_position
			S.statues_map.Store(temp_backward.Ins_id+"_"+"hold", "no")

		}
	} else {
		if temp_backward.StatusMsg == "报单已提交" || temp_backward.StatusMsg == "全部成交报单已提交" {

		} else {
			S.statues_map.Store(temp_backward.Ins_id+"_"+"state", "sleep")
		}
	}

}

// 依次处理传入的tick/bar，判断是否有信号生成
func (S *Strategy) Start() {
	// tick
	go func() {
		for {
			t_price := <-S.Tick_price_chan
			/////////平仓检查
			state, _ := S.statues_map.Load(t_price.Ins_id + "_" + "state")
			hold, _ := S.statues_map.Load(t_price.Ins_id + "_" + "hold")
			// 判断对应合约状态是否为sleep，判断对应合约持仓是否为yes，判断是否止盈止损
			if state.(string) == "sleep" && hold.(string) == "yes" {
				S.CheckClose(t_price)
				/////////开仓检查
			} else if state.(string) == "sleep" && hold.(string) == "no" { // 判断对应合约状态是否为sleep，判断对应合约持仓是否为no
				signal_judge, insid, direction, open_price, win_price, lose_price, amount := S.CheckSignal(t_price)
				if signal_judge {
					// S.trade_loger.Println("信号：//", signal_judge, insid, direction, open_price, win_price, lose_price, amount)
					S.OpenSignalSend(insid, direction, open_price, win_price, lose_price, amount)
				}
			}
		}
	}()

	// respon
	go func() {
		for {
			temp_backward := <-S.Signal_backward_chan
			S.trade_loger.Println(temp_backward)
			S.CheckRespon(temp_backward)
		}
	}()

}

// 输入tick价格，返回是否是信号，开仓方向，开仓价格，止盈价格，止损价格(添加合约id)
func (S *Strategy) CheckSignal(tick_price global.Tick_info) (bool, string, string, float64, float64, float64, int) {

	return S.SignalCallBack(tick_price)
}
