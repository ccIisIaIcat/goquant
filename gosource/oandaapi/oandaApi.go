package oandaapi

import (
	"global"
	"net/http"
)

type OandaObj struct {
	// Public
	User_config global.ConfigUserOanda
	Port_type   string // 用于标明是测试服还是实盘
	// Private
	base_url string
	client   *http.Client
}

func (O *OandaObj) Init() {
	// 检查端口
	var judge_user global.ConfigUserOanda
	if O.User_config == judge_user {
		panic("missing User_config")
	}
	if O.Port_type == "" {
		panic("missing port_type")
	} else if O.Port_type == "Test" {
		O.base_url = "https://api-fxpractice.oanda.com"
	} else {
		O.base_url = "https://api-fxtrade.oanda.com"
	}
	// 声明客户端
	O.client = &http.Client{}
}
