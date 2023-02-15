package main

import (
	"bytes"
	"errors"
	"flag"
	"fmt"
	"os"
	"path"
	"path/filepath"
	"regexp"
	"runtime"
	"strings"
	"text/template"

	"golang.org/x/text/encoding/simplifiedchinese"
)

var (
	// source path
	srcpath string
	// platform
	csys string
	// output path
	outpath string
	// language
	lang string
)

// Funciton Structure
type fieldStruct struct {
	FieldType string
	FieldName string
	Comment   string
}

// Template Structure
type tplStruct struct {
	FuncTypeName string
	FuncRtn      string
	FuncName     string
	Comment      string
	FuncFields   []fieldStruct
}

// Template
func tmpl(tplFileName string, content interface{}, funcMap template.FuncMap, outPath string) {
	_, curFile, _, _ := runtime.Caller(1)
	tplPath := path.Join(filepath.Dir(curFile), "wrap_tpl") // 模板文件在执行文件同级目录下的wrap_tpl文件夹下

	fm := make(template.FuncMap, 0)
	fm["trimStar"] = func(str string) string {
		return strings.TrimPrefix(str, "*")
	}

	for k, v := range funcMap {
		fm[k] = v
	}

	t := template.New(path.Base(tplFileName)).Delims("[[", "]]").Funcs(fm)
	t, err := t.ParseFiles(path.Join(tplPath, tplFileName))
	if err != nil {
		panic(err)
	}
	var buf = bytes.Buffer{}
	err = t.Execute(&buf, content) // ***
	if err != nil {
		panic(err)
	}

	// 写入 .h
	fname := strings.TrimSuffix(tplFileName, filepath.Ext(tplFileName))
	csys_flag := csys
	if csys_flag == "macos" {
		csys_flag = "darwin"
	}
	if strings.Contains(fname, "go") {
		if strings.Contains(fname, "win") || strings.Contains(fname, "nix") {
			fslice1 := strings.Split(fname, "_")
			fslice2 := strings.Split(fslice1[2], ".")
			fname = fslice1[0] + "_" + fslice1[1] + "_" + csys_flag + "." + fslice2[1]
		} else {
			fslice1 := strings.Split(fname, "_")
			fslice2 := strings.Split(fslice1[1], ".")
			fname = fslice1[0] + "_" + fslice2[0] + "_" + csys_flag + "." + fslice2[1]
		}
	}

	err = os.WriteFile(path.Join(outPath, fname),
		buf.Bytes(),
		os.ModePerm)
	if err != nil {
		panic(err)
	}
}

func gen_cwrap(tplExeFunc func(title string, on []*tplStruct, fn []*tplStruct)) {
	srcp1 := path.Join(srcpath, "ThostFtdcMdApi.h")
	srcp2 := path.Join(srcpath, "ThostFtdcTraderApi.h")
	for _, hFileName := range []string{srcp1, srcp2} {
		var title string
		if strings.Contains(hFileName, "ThostFtdcMdApi") {
			title = "ctpquote_api"
		} else {
			title = "ctptrade_api"
		}
		bsFile, err := os.ReadFile(hFileName)
		if err != nil {
			panic(err)
		}
		// 汉字处理
		bsFile, _ = simplifiedchinese.GB18030.NewDecoder().Bytes(bsFile)
		strFile := string(bsFile)
		strFile = strings.ReplaceAll(strFile, "\r\n", "\n") // 换行符用 \n 避免 win和 lnx执行时不一致
		/*
			///登录请求响应
			virtual void OnRspUserLogin(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};
		*/
		re := regexp.MustCompile(`\t///(.*)\n[^v]*virtual\s+(\w+)\s+(\w+)\(([^)]*)\)`) // 分解函数定义:注释,返回类型,函数名,参数字段四部分
		funs := re.FindAllStringSubmatch(strFile, -1)
		tplsOn := make([]*tplStruct, 0)
		tplsFn := make([]*tplStruct, 0)
		for _, fun := range funs {
			funComment, funRtn, funName, funParams := fun[1], fun[2], fun[3], fun[4]
			re := regexp.MustCompile(`(\w+)\s+([*]?[ ]?\w+)[,]?\s*`) //参数分解:类型,名称
			fields := re.FindAllStringSubmatch(funParams, -1)
			funFields := make([]fieldStruct, 0)
			for _, field := range fields {
				funFields = append(funFields, fieldStruct{FieldType: field[1], FieldName: field[2]})
			}
			if strings.HasPrefix(funName, "On") { // On 响应函数
				tplsOn = append(tplsOn, &tplStruct{
					Comment:      funComment,
					FuncTypeName: "FP_" + funName,
					FuncRtn:      funRtn,
					FuncName:     funName,
					FuncFields:   funFields,
				})
			} else {
				tplsFn = append(tplsFn, &tplStruct{
					Comment:      funComment,
					FuncTypeName: "FP_" + funName,
					FuncRtn:      funRtn,
					FuncName:     funName,
					FuncFields:   funFields,
				})
			}
		}
		tplExeFunc(title, tplsOn, tplsFn)
	}
}

