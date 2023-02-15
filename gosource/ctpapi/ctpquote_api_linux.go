package ctpapi

/*
#cgo LDFLAGS: -L${SRCDIR}/../../libs/ctpapi -lctpquote_api
#include "cctpquote_api_linux.h"
*/
import "C"
import (
	"os"
	"unsafe"
)

type Quote struct {
	api     unsafe.Pointer
	pSpi    unsafe.Pointer
	version string
	logdir  string

    // 当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。
    OnFrontConnected_ func()
    // 当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。
    OnFrontDisconnected_ func(nReason int)
    // 心跳超时警告。当长时间未收到报文时，该方法被调用。
    OnHeartBeatWarning_ func(nTimeLapse int)
    // 登录请求响应
    OnRspUserLogin_ func(pRspUserLogin *CThostFtdcRspUserLoginField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 登出请求响应
    OnRspUserLogout_ func(pUserLogout *CThostFtdcUserLogoutField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询组播合约响应
    OnRspQryMulticastInstrument_ func(pMulticastInstrument *CThostFtdcMulticastInstrumentField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 错误应答
    OnRspError_ func(pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 订阅行情应答
    OnRspSubMarketData_ func(pSpecificInstrument *CThostFtdcSpecificInstrumentField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 取消订阅行情应答
    OnRspUnSubMarketData_ func(pSpecificInstrument *CThostFtdcSpecificInstrumentField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 订阅询价应答
    OnRspSubForQuoteRsp_ func(pSpecificInstrument *CThostFtdcSpecificInstrumentField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 取消订阅询价应答
    OnRspUnSubForQuoteRsp_ func(pSpecificInstrument *CThostFtdcSpecificInstrumentField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 深度行情通知
    OnRtnDepthMarketData_ func(pDepthMarketData *CThostFtdcDepthMarketDataField)
    // 询价通知
    OnRtnForQuoteRsp_ func(pForQuoteRsp *CThostFtdcForQuoteRspField)
    
}

var q *Quote

func InitQuote() *Quote {
	q = new(Quote)
	q.logdir = "./log/"
	// 执行目录下创建 log目录
	_, err := os.Stat("log")
	if err != nil {
		os.Mkdir("log", os.ModePerm)
	}
	q.api = q.CreateApi()
	q.pSpi = q.CreateSpi()
	q.version = q.GetApiVersion()

	return q
}

func (q *Quote) CreateApi() unsafe.Pointer {
	api := C.qCreateApi(C.CString(q.logdir), C._Bool(false), C._Bool(false))
	return api
}

func (q *Quote) CreateSpi() unsafe.Pointer {
	pSpi := C.qCreateSpi()
	return pSpi
}

func (q *Quote) GetApiVersion() string {
    return C.GoString((*C.char)(C.qGetApiVersion()))
}

func (q *Quote) GetTradingDay() string {
    return C.GoString((*C.char)(C.qGetTradingDay(q.api)))
}
 
func (q *Quote) Release() { 
	  
	C.qRelease(q.api)
}
 
func (q *Quote) Init() { 
	  
	C.qInit(q.api)
}

func (q *Quote) Join() int32 {
	  
	res := C.qJoin(q.api)
	return int32(res)
}
 
func (q *Quote) RegisterFront(pszFrontAddress []byte) { 
	    
	C.qRegisterFront(q.api, (*C.char)(unsafe.Pointer(C.CBytes(pszFrontAddress))))
}
 
func (q *Quote) RegisterNameServer(pszNsAddress []byte) { 
	    
	C.qRegisterNameServer(q.api, (*C.char)(unsafe.Pointer(C.CBytes(pszNsAddress))))
}
 
func (q *Quote) RegisterFensUserInfo( pFensUserInfo *CThostFtdcFensUserInfoField) { 
	    
	C.qRegisterFensUserInfo(q.api, (*C.struct_CThostFtdcFensUserInfoField)(unsafe.Pointer( pFensUserInfo)))
}
 
func (q *Quote) RegisterSpi() { 
	    
	C.qRegisterSpi(q.api, q.pSpi)
}

func (q *Quote) SubscribeMarketData(ppInstrumentID [][]byte , nCount int) int32 {
	   
	tmp_arr := make([]*C.char, len(ppInstrumentID))
		for i := 0; i < len(tmp_arr); i++ {
			tmp_arr[i] = (*C.char)(unsafe.Pointer(C.CBytes(ppInstrumentID[i])))
		}
	   
	res := C.qSubscribeMarketData(q.api, (**C.char)(unsafe.Pointer(&tmp_arr[0])), C.int(nCount))
	return int32(res)
}

func (q *Quote) UnSubscribeMarketData(ppInstrumentID [][]byte , nCount int) int32 {
	   
	tmp_arr := make([]*C.char, len(ppInstrumentID))
		for i := 0; i < len(tmp_arr); i++ {
			tmp_arr[i] = (*C.char)(unsafe.Pointer(C.CBytes(ppInstrumentID[i])))
		}
	   
	res := C.qUnSubscribeMarketData(q.api, (**C.char)(unsafe.Pointer(&tmp_arr[0])), C.int(nCount))
	return int32(res)
}

func (q *Quote) SubscribeForQuoteRsp(ppInstrumentID [][]byte , nCount int) int32 {
	   
	tmp_arr := make([]*C.char, len(ppInstrumentID))
		for i := 0; i < len(tmp_arr); i++ {
			tmp_arr[i] = (*C.char)(unsafe.Pointer(C.CBytes(ppInstrumentID[i])))
		}
	   
	res := C.qSubscribeForQuoteRsp(q.api, (**C.char)(unsafe.Pointer(&tmp_arr[0])), C.int(nCount))
	return int32(res)
}

func (q *Quote) UnSubscribeForQuoteRsp(ppInstrumentID [][]byte , nCount int) int32 {
	   
	tmp_arr := make([]*C.char, len(ppInstrumentID))
		for i := 0; i < len(tmp_arr); i++ {
			tmp_arr[i] = (*C.char)(unsafe.Pointer(C.CBytes(ppInstrumentID[i])))
		}
	   
	res := C.qUnSubscribeForQuoteRsp(q.api, (**C.char)(unsafe.Pointer(&tmp_arr[0])), C.int(nCount))
	return int32(res)
}

func (q *Quote) ReqUserLogin(pReqUserLoginField *CThostFtdcReqUserLoginField, nRequestID int) int32 {
	      
	res := C.qReqUserLogin(q.api, (*C.struct_CThostFtdcReqUserLoginField)(unsafe.Pointer(pReqUserLoginField)), C.int(nRequestID))
	return int32(res)
}

func (q *Quote) ReqUserLogout(pUserLogout *CThostFtdcUserLogoutField, nRequestID int) int32 {
	      
	res := C.qReqUserLogout(q.api, (*C.struct_CThostFtdcUserLogoutField)(unsafe.Pointer(pUserLogout)), C.int(nRequestID))
	return int32(res)
}

func (q *Quote) ReqQryMulticastInstrument(pQryMulticastInstrument *CThostFtdcQryMulticastInstrumentField, nRequestID int) int32 {
	      
	res := C.qReqQryMulticastInstrument(q.api, (*C.struct_CThostFtdcQryMulticastInstrumentField)(unsafe.Pointer(pQryMulticastInstrument)), C.int(nRequestID))
	return int32(res)
}


// 当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。
func (q *Quote) OnFrontConnected (fn func()) {
	q.OnFrontConnected_ = fn
	C.qOnFrontConnected(q.pSpi, C.qOnFrontConnected_)
}
// 当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。
func (q *Quote) OnFrontDisconnected (fn func(nReason int)) {
	q.OnFrontDisconnected_ = fn
	C.qOnFrontDisconnected(q.pSpi, C.qOnFrontDisconnected_)
}
// 心跳超时警告。当长时间未收到报文时，该方法被调用。
func (q *Quote) OnHeartBeatWarning (fn func(nTimeLapse int)) {
	q.OnHeartBeatWarning_ = fn
	C.qOnHeartBeatWarning(q.pSpi, C.qOnHeartBeatWarning_)
}
// 登录请求响应
func (q *Quote) OnRspUserLogin (fn func(pRspUserLogin *CThostFtdcRspUserLoginField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	q.OnRspUserLogin_ = fn
	C.qOnRspUserLogin(q.pSpi, C.qOnRspUserLogin_)
}
// 登出请求响应
func (q *Quote) OnRspUserLogout (fn func(pUserLogout *CThostFtdcUserLogoutField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	q.OnRspUserLogout_ = fn
	C.qOnRspUserLogout(q.pSpi, C.qOnRspUserLogout_)
}
// 请求查询组播合约响应
func (q *Quote) OnRspQryMulticastInstrument (fn func(pMulticastInstrument *CThostFtdcMulticastInstrumentField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	q.OnRspQryMulticastInstrument_ = fn
	C.qOnRspQryMulticastInstrument(q.pSpi, C.qOnRspQryMulticastInstrument_)
}
// 错误应答
func (q *Quote) OnRspError (fn func(pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	q.OnRspError_ = fn
	C.qOnRspError(q.pSpi, C.qOnRspError_)
}
// 订阅行情应答
func (q *Quote) OnRspSubMarketData (fn func(pSpecificInstrument *CThostFtdcSpecificInstrumentField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	q.OnRspSubMarketData_ = fn
	C.qOnRspSubMarketData(q.pSpi, C.qOnRspSubMarketData_)
}
// 取消订阅行情应答
func (q *Quote) OnRspUnSubMarketData (fn func(pSpecificInstrument *CThostFtdcSpecificInstrumentField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	q.OnRspUnSubMarketData_ = fn
	C.qOnRspUnSubMarketData(q.pSpi, C.qOnRspUnSubMarketData_)
}
// 订阅询价应答
func (q *Quote) OnRspSubForQuoteRsp (fn func(pSpecificInstrument *CThostFtdcSpecificInstrumentField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	q.OnRspSubForQuoteRsp_ = fn
	C.qOnRspSubForQuoteRsp(q.pSpi, C.qOnRspSubForQuoteRsp_)
}
// 取消订阅询价应答
func (q *Quote) OnRspUnSubForQuoteRsp (fn func(pSpecificInstrument *CThostFtdcSpecificInstrumentField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	q.OnRspUnSubForQuoteRsp_ = fn
	C.qOnRspUnSubForQuoteRsp(q.pSpi, C.qOnRspUnSubForQuoteRsp_)
}
// 深度行情通知
func (q *Quote) OnRtnDepthMarketData (fn func(pDepthMarketData *CThostFtdcDepthMarketDataField)) {
	q.OnRtnDepthMarketData_ = fn
	C.qOnRtnDepthMarketData(q.pSpi, C.qOnRtnDepthMarketData_)
}
// 询价通知
func (q *Quote) OnRtnForQuoteRsp (fn func(pForQuoteRsp *CThostFtdcForQuoteRspField)) {
	q.OnRtnForQuoteRsp_ = fn
	C.qOnRtnForQuoteRsp(q.pSpi, C.qOnRtnForQuoteRsp_)
}



//export qOnFrontConnected_
func qOnFrontConnected_() C.int {
    if q.OnFrontConnected_ != nil{
        q.OnFrontConnected_()
    }
	return 0
}

//export qOnFrontDisconnected_
func qOnFrontDisconnected_(nReason C.int) C.int {
    if q.OnFrontDisconnected_ != nil{
        q.OnFrontDisconnected_(int(nReason))
    }
	return 0
}

//export qOnHeartBeatWarning_
func qOnHeartBeatWarning_(nTimeLapse C.int) C.int {
    if q.OnHeartBeatWarning_ != nil{
        q.OnHeartBeatWarning_(int(nTimeLapse))
    }
	return 0
}

//export qOnRspUserLogin_
func qOnRspUserLogin_(pRspUserLogin *C.struct_CThostFtdcRspUserLoginField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if q.OnRspUserLogin_ != nil{
        q.OnRspUserLogin_((*CThostFtdcRspUserLoginField)(unsafe.Pointer(pRspUserLogin)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export qOnRspUserLogout_
func qOnRspUserLogout_(pUserLogout *C.struct_CThostFtdcUserLogoutField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if q.OnRspUserLogout_ != nil{
        q.OnRspUserLogout_((*CThostFtdcUserLogoutField)(unsafe.Pointer(pUserLogout)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export qOnRspQryMulticastInstrument_
func qOnRspQryMulticastInstrument_(pMulticastInstrument *C.struct_CThostFtdcMulticastInstrumentField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if q.OnRspQryMulticastInstrument_ != nil{
        q.OnRspQryMulticastInstrument_((*CThostFtdcMulticastInstrumentField)(unsafe.Pointer(pMulticastInstrument)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export qOnRspError_
func qOnRspError_(pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if q.OnRspError_ != nil{
        q.OnRspError_((*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export qOnRspSubMarketData_
func qOnRspSubMarketData_(pSpecificInstrument *C.struct_CThostFtdcSpecificInstrumentField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if q.OnRspSubMarketData_ != nil{
        q.OnRspSubMarketData_((*CThostFtdcSpecificInstrumentField)(unsafe.Pointer(pSpecificInstrument)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export qOnRspUnSubMarketData_
func qOnRspUnSubMarketData_(pSpecificInstrument *C.struct_CThostFtdcSpecificInstrumentField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if q.OnRspUnSubMarketData_ != nil{
        q.OnRspUnSubMarketData_((*CThostFtdcSpecificInstrumentField)(unsafe.Pointer(pSpecificInstrument)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export qOnRspSubForQuoteRsp_
func qOnRspSubForQuoteRsp_(pSpecificInstrument *C.struct_CThostFtdcSpecificInstrumentField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if q.OnRspSubForQuoteRsp_ != nil{
        q.OnRspSubForQuoteRsp_((*CThostFtdcSpecificInstrumentField)(unsafe.Pointer(pSpecificInstrument)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export qOnRspUnSubForQuoteRsp_
func qOnRspUnSubForQuoteRsp_(pSpecificInstrument *C.struct_CThostFtdcSpecificInstrumentField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if q.OnRspUnSubForQuoteRsp_ != nil{
        q.OnRspUnSubForQuoteRsp_((*CThostFtdcSpecificInstrumentField)(unsafe.Pointer(pSpecificInstrument)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export qOnRtnDepthMarketData_
func qOnRtnDepthMarketData_(pDepthMarketData *C.struct_CThostFtdcDepthMarketDataField) C.int {
    if q.OnRtnDepthMarketData_ != nil{
        q.OnRtnDepthMarketData_((*CThostFtdcDepthMarketDataField)(unsafe.Pointer(pDepthMarketData)))
    }
	return 0
}

//export qOnRtnForQuoteRsp_
func qOnRtnForQuoteRsp_(pForQuoteRsp *C.struct_CThostFtdcForQuoteRspField) C.int {
    if q.OnRtnForQuoteRsp_ != nil{
        q.OnRtnForQuoteRsp_((*CThostFtdcForQuoteRspField)(unsafe.Pointer(pForQuoteRsp)))
    }
	return 0
}
