#pragma once
#ifdef _WIN32  //64位系统没有预定义 WIN32
#ifdef __cplusplus
#define DLL_EXPORT_C_DECL extern "C" __declspec(dllexport)
#else
#define DLL_EXPORT_C_DECL __declspec(dllexport)
#endif
#else
#ifdef __cplusplus
#define DLL_EXPORT_C_DECL extern "C"
#else
#define DLL_EXPORT_C_DECL extern
#endif
#endif

#ifdef _WIN32
#define WIN32_LEAN_AND_MEAN             //  从 Windows 头文件中排除极少使用的信息
#include "stddef.h"
#ifdef WIN32
#define WPCTP      __cdecl
#include "../../../ctpapi/windows/ThostFtdcMdApi.h"
#else
#define WPCTP      __stdcall
#include "../../../ctpapi/windows/ThostFtdcMdApi.h"
#endif
#elif __APPLE__
#define WPCTP
#include "../../../ctpapi/macos/ThostFtdcMdApi.h"
#elif __linux__
#define WPCTP
#include "../../../ctpapi/linux/ThostFtdcMdApi.h"
#endif

#include <string.h>

class Quote : public CThostFtdcMdSpi
{
public:
    Quote();
	
    
	// 当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。
	typedef int (WPCTP *FP_OnFrontConnected)();
	void *OnFrontConnected_;
	virtual void OnFrontConnected(){ if(OnFrontConnected_) ((FP_OnFrontConnected)OnFrontConnected_)(); }
    
	// 当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。
	typedef int (WPCTP *FP_OnFrontDisconnected)(int nReason);
	void *OnFrontDisconnected_;
	virtual void OnFrontDisconnected(int nReason){ if(OnFrontDisconnected_) ((FP_OnFrontDisconnected)OnFrontDisconnected_)(nReason); }
    
	// 心跳超时警告。当长时间未收到报文时，该方法被调用。
	typedef int (WPCTP *FP_OnHeartBeatWarning)(int nTimeLapse);
	void *OnHeartBeatWarning_;
	virtual void OnHeartBeatWarning(int nTimeLapse){ if(OnHeartBeatWarning_) ((FP_OnHeartBeatWarning)OnHeartBeatWarning_)(nTimeLapse); }
    
	// 登录请求响应
	typedef int (WPCTP *FP_OnRspUserLogin)(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspUserLogin_;
	virtual void OnRspUserLogin(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspUserLogin_) ((FP_OnRspUserLogin)OnRspUserLogin_)(pRspUserLogin, pRspInfo, nRequestID, bIsLast); }
    
	// 登出请求响应
	typedef int (WPCTP *FP_OnRspUserLogout)(CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspUserLogout_;
	virtual void OnRspUserLogout(CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspUserLogout_) ((FP_OnRspUserLogout)OnRspUserLogout_)(pUserLogout, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询组播合约响应
	typedef int (WPCTP *FP_OnRspQryMulticastInstrument)(CThostFtdcMulticastInstrumentField *pMulticastInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryMulticastInstrument_;
	virtual void OnRspQryMulticastInstrument(CThostFtdcMulticastInstrumentField *pMulticastInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryMulticastInstrument_) ((FP_OnRspQryMulticastInstrument)OnRspQryMulticastInstrument_)(pMulticastInstrument, pRspInfo, nRequestID, bIsLast); }
    
	// 错误应答
	typedef int (WPCTP *FP_OnRspError)(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspError_;
	virtual void OnRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspError_) ((FP_OnRspError)OnRspError_)(pRspInfo, nRequestID, bIsLast); }
    
	// 订阅行情应答
	typedef int (WPCTP *FP_OnRspSubMarketData)(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspSubMarketData_;
	virtual void OnRspSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspSubMarketData_) ((FP_OnRspSubMarketData)OnRspSubMarketData_)(pSpecificInstrument, pRspInfo, nRequestID, bIsLast); }
    
	// 取消订阅行情应答
	typedef int (WPCTP *FP_OnRspUnSubMarketData)(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspUnSubMarketData_;
	virtual void OnRspUnSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspUnSubMarketData_) ((FP_OnRspUnSubMarketData)OnRspUnSubMarketData_)(pSpecificInstrument, pRspInfo, nRequestID, bIsLast); }
    
	// 订阅询价应答
	typedef int (WPCTP *FP_OnRspSubForQuoteRsp)(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspSubForQuoteRsp_;
	virtual void OnRspSubForQuoteRsp(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspSubForQuoteRsp_) ((FP_OnRspSubForQuoteRsp)OnRspSubForQuoteRsp_)(pSpecificInstrument, pRspInfo, nRequestID, bIsLast); }
    
	// 取消订阅询价应答
	typedef int (WPCTP *FP_OnRspUnSubForQuoteRsp)(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspUnSubForQuoteRsp_;
	virtual void OnRspUnSubForQuoteRsp(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspUnSubForQuoteRsp_) ((FP_OnRspUnSubForQuoteRsp)OnRspUnSubForQuoteRsp_)(pSpecificInstrument, pRspInfo, nRequestID, bIsLast); }
    
	// 深度行情通知
	typedef int (WPCTP *FP_OnRtnDepthMarketData)(CThostFtdcDepthMarketDataField *pDepthMarketData);
	void *OnRtnDepthMarketData_;
	virtual void OnRtnDepthMarketData(CThostFtdcDepthMarketDataField *pDepthMarketData){ if(OnRtnDepthMarketData_) ((FP_OnRtnDepthMarketData)OnRtnDepthMarketData_)(pDepthMarketData); }
    
	// 询价通知
	typedef int (WPCTP *FP_OnRtnForQuoteRsp)(CThostFtdcForQuoteRspField *pForQuoteRsp);
	void *OnRtnForQuoteRsp_;
	virtual void OnRtnForQuoteRsp(CThostFtdcForQuoteRspField *pForQuoteRsp){ if(OnRtnForQuoteRsp_) ((FP_OnRtnForQuoteRsp)OnRtnForQuoteRsp_)(pForQuoteRsp); }
    
};