// Generate datatype
func gen_datatype(srcpath string, fn func([]*tplStruct)) {
	srcpath = path.Join(srcpath, "ThostFtdcUserApiDataType.h")
	bsFile, err := os.ReadFile(srcpath)
	if err != nil {
		panic(err)
	}
	bsFile, _ = simplifiedchinese.GB18030.NewDecoder().Bytes(bsFile)
	strFile := string(bsFile)
	strFile = strings.ReplaceAll(strings.ReplaceAll(strFile, "\r\n", "\n"), "\n\t", "\n")

	/*
		/////////////////////////////////////////////////////////////////////////
		///TFtdcExchangePropertyType是一个交易所属性类型
		/////////////////////////////////////////////////////////////////////////
		///正常
		#define THOST_FTDC_EXP_Normal '0'
		///根据成交生成报单
		#define THOST_FTDC_EXP_GenOrderByTrade '1'

		typedef char TThostFtdcExchangePropertyType;

		=>
		// 交易所属性类型
		type TThostFtdcExchangePropertyType byte
		const THOST_FTDC_EXP_Normal = '0' // 正常
		const THOST_FTDC_EXP_GenOrderByTrade = '1' // 根据成交生成报单
	*/
	re := regexp.MustCompile(`/+.+是一个(.*)\n/*\n([^;]+)typedef\s+(\w+)\s+(\w+)\s*;`) // 注释,defines,类型,名称
	types := re.FindAllStringSubmatch(strFile, -1)

	tss := make([]*tplStruct, 0)
	for _, v := range types {
		ts := &tplStruct{
			Comment:      v[1], // 注释
			FuncTypeName: v[3], // 基础类型
			FuncName:     v[4],
		}
		reSub := regexp.MustCompile(`/+(.*)\n#define\s+(\w+)\s+'(.+)'`) // 注释,名称,值 \w改为.因为有'#'的情况
		defines := reSub.FindAllStringSubmatch(v[2], -1)
		for _, v := range defines {
			ts.FuncFields = append(ts.FuncFields, fieldStruct{
				Comment:   v[1],
				FieldType: v[2],
				FieldName: v[3],
			})
		}
		tss = append(tss, ts)
	}

	/*	/////////////////////////////////////////////////////////////////////////
		///TFtdcTraderIDType是一个交易所交易员代码类型
		/////////////////////////////////////////////////////////////////////////
		typedef char TThostFtdcTraderIDType[21];
	*/
	re = regexp.MustCompile(`/+.+是一个(.*)\n/*\ntypedef\s+(\w+)\s+(.+)\s*;`)
	types = re.FindAllStringSubmatch(strFile, -1)
	for _, v := range types {
		ts := &tplStruct{
			Comment:      v[1],
			FuncTypeName: v[2], // 基础类型
			FuncName:     v[3],
		}
		// typedef char TThostFtdcTraderIDType[21]; -> type TThostFtdcTraderIDType [21]byte
		if strings.Contains(ts.FuncName, "[") {
			ts.FuncTypeName = "[" + strings.Split(ts.FuncName, "[")[1] + "byte"
			ts.FuncName = strings.Split(ts.FuncName, "[")[0]
		}
		tss = append(tss, ts)
	}
	fn(tss)
}

