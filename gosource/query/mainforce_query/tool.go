package mainforce_query

import (
	"fmt"
	"net/http"
	"strings"

	"github.com/PuerkitoBio/goquery"
)

// 判断两个字典是否完全一致
func judge_dic(dic_1 map[string]string, dic_2 map[string]string) bool {
	for k := range dic_1 {
		if dic_1[k] != dic_2[k] {
			return false
		}
	}
	return true
}

func Search(info_type string) map[string](map[string]string) {
	res, err := http.Get(info_type)
	if err != nil {
		fmt.Println(err)
	}
	defer res.Body.Close()
	if res.StatusCode != 200 {
		fmt.Printf("status code error: %d %s", res.StatusCode, res.Status)
	}

	doc, err := goquery.NewDocumentFromReader(res.Body)
	if err != nil {
		fmt.Println(err)
	}
	tool_list := make([][]string, 0)
	doc.Find("tr").Each(func(i int, selection *goquery.Selection) {
		b := strings.Replace(selection.Text(), " ", "", -1)
		dede := strings.Split(b, "\n")
		tool_list = append(tool_list, dede)
	})
	tool_list[0] = append(tool_list[0][1:2], tool_list[0][5:]...)
	tool_list[0] = tool_list[0][:len(tool_list[0])-1]
	name_list := tool_list[0]
	tool_map := make(map[string](map[string]string), 0)
	for i := 1; i < len(tool_list)-1; i++ {
		for j := 0; j < len(tool_list[i]); j++ {
			if tool_list[i][j] == "" || tool_list[i][j] == " " {
				tool_list[i] = append(tool_list[i][:j], tool_list[i][j+1:]...)
			}
		}
		tool_list[i] = tool_list[i][1:]
		tool_list[i] = append(tool_list[i][:1], tool_list[i][2:]...)
		tool_map[tool_list[i][0]] = make(map[string]string, 0)
		for j := 1; j < len(name_list); j++ {
			(tool_map[tool_list[i][0]])[name_list[j]] = tool_list[i][j]
		}

	}
	return tool_map
}
