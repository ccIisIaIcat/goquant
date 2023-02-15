#include "ctpquote_api.h"
#include <string.h>


Quote::Quote()
{
	OnFrontConnected_ = NULL;
	OnFrontDisconnected_ = NULL;
	OnHeartBeatWarning_ = NULL;
	OnRspUserLogin_ = NULL;
	OnRspUserLogout_ = NULL;
	OnRspQryMulticastInstrument_ = NULL;
	OnRspError_ = NULL;
	OnRspSubMarketData_ = NULL;
	OnRspUnSubMarketData_ = NULL;
	OnRspSubForQuoteRsp_ = NULL;
	OnRspUnSubForQuoteRsp_ = NULL;
	OnRtnDepthMarketData_ = NULL;
	OnRtnForQuoteRsp_ = NULL;
	
}


DLL_EXPORT_C_DECL void* WPCTP qCreateApi(const char *pszFlowPath = "", const bool bIsUsingUdp=false, const bool bIsMulticast=false) { return CThostFtdcMdApi::CreateFtdcMdApi(pszFlowPath, bIsUsingUdp, bIsMulticast); }
DLL_EXPORT_C_DECL void* WPCTP qCreateSpi() { return new Quote(); }
DLL_EXPORT_C_DECL void* WPCTP qGetApiVersion() { return (void*)CThostFtdcMdApi::GetApiVersion(); }
DLL_EXPORT_C_DECL void* WPCTP qGetTradingDay(CThostFtdcMdApi *api) { return (void*)api->GetTradingDay(); }

// 当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。
DLL_EXPORT_C_DECL void WPCTP qOnFrontConnected(Quote* spi, void* func){ spi->OnFrontConnected_ = func; }

// 当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。
DLL_EXPORT_C_DECL void WPCTP qOnFrontDisconnected(Quote* spi, void* func){ spi->OnFrontDisconnected_ = func; }

// 心跳超时警告。当长时间未收到报文时，该方法被调用。
DLL_EXPORT_C_DECL void WPCTP qOnHeartBeatWarning(Quote* spi, void* func){ spi->OnHeartBeatWarning_ = func; }

// 登录请求响应
DLL_EXPORT_C_DECL void WPCTP qOnRspUserLogin(Quote* spi, void* func){ spi->OnRspUserLogin_ = func; }

// 登出请求响应
DLL_EXPORT_C_DECL void WPCTP qOnRspUserLogout(Quote* spi, void* func){ spi->OnRspUserLogout_ = func; }

// 请求查询组播合约响应
DLL_EXPORT_C_DECL void WPCTP qOnRspQryMulticastInstrument(Quote* spi, void* func){ spi->OnRspQryMulticastInstrument_ = func; }

// 错误应答
DLL_EXPORT_C_DECL void WPCTP qOnRspError(Quote* spi, void* func){ spi->OnRspError_ = func; }

// 订阅行情应答
DLL_EXPORT_C_DECL void WPCTP qOnRspSubMarketData(Quote* spi, void* func){ spi->OnRspSubMarketData_ = func; }

// 取消订阅行情应答
DLL_EXPORT_C_DECL void WPCTP qOnRspUnSubMarketData(Quote* spi, void* func){ spi->OnRspUnSubMarketData_ = func; }

// 订阅询价应答
DLL_EXPORT_C_DECL void WPCTP qOnRspSubForQuoteRsp(Quote* spi, void* func){ spi->OnRspSubForQuoteRsp_ = func; }

// 取消订阅询价应答
DLL_EXPORT_C_DECL void WPCTP qOnRspUnSubForQuoteRsp(Quote* spi, void* func){ spi->OnRspUnSubForQuoteRsp_ = func; }

// 深度行情通知
DLL_EXPORT_C_DECL void WPCTP qOnRtnDepthMarketData(Quote* spi, void* func){ spi->OnRtnDepthMarketData_ = func; }

// 询价通知
DLL_EXPORT_C_DECL void WPCTP qOnRtnForQuoteRsp(Quote* spi, void* func){ spi->OnRtnForQuoteRsp_ = func; }


// 创建MdApi
DLL_EXPORT_C_DECL void WPCTP qRelease(CThostFtdcMdApi *api){ api->Release(); return; }

// 初始化
DLL_EXPORT_C_DECL void WPCTP qInit(CThostFtdcMdApi *api){ api->Init(); return; }

// 等待接口线程结束运行
DLL_EXPORT_C_DECL int WPCTP qJoin(CThostFtdcMdApi *api){ return api->Join(); }

// 注册前置机网络地址
DLL_EXPORT_C_DECL void WPCTP qRegisterFront(CThostFtdcMdApi *api, char *pszFrontAddress){ api->RegisterFront(pszFrontAddress); return; }

// @remark RegisterNameServer优先于RegisterFront
DLL_EXPORT_C_DECL void WPCTP qRegisterNameServer(CThostFtdcMdApi *api, char *pszNsAddress){ api->RegisterNameServer(pszNsAddress); return; }

// 注册名字服务器用户信息
DLL_EXPORT_C_DECL void WPCTP qRegisterFensUserInfo(CThostFtdcMdApi *api, CThostFtdcFensUserInfoField * pFensUserInfo){ api->RegisterFensUserInfo( pFensUserInfo); return; }

// 注册回调接口
DLL_EXPORT_C_DECL void WPCTP qRegisterSpi(CThostFtdcMdApi *api, CThostFtdcMdSpi *pSpi){ api->RegisterSpi(pSpi); return; }

// 订阅行情。
DLL_EXPORT_C_DECL int WPCTP qSubscribeMarketData(CThostFtdcMdApi *api, char *ppInstrumentID[], int nCount){ return api->SubscribeMarketData(ppInstrumentID, nCount); }

// 退订行情。
DLL_EXPORT_C_DECL int WPCTP qUnSubscribeMarketData(CThostFtdcMdApi *api, char *ppInstrumentID[], int nCount){ return api->UnSubscribeMarketData(ppInstrumentID, nCount); }

// 订阅询价。
DLL_EXPORT_C_DECL int WPCTP qSubscribeForQuoteRsp(CThostFtdcMdApi *api, char *ppInstrumentID[], int nCount){ return api->SubscribeForQuoteRsp(ppInstrumentID, nCount); }

// 退订询价。
DLL_EXPORT_C_DECL int WPCTP qUnSubscribeForQuoteRsp(CThostFtdcMdApi *api, char *ppInstrumentID[], int nCount){ return api->UnSubscribeForQuoteRsp(ppInstrumentID, nCount); }

// 用户登录请求
DLL_EXPORT_C_DECL int WPCTP qReqUserLogin(CThostFtdcMdApi *api, CThostFtdcReqUserLoginField *pReqUserLoginField, int nRequestID){ return api->ReqUserLogin(pReqUserLoginField, nRequestID); }

// 登出请求
DLL_EXPORT_C_DECL int WPCTP qReqUserLogout(CThostFtdcMdApi *api, CThostFtdcUserLogoutField *pUserLogout, int nRequestID){ return api->ReqUserLogout(pUserLogout, nRequestID); }

// 请求查询组播合约
DLL_EXPORT_C_DECL int WPCTP qReqQryMulticastInstrument(CThostFtdcMdApi *api, CThostFtdcQryMulticastInstrumentField *pQryMulticastInstrument, int nRequestID){ return api->ReqQryMulticastInstrument(pQryMulticastInstrument, nRequestID); }