// Generate struct
func gen_struct(srcpath string, fn func([]*tplStruct)) {
	srcpath = path.Join(srcpath, "ThostFtdcUserApiStruct.h")
	bsFile, err := os.ReadFile(srcpath)
	if err != nil {
		panic(err)
	}
	bsFile, _ = simplifiedchinese.GB18030.NewDecoder().Bytes(bsFile)
	strFile := string(bsFile)

	re := regexp.MustCompile(`///(\S*)\s*struct\s*(\w*)\s*{([^}]*)}`) // 分成struct的注释,名称,字段两部分
	structs := re.FindAllStringSubmatch(strFile, -1)
	tss := make([]*tplStruct, 0)
	for _, strc := range structs {
		ts := &tplStruct{
			Comment:      strc[1],
			FuncTypeName: strc[2],
		}
		re = regexp.MustCompile(`///([^\r\n]*)\s*(\w+)\s+([^;]+);`) // 所有字段再分解成各个单独字段: 注释(可能含空格),类型,名称
		fields := re.FindAllStringSubmatch(strc[3], -1)
		for _, v := range fields {
			ts.FuncFields = append(ts.FuncFields, fieldStruct{
				Comment:   v[1],
				FieldType: v[2],
				FieldName: v[3],
			})
		}
		tss = append(tss, ts)
	}
	fn(tss)
}

func cfm(title string, tplsOn, tplsFn []*tplStruct) {
	mpCpp := make(map[string]interface{})
	mpCpp["On"] = tplsOn
	mpCpp["Fn"] = tplsFn
	mpCpp["Pf"] = csys
	tmpl(title+".h.tpl", mpCpp, nil, outpath)
	tmpl(title+".cpp.tpl", mpCpp, nil, outpath)
}

func ccfm(title string, tplsOn, tplsFn []*tplStruct) {
	mpCpp := make(map[string]interface{})
	mpCpp["On"] = tplsOn
	mpCpp["Fn"] = tplsFn
	mpCpp["Pf"] = csys
	fm := make(template.FuncMap)
	fm["struct_Type"] = func(structType string) string {
		if structType == "CThostFtdcMdSpi" {
			return "void"
		}
		if structType == "CThostFtdcTraderSpi" {
			return "void"
		}
		if strings.HasSuffix(structType, "Field") { // struct
			return "struct " + structType // struct CThostFtdcRspUserLoginField *pRspUserLogin
		}
		if structType == "bool" {
			return "_Bool"
		}
		if structType == "THOST_TE_RESUME_TYPE" {
			return "int"
		}
		return structType
	}
	tmpl("c"+title+".h.go.tpl", mpCpp, fm, outpath)
}

