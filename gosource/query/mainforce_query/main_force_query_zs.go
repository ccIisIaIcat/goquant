package mainforce_query

import (
	"strconv"
	"strings"
	"time"
)

// 郑商主力查询所

type Main_force_quert_zs struct {
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
func (M *Main_force_quert_zs) init() {
	M.instrument_type = make(map[string][]string, 0)
	M.mainforce_dic = make(map[string]string, 0)
	M.instrument_time = make(map[string]string, 0)
	M.symbol_code = map[string]string{"动力煤": "ZC", "玻璃": "FG", "甲醇": "MA", "菜粕": "RM", "菜油": "OI", "棉花": "CF", "白糖": "SR", "纯碱": "SA", "锰硅": "SM", "棉纱": "CY", "红枣": "CJ", "精对苯二甲酸": "TA", "硅铁": "SF", "短纤": "PF", "苹果": "AP", "尿素": "UR", "晚籼稻": "LR", "强麦": "WH", "普麦": "PM", "菜籽": "RS", "早灿稻": "RI", "粳稻谷": "JR"}
	M.tool_map = map[string]string{"棉花": "棉花", "苹果": "苹果", "普通小麦": "普麦", "菜油": "菜油", "白糖": "白糖", "动煤": "动力煤", "玻璃": "玻璃", "甲醇": "甲醇", "菜粕": "菜粕", "PTA": "精对苯二甲酸", "棉纱": "棉纱", "菜籽": "菜籽", "硅铁": "硅铁", "锰硅": "锰硅", "早稻": "早灿稻", "强麦": "强麦", "粳稻": "粳稻谷", "晚籼稻": "晚籼稻", "红枣": "红枣", "尿素": "尿素", "纯碱": "纯碱", "短纤": "短纤"}

	M.instrument_info_detail = make(map[string](map[string]string), 0)
	M.month, _ = strconv.Atoi(time.Now().Format("01"))
	M.year, _ = strconv.Atoi(time.Now().Format("2006")[3:])
}

// 用于爬取上交所品种的所有合约，并生成主力合约
// 返回不同品种的合约列表和主力合约列表

func (M *Main_force_quert_zs) up_date_map(new_dic map[string]map[string]string) map[string]map[string]string {
	for k, v := range new_dic {
		if k == "棉花主连" {
			new_dic["棉花连续"] = v
			delete(new_dic, "棉花主连")
		}
		if k == "花生" {
			delete(new_dic, "花生")
		}
		if k == "棉纱XX连续" {
			new_dic["棉纱连续"] = v
			delete(new_dic, "棉纱XX连续")
		}
	}
	return new_dic
}

func (M *Main_force_quert_zs) Query_main_force() (map[string][]string, map[string]string) {
	M.init()
	lala := M.up_date_map(Search("https://quote.fx678.com/exchange/CZCE"))

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
				M.instrument_type[s[0][:len(s[0])-3]] = []string{k}
			} else {
				M.instrument_type[s[0][:len(s[0])-3]] = append(M.instrument_type[s[0][:len(s[0])-4]], k)
			}
			cat_name := s[0][:len(s[0])-3] + "_con"
			target_dic := M.instrument_info_detail[cat_name]
			if judge_dic(target_dic, v) {
				M.mainforce_dic[cat_name] = k
			}
		}
	}

	// 返回主力合约字典和品种的不同合约
	return M.instrument_type, M.mainforce_dic
}
