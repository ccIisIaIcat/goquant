package global

type InstrumentsUseField struct {
	InstrumentID   string
	InstrumentName string
	InstLifePhase  string
	ExchangeInstID string
	ExchangeID     string
}

type Tick_info struct {
	Exchange   string
	Ins_id     string
	Time       string
	Last_price float64
	Volume     float64
	Turnover   float64
	AskPrice1  float64
	AskVolume1 int
	BidPrice1  float64
	BidVolume1 int
	AskPrice2  float64
	AskVolume2 int
	BidPrice2  float64
	BidVolume2 int
	AskPrice3  float64
	AskVolume3 int
	BidPrice3  float64
	BidVolume3 int
	AskPrice4  float64
	AskVolume4 int
	BidPrice4  float64
	BidVolume4 int
	AskPrice5  float64
	AskVolume5 int
	BidPrice5  float64
	BidVolume5 int
}

type Price_dic struct {
	Date_time  string
	Open       float64
	High       float64
	Low        float64
	Close      float64
	Volumn     float64
	Ins_id     string
	Update_ask float64
	Update_bid float64
}
