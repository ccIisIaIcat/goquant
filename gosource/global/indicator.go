package global

type Cur_obj struct {
	Date_time string
	Price     float64
	Close     float64
	Volumn    float64
	Dist      int
	Type      int
}

type Signal_obj struct {
	P1_price float64
	P1_time  string
	P2_price float64
	P2_time  string
	P3_price float64
	P3_time  string
	Type     int
}
