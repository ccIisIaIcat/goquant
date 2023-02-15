package record

// 用于实时存储数据的mysql对象

import (
	"database/sql"
	"fmt"
	"global"
	"log"
	"strconv"

	_ "github.com/go-sql-driver/mysql"
)

type Mysql_obj struct {
	// Public
	Table_list     []string //用于存放数据的表名
	Tick_info_chan chan global.Tick_info
	Bar_info_chan  chan global.Price_dic
	Stmt_query     map[string](*sql.Stmt) //每一个表名生成一个stmt指针，方便数据的插入
	Table_type     string                 // 表结构和句柄类型，默认全量
	Database_name  string
	Mysql_config   global.ConfigMysql
	// Private
	db       *sql.DB
	username string
	password string
	host     string
	port     string
}

// 初始化，同时为Table_list中的标的建表和生成默认句柄
// Exchange, Ins_id, Time, Last_price, Volume, Turnover,
// AskPrice1, AskVolume1, BidPrice1, BidVolume1, AskPrice2, AskVolume2, BidPrice2, BidVolume2, AskPrice3, AskVolume3, BidPrice3, BidVolume3,
// AskPrice4, AskVolume4, BidPrice4, BidVolume4, AskPrice5, AskVolume5, BidPrice5, BidVolume5
func (M *Mysql_obj) Init() {
	// 判断mysql配置
	var judge_mysql global.ConfigMysql
	if M.Mysql_config == judge_mysql {
		panic("missing mysql config")
	} else {
		M.username = M.Mysql_config.User
		M.password = M.Mysql_config.Password
		M.host = M.Mysql_config.Host
		M.port = M.Mysql_config.Port
	}
	dsn := M.username + ":" + M.password + "@tcp(" + M.host + ":" + M.port + ")/" + M.Database_name
	var err error
	M.db, err = sql.Open("mysql", dsn)
	if err != nil {
		log.Println("db格式错误:", err)
		panic("db格式错误")
	}
	err = M.db.Ping()
	if err != nil {
		log.Println("db建立链接出错：", err)
		panic("db建立链接出错")
	}
	if cap(M.Tick_info_chan) == 0 && cap(M.Bar_info_chan) == 0 && M.Table_type != "OandaBarM1" {
		panic("missing Tick_info_chan/Bar_info_chan")
	}
	log.Println("database:", M.Database_name, "连接成功！")

	M.Stmt_query = make(map[string]*sql.Stmt, 0)

	if M.Table_type == "" || M.Table_type == "All" {
		log.Println("开始创建表")
		M.CreateTable()
		log.Println("开始创建句柄")
		M.CreatStmtPointer()
	} else if M.Table_type == "Part" {
		log.Println("开始创建表")
		M.CreateTablePart()
		log.Println("开始创建句柄")
		M.CreatStmtPointerPart()
	} else if M.Table_type == "OandaBarM1" {
		log.Println("开始创建表")
		M.CreateTableOandaBarM1()
		log.Println("开始创建句柄")
		M.CreatStmtPointerOandaBarM1()

	} else {
		panic("自定义表结构未找到")
	}

}

// 根据结构体中声明的Table_list建表
func (M *Mysql_obj) CreateTable() {
	for i := 0; i < len(M.Table_list); i++ {
		sql := "CREATE TABLE IF NOT EXISTS " + "`" + M.Table_list[i] + "`" +
			" (id int PRIMARY KEY AUTO_INCREMENT, Exchange varchar(10), Instrument varchar(100), DateTime varchar(100), Last_price double, Volume double, Turnover double, " +
			"AskPrice1 double, AskVolume1 int, BidPrice1 double, BidVolume1 int, " +
			"AskPrice2 double, AskVolume2 int, BidPrice2 double, BidVolume2 int, " +
			"AskPrice3 double, AskVolume3 int, BidPrice3 double, BidVolume3 int, " +
			"AskPrice4 double, AskVolume4 int, BidPrice4 double, BidVolume4 int, " +
			"AskPrice5 double, AskVolume5 int, BidPrice5 double, BidVolume5 int) " +
			"ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;"
		M.CreateTableCustom(M.Table_list[i], sql)
	}
	log.Println("建表成功/表已存在")
}

// 自定义建表
func (M *Mysql_obj) CreateTableCustom(insid string, sql string) {
	_, err := M.db.Exec(sql)
	if err != nil {
		panic(err)
	}
}

// 根据传入Table_list，生成stmt_dic
func (M *Mysql_obj) CreatStmtPointer() {
	for i := 0; i < len(M.Table_list); i++ {
		sql_insert_1 := "insert into " + "`" + M.Table_list[i] + "`" +
			" (Exchange, Instrument, DateTime, Last_price, Volume, Turnover, AskPrice1, AskVolume1, BidPrice1, BidVolume1,AskPrice2, AskVolume2, BidPrice2, BidVolume2,AskPrice3, AskVolume3, BidPrice3, BidVolume3,AskPrice4, AskVolume4, BidPrice4, BidVolume4,AskPrice5, AskVolume5, BidPrice5, BidVolume5) " +
			"values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);"
		M.CreatStmtPointerCustom(M.Table_list[i], sql_insert_1)
	}
}

func (M *Mysql_obj) CreatStmtPointerCustom(insid string, sql string) {
	stmt, err := M.db.Prepare(sql)
	if err != nil {
		fmt.Println(insid, "stmt错误", err)
	} else {
		M.Stmt_query[insid] = stmt
	}
}

// 结束时关闭所有table_list中声明的句柄，并关闭数据库连接
func (M *Mysql_obj) CloseStmt() {
	for i := 0; i < len(M.Table_list); i++ {
		M.Stmt_query[M.Table_list[i]].Close()
	}
	M.db.Close()
}

