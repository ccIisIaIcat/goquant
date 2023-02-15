package fake

import (
	"errors"
	"global"
)

// 用于接收信号数据，并根据信号生成伪回执
type FakeTrade struct {
	Signal_chan           chan global.Trade_signal
	Signal_backward_chan  chan global.Signal_backward
	Connection_check_chan chan string
}

func (F *FakeTrade) Init() {
	if cap(F.Signal_chan) == 0 {
		panic(errors.New("missing Signal_chan"))
	}
	if cap(F.Signal_backward_chan) == 0 {
		panic(errors.New("missing Siganl_backward_chan"))
	}
	F.Connection_check_chan = make(chan string, 5)
}

// 接收数据，并返回对应的成交完成回执
func (F *FakeTrade) Start() {
	info := "伪交易流开启成功"
	F.Connection_check_chan <- info
	for {
		temp_siganl := <-F.Signal_chan
		temp_siganl_backward := global.Signal_backward{Info_type: "委托回执", StatusMsg: "全部成交报单已提交", Limit_price: temp_siganl.Price, Limit_amount: 1, Ins_id: temp_siganl.Ins_id, Exc_id: temp_siganl.Exchange, Direction: temp_siganl.Direction, OffsetFlag: temp_siganl.Open_Close}
		F.Signal_backward_chan <- temp_siganl_backward
	}

}
