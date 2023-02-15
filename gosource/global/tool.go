package global

import (
	"errors"
	"strings"
	"time"
)

func Never_stop(judge chan bool) {
	for {
		select {
		case judge_obj := <-judge:
			if judge_obj {
				break
			}
		case <-time.After(20 * time.Second):
			continue
		}
	}
}

func Never_stop_direct() {
	for {
		time.Sleep(time.Hour)
	}
}

func ReqID(nRequestID *int) int {
	*nRequestID++
	return *nRequestID
}

func IsContain(item string, item_arr []string) error {
	for _, cit := range item_arr {
		if item == cit {
			return nil
		}
	}
	return errors.New("Not Contain")
}

func SameTradeDayJudge(time_1 string, time_2 string) bool {
	new_time_1 := strings.Split(time_1, " ")
	new_time_2 := strings.Split(time_2, " ")
	if new_time_1[1] > "15:00:00" {
		tm1, _ := time.Parse("2006-01-02", new_time_1[0])
		new_time_1[0] = tm1.AddDate(0, 0, 1).Format("2006-01-02")
	}
	if new_time_2[1] > "15:00:00" {
		tm2, _ := time.Parse("2006-01-02", new_time_2[0])
		new_time_2[0] = tm2.AddDate(0, 0, 1).Format("2006-01-02")
	}
	// fmt.Println(new_time_1, new_time_2)
	if new_time_1[0] == new_time_2[0] {
		return true
	} else {
		return false
	}
}