func (M *Mysql_obj) InsertByTick() {
	for {
		t_price := <-M.Tick_info_chan
		// Exchange, Ins_id, Time, Last_price, Volume, Turnover,
		// AskPrice1, AskVolume1, BidPrice1, BidVolume1, AskPrice2, AskVolume2, BidPrice2, BidVolume2, AskPrice3, AskVolume3, BidPrice3, BidVolume3,
		// AskPrice4, AskVolume4, BidPrice4, BidVolume4, AskPrice5, AskVolume5, BidPrice5, BidVolume5
		_, err := M.Stmt_query[t_price.Ins_id].Exec(
			t_price.Exchange, t_price.Ins_id, t_price.Time, t_price.Last_price, t_price.Volume, t_price.Turnover,
			t_price.AskPrice1, t_price.AskVolume1, t_price.BidPrice1, t_price.BidVolume1,
			t_price.AskPrice2, t_price.AskVolume2, t_price.BidPrice2, t_price.BidVolume2,
			t_price.AskPrice3, t_price.AskVolume3, t_price.BidPrice3, t_price.BidVolume3,
			t_price.AskPrice4, t_price.AskVolume4, t_price.BidPrice4, t_price.BidVolume4,
			t_price.AskPrice5, t_price.AskVolume5, t_price.BidPrice5, t_price.BidVolume5)
		if err != nil {
			fmt.Println(err)
		}

	}

}

// 根据结构体中声明的Table_list建表
func (M *Mysql_obj) CreateTablePart() {
	for i := 0; i < len(M.Table_list); i++ {
		sql := "CREATE TABLE IF NOT EXISTS " + M.Table_list[i] + " (id int PRIMARY KEY AUTO_INCREMENT,ts varchar(200),Last_price double,A1p double,A1q int,B1p double,B1q int)" + "ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;"
		M.CreateTableCustom(M.Table_list[i], sql)
	}
	log.Println("建表成功/表已存在")
}

// 根据传入Table_list，生成stmt_dic
func (M *Mysql_obj) CreatStmtPointerPart() {
	for i := 0; i < len(M.Table_list); i++ {
		sql_insert_1 := "insert into " + M.Table_list[i] + " (ts,Last_price,A1p,A1q,B1p,B1q) values(?,?,?,?,?,?);"
		M.CreatStmtPointerCustom(M.Table_list[i], sql_insert_1)
	}
}

// 根据结构体中声明的Table_list建表
func (M *Mysql_obj) CreateTableOandaBarM1() {
	for i := 0; i < len(M.Table_list); i++ {
		sql := "CREATE TABLE IF NOT EXISTS " + M.Table_list[i] + "_M1Bar" + " (id int PRIMARY KEY AUTO_INCREMENT,time varchar(200),openA double,highA double,lowA int,closeA double,openB double,highB double,lowB int,closeB double,volumn int)" + "ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;"
		M.CreateTableCustom(M.Table_list[i], sql)
	}
	log.Println("建表成功/表已存在")
}

// 根据传入Table_list，生成stmt_dic
func (M *Mysql_obj) CreatStmtPointerOandaBarM1() {
	for i := 0; i < len(M.Table_list); i++ {
		sql_insert_1 := "insert into " + M.Table_list[i] + "_M1Bar" + " (time,openA,highA,lowA,closeA,openB,highB,lowB,closeB,volumn) values(?,?,?,?,?,?,?,?,?,?);"
		M.CreatStmtPointerCustom(M.Table_list[i], sql_insert_1)
	}
}

func (M *Mysql_obj) InsertByOandaBarM1(bar_info []map[string]interface{}, ins_id string) {
	// fmt.Printf("[saving " + ins_id + "] processing:")
	for k := 0; k < len(bar_info); k++ {
		// if int((float64(k)/float64(len(bar_info)))*100)%10 == 0 {
		// 	fmt.Printf(">")
		// }
		closeA, _ := strconv.ParseFloat(bar_info[k]["ask"].(map[string]interface{})["c"].(string), 64)
		openA, _ := strconv.ParseFloat(bar_info[k]["ask"].(map[string]interface{})["o"].(string), 64)
		highA, _ := strconv.ParseFloat(bar_info[k]["ask"].(map[string]interface{})["h"].(string), 64)
		lowA, _ := strconv.ParseFloat(bar_info[k]["ask"].(map[string]interface{})["l"].(string), 64)
		closeB, _ := strconv.ParseFloat(bar_info[k]["bid"].(map[string]interface{})["c"].(string), 64)
		openB, _ := strconv.ParseFloat(bar_info[k]["bid"].(map[string]interface{})["o"].(string), 64)
		highB, _ := strconv.ParseFloat(bar_info[k]["bid"].(map[string]interface{})["h"].(string), 64)
		lowB, _ := strconv.ParseFloat(bar_info[k]["bid"].(map[string]interface{})["l"].(string), 64)
		volume := int(bar_info[k]["volume"].(float64))
		M.Stmt_query[ins_id].Exec(bar_info[k]["time"].(string), openA, highA, lowA, closeA, openB, closeB, highB, lowB, volume)
	}
	fmt.Println(ins_id, " get")

}

func (M *Mysql_obj) InsertByTickPart() {
	for {
		t_price := <-M.Tick_info_chan
		// ts,Last_price,A1p,A1q,B1p,B1q

		_, err := M.Stmt_query[t_price.Ins_id].Exec(t_price.Time, t_price.Last_price, t_price.AskPrice1, t_price.AskVolume1, t_price.BidPrice1, t_price.BidVolume1)
		if err != nil {
			fmt.Println("mysql insert err", err)
		}
	}

}
