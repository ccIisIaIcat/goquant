package mainforce_query

// 上交所主力合约查询

import (
	"strconv"
	"strings"
	"time"
)

type Main_force_quert_sq struct {
	instrument_type        map[string]([]string)          //上交所品种清单,key:品种类别，values：对应品种合约
	mainforce_dic          map[string]string              //每个品种对应主力合约的合约编号
	instrument_time        map[string]string              //不同品种类别交易时间
	symbol_code            map[string]string              //不同品种和对应代码
	tool_map               map[string]string              //方便爬虫处理的一个字符对应
	instrument_info_detail map[string](map[string]string) //储存每一笔合约的具体信息，用于判断主力合约
	month                  int                            //当前月份
	year                   int                            //当前年份
}

// 初始化各类信息结构体
func (M *Main_force_quert_sq) init() {
	M.instrument_type = make(map[string][]string, 0)
	M.mainforce_dic = make(map[string]string, 0)
	M.instrument_time = make(map[string]string, 0)
	M.symbol_code = map[string]string{"铜": "cu", "铅": "pb", "锌": "zn", "铝": "al", "锡": "sn", "镍": "ni", "不锈钢": "ss", "燃料油": "fu", "天然橡胶": "ru", "沥青": "bu", "纸浆": "sp", "螺纹钢": "rb", "热轧卷板": "hc", "黄金": "au", "白银": "ag", "线材": "wr"}
	M.tool_map = map[string]string{"沪金": "黄金", "沪锌": "锌", "沪镍": "镍", "沪铅": "铅", "沪铜": "铜", "沪锡": "锡", "沪铝": "铝", "沪银": "白银", "燃油": "燃料油", "线材": "线材", "纸浆": "纸浆", "橡胶": "天然橡胶", "螺纹": "螺纹钢", "沥青": "沥青", "不锈钢": "不锈钢", "热卷": "热轧卷板", "燃料油": "燃料油", "热轧卷板": "热轧卷板"}

	M.instrument_info_detail = make(map[string](map[string]string), 0)
	M.month, _ = strconv.Atoi(time.Now().Format("01"))
	M.year, _ = strconv.Atoi(time.Now().Format("2006")[2:])
}

// 用于爬取上交所品种的所有合约，并生成主力合约
// 返回不同品种的合约列表和主力合约列表
func (M *Main_force_quert_sq) Query_main_force() (map[string][]string, map[string]string) {
	M.init()
	lala := Search("https://quote.fx678.com/exchange/SHFE")

	// 对map的key进行重命名
	for k, v := range lala {
		rt := []rune(k)
		if string(rt[len(rt)-2:]) == "连续" {
			cn_name := M.symbol_code[M.tool_map[string(rt[:len(rt)-2])]] + "_con"
			M.instrument_info_detail[cn_name] = v
		} else {
			cn_name := M.tool_map[string(rt[:len(rt)-4])]
			mon, _ := strconv.Atoi(string(rt[len(rt)-2:]))
			if mon >= M.month {
				cn_name = M.symbol_code[cn_name] + strconv.Itoa(M.year) + string(rt[len(rt)-2:])
			} else {
				cn_name = M.symbol_code[cn_name] + strconv.Itoa(M.year+1) + string(rt[len(rt)-2:])
			}
			M.instrument_info_detail[cn_name] = v
		}
	}

	// 寻找每个品种对应的主力合约
	for k, v := range M.instrument_info_detail {
		s := strings.Split(k, "_")
		if len(s) == 1 {
			if len(M.instrument_type[s[0][:len(s[0])-4]]) == 0 {
				M.instrument_type[s[0][:len(s[0])-4]] = []string{k}
			} else {
				M.instrument_type[s[0][:len(s[0])-4]] = append(M.instrument_type[s[0][:len(s[0])-4]], k)
			}
			cat_name := s[0][:len(s[0])-4] + "_con"
			target_dic := M.instrument_info_detail[cat_name]
			if judge_dic(target_dic, v) {
				M.mainforce_dic[cat_name] = k
			}
		}
	}

	// 返回主力合约字典和品种的不同合约
	return M.instrument_type, M.mainforce_dic
}
