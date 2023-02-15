package ctpapi

/*
#cgo LDFLAGS: -L${SRCDIR}/../../libs/ctpapi -lctptrade_api
#include "cctptrade_api_[[if eq .Pf "macos"]]darwin[[else]][[.Pf]][[end]].h"
*/
import "C"
import (
	"os"
	"unsafe"
)

type Trade struct {
	api     unsafe.Pointer
	pSpi    unsafe.Pointer
	version string
	logdir  string

    [[ range .On]]// [[ .Comment ]]
    [[ .FuncName ]]_ func([[ range $i,$v := .FuncFields ]][[ if gt $i 0 ]], [[ end ]][[if eq .FieldName "*ppInstrumentID"]][[ .FieldName|trimStar ]] [][]byte [[else]][[ .FieldName|trimStar ]] [[ .FieldType|ctp_type ]][[end]][[ end ]])
    [[ end]]
}

var t *Trade

func InitTrade() *Trade{
	t = new(Trade)
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


func (t *Trade) CreateApi() unsafe.Pointer {
	api := C.tCreateApi(C.CString(t.logdir))
	return api
}

func (t *Trade) CreateSpi() unsafe.Pointer {
	pSpi := C.tCreateSpi()
	return pSpi
}

func (t *Trade) GetApiVersion() string {
    return C.GoString((*C.char)(C.tGetApiVersion()))
}

func (t *Trade) GetTradingDay() string {
    return C.GoString((*C.char)(C.tGetTradingDay(t.api)))
}

func (t *Trade) CTP_GetSystemInfo(pSystemInfo *TThostFtdcClientSystemInfoType, nLen TThostFtdcSystemInfoLenType) int32 {
	pchar := C.malloc(C.size_t(nLen))
	res := C.dCTP_GetSystemInfo((*C.char)(unsafe.Pointer(pchar)), C.int(nLen))
	copy(pSystemInfo[:], C.GoBytes(unsafe.Pointer(pchar), C.int(nLen)))
	C.free(unsafe.Pointer(pchar))
	return int32(res)
}

[[ if eq .Pf "macos"]]func (t *Trade) CTP_GetSystemInfoUnAesEncode(pSystemInfo *TThostFtdcClientSystemInfoType, nLen TThostFtdcSystemInfoLenType) int32 {
	pchar := C.malloc(C.size_t(nLen))
	res := C.dCTP_GetSystemInfoUnAesEncode((*C.char)(unsafe.Pointer(pchar)), C.int(nLen))
	copy(pSystemInfo[:], C.GoBytes(unsafe.Pointer(pchar), C.int(nLen)))
	C.free(unsafe.Pointer(pchar))
	return int32(res)
}[[ end ]]

func (t *Trade) CTP_GetDataCollectApiVersion() string {
	return C.GoString((*C.char)(C.dCTP_GetDataCollectApiVersion()))
}
[[ range .Fn]][[ if eq .FuncRtn "void"]][[if eq .FuncName "RegisterSpi"]]
func (t *Trade) [[ .FuncName ]]() { [[else]]
func (t *Trade) [[ .FuncName ]]([[ range $i,$v := .FuncFields ]][[ if gt $i 0 ]][[ if gt $i 1 ]], [[ end ]][[if eq .FieldName "*ppInstrumentID"]][[ .FieldName|trimStar ]] [][]byte [[else]][[ .FieldName|trimStar ]] [[ .FieldType|ctp_type ]][[end]][[ end ]][[end]]) { [[end]]
	[[ range .FuncFields ]] [[ supType .FieldType .FieldName ]] [[ end ]]
	C.t[[ .FuncName ]]([[ range $i,$v := .FuncFields ]][[ if gt $i 0 ]], [[ end ]][[ fldType .FieldType .FieldName ]][[ end ]])
}[[ else ]][[if eq .FuncName "ReqUserLogin"]]
func (t *Trade) [[ .FuncName ]]([[ range $i,$v := .FuncFields ]][[ if gt $i 0 ]][[ if lt $i 3 ]][[ if gt $i 1 ]], [[ end ]][[if eq .FieldName "*ppInstrumentID"]][[ .FieldName|trimStar ]] [][]byte [[else]][[ .FieldName|trimStar ]] [[ .FieldType|ctp_type ]][[end]][[ end ]][[end]][[end]]) [[ .FuncRtn ]]32 {
	[[ range .FuncFields ]] [[ supType .FieldType .FieldName ]] [[ end ]][[ if eq $.Pf "macos"]]
	var systemInfo TThostFtdcClientSystemInfoType
	var length TThostFtdcSystemInfoLenType = 273
	t.CTP_GetSystemInfoUnAesEncode(&systemInfo, length)[[end]]
	res := C.t[[ .FuncName ]]([[ range $i,$v := .FuncFields ]][[ if gt $i 0 ]], [[ end ]][[ fldType .FieldType .FieldName ]][[ end ]])
	return [[ .FuncRtn ]]32(res)
}[[else]]
func (t *Trade) [[ .FuncName ]]([[ range $i,$v := .FuncFields ]][[ if gt $i 0 ]][[ if gt $i 1 ]], [[ end ]][[if eq .FieldName "*ppInstrumentID"]][[ .FieldName|trimStar ]] [][]byte [[else]][[ .FieldName|trimStar ]] [[ .FieldType|ctp_type ]][[end]][[ end ]][[end]]) [[ .FuncRtn ]]32 {
	[[ range .FuncFields ]] [[ supType .FieldType .FieldName ]] [[ end ]]
	res := C.t[[ .FuncName ]]([[ range $i,$v := .FuncFields ]][[ if gt $i 0 ]], [[ end ]][[ fldType .FieldType .FieldName ]][[ end ]])
	return [[ .FuncRtn ]]32(res)
}[[ end ]][[ end ]]
[[end]]
[[ range .On]]// [[ .Comment ]]
func (t *Trade) [[ .FuncName ]] (fn func([[ range $i,$v := .FuncFields ]][[ if gt $i 0 ]], [[ end ]][[if eq .FieldName "*ppInstrumentID"]][[ .FieldName|trimStar ]] [][]byte [[else]][[ .FieldName|trimStar ]] [[ .FieldType|ctp_type ]][[end]][[ end ]])) {
	t.[[ .FuncName ]]_ = fn
	C.t[[ .FuncName ]](t.pSpi, C.t[[ .FuncName ]]_)
}
[[ end]]

[[ range .On ]]
//export t[[ .FuncName ]]_
func t[[ .FuncName ]]_([[ range $i, $v := .FuncFields ]][[ if gt $i 0]], [[ end ]][[ .FieldName|trimStar ]] [[ .FieldType|C_struct]][[ end ]]) C.int {
    if t.[[ .FuncName ]]_ != nil{
        t.[[ .FuncName ]]_([[ range $i,$v := .FuncFields ]][[ if gt $i 0 ]], [[ end ]][[ ctp_param .FieldType .FieldName ]][[ end ]])
    }
	return 0
}
[[ end ]]