package main

import (
	"fake"
	"fmt"
	"global"
)

func main() {
	fmt.Println("hello world")
	tick_chan := make(chan global.Tick_info, 200)
	f := fake.FakeQueryMongo{Query_list: []string{"ag2302"}, Database_name: "quant_info", Tick_info_chan: tick_chan}
	f.Init()
	f.Start()
	go func() {
		for {
			t_price := <-tick_chan
			fmt.Println(t_price)
		}
	}()

	global.Never_stop_direct()

}
