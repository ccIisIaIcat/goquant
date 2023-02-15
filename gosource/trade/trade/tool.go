package trade

import "time"

func (T *TradeBySignal) waitForBackward(back string) {
	for !T.login_record[back] {
		time.Sleep(time.Second * 1)
	}
}

func (T *TradeBySignal) ReqID(nRequestID *int) int {
	*nRequestID++
	return *nRequestID
}
