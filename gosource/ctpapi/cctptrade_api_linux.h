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

DLL_EXPORT_C_DECL int WPCTP dCTP_GetSystemInfo(char* pSystemInfo, int nLen);

DLL_EXPORT_C_DECL void* WPCTP dCTP_GetDataCollectApiVersion();
DLL_EXPORT_C_DECL void* WPCTP tCreateApi(const char *pszFlowPath);
DLL_EXPORT_C_DECL void* WPCTP tCreateSpi();
DLL_EXPORT_C_DECL void* WPCTP tGetApiVersion();
DLL_EXPORT_C_DECL void* WPCTP tGetTradingDay(void *api);

// 当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。
DLL_EXPORT_C_DECL void WPCTP tOnFrontConnected(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnFrontConnected_();

// 当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。
DLL_EXPORT_C_DECL void WPCTP tOnFrontDisconnected(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnFrontDisconnected_(int nReason);

// 心跳超时警告。当长时间未收到报文时，该方法被调用。
DLL_EXPORT_C_DECL void WPCTP tOnHeartBeatWarning(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnHeartBeatWarning_(int nTimeLapse);

// 客户端认证响应
DLL_EXPORT_C_DECL void WPCTP tOnRspAuthenticate(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspAuthenticate_(struct CThostFtdcRspAuthenticateField *pRspAuthenticateField, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 登录请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspUserLogin(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspUserLogin_(struct CThostFtdcRspUserLoginField *pRspUserLogin, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 登出请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspUserLogout(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspUserLogout_(struct CThostFtdcUserLogoutField *pUserLogout, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 用户口令更新请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspUserPasswordUpdate(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspUserPasswordUpdate_(struct CThostFtdcUserPasswordUpdateField *pUserPasswordUpdate, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 资金账户口令更新请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspTradingAccountPasswordUpdate(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspTradingAccountPasswordUpdate_(struct CThostFtdcTradingAccountPasswordUpdateField *pTradingAccountPasswordUpdate, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 查询用户当前支持的认证模式的回复
DLL_EXPORT_C_DECL void WPCTP tOnRspUserAuthMethod(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspUserAuthMethod_(struct CThostFtdcRspUserAuthMethodField *pRspUserAuthMethod, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 获取图形验证码请求的回复
DLL_EXPORT_C_DECL void WPCTP tOnRspGenUserCaptcha(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspGenUserCaptcha_(struct CThostFtdcRspGenUserCaptchaField *pRspGenUserCaptcha, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 获取短信验证码请求的回复
DLL_EXPORT_C_DECL void WPCTP tOnRspGenUserText(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspGenUserText_(struct CThostFtdcRspGenUserTextField *pRspGenUserText, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 报单录入请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspOrderInsert(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspOrderInsert_(struct CThostFtdcInputOrderField *pInputOrder, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 预埋单录入请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspParkedOrderInsert(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspParkedOrderInsert_(struct CThostFtdcParkedOrderField *pParkedOrder, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 预埋撤单录入请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspParkedOrderAction(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspParkedOrderAction_(struct CThostFtdcParkedOrderActionField *pParkedOrderAction, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 报单操作请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspOrderAction(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspOrderAction_(struct CThostFtdcInputOrderActionField *pInputOrderAction, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 查询最大报单数量响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryMaxOrderVolume(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryMaxOrderVolume_(struct CThostFtdcQryMaxOrderVolumeField *pQryMaxOrderVolume, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 投资者结算结果确认响应
DLL_EXPORT_C_DECL void WPCTP tOnRspSettlementInfoConfirm(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspSettlementInfoConfirm_(struct CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 删除预埋单响应
DLL_EXPORT_C_DECL void WPCTP tOnRspRemoveParkedOrder(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspRemoveParkedOrder_(struct CThostFtdcRemoveParkedOrderField *pRemoveParkedOrder, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 删除预埋撤单响应
DLL_EXPORT_C_DECL void WPCTP tOnRspRemoveParkedOrderAction(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspRemoveParkedOrderAction_(struct CThostFtdcRemoveParkedOrderActionField *pRemoveParkedOrderAction, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 执行宣告录入请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspExecOrderInsert(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspExecOrderInsert_(struct CThostFtdcInputExecOrderField *pInputExecOrder, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 执行宣告操作请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspExecOrderAction(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspExecOrderAction_(struct CThostFtdcInputExecOrderActionField *pInputExecOrderAction, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 询价录入请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspForQuoteInsert(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspForQuoteInsert_(struct CThostFtdcInputForQuoteField *pInputForQuote, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 报价录入请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQuoteInsert(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQuoteInsert_(struct CThostFtdcInputQuoteField *pInputQuote, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 报价操作请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQuoteAction(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQuoteAction_(struct CThostFtdcInputQuoteActionField *pInputQuoteAction, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 批量报单操作请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspBatchOrderAction(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspBatchOrderAction_(struct CThostFtdcInputBatchOrderActionField *pInputBatchOrderAction, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 期权自对冲录入请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspOptionSelfCloseInsert(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspOptionSelfCloseInsert_(struct CThostFtdcInputOptionSelfCloseField *pInputOptionSelfClose, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 期权自对冲操作请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspOptionSelfCloseAction(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspOptionSelfCloseAction_(struct CThostFtdcInputOptionSelfCloseActionField *pInputOptionSelfCloseAction, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 申请组合录入请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspCombActionInsert(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspCombActionInsert_(struct CThostFtdcInputCombActionField *pInputCombAction, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询报单响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryOrder(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryOrder_(struct CThostFtdcOrderField *pOrder, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询成交响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryTrade(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryTrade_(struct CThostFtdcTradeField *pTrade, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询投资者持仓响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryInvestorPosition(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryInvestorPosition_(struct CThostFtdcInvestorPositionField *pInvestorPosition, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询资金账户响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryTradingAccount(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryTradingAccount_(struct CThostFtdcTradingAccountField *pTradingAccount, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询投资者响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryInvestor(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryInvestor_(struct CThostFtdcInvestorField *pInvestor, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询交易编码响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryTradingCode(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryTradingCode_(struct CThostFtdcTradingCodeField *pTradingCode, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询合约保证金率响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryInstrumentMarginRate(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryInstrumentMarginRate_(struct CThostFtdcInstrumentMarginRateField *pInstrumentMarginRate, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询合约手续费率响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryInstrumentCommissionRate(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryInstrumentCommissionRate_(struct CThostFtdcInstrumentCommissionRateField *pInstrumentCommissionRate, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询交易所响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryExchange(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryExchange_(struct CThostFtdcExchangeField *pExchange, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询产品响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryProduct(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryProduct_(struct CThostFtdcProductField *pProduct, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询合约响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryInstrument(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryInstrument_(struct CThostFtdcInstrumentField *pInstrument, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询行情响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryDepthMarketData(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryDepthMarketData_(struct CThostFtdcDepthMarketDataField *pDepthMarketData, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询交易员报盘机响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryTraderOffer(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryTraderOffer_(struct CThostFtdcTraderOfferField *pTraderOffer, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询投资者结算结果响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQrySettlementInfo(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQrySettlementInfo_(struct CThostFtdcSettlementInfoField *pSettlementInfo, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询转帐银行响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryTransferBank(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryTransferBank_(struct CThostFtdcTransferBankField *pTransferBank, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询投资者持仓明细响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryInvestorPositionDetail(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryInvestorPositionDetail_(struct CThostFtdcInvestorPositionDetailField *pInvestorPositionDetail, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询客户通知响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryNotice(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryNotice_(struct CThostFtdcNoticeField *pNotice, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询结算信息确认响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQrySettlementInfoConfirm(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQrySettlementInfoConfirm_(struct CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询投资者持仓明细响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryInvestorPositionCombineDetail(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryInvestorPositionCombineDetail_(struct CThostFtdcInvestorPositionCombineDetailField *pInvestorPositionCombineDetail, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 查询保证金监管系统经纪公司资金账户密钥响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryCFMMCTradingAccountKey(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryCFMMCTradingAccountKey_(struct CThostFtdcCFMMCTradingAccountKeyField *pCFMMCTradingAccountKey, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询仓单折抵信息响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryEWarrantOffset(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryEWarrantOffset_(struct CThostFtdcEWarrantOffsetField *pEWarrantOffset, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询投资者品种/跨品种保证金响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryInvestorProductGroupMargin(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryInvestorProductGroupMargin_(struct CThostFtdcInvestorProductGroupMarginField *pInvestorProductGroupMargin, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询交易所保证金率响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryExchangeMarginRate(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryExchangeMarginRate_(struct CThostFtdcExchangeMarginRateField *pExchangeMarginRate, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询交易所调整保证金率响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryExchangeMarginRateAdjust(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryExchangeMarginRateAdjust_(struct CThostFtdcExchangeMarginRateAdjustField *pExchangeMarginRateAdjust, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询汇率响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryExchangeRate(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryExchangeRate_(struct CThostFtdcExchangeRateField *pExchangeRate, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询二级代理操作员银期权限响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQrySecAgentACIDMap(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQrySecAgentACIDMap_(struct CThostFtdcSecAgentACIDMapField *pSecAgentACIDMap, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询产品报价汇率
DLL_EXPORT_C_DECL void WPCTP tOnRspQryProductExchRate(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryProductExchRate_(struct CThostFtdcProductExchRateField *pProductExchRate, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询产品组
DLL_EXPORT_C_DECL void WPCTP tOnRspQryProductGroup(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryProductGroup_(struct CThostFtdcProductGroupField *pProductGroup, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询做市商合约手续费率响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryMMInstrumentCommissionRate(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryMMInstrumentCommissionRate_(struct CThostFtdcMMInstrumentCommissionRateField *pMMInstrumentCommissionRate, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询做市商期权合约手续费响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryMMOptionInstrCommRate(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryMMOptionInstrCommRate_(struct CThostFtdcMMOptionInstrCommRateField *pMMOptionInstrCommRate, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询报单手续费响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryInstrumentOrderCommRate(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryInstrumentOrderCommRate_(struct CThostFtdcInstrumentOrderCommRateField *pInstrumentOrderCommRate, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询资金账户响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQrySecAgentTradingAccount(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQrySecAgentTradingAccount_(struct CThostFtdcTradingAccountField *pTradingAccount, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询二级代理商资金校验模式响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQrySecAgentCheckMode(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQrySecAgentCheckMode_(struct CThostFtdcSecAgentCheckModeField *pSecAgentCheckMode, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询二级代理商信息响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQrySecAgentTradeInfo(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQrySecAgentTradeInfo_(struct CThostFtdcSecAgentTradeInfoField *pSecAgentTradeInfo, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询期权交易成本响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryOptionInstrTradeCost(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryOptionInstrTradeCost_(struct CThostFtdcOptionInstrTradeCostField *pOptionInstrTradeCost, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询期权合约手续费响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryOptionInstrCommRate(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryOptionInstrCommRate_(struct CThostFtdcOptionInstrCommRateField *pOptionInstrCommRate, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询执行宣告响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryExecOrder(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryExecOrder_(struct CThostFtdcExecOrderField *pExecOrder, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询询价响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryForQuote(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryForQuote_(struct CThostFtdcForQuoteField *pForQuote, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询报价响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryQuote(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryQuote_(struct CThostFtdcQuoteField *pQuote, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询期权自对冲响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryOptionSelfClose(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryOptionSelfClose_(struct CThostFtdcOptionSelfCloseField *pOptionSelfClose, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询投资单元响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryInvestUnit(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryInvestUnit_(struct CThostFtdcInvestUnitField *pInvestUnit, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询组合合约安全系数响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryCombInstrumentGuard(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryCombInstrumentGuard_(struct CThostFtdcCombInstrumentGuardField *pCombInstrumentGuard, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询申请组合响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryCombAction(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryCombAction_(struct CThostFtdcCombActionField *pCombAction, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询转帐流水响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryTransferSerial(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryTransferSerial_(struct CThostFtdcTransferSerialField *pTransferSerial, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询银期签约关系响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryAccountregister(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryAccountregister_(struct CThostFtdcAccountregisterField *pAccountregister, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 错误应答
DLL_EXPORT_C_DECL void WPCTP tOnRspError(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspError_(struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 报单通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnOrder(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRtnOrder_(struct CThostFtdcOrderField *pOrder);

// 成交通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnTrade(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRtnTrade_(struct CThostFtdcTradeField *pTrade);

// 报单录入错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnOrderInsert(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnErrRtnOrderInsert_(struct CThostFtdcInputOrderField *pInputOrder, struct CThostFtdcRspInfoField *pRspInfo);

// 报单操作错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnOrderAction(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnErrRtnOrderAction_(struct CThostFtdcOrderActionField *pOrderAction, struct CThostFtdcRspInfoField *pRspInfo);

// 合约交易状态通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnInstrumentStatus(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRtnInstrumentStatus_(struct CThostFtdcInstrumentStatusField *pInstrumentStatus);

// 交易所公告通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnBulletin(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRtnBulletin_(struct CThostFtdcBulletinField *pBulletin);

// 交易通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnTradingNotice(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRtnTradingNotice_(struct CThostFtdcTradingNoticeInfoField *pTradingNoticeInfo);

// 提示条件单校验错误
DLL_EXPORT_C_DECL void WPCTP tOnRtnErrorConditionalOrder(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRtnErrorConditionalOrder_(struct CThostFtdcErrorConditionalOrderField *pErrorConditionalOrder);

// 执行宣告通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnExecOrder(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRtnExecOrder_(struct CThostFtdcExecOrderField *pExecOrder);

// 执行宣告录入错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnExecOrderInsert(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnErrRtnExecOrderInsert_(struct CThostFtdcInputExecOrderField *pInputExecOrder, struct CThostFtdcRspInfoField *pRspInfo);

// 执行宣告操作错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnExecOrderAction(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnErrRtnExecOrderAction_(struct CThostFtdcExecOrderActionField *pExecOrderAction, struct CThostFtdcRspInfoField *pRspInfo);

// 询价录入错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnForQuoteInsert(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnErrRtnForQuoteInsert_(struct CThostFtdcInputForQuoteField *pInputForQuote, struct CThostFtdcRspInfoField *pRspInfo);

// 报价通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnQuote(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRtnQuote_(struct CThostFtdcQuoteField *pQuote);

// 报价录入错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnQuoteInsert(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnErrRtnQuoteInsert_(struct CThostFtdcInputQuoteField *pInputQuote, struct CThostFtdcRspInfoField *pRspInfo);

// 报价操作错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnQuoteAction(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnErrRtnQuoteAction_(struct CThostFtdcQuoteActionField *pQuoteAction, struct CThostFtdcRspInfoField *pRspInfo);

// 询价通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnForQuoteRsp(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRtnForQuoteRsp_(struct CThostFtdcForQuoteRspField *pForQuoteRsp);

// 保证金监控中心用户令牌
DLL_EXPORT_C_DECL void WPCTP tOnRtnCFMMCTradingAccountToken(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRtnCFMMCTradingAccountToken_(struct CThostFtdcCFMMCTradingAccountTokenField *pCFMMCTradingAccountToken);

// 批量报单操作错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnBatchOrderAction(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnErrRtnBatchOrderAction_(struct CThostFtdcBatchOrderActionField *pBatchOrderAction, struct CThostFtdcRspInfoField *pRspInfo);

// 期权自对冲通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnOptionSelfClose(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRtnOptionSelfClose_(struct CThostFtdcOptionSelfCloseField *pOptionSelfClose);

// 期权自对冲录入错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnOptionSelfCloseInsert(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnErrRtnOptionSelfCloseInsert_(struct CThostFtdcInputOptionSelfCloseField *pInputOptionSelfClose, struct CThostFtdcRspInfoField *pRspInfo);

// 期权自对冲操作错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnOptionSelfCloseAction(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnErrRtnOptionSelfCloseAction_(struct CThostFtdcOptionSelfCloseActionField *pOptionSelfCloseAction, struct CThostFtdcRspInfoField *pRspInfo);

// 申请组合通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnCombAction(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRtnCombAction_(struct CThostFtdcCombActionField *pCombAction);

// 申请组合录入错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnCombActionInsert(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnErrRtnCombActionInsert_(struct CThostFtdcInputCombActionField *pInputCombAction, struct CThostFtdcRspInfoField *pRspInfo);

// 请求查询签约银行响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryContractBank(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryContractBank_(struct CThostFtdcContractBankField *pContractBank, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询预埋单响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryParkedOrder(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryParkedOrder_(struct CThostFtdcParkedOrderField *pParkedOrder, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询预埋撤单响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryParkedOrderAction(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryParkedOrderAction_(struct CThostFtdcParkedOrderActionField *pParkedOrderAction, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询交易通知响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryTradingNotice(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryTradingNotice_(struct CThostFtdcTradingNoticeField *pTradingNotice, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询经纪公司交易参数响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryBrokerTradingParams(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryBrokerTradingParams_(struct CThostFtdcBrokerTradingParamsField *pBrokerTradingParams, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询经纪公司交易算法响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryBrokerTradingAlgos(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryBrokerTradingAlgos_(struct CThostFtdcBrokerTradingAlgosField *pBrokerTradingAlgos, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求查询监控中心用户令牌
DLL_EXPORT_C_DECL void WPCTP tOnRspQueryCFMMCTradingAccountToken(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQueryCFMMCTradingAccountToken_(struct CThostFtdcQueryCFMMCTradingAccountTokenField *pQueryCFMMCTradingAccountToken, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 银行发起银行资金转期货通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnFromBankToFutureByBank(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRtnFromBankToFutureByBank_(struct CThostFtdcRspTransferField *pRspTransfer);

// 银行发起期货资金转银行通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnFromFutureToBankByBank(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRtnFromFutureToBankByBank_(struct CThostFtdcRspTransferField *pRspTransfer);

// 银行发起冲正银行转期货通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnRepealFromBankToFutureByBank(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRtnRepealFromBankToFutureByBank_(struct CThostFtdcRspRepealField *pRspRepeal);

// 银行发起冲正期货转银行通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnRepealFromFutureToBankByBank(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRtnRepealFromFutureToBankByBank_(struct CThostFtdcRspRepealField *pRspRepeal);

// 期货发起银行资金转期货通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnFromBankToFutureByFuture(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRtnFromBankToFutureByFuture_(struct CThostFtdcRspTransferField *pRspTransfer);

// 期货发起期货资金转银行通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnFromFutureToBankByFuture(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRtnFromFutureToBankByFuture_(struct CThostFtdcRspTransferField *pRspTransfer);

// 系统运行时期货端手工发起冲正银行转期货请求，银行处理完毕后报盘发回的通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnRepealFromBankToFutureByFutureManual(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRtnRepealFromBankToFutureByFutureManual_(struct CThostFtdcRspRepealField *pRspRepeal);

// 系统运行时期货端手工发起冲正期货转银行请求，银行处理完毕后报盘发回的通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnRepealFromFutureToBankByFutureManual(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRtnRepealFromFutureToBankByFutureManual_(struct CThostFtdcRspRepealField *pRspRepeal);

// 期货发起查询银行余额通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnQueryBankBalanceByFuture(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRtnQueryBankBalanceByFuture_(struct CThostFtdcNotifyQueryAccountField *pNotifyQueryAccount);

// 期货发起银行资金转期货错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnBankToFutureByFuture(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnErrRtnBankToFutureByFuture_(struct CThostFtdcReqTransferField *pReqTransfer, struct CThostFtdcRspInfoField *pRspInfo);

// 期货发起期货资金转银行错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnFutureToBankByFuture(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnErrRtnFutureToBankByFuture_(struct CThostFtdcReqTransferField *pReqTransfer, struct CThostFtdcRspInfoField *pRspInfo);

// 系统运行时期货端手工发起冲正银行转期货错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnRepealBankToFutureByFutureManual(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnErrRtnRepealBankToFutureByFutureManual_(struct CThostFtdcReqRepealField *pReqRepeal, struct CThostFtdcRspInfoField *pRspInfo);

// 系统运行时期货端手工发起冲正期货转银行错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnRepealFutureToBankByFutureManual(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnErrRtnRepealFutureToBankByFutureManual_(struct CThostFtdcReqRepealField *pReqRepeal, struct CThostFtdcRspInfoField *pRspInfo);

// 期货发起查询银行余额错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnQueryBankBalanceByFuture(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnErrRtnQueryBankBalanceByFuture_(struct CThostFtdcReqQueryAccountField *pReqQueryAccount, struct CThostFtdcRspInfoField *pRspInfo);

// 期货发起冲正银行转期货请求，银行处理完毕后报盘发回的通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnRepealFromBankToFutureByFuture(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRtnRepealFromBankToFutureByFuture_(struct CThostFtdcRspRepealField *pRspRepeal);

// 期货发起冲正期货转银行请求，银行处理完毕后报盘发回的通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnRepealFromFutureToBankByFuture(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRtnRepealFromFutureToBankByFuture_(struct CThostFtdcRspRepealField *pRspRepeal);

// 期货发起银行资金转期货应答
DLL_EXPORT_C_DECL void WPCTP tOnRspFromBankToFutureByFuture(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspFromBankToFutureByFuture_(struct CThostFtdcReqTransferField *pReqTransfer, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 期货发起期货资金转银行应答
DLL_EXPORT_C_DECL void WPCTP tOnRspFromFutureToBankByFuture(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspFromFutureToBankByFuture_(struct CThostFtdcReqTransferField *pReqTransfer, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 期货发起查询银行余额应答
DLL_EXPORT_C_DECL void WPCTP tOnRspQueryBankAccountMoneyByFuture(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQueryBankAccountMoneyByFuture_(struct CThostFtdcReqQueryAccountField *pReqQueryAccount, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 银行发起银期开户通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnOpenAccountByBank(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRtnOpenAccountByBank_(struct CThostFtdcOpenAccountField *pOpenAccount);

// 银行发起银期销户通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnCancelAccountByBank(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRtnCancelAccountByBank_(struct CThostFtdcCancelAccountField *pCancelAccount);

// 银行发起变更银行账号通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnChangeAccountByBank(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRtnChangeAccountByBank_(struct CThostFtdcChangeAccountField *pChangeAccount);

// 请求查询分类合约响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryClassifiedInstrument(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryClassifiedInstrument_(struct CThostFtdcInstrumentField *pInstrument, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 请求组合优惠比例响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryCombPromotionParam(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryCombPromotionParam_(struct CThostFtdcCombPromotionParamField *pCombPromotionParam, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 投资者风险结算持仓查询响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryRiskSettleInvstPosition(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryRiskSettleInvstPosition_(struct CThostFtdcRiskSettleInvstPositionField *pRiskSettleInvstPosition, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 风险结算产品查询响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryRiskSettleProductStatus(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryRiskSettleProductStatus_(struct CThostFtdcRiskSettleProductStatusField *pRiskSettleProductStatus, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// SPBM期货合约参数查询响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQrySPBMFutureParameter(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQrySPBMFutureParameter_(struct CThostFtdcSPBMFutureParameterField *pSPBMFutureParameter, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// SPBM期权合约参数查询响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQrySPBMOptionParameter(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQrySPBMOptionParameter_(struct CThostFtdcSPBMOptionParameterField *pSPBMOptionParameter, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// SPBM品种内对锁仓折扣参数查询响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQrySPBMIntraParameter(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQrySPBMIntraParameter_(struct CThostFtdcSPBMIntraParameterField *pSPBMIntraParameter, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// SPBM跨品种抵扣参数查询响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQrySPBMInterParameter(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQrySPBMInterParameter_(struct CThostFtdcSPBMInterParameterField *pSPBMInterParameter, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// SPBM组合保证金套餐查询响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQrySPBMPortfDefinition(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQrySPBMPortfDefinition_(struct CThostFtdcSPBMPortfDefinitionField *pSPBMPortfDefinition, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 投资者SPBM套餐选择查询响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQrySPBMInvestorPortfDef(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQrySPBMInvestorPortfDef_(struct CThostFtdcSPBMInvestorPortfDefField *pSPBMInvestorPortfDef, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 投资者新型组合保证金系数查询响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryInvestorPortfMarginRatio(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryInvestorPortfMarginRatio_(struct CThostFtdcInvestorPortfMarginRatioField *pInvestorPortfMarginRatio, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);

// 投资者产品SPBM明细查询响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryInvestorProdSPBMDetail(void* spi, void* func);
DLL_EXPORT_C_DECL int tOnRspQryInvestorProdSPBMDetail_(struct CThostFtdcInvestorProdSPBMDetailField *pInvestorProdSPBMDetail, struct CThostFtdcRspInfoField *pRspInfo, int nRequestID, _Bool bIsLast);


// 创建TraderApi
DLL_EXPORT_C_DECL void WPCTP tRelease(void *api);

// 初始化
DLL_EXPORT_C_DECL void WPCTP tInit(void *api);

// 等待接口线程结束运行
DLL_EXPORT_C_DECL int WPCTP tJoin(void *api);

// 注册前置机网络地址
DLL_EXPORT_C_DECL void WPCTP tRegisterFront(void *api, char *pszFrontAddress);

// @remark RegisterNameServer优先于RegisterFront
DLL_EXPORT_C_DECL void WPCTP tRegisterNameServer(void *api, char *pszNsAddress);

// 注册名字服务器用户信息
DLL_EXPORT_C_DECL void WPCTP tRegisterFensUserInfo(void *api, struct CThostFtdcFensUserInfoField * pFensUserInfo);

// 注册回调接口
DLL_EXPORT_C_DECL void WPCTP tRegisterSpi(void *api, void *pSpi);

// 订阅私有流。
DLL_EXPORT_C_DECL void WPCTP tSubscribePrivateTopic(void *api, int nResumeType);

// 订阅公共流。
DLL_EXPORT_C_DECL void WPCTP tSubscribePublicTopic(void *api, int nResumeType);

// 客户端认证请求
DLL_EXPORT_C_DECL int WPCTP tReqAuthenticate(void *api, struct CThostFtdcReqAuthenticateField *pReqAuthenticateField, int nRequestID);

// 注册用户终端信息，用于中继服务器多连接模式
DLL_EXPORT_C_DECL int WPCTP tRegisterUserSystemInfo(void *api, struct CThostFtdcUserSystemInfoField *pUserSystemInfo);

// 上报用户终端信息，用于中继服务器操作员登录模式
DLL_EXPORT_C_DECL int WPCTP tSubmitUserSystemInfo(void *api, struct CThostFtdcUserSystemInfoField *pUserSystemInfo);

// 用户登录请求
DLL_EXPORT_C_DECL int WPCTP tReqUserLogin(void *api, struct CThostFtdcReqUserLoginField *pReqUserLoginField, int nRequestID);

// 登出请求
DLL_EXPORT_C_DECL int WPCTP tReqUserLogout(void *api, struct CThostFtdcUserLogoutField *pUserLogout, int nRequestID);

// 用户口令更新请求
DLL_EXPORT_C_DECL int WPCTP tReqUserPasswordUpdate(void *api, struct CThostFtdcUserPasswordUpdateField *pUserPasswordUpdate, int nRequestID);

// 资金账户口令更新请求
DLL_EXPORT_C_DECL int WPCTP tReqTradingAccountPasswordUpdate(void *api, struct CThostFtdcTradingAccountPasswordUpdateField *pTradingAccountPasswordUpdate, int nRequestID);

// 查询用户当前支持的认证模式
DLL_EXPORT_C_DECL int WPCTP tReqUserAuthMethod(void *api, struct CThostFtdcReqUserAuthMethodField *pReqUserAuthMethod, int nRequestID);

// 用户发出获取图形验证码请求
DLL_EXPORT_C_DECL int WPCTP tReqGenUserCaptcha(void *api, struct CThostFtdcReqGenUserCaptchaField *pReqGenUserCaptcha, int nRequestID);

// 用户发出获取短信验证码请求
DLL_EXPORT_C_DECL int WPCTP tReqGenUserText(void *api, struct CThostFtdcReqGenUserTextField *pReqGenUserText, int nRequestID);

// 用户发出带有图片验证码的登陆请求
DLL_EXPORT_C_DECL int WPCTP tReqUserLoginWithCaptcha(void *api, struct CThostFtdcReqUserLoginWithCaptchaField *pReqUserLoginWithCaptcha, int nRequestID);

// 用户发出带有短信验证码的登陆请求
DLL_EXPORT_C_DECL int WPCTP tReqUserLoginWithText(void *api, struct CThostFtdcReqUserLoginWithTextField *pReqUserLoginWithText, int nRequestID);

// 用户发出带有动态口令的登陆请求
DLL_EXPORT_C_DECL int WPCTP tReqUserLoginWithOTP(void *api, struct CThostFtdcReqUserLoginWithOTPField *pReqUserLoginWithOTP, int nRequestID);

// 报单录入请求
DLL_EXPORT_C_DECL int WPCTP tReqOrderInsert(void *api, struct CThostFtdcInputOrderField *pInputOrder, int nRequestID);

// 预埋单录入请求
DLL_EXPORT_C_DECL int WPCTP tReqParkedOrderInsert(void *api, struct CThostFtdcParkedOrderField *pParkedOrder, int nRequestID);

// 预埋撤单录入请求
DLL_EXPORT_C_DECL int WPCTP tReqParkedOrderAction(void *api, struct CThostFtdcParkedOrderActionField *pParkedOrderAction, int nRequestID);

// 报单操作请求
DLL_EXPORT_C_DECL int WPCTP tReqOrderAction(void *api, struct CThostFtdcInputOrderActionField *pInputOrderAction, int nRequestID);

// 查询最大报单数量请求
DLL_EXPORT_C_DECL int WPCTP tReqQryMaxOrderVolume(void *api, struct CThostFtdcQryMaxOrderVolumeField *pQryMaxOrderVolume, int nRequestID);

// 投资者结算结果确认
DLL_EXPORT_C_DECL int WPCTP tReqSettlementInfoConfirm(void *api, struct CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, int nRequestID);

// 请求删除预埋单
DLL_EXPORT_C_DECL int WPCTP tReqRemoveParkedOrder(void *api, struct CThostFtdcRemoveParkedOrderField *pRemoveParkedOrder, int nRequestID);

// 请求删除预埋撤单
DLL_EXPORT_C_DECL int WPCTP tReqRemoveParkedOrderAction(void *api, struct CThostFtdcRemoveParkedOrderActionField *pRemoveParkedOrderAction, int nRequestID);

// 执行宣告录入请求
DLL_EXPORT_C_DECL int WPCTP tReqExecOrderInsert(void *api, struct CThostFtdcInputExecOrderField *pInputExecOrder, int nRequestID);

// 执行宣告操作请求
DLL_EXPORT_C_DECL int WPCTP tReqExecOrderAction(void *api, struct CThostFtdcInputExecOrderActionField *pInputExecOrderAction, int nRequestID);

// 询价录入请求
DLL_EXPORT_C_DECL int WPCTP tReqForQuoteInsert(void *api, struct CThostFtdcInputForQuoteField *pInputForQuote, int nRequestID);

// 报价录入请求
DLL_EXPORT_C_DECL int WPCTP tReqQuoteInsert(void *api, struct CThostFtdcInputQuoteField *pInputQuote, int nRequestID);

// 报价操作请求
DLL_EXPORT_C_DECL int WPCTP tReqQuoteAction(void *api, struct CThostFtdcInputQuoteActionField *pInputQuoteAction, int nRequestID);

// 批量报单操作请求
DLL_EXPORT_C_DECL int WPCTP tReqBatchOrderAction(void *api, struct CThostFtdcInputBatchOrderActionField *pInputBatchOrderAction, int nRequestID);

// 期权自对冲录入请求
DLL_EXPORT_C_DECL int WPCTP tReqOptionSelfCloseInsert(void *api, struct CThostFtdcInputOptionSelfCloseField *pInputOptionSelfClose, int nRequestID);

// 期权自对冲操作请求
DLL_EXPORT_C_DECL int WPCTP tReqOptionSelfCloseAction(void *api, struct CThostFtdcInputOptionSelfCloseActionField *pInputOptionSelfCloseAction, int nRequestID);

// 申请组合录入请求
DLL_EXPORT_C_DECL int WPCTP tReqCombActionInsert(void *api, struct CThostFtdcInputCombActionField *pInputCombAction, int nRequestID);

// 请求查询报单
DLL_EXPORT_C_DECL int WPCTP tReqQryOrder(void *api, struct CThostFtdcQryOrderField *pQryOrder, int nRequestID);

// 请求查询成交
DLL_EXPORT_C_DECL int WPCTP tReqQryTrade(void *api, struct CThostFtdcQryTradeField *pQryTrade, int nRequestID);

// 请求查询投资者持仓
DLL_EXPORT_C_DECL int WPCTP tReqQryInvestorPosition(void *api, struct CThostFtdcQryInvestorPositionField *pQryInvestorPosition, int nRequestID);

// 请求查询资金账户
DLL_EXPORT_C_DECL int WPCTP tReqQryTradingAccount(void *api, struct CThostFtdcQryTradingAccountField *pQryTradingAccount, int nRequestID);

// 请求查询投资者
DLL_EXPORT_C_DECL int WPCTP tReqQryInvestor(void *api, struct CThostFtdcQryInvestorField *pQryInvestor, int nRequestID);

// 请求查询交易编码
DLL_EXPORT_C_DECL int WPCTP tReqQryTradingCode(void *api, struct CThostFtdcQryTradingCodeField *pQryTradingCode, int nRequestID);

// 请求查询合约保证金率
DLL_EXPORT_C_DECL int WPCTP tReqQryInstrumentMarginRate(void *api, struct CThostFtdcQryInstrumentMarginRateField *pQryInstrumentMarginRate, int nRequestID);

// 请求查询合约手续费率
DLL_EXPORT_C_DECL int WPCTP tReqQryInstrumentCommissionRate(void *api, struct CThostFtdcQryInstrumentCommissionRateField *pQryInstrumentCommissionRate, int nRequestID);

// 请求查询交易所
DLL_EXPORT_C_DECL int WPCTP tReqQryExchange(void *api, struct CThostFtdcQryExchangeField *pQryExchange, int nRequestID);

// 请求查询产品
DLL_EXPORT_C_DECL int WPCTP tReqQryProduct(void *api, struct CThostFtdcQryProductField *pQryProduct, int nRequestID);

// 请求查询合约
DLL_EXPORT_C_DECL int WPCTP tReqQryInstrument(void *api, struct CThostFtdcQryInstrumentField *pQryInstrument, int nRequestID);

// 请求查询行情
DLL_EXPORT_C_DECL int WPCTP tReqQryDepthMarketData(void *api, struct CThostFtdcQryDepthMarketDataField *pQryDepthMarketData, int nRequestID);

// 请求查询交易员报盘机
DLL_EXPORT_C_DECL int WPCTP tReqQryTraderOffer(void *api, struct CThostFtdcQryTraderOfferField *pQryTraderOffer, int nRequestID);

// 请求查询投资者结算结果
DLL_EXPORT_C_DECL int WPCTP tReqQrySettlementInfo(void *api, struct CThostFtdcQrySettlementInfoField *pQrySettlementInfo, int nRequestID);

// 请求查询转帐银行
DLL_EXPORT_C_DECL int WPCTP tReqQryTransferBank(void *api, struct CThostFtdcQryTransferBankField *pQryTransferBank, int nRequestID);

// 请求查询投资者持仓明细
DLL_EXPORT_C_DECL int WPCTP tReqQryInvestorPositionDetail(void *api, struct CThostFtdcQryInvestorPositionDetailField *pQryInvestorPositionDetail, int nRequestID);

// 请求查询客户通知
DLL_EXPORT_C_DECL int WPCTP tReqQryNotice(void *api, struct CThostFtdcQryNoticeField *pQryNotice, int nRequestID);

// 请求查询结算信息确认
DLL_EXPORT_C_DECL int WPCTP tReqQrySettlementInfoConfirm(void *api, struct CThostFtdcQrySettlementInfoConfirmField *pQrySettlementInfoConfirm, int nRequestID);

// 请求查询投资者持仓明细
DLL_EXPORT_C_DECL int WPCTP tReqQryInvestorPositionCombineDetail(void *api, struct CThostFtdcQryInvestorPositionCombineDetailField *pQryInvestorPositionCombineDetail, int nRequestID);

// 请求查询保证金监管系统经纪公司资金账户密钥
DLL_EXPORT_C_DECL int WPCTP tReqQryCFMMCTradingAccountKey(void *api, struct CThostFtdcQryCFMMCTradingAccountKeyField *pQryCFMMCTradingAccountKey, int nRequestID);

// 请求查询仓单折抵信息
DLL_EXPORT_C_DECL int WPCTP tReqQryEWarrantOffset(void *api, struct CThostFtdcQryEWarrantOffsetField *pQryEWarrantOffset, int nRequestID);

// 请求查询投资者品种/跨品种保证金
DLL_EXPORT_C_DECL int WPCTP tReqQryInvestorProductGroupMargin(void *api, struct CThostFtdcQryInvestorProductGroupMarginField *pQryInvestorProductGroupMargin, int nRequestID);

// 请求查询交易所保证金率
DLL_EXPORT_C_DECL int WPCTP tReqQryExchangeMarginRate(void *api, struct CThostFtdcQryExchangeMarginRateField *pQryExchangeMarginRate, int nRequestID);

// 请求查询交易所调整保证金率
DLL_EXPORT_C_DECL int WPCTP tReqQryExchangeMarginRateAdjust(void *api, struct CThostFtdcQryExchangeMarginRateAdjustField *pQryExchangeMarginRateAdjust, int nRequestID);

// 请求查询汇率
DLL_EXPORT_C_DECL int WPCTP tReqQryExchangeRate(void *api, struct CThostFtdcQryExchangeRateField *pQryExchangeRate, int nRequestID);

// 请求查询二级代理操作员银期权限
DLL_EXPORT_C_DECL int WPCTP tReqQrySecAgentACIDMap(void *api, struct CThostFtdcQrySecAgentACIDMapField *pQrySecAgentACIDMap, int nRequestID);

// 请求查询产品报价汇率
DLL_EXPORT_C_DECL int WPCTP tReqQryProductExchRate(void *api, struct CThostFtdcQryProductExchRateField *pQryProductExchRate, int nRequestID);

// 请求查询产品组
DLL_EXPORT_C_DECL int WPCTP tReqQryProductGroup(void *api, struct CThostFtdcQryProductGroupField *pQryProductGroup, int nRequestID);

// 请求查询做市商合约手续费率
DLL_EXPORT_C_DECL int WPCTP tReqQryMMInstrumentCommissionRate(void *api, struct CThostFtdcQryMMInstrumentCommissionRateField *pQryMMInstrumentCommissionRate, int nRequestID);

// 请求查询做市商期权合约手续费
DLL_EXPORT_C_DECL int WPCTP tReqQryMMOptionInstrCommRate(void *api, struct CThostFtdcQryMMOptionInstrCommRateField *pQryMMOptionInstrCommRate, int nRequestID);

// 请求查询报单手续费
DLL_EXPORT_C_DECL int WPCTP tReqQryInstrumentOrderCommRate(void *api, struct CThostFtdcQryInstrumentOrderCommRateField *pQryInstrumentOrderCommRate, int nRequestID);

// 请求查询资金账户
DLL_EXPORT_C_DECL int WPCTP tReqQrySecAgentTradingAccount(void *api, struct CThostFtdcQryTradingAccountField *pQryTradingAccount, int nRequestID);

// 请求查询二级代理商资金校验模式
DLL_EXPORT_C_DECL int WPCTP tReqQrySecAgentCheckMode(void *api, struct CThostFtdcQrySecAgentCheckModeField *pQrySecAgentCheckMode, int nRequestID);

// 请求查询二级代理商信息
DLL_EXPORT_C_DECL int WPCTP tReqQrySecAgentTradeInfo(void *api, struct CThostFtdcQrySecAgentTradeInfoField *pQrySecAgentTradeInfo, int nRequestID);

// 请求查询期权交易成本
DLL_EXPORT_C_DECL int WPCTP tReqQryOptionInstrTradeCost(void *api, struct CThostFtdcQryOptionInstrTradeCostField *pQryOptionInstrTradeCost, int nRequestID);

// 请求查询期权合约手续费
DLL_EXPORT_C_DECL int WPCTP tReqQryOptionInstrCommRate(void *api, struct CThostFtdcQryOptionInstrCommRateField *pQryOptionInstrCommRate, int nRequestID);

// 请求查询执行宣告
DLL_EXPORT_C_DECL int WPCTP tReqQryExecOrder(void *api, struct CThostFtdcQryExecOrderField *pQryExecOrder, int nRequestID);

// 请求查询询价
DLL_EXPORT_C_DECL int WPCTP tReqQryForQuote(void *api, struct CThostFtdcQryForQuoteField *pQryForQuote, int nRequestID);

// 请求查询报价
DLL_EXPORT_C_DECL int WPCTP tReqQryQuote(void *api, struct CThostFtdcQryQuoteField *pQryQuote, int nRequestID);

// 请求查询期权自对冲
DLL_EXPORT_C_DECL int WPCTP tReqQryOptionSelfClose(void *api, struct CThostFtdcQryOptionSelfCloseField *pQryOptionSelfClose, int nRequestID);

// 请求查询投资单元
DLL_EXPORT_C_DECL int WPCTP tReqQryInvestUnit(void *api, struct CThostFtdcQryInvestUnitField *pQryInvestUnit, int nRequestID);

// 请求查询组合合约安全系数
DLL_EXPORT_C_DECL int WPCTP tReqQryCombInstrumentGuard(void *api, struct CThostFtdcQryCombInstrumentGuardField *pQryCombInstrumentGuard, int nRequestID);

// 请求查询申请组合
DLL_EXPORT_C_DECL int WPCTP tReqQryCombAction(void *api, struct CThostFtdcQryCombActionField *pQryCombAction, int nRequestID);

// 请求查询转帐流水
DLL_EXPORT_C_DECL int WPCTP tReqQryTransferSerial(void *api, struct CThostFtdcQryTransferSerialField *pQryTransferSerial, int nRequestID);

// 请求查询银期签约关系
DLL_EXPORT_C_DECL int WPCTP tReqQryAccountregister(void *api, struct CThostFtdcQryAccountregisterField *pQryAccountregister, int nRequestID);

// 请求查询签约银行
DLL_EXPORT_C_DECL int WPCTP tReqQryContractBank(void *api, struct CThostFtdcQryContractBankField *pQryContractBank, int nRequestID);

// 请求查询预埋单
DLL_EXPORT_C_DECL int WPCTP tReqQryParkedOrder(void *api, struct CThostFtdcQryParkedOrderField *pQryParkedOrder, int nRequestID);

// 请求查询预埋撤单
DLL_EXPORT_C_DECL int WPCTP tReqQryParkedOrderAction(void *api, struct CThostFtdcQryParkedOrderActionField *pQryParkedOrderAction, int nRequestID);

// 请求查询交易通知
DLL_EXPORT_C_DECL int WPCTP tReqQryTradingNotice(void *api, struct CThostFtdcQryTradingNoticeField *pQryTradingNotice, int nRequestID);

// 请求查询经纪公司交易参数
DLL_EXPORT_C_DECL int WPCTP tReqQryBrokerTradingParams(void *api, struct CThostFtdcQryBrokerTradingParamsField *pQryBrokerTradingParams, int nRequestID);

// 请求查询经纪公司交易算法
DLL_EXPORT_C_DECL int WPCTP tReqQryBrokerTradingAlgos(void *api, struct CThostFtdcQryBrokerTradingAlgosField *pQryBrokerTradingAlgos, int nRequestID);

// 请求查询监控中心用户令牌
DLL_EXPORT_C_DECL int WPCTP tReqQueryCFMMCTradingAccountToken(void *api, struct CThostFtdcQueryCFMMCTradingAccountTokenField *pQueryCFMMCTradingAccountToken, int nRequestID);

// 期货发起银行资金转期货请求
DLL_EXPORT_C_DECL int WPCTP tReqFromBankToFutureByFuture(void *api, struct CThostFtdcReqTransferField *pReqTransfer, int nRequestID);

// 期货发起期货资金转银行请求
DLL_EXPORT_C_DECL int WPCTP tReqFromFutureToBankByFuture(void *api, struct CThostFtdcReqTransferField *pReqTransfer, int nRequestID);

// 期货发起查询银行余额请求
DLL_EXPORT_C_DECL int WPCTP tReqQueryBankAccountMoneyByFuture(void *api, struct CThostFtdcReqQueryAccountField *pReqQueryAccount, int nRequestID);

// 请求查询分类合约
DLL_EXPORT_C_DECL int WPCTP tReqQryClassifiedInstrument(void *api, struct CThostFtdcQryClassifiedInstrumentField *pQryClassifiedInstrument, int nRequestID);

// 请求组合优惠比例
DLL_EXPORT_C_DECL int WPCTP tReqQryCombPromotionParam(void *api, struct CThostFtdcQryCombPromotionParamField *pQryCombPromotionParam, int nRequestID);

// 投资者风险结算持仓查询
DLL_EXPORT_C_DECL int WPCTP tReqQryRiskSettleInvstPosition(void *api, struct CThostFtdcQryRiskSettleInvstPositionField *pQryRiskSettleInvstPosition, int nRequestID);

// 风险结算产品查询
DLL_EXPORT_C_DECL int WPCTP tReqQryRiskSettleProductStatus(void *api, struct CThostFtdcQryRiskSettleProductStatusField *pQryRiskSettleProductStatus, int nRequestID);

// SPBM期货合约参数查询
DLL_EXPORT_C_DECL int WPCTP tReqQrySPBMFutureParameter(void *api, struct CThostFtdcQrySPBMFutureParameterField *pQrySPBMFutureParameter, int nRequestID);

// SPBM期权合约参数查询
DLL_EXPORT_C_DECL int WPCTP tReqQrySPBMOptionParameter(void *api, struct CThostFtdcQrySPBMOptionParameterField *pQrySPBMOptionParameter, int nRequestID);

// SPBM品种内对锁仓折扣参数查询
DLL_EXPORT_C_DECL int WPCTP tReqQrySPBMIntraParameter(void *api, struct CThostFtdcQrySPBMIntraParameterField *pQrySPBMIntraParameter, int nRequestID);

// SPBM跨品种抵扣参数查询
DLL_EXPORT_C_DECL int WPCTP tReqQrySPBMInterParameter(void *api, struct CThostFtdcQrySPBMInterParameterField *pQrySPBMInterParameter, int nRequestID);

// SPBM组合保证金套餐查询
DLL_EXPORT_C_DECL int WPCTP tReqQrySPBMPortfDefinition(void *api, struct CThostFtdcQrySPBMPortfDefinitionField *pQrySPBMPortfDefinition, int nRequestID);

// 投资者SPBM套餐选择查询
DLL_EXPORT_C_DECL int WPCTP tReqQrySPBMInvestorPortfDef(void *api, struct CThostFtdcQrySPBMInvestorPortfDefField *pQrySPBMInvestorPortfDef, int nRequestID);

// 投资者新型组合保证金系数查询
DLL_EXPORT_C_DECL int WPCTP tReqQryInvestorPortfMarginRatio(void *api, struct CThostFtdcQryInvestorPortfMarginRatioField *pQryInvestorPortfMarginRatio, int nRequestID);

// 投资者产品SPBM明细查询
DLL_EXPORT_C_DECL int WPCTP tReqQryInvestorProdSPBMDetail(void *api, struct CThostFtdcQryInvestorProdSPBMDetailField *pQryInvestorProdSPBMDetail, int nRequestID);
