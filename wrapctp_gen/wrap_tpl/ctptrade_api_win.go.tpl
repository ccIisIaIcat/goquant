package ctpapi

import (
	"os"
	"path"
	"path/filepath"
	"runtime"
	"syscall"
	"unsafe"
)

type Trade struct {
	h       *syscall.DLL
	api     uintptr
	pSpi    uintptr
	version string
	logdir  string

    [[ range .On]]// [[ .Comment ]]
    [[ .FuncName ]]_ func([[ range $i,$v := .FuncFields ]][[ if gt $i 0 ]], [[ end ]][[if eq .FieldName "*ppInstrumentID"]][[ .FieldName|trimStar ]] [][]byte [[else]][[ .FieldName|trimStar ]] [[ .FieldType|ctp_type ]][[end]][[ end ]])
    [[ end]]
}

func InitTrade() *Trade {
	t := new(Trade)
	// Load DLL
	workPath, _ := os.Getwd()
	_, curFile, _, _ := runtime.Caller(1)
	dllPath := filepath.Dir(curFile)
	dllPath = path.Join(dllPath, "../../libs/ctpapi/")
	_ = os.Chdir(dllPath)
	t.h = syscall.MustLoadDLL("ctptrade_api.dll")
	os.Chdir(workPath)

	t.logdir = "./log/"
	// 执行目录下创建 log目录
	_, err := os.Stat("log")
	if err != nil {
		os.Mkdir("log", os.ModePerm)
	}
	t.api = t.CreateApi()
	t.pSpi = t.CreateSpi()
	t.version = t.GetApiVersion()

	return t
}

func (t *Trade) CreateApi() uintptr {
	bs, _ := syscall.BytePtrFromString(t.logdir)
	api, _, _ := t.h.MustFindProc("tCreateApi").Call(uintptr(unsafe.Pointer(bs)))
	return api
}

func (t *Trade) CreateSpi() uintptr {
	pSpi, _, _ := t.h.MustFindProc("tCreateSpi").Call()
	return pSpi
}

func (t *Trade) GetApiVersion() string {
	ver, _, _ := t.h.MustFindProc("tGetApiVersion").Call()
	p := (*byte)(unsafe.Pointer(ver))
	data := make([]byte, 0)
	for *p != 0 {
		data = append(data, *p)
		ver += unsafe.Sizeof(byte(0))
		p = (*byte)(unsafe.Pointer(ver))
	}

	return string(data)
}

func (t *Trade) GetTradingDay() string {
	ver, _, _ := t.h.MustFindProc("tGetTradingDay").Call(uintptr(t.api))
	p := (*byte)(unsafe.Pointer(ver))
	data := make([]byte, 0)
	for *p != 0 {
		data = append(data, *p)
		ver += unsafe.Sizeof(byte(0))
		p = (*byte)(unsafe.Pointer(ver))
	}

	return string(data)
}

func (t *Trade) CTP_GetSystemInfo(pSystemInfo *TThostFtdcClientSystemInfoType, nLen TThostFtdcSystemInfoLenType) int32 {
	res, _, _ := t.h.MustFindProc("dCTP_GetSystemInfo").Call(uintptr(unsafe.Pointer(pSystemInfo)), uintptr(nLen))
	return int32(res)
}

[[ if eq .Pf "macos"]]func (t *Trade) CTP_GetSystemInfoUnAesEncode(pSystemInfo *TThostFtdcClientSystemInfoType, nLen TThostFtdcSystemInfoLenType) int32 {
	res, _, _ := t.h.MustFindProc("dCTP_GetSystemInfoUnAesEncode").Call(uintptr(unsafe.Pointer(pSystemInfo), uintptr(nLen)))
	return int32(res)
}[[ end ]]

func (t *Trade) CTP_GetDataCollectApiVersion() string {
	ver, _, _ := t.h.MustFindProc("dCTP_GetDataCollectApiVersion").Call()
	p := (*byte)(unsafe.Pointer(ver))
	data := make([]byte, 0)
	for *p != 0 {
		data = append(data, *p)
		ver += unsafe.Sizeof(byte(0))
		p = (*byte)(unsafe.Pointer(ver))
	}
	return string(data)
}
[[ range .Fn]][[if eq .FuncRtn "void"]]
[[if eq .FuncName "RegisterSpi"]]
func (t *Trade) [[ .FuncName ]]() { [[else]]
func (t *Trade) [[ .FuncName ]]([[ range $i,$v := .FuncFields ]][[ if gt $i 0 ]][[ if gt $i 1 ]], [[ end ]][[if eq .FieldName "*ppInstrumentID"]][[ .FieldName|trimStar ]] [][]byte [[else]][[ .FieldName|trimStar ]] [[ .FieldType|ctp_type ]][[end]][[ end ]][[end]]) { [[end]]
	t.h.MustFindProc("t[[ .FuncName ]]").Call([[ range $i,$v := .FuncFields ]][[ if gt $i 0 ]], [[ end ]][[ fldType .FieldType .FieldName ]][[ end ]])
}[[ else ]]
func (t *Trade) [[ .FuncName ]]([[ range $i,$v := .FuncFields ]][[ if gt $i 0 ]][[ if gt $i 1 ]], [[ end ]][[if eq .FieldName "*ppInstrumentID"]][[ .FieldName|trimStar ]] [][]byte [[else]][[ .FieldName|trimStar ]] [[ .FieldType|ctp_type ]][[end]][[ end ]][[end]]) [[ .FuncRtn ]]32 {
	res, _, _ := t.h.MustFindProc("t[[ .FuncName ]]").Call([[ range $i,$v := .FuncFields ]][[ if gt $i 0 ]], [[ end ]][[ fldType .FieldType .FieldName ]][[ end ]])
	return [[ .FuncRtn ]]32(res)
}
[[ end]][[ end ]]
[[ range .On ]]
// [[ .Comment ]]
func (t *Trade) [[ .FuncName ]](fn func([[ range $i, $v := .FuncFields ]][[ if gt $i 0]], [[ end ]][[ .FieldName|trimStar ]] [[ .FieldType|ctp_type]][[ end ]])) {
    t.[[ .FuncName ]]_ = fn
	t.h.MustFindProc("t[[ .FuncName ]]").Call(t.pSpi, syscall.NewCallback(t.[[.FuncName]]__))
}
[[ end ]]
[[ range .On ]]
// [[ .Comment ]]
func (t *Trade) [[ .FuncName ]]__([[ range $i, $v := .FuncFields ]][[ if gt $i 0]], [[ end ]][[ .FieldName|trimStar ]] [[ .FieldType|ctp_type]][[ end ]]) uintptr {
    if t.[[ .FuncName ]]_ != nil {    
	    t.[[ .FuncName ]]_([[ range $i,$v := .FuncFields ]][[ if gt $i 0 ]], [[ end ]][[ .FieldName|trimStar ]][[ end ]])
    }
	return 0
}
[[ end ]]