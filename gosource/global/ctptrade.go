package global

type Trade_signal struct {
	Ins_id       string  // 合约名称
	Open_Close   string  // 开仓还是平仓
	Closing_type string  // 如果是平仓，是今平还是昨平
	Direction    string  // 开仓买卖方向/平仓买卖方向
	Price        float64 // 期望成交价格
	Stop_price   float64 // 止损价格
	Amount       int     // 期望成交笔数
	Exchange     string  // 交易所

	// // 成交类型
	// Trade_type string //成交类型，确定当前成交是一个只报单的成交类型(unreal_time)，还是需要即时tick成交的类型(real_time)
	// //（PS:当成交为即时tick成交类型时，如果在1秒内没有产生成交回执则执行撤单操作，在此执行区间内不允许新的报单提交）

	Start_time int64 // 成交本地开始时间，也作为本地持仓信息的唯一标识
	End_time   int64 // 成交本地完成时间

	More_info []string // 有关该信号的更多的信息
}

type Signal_backward struct {
	Info_type     string  // 响应/成交/错误
	Err_info      string  // 如果是错误，错误的内容
	StatusMsg     string  // 如果是响应，返回委托信息
	Limit_price   float64 // 如果是响应，返回限价价格
	Limit_amount  int     // 如果是响应，返回报单数量
	Deal_price    float64 // 如果是成交，返回成交价格
	Deal_amount   int     // 如果是成交，返回成交数量
	Deal_order_id string  // 如果是成交，返回成交id
	Ins_id        string  // 如果是成交或响应，返回标的品种
	Exc_id        string  // 如果是成交或响应，返回交易所id
	OrderSysID    string  // 如果是成交或响应，返回报单编号
	Direction     string  // 如果是响应或成交，返回交易方向
	OrderRef      string  // 如果是响应或成交，返回报单引用
	OffsetFlag    string  // 如果是响应或成交，返回开平标志

	Side int // 买卖方向

}

type Position_record struct {
	Ins_id          string
	Direction       string
	Stop_price_win  float64
	Stop_price_lose float64
	Day_record      string // 用于判断平今和平昨
	Amount          int    //持仓
}