func pycfm(title string, on, fn []*tplStruct) {
	funcs := make(map[string]interface{})
	funcs["On"] = on
	funcs["Fn"] = fn
	funcs["Pf"] = csys
	fm := make(template.FuncMap)
	fm["baseType"] = func(preType string) string {
		if preType == "CThostFtdcMdSpi" {
			return "c_void_p"
		}
		if preType == "CThostFtdcTraderSpi" {
			return "c_void_p"
		}
		if preType == "int" { // SubscribeMarketData(char *ppInstrumentID[], int nCount)
			return "c_int32"
		}
		return "c_void_p" // char*  CThost结构体
	}
	fm["fnBaseType"] = func(fieldTypeName string) string {
		if fieldTypeName == "char" {
			return "str"
		}
		if fieldTypeName == "CThostFtdcMdSpi" {
			return "c_void_p"
		}
		if fieldTypeName == "CThostFtdcTraderSpi" {
			return "c_void_p"
		}
		return fieldTypeName
	}
	fm["evBaseType"] = func(fieldTypeName string) string {
		if strings.HasPrefix(fieldTypeName, "CThostFtdc") { // struct
			return fmt.Sprintf("POINTER(%s)", fieldTypeName)
		}
		if fieldTypeName == "int" {
			return "c_int32"
		}
		if fieldTypeName == "bool" {
			return "c_bool"
		}
		return fieldTypeName
	}
	fm["param"] = func(fieldType, fieldName string) string {
		if fieldName == "ppInstrumentID" { // 类型为 Array[c_char_p]
			return fieldName
		}
		if fieldName == "pSpi" {
			return fmt.Sprintf("self.%s", fieldName)
		}
		if fieldType == "char" {
			return fmt.Sprintf("bytes(%s, encoding='ascii')", fieldName)
		}
		if fieldType == "CThostFtdcMdSpi" {
			return fieldName
		}
		if fieldType == "CThostFtdcTraderSpi" {
			return fieldName
		}
		if strings.HasPrefix(fieldType, "CThostFtdc") {
			return fmt.Sprintf("byref(%s)", fieldName)
		}
		return fieldName
	}
	fm["onParam"] = func(fieldType, fieldName string) string {
		if strings.HasPrefix(fieldType, "CThostFtdc") {
			// self.OnRspQryInvestorPosition(copy.deepcopy(POINTER(CThostFtdcInvestorPositionField).from_param(pInvestorPosition).contents) if pInvestorPosition else CThostFtdcInvestorPositionField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)
			return fmt.Sprintf("copy.deepcopy(POINTER(%s).from_param(%s).contents) if %s else %s()", fieldType, fieldName, fieldName, fieldType)
		}
		return fieldName
	}
	tmpl(title+".py.tpl", funcs, fm, outpath)
}

func wgocfm(title string, tplsOn, tplsFn []*tplStruct) {
	// for _, v := range [][]*tplStruct{tplsOn, tplsFn} {
	for _, fn := range tplsFn { // 主调函数
		// 增加 void* api 首个参数
		tmp := []fieldStruct{{FieldType: "void*", FieldName: "api"}}
		tmp = append(tmp, fn.FuncFields...)
		fn.FuncFields = tmp
	}
	// }
	mpCpp := make(map[string]interface{})
	mpCpp["On"] = tplsOn
	mpCpp["Fn"] = tplsFn
	mpCpp["Pf"] = csys
	fm := make(template.FuncMap)
	fm["ctp_type"] = func(structType string) string {
		if strings.HasSuffix(structType, "Field") { // struct
			return fmt.Sprintf("*%s", structType) // *CThostFtdcUserLogoutField
		}
		if structType == "void*" {
			return "uintptr"
		}
		if structType == "char" {
			return "[]byte"
		}
		if structType == "CThostFtdcMdSpi" {
			return "uintptr"
		}
		if structType == "CThostFtdcTraderSpi" {
			return "uintptr"
		}
		if structType == "THOST_TE_RESUME_TYPE" {
			return "THOST_TE_RESUME_TYPE"
		}
		return structType
	}
	fm["fldType"] = func(structType string, str string) string {
		if strings.Contains(str, "*") {
			if str == "*pSpi" {
				if title == "ctpquote_api" {
					return fmt.Sprintf("uintptr(q.%s)", strings.TrimPrefix(str, "*"))
				} else {
					return fmt.Sprintf("uintptr(t.%s)", strings.TrimPrefix(str, "*"))
				}
			} else {
				if structType == "char" {
					return fmt.Sprintf("uintptr(unsafe.Pointer(&%s[0]))", strings.TrimPrefix(str, "*"))
				} else {
					return fmt.Sprintf("uintptr(unsafe.Pointer(%s))", strings.TrimPrefix(str, "*"))
				}
			}
		} else {
			if str == "api" {
				if title == "ctpquote_api" {
					return fmt.Sprintf("uintptr(q.%s)", str)
				} else {
					return fmt.Sprintf("uintptr(t.%s)", str)
				}
			} else {
				return fmt.Sprintf("uintptr(%s)", str)
			}
		}
	}
	tmpl(title+"_win.go.tpl", mpCpp, fm, outpath)
}

