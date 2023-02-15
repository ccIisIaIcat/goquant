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

#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#ifdef _WIN32
#define WIN32_LEAN_AND_MEAN             //  从 Windows 头文件中排除极少使用的信息
#include "stddef.h"
#ifdef WIN32
#define WPCTP      __cdecl
#include "../../csource/ctpapi/windows/ThostFtdcUserApiDataType.h"
#include "../../csource/ctpapi/windows/ThostFtdcUserApiStruct.h"
#else
#define WPCTP      __stdcall
#include "../../csource/ctpapi/windows/ThostFtdcUserApiDataType.h"
#include "../../csource/ctpapi/windows/ThostFtdcUserApiStruct.h"
#endif
#elif __APPLE__
#define WPCTP
#include "../../csource/ctpapi/macos/ThostFtdcUserApiDataType.h"
#include "../../csource/ctpapi/macos/ThostFtdcUserApiStruct.h"
#elif __linux__
#define WPCTP
#include "../../csource/ctpapi/linux/ThostFtdcUserApiDataType.h"
#include "../../csource/ctpapi/linux/ThostFtdcUserApiStruct.h"
#endif

#define bool _Bool

DLL_EXPORT_C_DECL void* WPCTP qCreateApi(const char *pszFlowPath, const bool bIsUsingUdp, const bool bIsMulticast);
DLL_EXPORT_C_DECL void* WPCTP qCreateSpi();
DLL_EXPORT_C_DECL void* WPCTP qGetApiVersion();
DLL_EXPORT_C_DECL void* WPCTP qGetTradingDay(void *api);

// 当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。
DLL_EXPORT_C_DECL void WPCTP qOnFrontConnected(void* spi, void* func);
DLL_EXPORT_C_DECL int qOnFrontConnected_();

// 当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。
DLL_EXPORT_C_DECL void WPCTP qOnFrontDisconnected(void* spi, void* func);
DLL_EXPORT_C_DECL int qOnFrontDisconnected_(int nReason);

// 心跳超时警告。当长时间未收到报文时，该方法被调用。
DLL_EXPORT_C_DECL void WPCTP qOnHeartBeatWarning(void* spi, void* func);
DLL_EXPORT_C_DECL int qOnHeartBeatWarning_(int nTimeLapse);

// 登录请求响应
DLL_EXPORT_C_DECL void WPCTP qOnRspUserLogin(void* spi, void* func);
DLL_EXPORT_C_DECL int qOnRspUserLogin_(struct CThostFtdcRspUserLoginField *pRspUserLogin, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 登出请求响应
DLL_EXPORT_C_DECL void WPCTP qOnRspUserLogout(void* spi, void* func);
DLL_EXPORT_C_DECL int qOnRspUserLogout_(struct CThostFtdcUserLogoutField *pUserLogout, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询组播合约响应
DLL_EXPORT_C_DECL void WPCTP qOnRspQryMulticastInstrument(void* spi, void* func);
DLL_EXPORT_C_DECL int qOnRspQryMulticastInstrument_(struct CThostFtdcMulticastInstrumentField *pMulticastInstrument, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 错误应答
DLL_EXPORT_C_DECL void WPCTP qOnRspError(void* spi, void* func);
DLL_EXPORT_C_DECL int qOnRspError_(struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 订阅行情应答
DLL_EXPORT_C_DECL void WPCTP qOnRspSubMarketData(void* spi, void* func);
DLL_EXPORT_C_DECL int qOnRspSubMarketData_(struct CThostFtdcSpecificInstrumentField *pSpecificInstrument, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 取消订阅行情应答
DLL_EXPORT_C_DECL void WPCTP qOnRspUnSubMarketData(void* spi, void* func);
DLL_EXPORT_C_DECL int qOnRspUnSubMarketData_(struct CThostFtdcSpecificInstrumentField *pSpecificInstrument, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 订阅询价应答
DLL_EXPORT_C_DECL void WPCTP qOnRspSubForQuoteRsp(void* spi, void* func);
DLL_EXPORT_C_DECL int qOnRspSubForQuoteRsp_(struct CThostFtdcSpecificInstrumentField *pSpecificInstrument, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 取消订阅询价应答
DLL_EXPORT_C_DECL void WPCTP qOnRspUnSubForQuoteRsp(void* spi, void* func);
DLL_EXPORT_C_DECL int qOnRspUnSubForQuoteRsp_(struct CThostFtdcSpecificInstrumentField *pSpecificInstrument, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 深度行情通知
DLL_EXPORT_C_DECL void WPCTP qOnRtnDepthMarketData(void* spi, void* func);
DLL_EXPORT_C_DECL int qOnRtnDepthMarketData_(struct CThostFtdcDepthMarketDataField *pDepthMarketData);

// 询价通知
DLL_EXPORT_C_DECL void WPCTP qOnRtnForQuoteRsp(void* spi, void* func);
DLL_EXPORT_C_DECL int qOnRtnForQuoteRsp_(struct CThostFtdcForQuoteRspField *pForQuoteRsp);


// 创建MdApi
DLL_EXPORT_C_DECL void WPCTP qRelease(void *api);

// 初始化
DLL_EXPORT_C_DECL void WPCTP qInit(void *api);

// 等待接口线程结束运行
DLL_EXPORT_C_DECL int WPCTP qJoin(void *api);

// 注册前置机网络地址
DLL_EXPORT_C_DECL void WPCTP qRegisterFront(void *api, char *pszFrontAddress);

// @remark RegisterNameServer优先于RegisterFront
DLL_EXPORT_C_DECL void WPCTP qRegisterNameServer(void *api, char *pszNsAddress);

// 注册名字服务器用户信息
DLL_EXPORT_C_DECL void WPCTP qRegisterFensUserInfo(void *api, struct CThostFtdcFensUserInfoField * pFensUserInfo);

// 注册回调接口
DLL_EXPORT_C_DECL void WPCTP qRegisterSpi(void *api, void *pSpi);

// 订阅行情。
DLL_EXPORT_C_DECL int WPCTP qSubscribeMarketData(void *api, char *ppInstrumentID[], int nCount);

// 退订行情。
DLL_EXPORT_C_DECL int WPCTP qUnSubscribeMarketData(void *api, char *ppInstrumentID[], int nCount);

// 订阅询价。
DLL_EXPORT_C_DECL int WPCTP qSubscribeForQuoteRsp(void *api, char *ppInstrumentID[], int nCount);

// 退订询价。
DLL_EXPORT_C_DECL int WPCTP qUnSubscribeForQuoteRsp(void *api, char *ppInstrumentID[], int nCount);

// 用户登录请求
DLL_EXPORT_C_DECL int WPCTP qReqUserLogin(void *api, struct CThostFtdcReqUserLoginField *pReqUserLoginField, int nRequestID);

// 登出请求
DLL_EXPORT_C_DECL int WPCTP qReqUserLogout(void *api, struct CThostFtdcUserLogoutField *pUserLogout, int nRequestID);

// 请求查询组播合约
DLL_EXPORT_C_DECL int WPCTP qReqQryMulticastInstrument(void *api, struct CThostFtdcQryMulticastInstrumentField *pQryMulticastInstrument, int nRequestID);

