package ctpapi

import (
	"os"
	"path"
	"path/filepath"
	"runtime"
	"syscall"
	"unsafe"
)

type Quote struct {
	h       *syscall.DLL
	api     uintptr
	pSpi    uintptr
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

func InitQuote() *Quote {
	q := new(Quote)
	// Load DLL
	workPath, _ := os.Getwd()
	_, curFile, _, _ := runtime.Caller(1)
	dllPath := filepath.Dir(curFile)
	dllPath = path.Join(dllPath, "../../libs/ctpapi/")
	_ = os.Chdir(dllPath)
	q.h = syscall.MustLoadDLL("ctpquote_api.dll")
	os.Chdir(workPath)

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

func (q *Quote) CreateApi() uintptr {
	bs, _ := syscall.BytePtrFromString(q.logdir)
	api, _, _ := q.h.MustFindProc("qCreateApi").Call(uintptr(unsafe.Pointer(bs)))
	return api
}

func (q *Quote) CreateSpi() uintptr {
	pSpi, _, _ := q.h.MustFindProc("qCreateSpi").Call()
	return pSpi
}

func (q *Quote) GetApiVersion() string {
	ver, _, _ := q.h.MustFindProc("qGetApiVersion").Call()
	p := (*byte)(unsafe.Pointer(ver))
	data := make([]byte, 0)
	for *p != 0 {
		data = append(data, *p)
		ver += unsafe.Sizeof(byte(0))
		p = (*byte)(unsafe.Pointer(ver))
	}

	return string(data)
}

func (q *Quote) GetTradingDay() string {
	ver, _, _ := q.h.MustFindProc("qGetTradingDay").Call(uintptr(q.api))
	p := (*byte)(unsafe.Pointer(ver))
	data := make([]byte, 0)
	for *p != 0 {
		data = append(data, *p)
		ver += unsafe.Sizeof(byte(0))
		p = (*byte)(unsafe.Pointer(ver))
	}

	return string(data)
}

func (q *Quote) Release() {
	q.h.MustFindProc("qRelease").Call(uintptr(q.api))
}

func (q *Quote) Init() {
	q.h.MustFindProc("qInit").Call(uintptr(q.api))
}
func (q *Quote) Join() int32 {
	res, _, _ := q.h.MustFindProc("qJoin").Call(uintptr(q.api))
	return int32(res)
}

func (q *Quote) RegisterFront(pszFrontAddress []byte) {
	q.h.MustFindProc("qRegisterFront").Call(uintptr(q.api), uintptr(unsafe.Pointer(&pszFrontAddress[0])))
}

func (q *Quote) RegisterNameServer(pszNsAddress []byte) {
	q.h.MustFindProc("qRegisterNameServer").Call(uintptr(q.api), uintptr(unsafe.Pointer(&pszNsAddress[0])))
}

func (q *Quote) RegisterFensUserInfo(pFensUserInfo *CThostFtdcFensUserInfoField) {
	q.h.MustFindProc("qRegisterFensUserInfo").Call(uintptr(q.api), uintptr(unsafe.Pointer(pFensUserInfo)))
}

func (q *Quote) RegisterSpi() {
	q.h.MustFindProc("qRegisterSpi").Call(uintptr(q.api), uintptr(q.pSpi))
}
func (q *Quote) SubscribeMarketData(ppInstrumentID [][]byte, nCount int) int32 {
	res, _, _ := q.h.MustFindProc("qSubscribeMarketData").Call(uintptr(q.api), uintptr(unsafe.Pointer(&ppInstrumentID[0])), uintptr(nCount))
	return int32(res)
}
func (q *Quote) UnSubscribeMarketData(ppInstrumentID [][]byte, nCount int) int32 {
	res, _, _ := q.h.MustFindProc("qUnSubscribeMarketData").Call(uintptr(q.api), uintptr(unsafe.Pointer(&ppInstrumentID[0])), uintptr(nCount))
	return int32(res)
}
func (q *Quote) SubscribeForQuoteRsp(ppInstrumentID [][]byte, nCount int) int32 {
	res, _, _ := q.h.MustFindProc("qSubscribeForQuoteRsp").Call(uintptr(q.api), uintptr(unsafe.Pointer(&ppInstrumentID[0])), uintptr(nCount))
	return int32(res)
}
func (q *Quote) UnSubscribeForQuoteRsp(ppInstrumentID [][]byte, nCount int) int32 {
	res, _, _ := q.h.MustFindProc("qUnSubscribeForQuoteRsp").Call(uintptr(q.api), uintptr(unsafe.Pointer(&ppInstrumentID[0])), uintptr(nCount))
	return int32(res)
}
func (q *Quote) ReqUserLogin(pReqUserLoginField *CThostFtdcReqUserLoginField, nRequestID int) int32 {
	res, _, _ := q.h.MustFindProc("qReqUserLogin").Call(uintptr(q.api), uintptr(unsafe.Pointer(pReqUserLoginField)), uintptr(nRequestID))
	return int32(res)
}
func (q *Quote) ReqUserLogout(pUserLogout *CThostFtdcUserLogoutField, nRequestID int) int32 {
	res, _, _ := q.h.MustFindProc("qReqUserLogout").Call(uintptr(q.api), uintptr(unsafe.Pointer(pUserLogout)), uintptr(nRequestID))
	return int32(res)
}
func (q *Quote) ReqQryMulticastInstrument(pQryMulticastInstrument *CThostFtdcQryMulticastInstrumentField, nRequestID int) int32 {
	res, _, _ := q.h.MustFindProc("qReqQryMulticastInstrument").Call(uintptr(q.api), uintptr(unsafe.Pointer(pQryMulticastInstrument)), uintptr(nRequestID))
	return int32(res)
}

// 当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。
func (q *Quote) OnFrontConnected(fn func()) {
	q.OnFrontConnected_ = fn
	q.h.MustFindProc("qOnFrontConnected").Call(q.pSpi, syscall.NewCallback(q.OnFrontConnected__))
}

// 当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。
func (q *Quote) OnFrontDisconnected(fn func(nReason int)) {
	q.OnFrontDisconnected_ = fn
	q.h.MustFindProc("qOnFrontDisconnected").Call(q.pSpi, syscall.NewCallback(q.OnFrontDisconnected__))
}

// 心跳超时警告。当长时间未收到报文时，该方法被调用。
func (q *Quote) OnHeartBeatWarning(fn func(nTimeLapse int)) {
	q.OnHeartBeatWarning_ = fn
	q.h.MustFindProc("qOnHeartBeatWarning").Call(q.pSpi, syscall.NewCallback(q.OnHeartBeatWarning__))
}

// 登录请求响应
func (q *Quote) OnRspUserLogin(fn func(pRspUserLogin *CThostFtdcRspUserLoginField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	q.OnRspUserLogin_ = fn
	q.h.MustFindProc("qOnRspUserLogin").Call(q.pSpi, syscall.NewCallback(q.OnRspUserLogin__))
}

// 登出请求响应
func (q *Quote) OnRspUserLogout(fn func(pUserLogout *CThostFtdcUserLogoutField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	q.OnRspUserLogout_ = fn
	q.h.MustFindProc("qOnRspUserLogout").Call(q.pSpi, syscall.NewCallback(q.OnRspUserLogout__))
}

// 请求查询组播合约响应
func (q *Quote) OnRspQryMulticastInstrument(fn func(pMulticastInstrument *CThostFtdcMulticastInstrumentField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	q.OnRspQryMulticastInstrument_ = fn
	q.h.MustFindProc("qOnRspQryMulticastInstrument").Call(q.pSpi, syscall.NewCallback(q.OnRspQryMulticastInstrument__))
}

// 错误应答
func (q *Quote) OnRspError(fn func(pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	q.OnRspError_ = fn
	q.h.MustFindProc("qOnRspError").Call(q.pSpi, syscall.NewCallback(q.OnRspError__))
}

// 订阅行情应答
func (q *Quote) OnRspSubMarketData(fn func(pSpecificInstrument *CThostFtdcSpecificInstrumentField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	q.OnRspSubMarketData_ = fn
	q.h.MustFindProc("qOnRspSubMarketData").Call(q.pSpi, syscall.NewCallback(q.OnRspSubMarketData__))
}

// 取消订阅行情应答
func (q *Quote) OnRspUnSubMarketData(fn func(pSpecificInstrument *CThostFtdcSpecificInstrumentField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	q.OnRspUnSubMarketData_ = fn
	q.h.MustFindProc("qOnRspUnSubMarketData").Call(q.pSpi, syscall.NewCallback(q.OnRspUnSubMarketData__))
}

// 订阅询价应答
func (q *Quote) OnRspSubForQuoteRsp(fn func(pSpecificInstrument *CThostFtdcSpecificInstrumentField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	q.OnRspSubForQuoteRsp_ = fn
	q.h.MustFindProc("qOnRspSubForQuoteRsp").Call(q.pSpi, syscall.NewCallback(q.OnRspSubForQuoteRsp__))
}

// 取消订阅询价应答
func (q *Quote) OnRspUnSubForQuoteRsp(fn func(pSpecificInstrument *CThostFtdcSpecificInstrumentField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	q.OnRspUnSubForQuoteRsp_ = fn
	q.h.MustFindProc("qOnRspUnSubForQuoteRsp").Call(q.pSpi, syscall.NewCallback(q.OnRspUnSubForQuoteRsp__))
}

// 深度行情通知
func (q *Quote) OnRtnDepthMarketData(fn func(pDepthMarketData *CThostFtdcDepthMarketDataField)) {
	q.OnRtnDepthMarketData_ = fn
	q.h.MustFindProc("qOnRtnDepthMarketData").Call(q.pSpi, syscall.NewCallback(q.OnRtnDepthMarketData__))
}

// 询价通知
func (q *Quote) OnRtnForQuoteRsp(fn func(pForQuoteRsp *CThostFtdcForQuoteRspField)) {
	q.OnRtnForQuoteRsp_ = fn
	q.h.MustFindProc("qOnRtnForQuoteRsp").Call(q.pSpi, syscall.NewCallback(q.OnRtnForQuoteRsp__))
}

// 当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。
func (q *Quote) OnFrontConnected__() uintptr {
	if q.OnFrontConnected_ != nil {
		q.OnFrontConnected_()
	}
	return 0
}

// 当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。
func (q *Quote) OnFrontDisconnected__(nReason int) uintptr {
	if q.OnFrontDisconnected_ != nil {
		q.OnFrontDisconnected_(nReason)
	}
	return 0
}

// 心跳超时警告。当长时间未收到报文时，该方法被调用。
func (q *Quote) OnHeartBeatWarning__(nTimeLapse int) uintptr {
	if q.OnHeartBeatWarning_ != nil {
		q.OnHeartBeatWarning_(nTimeLapse)
	}
	return 0
}

// 登录请求响应
func (q *Quote) OnRspUserLogin__(pRspUserLogin *CThostFtdcRspUserLoginField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
	if q.OnRspUserLogin_ != nil {
		q.OnRspUserLogin_(pRspUserLogin, pRspInfo, nRequestID, bIsLast)
	}
	return 0
}

// 登出请求响应
func (q *Quote) OnRspUserLogout__(pUserLogout *CThostFtdcUserLogoutField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
	if q.OnRspUserLogout_ != nil {
		q.OnRspUserLogout_(pUserLogout, pRspInfo, nRequestID, bIsLast)
	}
	return 0
}

// 请求查询组播合约响应
func (q *Quote) OnRspQryMulticastInstrument__(pMulticastInstrument *CThostFtdcMulticastInstrumentField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
	if q.OnRspQryMulticastInstrument_ != nil {
		q.OnRspQryMulticastInstrument_(pMulticastInstrument, pRspInfo, nRequestID, bIsLast)
	}
	return 0
}

// 错误应答
func (q *Quote) OnRspError__(pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
	if q.OnRspError_ != nil {
		q.OnRspError_(pRspInfo, nRequestID, bIsLast)
	}
	return 0
}

// 订阅行情应答
func (q *Quote) OnRspSubMarketData__(pSpecificInstrument *CThostFtdcSpecificInstrumentField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
	if q.OnRspSubMarketData_ != nil {
		q.OnRspSubMarketData_(pSpecificInstrument, pRspInfo, nRequestID, bIsLast)
	}
	return 0
}

// 取消订阅行情应答
func (q *Quote) OnRspUnSubMarketData__(pSpecificInstrument *CThostFtdcSpecificInstrumentField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
	if q.OnRspUnSubMarketData_ != nil {
		q.OnRspUnSubMarketData_(pSpecificInstrument, pRspInfo, nRequestID, bIsLast)
	}
	return 0
}

// 订阅询价应答
func (q *Quote) OnRspSubForQuoteRsp__(pSpecificInstrument *CThostFtdcSpecificInstrumentField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
	if q.OnRspSubForQuoteRsp_ != nil {
		q.OnRspSubForQuoteRsp_(pSpecificInstrument, pRspInfo, nRequestID, bIsLast)
	}
	return 0
}

// 取消订阅询价应答
func (q *Quote) OnRspUnSubForQuoteRsp__(pSpecificInstrument *CThostFtdcSpecificInstrumentField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
	if q.OnRspUnSubForQuoteRsp_ != nil {
		q.OnRspUnSubForQuoteRsp_(pSpecificInstrument, pRspInfo, nRequestID, bIsLast)
	}
	return 0
}

// 深度行情通知
func (q *Quote) OnRtnDepthMarketData__(pDepthMarketData *CThostFtdcDepthMarketDataField) uintptr {
	if q.OnRtnDepthMarketData_ != nil {
		q.OnRtnDepthMarketData_(pDepthMarketData)
	}
	return 0
}

// 询价通知
func (q *Quote) OnRtnForQuoteRsp__(pForQuoteRsp *CThostFtdcForQuoteRspField) uintptr {
	if q.OnRtnForQuoteRsp_ != nil {
		q.OnRtnForQuoteRsp_(pForQuoteRsp)
	}
	return 0
}