func xgocfm(title string, tplsOn, tplsFn []*tplStruct) {
	for _, fn := range tplsFn { // 主调函数
		// 增加 void* api 首个参数
		tmp := []fieldStruct{{FieldType: "void*", FieldName: "api"}}
		tmp = append(tmp, fn.FuncFields...)
		fn.FuncFields = tmp
	}
	funcs := make(map[string]interface{})
	funcs["On"] = tplsOn
	funcs["Fn"] = tplsFn
	funcs["Pf"] = csys
	fm := make(template.FuncMap)
	fm["struct_Type"] = func(structType string) string {
		if structType == "CThostFtdcMdSpi" {
			return "void"
		}
		if structType == "CThostFtdcTraderSpi" {
			return "void"
		}
		if strings.HasPrefix(structType, "CThostFtdc") { // struct
			return "struct " + structType // struct CThostFtdcRspUserLoginField *pRspUserLogin
		}
		if structType == "bool" {
			return "_Bool"
		}
		if structType == "THOST_TE_RESUME_TYPE" {
			return "int"
		}
		return structType
	}
	fm["C_struct"] = func(structType string) string {
		if strings.HasPrefix(structType, "CThostFtdc") { // struct
			return "*C.struct_" + structType // field *C.struct_CThostFtdcRspUserLoginField
		}
		if structType == "int" {
			return "C.int"
		}
		if structType == "bool" {
			return "C._Bool"
		}
		return structType
	}
	fm["ctp_type"] = func(structType string) string {
		if strings.HasPrefix(structType, "CThostFtdc") { // struct
			return fmt.Sprintf("*%s", structType) // *CThostFtdcUserLogoutField
		}
		if structType == "char" {
			return "[]byte"
		}
		return structType
	}
	fm["ctp_param"] = func(structType, field string) string {
		if strings.HasPrefix(structType, "CThostFtdc") { // struct
			return fmt.Sprintf("(*%s)(unsafe.Pointer(%s))", structType, strings.TrimPrefix(field, "*")) // (*CThostFtdcRspUserLoginField)(unsafe.Pointer(field))
		}
		if structType == "int" {
			return "int(" + field + ")"
		}
		if structType == "bool" {
			return "bool(" + field + ")"
		}
		return field
	}
	fm["fldType"] = func(structType string, field string) string {
		if field == "*ppInstrumentID" {
			return fmt.Sprintf("(**C.char)(unsafe.Pointer(&%s[0]))", "tmp_arr") // strings.TrimPrefix(field, "*")
		}
		if strings.HasSuffix(structType, "Field") {
			return fmt.Sprintf("(*C.struct_%s)(unsafe.Pointer(%s))", structType, strings.TrimPrefix(field, "*"))
		}
		if structType == "char" {
			return fmt.Sprintf("(*C.char)(unsafe.Pointer(C.CBytes(%s)))", strings.TrimPrefix(field, "*"))
		}
		if structType == "int" {
			return fmt.Sprintf("C.int(%s)", field)
		}
		if structType == "bool" {
			return fmt.Sprintf("C._Bool(%s)", field)
		}
		if structType == "THOST_TE_RESUME_TYPE" {
			return fmt.Sprintf("C.int(%s)", field)
		}
		if field == "*pSpi" || field == "api" {
			if title == "ctpquote_api" {
				return fmt.Sprintf("q.%s", strings.TrimPrefix(field, "*"))
			} else {
				return fmt.Sprintf("t.%s", strings.TrimPrefix(field, "*"))
			}
		}
		if structType == "TThostFtdcSystemInfoLenType" {
			return fmt.Sprintf("C.int(%s)", field)
		}
		if structType == "TThostFtdcClientSystemInfoType" {
			return fmt.Sprintf("(*C.char)(unsafe.Pointer(&%s[0]))", field)
		}
		return fmt.Sprintf("(%s %s)", structType, field)
	}

	fm["supType"] = func(structType string, field string) string {
		if field == "*ppInstrumentID" {
			return fmt.Sprintf(`
	tmp_arr := make([]*C.char, len(%s))
		for i := 0; i < len(tmp_arr); i++ {
			tmp_arr[i] = (*C.char)(unsafe.Pointer(C.CBytes(%s[i])))
		}
	`, strings.TrimPrefix(field, "*"), strings.TrimPrefix(field, "*"))
		}
		return fmt.Sprintf("")
	}

	tmpl(title+"_nix.go.tpl", funcs, fm, outpath)
}

