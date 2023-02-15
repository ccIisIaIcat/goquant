package mainforce_query

import (
	"strconv"
	"strings"
	"time"
)

// 郑商主力查询所

type Main_force_quert_ds struct {
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
func (M *Main_force_quert_ds) init() {
	M.instrument_type = make(map[string][]string, 0)
	M.mainforce_dic = make(map[string]string, 0)
	M.instrument_time = make(map[string]string, 0)
	M.symbol_code = map[string]string{"铁矿石": "i", "焦炭": "j", "焦煤": "jm", "豆一": "a", "豆二": "b", "豆粕": "m", "豆油": "y", "聚乙烯": "l", "聚氯乙烯": "v", "聚丙烯": "pp", "乙二醇": "eg", "玉米": "c", "粳米": "rr", "苯乙烯": "eb", "玉米淀粉": "cs", "棕榈油": "p", "液化石油气": "pg", "鸡蛋": "jd", "胶板": "bb", "纤维板": "fb"}
	M.tool_map = map[string]string{"豆一": "豆一", "豆二": "豆二", "铁矿": "铁矿石", "焦炭": "焦炭", "焦煤": "焦煤", "豆粕": "豆粕", "棕榈": "棕榈油", "豆油": "豆油", "玉米": "玉米", "淀粉": "玉米淀粉", "乙二醇": "乙二醇", "聚乙烯": "聚乙烯", "乙烯": "聚乙烯", "丙烯": "聚丙烯", "聚氯乙烯": "聚氯乙烯", "PVC": "聚氯乙烯", "苯乙烯": "苯乙烯", "纤维板": "纤维板", "胶合板": "胶板", "鸡蛋": "鸡蛋", "粳米": "粳米", "液化石油气": "液化石油气"}

	M.instrument_info_detail = make(map[string](map[string]string), 0)
	M.month, _ = strconv.Atoi(time.Now().Format("01"))
	M.year, _ = strconv.Atoi(time.Now().Format("2006")[2:])
}

// 用于爬取上交所品种的所有合约，并生成主力合约
// 返回不同品种的合约列表和主力合约列表

func (M *Main_force_quert_ds) up_date_map(new_dic map[string]map[string]string) map[string]map[string]string {
	for k := range new_dic {
		if k == "生猪连续" {
			delete(new_dic, "生猪连续")
		}
	}
	return new_dic
}

func (M *Main_force_quert_ds) Query_main_force() (map[string][]string, map[string]string) {
	M.init()
	lala := M.up_date_map(Search("https://quote.fx678.com/exchange/DCE"))

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

// https://quote.fx678.com/exchange/DCE
