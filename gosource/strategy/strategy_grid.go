package strategy

import (
	"fmt"
	"global"
)

// 写一个基于网格的demo交易，用来重排一下部署流程
type GridStrategy struct {
	Strategy
	Ins_id_list []string // 进行交易的合约名称
}

func (G *GridStrategy) Init() {
	G.SignalCallBack = G.Signal
	G.Strategy.Init()
}

// 在Strategy每有新的tick信息该函数都会被回调
func (G *GridStrategy) Signal(t_price global.Tick_info) (bool, string, string, float64, float64, float64, int) {
	if t_price.Ins_id == "ag2306" {
		fmt.Println(t_price.AskPrice1)
		fmt.Println(true, "ag2306", "买", t_price.AskPrice1, t_price.BidPrice1+3, t_price.BidPrice1-5, 500)
		return true, "ag2306", "买", t_price.AskPrice1, t_price.BidPrice1 + 3, t_price.BidPrice1 - 5, 500
	}
	return false, "", "", 0, 0, 0, 0
}