func pydfm(ts []*tplStruct) {
	fm := make(template.FuncMap)
	fm["baseType"] = func(preType string) string {
		if preType == "int" { // typedef int TThostFtdcIPPortType; -> TThostFtdcIPPortType = c_int32
			return "c_int32"
		}
		if preType == "double" { // typedef double TThostFtdcPriceType; -> TThostFtdcPriceType = c_double
			return "c_double"
		}
		if preType == "short" { // typedef short TThostFtdcSequenceSeriesType; -> TThostFtdcSequenceSeriesType = c_short
			return "c_short"
		}
		if preType == "char" { // typedef char TThostFtdcNewsUrgencyType;
			return "c_char"
		}
		// [nn]byte
		if strings.Contains(preType, "[") { // typedef char TThostFtdcTraderIDType[21]; -> TThostFtdcTraderIDType = c_char*21
			return "c_char*" + strings.Split(strings.Split(preType, "[")[1], "]")[0]
		}
		return preType
	}
	fm["atoi"] = func(char string) int {
		return int(char[0])
	}
	tmpl("ctp_datatype.py.tpl", ts, fm, outpath)
}

func godfm(ts []*tplStruct) {
	mpCpp := make(map[string]interface{})
	mpCpp["St"] = ts
	mpCpp["Pf"] = csys
	fm := make(template.FuncMap)
	fm["baseType"] = func(preType string) string {
		if preType == "int" { // typedef int TThostFtdcIPPortType; -> TThostFtdcIPPortType = c_int32
			return "int32"
		}
		if preType == "double" { // typedef double TThostFtdcPriceType; -> TThostFtdcPriceType = c_double
			return "float64"
		}
		if preType == "short" { // typedef short TThostFtdcSequenceSeriesType; -> TThostFtdcSequenceSeriesType = c_short
			return "int16"
		}
		if preType == "char" { // typedef char TThostFtdcNewsUrgencyType;
			return "byte"
		}
		return preType
	}

	tmpl("ctp_datatype.go.tpl", mpCpp, fm, outpath)
}

func pysfm(ts []*tplStruct) {
	fm := make(template.FuncMap)
	fm["baseType"] = func(fieldType string) string {
		return fieldType
	}
	tmpl("ctp_struct.py.tpl", ts, fm, outpath)
}

func gosfm(ts []*tplStruct) {
	mpCpp := make(map[string]interface{})
	mpCpp["St"] = ts
	mpCpp["Pf"] = csys
	tmpl("ctp_struct.go.tpl", mpCpp, nil, outpath)
}

// Judge Platform type
func iscontain(item string, item_arr []string) error {
	for _, cit := range item_arr {
		if item == cit {
			return nil
		}
	}
	return errors.New("must input: linux or windows or macos")
}

func main() {

	flag.StringVar(&srcpath, "srcpath", "../csource/ctpapi",
		"Base path of CTP API")

	flag.StringVar(&csys, "csys", "macos",
		"Generate Wrapper for System, support: linux,windows,macos")

	flag.StringVar(&outpath, "outpath", "../pysource/CTPApi",
		"Output path")

	flag.StringVar(&lang, "lang", "python",
		"Language Wrapper, support: python,golang")

	flag.Parse()

	var sys_arr = []string{"linux", "windows", "macos"}
	err := iscontain(csys, sys_arr)
	if err != nil {
		panic(err)
	}
	srcpath = path.Join(srcpath, csys)

	if lang == "c" {
		gen_cwrap(cfm)
	} else if lang == "python" {
		gen_datatype(srcpath, pydfm)
		gen_struct(srcpath, pysfm)
		gen_cwrap(pycfm)
	} else if lang == "golang" {
		gen_datatype(srcpath, godfm)
		gen_struct(srcpath, gosfm)
		if csys == "windows" {
			gen_cwrap(wgocfm)
		} else {
			gen_cwrap(ccfm)
			gen_cwrap(xgocfm)
		}
	}

}
