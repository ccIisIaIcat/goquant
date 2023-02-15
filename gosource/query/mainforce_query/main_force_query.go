package mainforce_query

import (
	"database/sql"
	"fmt"
	"time"

	_ "github.com/go-sql-driver/mysql"
)

// 用于整体获取需要的参数
// 对应存储与mysql
// mysql里有两个表，一个存储每天的主力数据，一个存储当天最新的主力数据
type Main_force_query struct {
	Username        string
	Password        string
	Database_name   string
	table_name      string //用于存放数据的表名
	db              *sql.DB
	Main_force_dic  map[string]string //每个品种对应的主力合约
	Main_force_list []string          //所有的主力合约列表
	date            string            // 当前日期
}

func (M *Main_force_query) Init() {
	M.Main_force_dic = make(map[string]string, 0)
	M.Main_force_list = make([]string, 0)
	M.table_name = "mainforce_record"
	// (TODO:add config)
	dsn := M.Username + ":" + M.Password + "@tcp(127.0.0.1:3306)/" + M.Database_name
	var err error
	M.db, err = sql.Open("mysql", dsn)
	if err != nil {
		fmt.Println("db格式错误:", err)
		return
	}
	err = M.db.Ping()
	if err != nil {
		fmt.Println("db建立链接出错：")
		panic(err)
	}
	fmt.Println("db连接成功！")

	M.date = time.Now().Format("2006-01-02")
	M.Get_main_force_info()
	M.Create_orderbook_table()
	M.Insert_main_force()
}

func (M *Main_force_query) Create_orderbook_table() {
	//生成对应表
	sql := "CREATE TABLE IF NOT EXISTS " + M.table_name + " (id int PRIMARY KEY AUTO_INCREMENT,date varchar(255),ins_type varchar(255),mainforce_code varchar(255))" + "ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;"
	_, err := M.db.Exec(sql)
	if err != nil {
		fmt.Println(err)
		panic(err)
	}
}

func (M *Main_force_query) Insert_main_force() {
	sql_insert := "insert into " + M.table_name + " (date,ins_type,mainforce_code) values(?,?,?);"
	stmt, err := M.db.Prepare(sql_insert)
	defer func() {
		err := stmt.Close()
		if err != nil {
			fmt.Println(err)
		}
	}()
	if err != nil {
		fmt.Println("stmt错误", err)
	}
	for k, v := range M.Main_force_dic {
		stmt.Exec(M.date, k[:len(k)-4], v)
	}

}

func (M *Main_force_query) Get_main_force_info() {
	answer_matrix := make(map[string]string, 0)
	answer_list := make([]string, 0)
	m_ds := Main_force_quert_ds{}
	m_sn := Main_force_quert_sn{}
	m_sq := Main_force_quert_sq{}
	m_zs := Main_force_quert_zs{}
	_, ds_map := m_ds.Query_main_force()
	_, sn_map := m_sn.Query_main_force()
	_, sq_map := m_sq.Query_main_force()
	_, zs_map := m_zs.Query_main_force()
	for k, v := range ds_map {
		answer_matrix[k] = v
		answer_list = append(answer_list, v)
	}
	for k, v := range sn_map {
		answer_matrix[k] = v
		answer_list = append(answer_list, v)
	}
	for k, v := range sq_map {
		answer_matrix[k] = v
		answer_list = append(answer_list, v)
	}
	for k, v := range zs_map {
		answer_matrix[k] = v
		answer_list = append(answer_list, v)
	}
	M.Main_force_dic = answer_matrix
	M.Main_force_list = answer_list
}

func QuickCheck() (map[string]string, []string, map[string]string) {
	// 大连商品DCE，上海期货SHFE，上能INE，郑商CZCE
	answer_matrix := make(map[string]string, 0)
	answer_list := make([]string, 0)
	answer_list_with_exchange := make(map[string]string, 0)
	m_ds := Main_force_quert_ds{}
	m_sn := Main_force_quert_sn{}
	m_sq := Main_force_quert_sq{}
	m_zs := Main_force_quert_zs{}
	_, ds_map := m_ds.Query_main_force()
	_, sn_map := m_sn.Query_main_force()
	_, sq_map := m_sq.Query_main_force()
	_, zs_map := m_zs.Query_main_force()
	for k, v := range ds_map {
		answer_matrix[k] = v
		answer_list = append(answer_list, v)
		answer_list_with_exchange[v] = "DCE"
	}
	for k, v := range sn_map {
		answer_matrix[k] = v
		answer_list = append(answer_list, v)
		answer_list_with_exchange[v] = "INE"
	}
	for k, v := range sq_map {
		answer_matrix[k] = v
		answer_list = append(answer_list, v)
		answer_list_with_exchange[v] = "SHFE"
	}
	for k, v := range zs_map {
		answer_matrix[k] = v
		answer_list = append(answer_list, v)
		answer_list_with_exchange[v] = "CZCE"
	}
	return answer_matrix, answer_list, answer_list_with_exchange
}

// 返回品种对应主力合约，主力合约列表，主力合约对应交易所
func QuickCheckCustom(Ex_id map[string]bool) (map[string]string, []string, map[string]string) {
	answer_matrix := make(map[string]string, 0)
	answer_list := make([]string, 0)
	answer_list_with_exchange := make(map[string]string, 0)
	if Ex_id["DCE"] {
		m_ds := Main_force_quert_ds{}
		_, ds_map := m_ds.Query_main_force()
		for k, v := range ds_map {
			answer_matrix[k] = v
			answer_list = append(answer_list, v)
			answer_list_with_exchange[v] = "DCE"
		}

	} else if Ex_id["INE"] {
		m_sn := Main_force_quert_sn{}
		_, sn_map := m_sn.Query_main_force()
		for k, v := range sn_map {
			answer_matrix[k] = v
			answer_list = append(answer_list, v)
			answer_list_with_exchange[v] = "INE"
		}
	} else if Ex_id["SHFE"] {
		m_sq := Main_force_quert_sq{}
		_, sq_map := m_sq.Query_main_force()
		for k, v := range sq_map {
			answer_matrix[k] = v
			answer_list = append(answer_list, v)
			answer_list_with_exchange[v] = "SHFE"
		}
	} else if Ex_id["CZCE"] {
		m_zs := Main_force_quert_zs{}
		_, zs_map := m_zs.Query_main_force()
		for k, v := range zs_map {
			answer_matrix[k] = v
			answer_list = append(answer_list, v)
			answer_list_with_exchange[v] = "CZCE"
		}
	}

	return answer_matrix, answer_list, answer_list_with_exchange
}
