package global

import (
	"gopkg.in/ini.v1"
)

type Config struct {
	PortInfo      map[string]ConfigPort
	UserInfo      map[string]ConfigUser
	MysqlInfo     map[string]ConfigMysql
	UserInfoOanda map[string]ConfigUserOanda
}

// 配置文件中的端口信息
type ConfigPort struct {
	TradePort  string
	MarketPort string
}

type ConfigUser struct {
	UserID   string
	Investor string
	Password string
	BrokerID string
	AppID    string
	AuthCode string
}

type ConfigMysql struct {
	Host     string
	Port     string
	User     string
	Password string
}

type ConfigUserOanda struct {
	Account       string
	Authorization string
}

func GetConfig(conf_path string) Config {
	cfg, err := ini.Load(conf_path)
	if err != nil {
		panic(err)
	}
	Config_obj := Config{}
	Config_obj.PortInfo = make(map[string]ConfigPort, 0)
	Config_obj.UserInfo = make(map[string]ConfigUser, 0)
	Config_obj.MysqlInfo = make(map[string]ConfigMysql, 0)
	Config_obj.UserInfoOanda = make(map[string]ConfigUserOanda, 0)
	// 读取端口，目前端口类型1，2，3，Test，Cp
	temp_list := []string{"1", "2", "3", "Test", "Cp"}
	for i := 0; i < len(temp_list); i++ {
		temp_port := ConfigPort{}
		temp_port.TradePort = cfg.Section("Port").Key("Trade" + temp_list[i]).String()
		temp_port.MarketPort = cfg.Section("Port").Key("Market" + temp_list[i]).String()
		Config_obj.PortInfo[temp_list[i]] = temp_port
	}
	// 读取用户，目前用户类型Test,Test1,Cp
	temp_list = []string{"Test", "Test1", "Cp"}
	for i := 0; i < len(temp_list); i++ {
		temp_user := ConfigUser{}
		temp_user.Investor = cfg.Section("User").Key("Investor" + temp_list[i]).String()
		temp_user.UserID = cfg.Section("User").Key("User" + temp_list[i]).String()
		temp_user.Password = cfg.Section("User").Key("Password" + temp_list[i]).String()
		temp_user.BrokerID = cfg.Section("User").Key("Broker" + temp_list[i]).String()
		temp_user.AppID = cfg.Section("User").Key("Appid" + temp_list[i]).String()
		temp_user.AuthCode = cfg.Section("User").Key("Authcode" + temp_list[i]).String()
		Config_obj.UserInfo[temp_list[i]] = temp_user
	}
	// 读取Mysql，目前Mysql类型Local
	temp_list = []string{"Local", "Local1", "Local2", "Rm", "Rm1"}
	for i := 0; i < len(temp_list); i++ {
		temp_mysql := ConfigMysql{}
		temp_mysql.Host = cfg.Section("Mysql").Key("Host" + temp_list[i]).String()
		temp_mysql.Port = cfg.Section("Mysql").Key("Port" + temp_list[i]).String()
		temp_mysql.User = cfg.Section("Mysql").Key("User" + temp_list[i]).String()
		temp_mysql.Password = cfg.Section("Mysql").Key("Password" + temp_list[i]).String()
		Config_obj.MysqlInfo[temp_list[i]] = temp_mysql
	}
	// 读取安达账户信息，目前anda类型Test
	temp_list = []string{"Test"}
	for i := 0; i < len(temp_list); i++ {
		temp_useroanda := ConfigUserOanda{}
		temp_useroanda.Account = cfg.Section("UserOanda").Key("Account" + temp_list[i]).String()
		temp_useroanda.Authorization = cfg.Section("UserOanda").Key("Authorization" + temp_list[i]).String()
		Config_obj.UserInfoOanda[temp_list[i]] = temp_useroanda
	}
	return Config_obj
}