DLL_EXPORT_C_DECL void* WPCTP qCreateApi(const char *pszFlowPath, const bool bIsUsingUdp, const bool bIsMulticast);
DLL_EXPORT_C_DECL void* WPCTP qCreateSpi();
DLL_EXPORT_C_DECL void* WPCTP qGetApiVersion();
DLL_EXPORT_C_DECL void* WPCTP qGetTradingDay(CThostFtdcMdApi *api);

// 当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。
DLL_EXPORT_C_DECL void WPCTP qOnFrontConnected(Quote* spi, void* func);

// 当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。
DLL_EXPORT_C_DECL void WPCTP qOnFrontDisconnected(Quote* spi, void* func);

// 心跳超时警告。当长时间未收到报文时，该方法被调用。
DLL_EXPORT_C_DECL void WPCTP qOnHeartBeatWarning(Quote* spi, void* func);

// 登录请求响应
DLL_EXPORT_C_DECL void WPCTP qOnRspUserLogin(Quote* spi, void* func);

// 登出请求响应
DLL_EXPORT_C_DECL void WPCTP qOnRspUserLogout(Quote* spi, void* func);

// 请求查询组播合约响应
DLL_EXPORT_C_DECL void WPCTP qOnRspQryMulticastInstrument(Quote* spi, void* func);

// 错误应答
DLL_EXPORT_C_DECL void WPCTP qOnRspError(Quote* spi, void* func);

// 订阅行情应答
DLL_EXPORT_C_DECL void WPCTP qOnRspSubMarketData(Quote* spi, void* func);

// 取消订阅行情应答
DLL_EXPORT_C_DECL void WPCTP qOnRspUnSubMarketData(Quote* spi, void* func);

// 订阅询价应答
DLL_EXPORT_C_DECL void WPCTP qOnRspSubForQuoteRsp(Quote* spi, void* func);

// 取消订阅询价应答
DLL_EXPORT_C_DECL void WPCTP qOnRspUnSubForQuoteRsp(Quote* spi, void* func);

// 深度行情通知
DLL_EXPORT_C_DECL void WPCTP qOnRtnDepthMarketData(Quote* spi, void* func);

// 询价通知
DLL_EXPORT_C_DECL void WPCTP qOnRtnForQuoteRsp(Quote* spi, void* func);


// 创建MdApi
DLL_EXPORT_C_DECL void WPCTP qRelease(CThostFtdcMdApi *api);

// 初始化
DLL_EXPORT_C_DECL void WPCTP qInit(CThostFtdcMdApi *api);

// 等待接口线程结束运行
DLL_EXPORT_C_DECL int WPCTP qJoin(CThostFtdcMdApi *api);

// 注册前置机网络地址
DLL_EXPORT_C_DECL void WPCTP qRegisterFront(CThostFtdcMdApi *api, char *pszFrontAddress);

// @remark RegisterNameServer优先于RegisterFront
DLL_EXPORT_C_DECL void WPCTP qRegisterNameServer(CThostFtdcMdApi *api, char *pszNsAddress);

// 注册名字服务器用户信息
DLL_EXPORT_C_DECL void WPCTP qRegisterFensUserInfo(CThostFtdcMdApi *api, CThostFtdcFensUserInfoField * pFensUserInfo);

// 注册回调接口
DLL_EXPORT_C_DECL void WPCTP qRegisterSpi(CThostFtdcMdApi *api, CThostFtdcMdSpi *pSpi);

// 订阅行情。
DLL_EXPORT_C_DECL int WPCTP qSubscribeMarketData(CThostFtdcMdApi *api, char *ppInstrumentID[], int nCount);

// 退订行情。
DLL_EXPORT_C_DECL int WPCTP qUnSubscribeMarketData(CThostFtdcMdApi *api, char *ppInstrumentID[], int nCount);

// 订阅询价。
DLL_EXPORT_C_DECL int WPCTP qSubscribeForQuoteRsp(CThostFtdcMdApi *api, char *ppInstrumentID[], int nCount);

// 退订询价。
DLL_EXPORT_C_DECL int WPCTP qUnSubscribeForQuoteRsp(CThostFtdcMdApi *api, char *ppInstrumentID[], int nCount);

// 用户登录请求
DLL_EXPORT_C_DECL int WPCTP qReqUserLogin(CThostFtdcMdApi *api, CThostFtdcReqUserLoginField *pReqUserLoginField, int nRequestID);

// 登出请求
DLL_EXPORT_C_DECL int WPCTP qReqUserLogout(CThostFtdcMdApi *api, CThostFtdcUserLogoutField *pUserLogout, int nRequestID);

// 请求查询组播合约
DLL_EXPORT_C_DECL int WPCTP qReqQryMulticastInstrument(CThostFtdcMdApi *api, CThostFtdcQryMulticastInstrumentField *pQryMulticastInstrument, int nRequestID);

