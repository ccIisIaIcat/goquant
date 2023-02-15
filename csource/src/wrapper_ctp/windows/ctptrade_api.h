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
#include "../../../ctpapi/windows/ThostFtdcTraderApi.h"
#include "../../../ctpapi/windows/DataCollect.h"
#else
#define WPCTP      __stdcall
#include "../../../ctpapi/windows/ThostFtdcTraderApi.h"
#include "../../../ctpapi/windows/DataCollect.h"
#endif
#elif __APPLE__
#define WPCTP
#include "../../../ctpapi/macos/ThostFtdcTraderApi.h"
#include "../../../ctpapi/macos/DataCollect.h"
#elif __linux__
#define WPCTP
#include "../../../ctpapi/linux/ThostFtdcTraderApi.h"
#include "../../../ctpapi/linux/DataCollect.h"
#endif

#include <string.h>

DLL_EXPORT_C_DECL int WPCTP dCTP_GetSystemInfo(char* pSystemInfo, int nLen);

DLL_EXPORT_C_DECL void* WPCTP dCTP_GetDataCollectApiVersion();

class Trade : public CThostFtdcTraderSpi
{
public:
    Trade();

    
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
    
	// 客户端认证响应
	typedef int (WPCTP *FP_OnRspAuthenticate)(CThostFtdcRspAuthenticateField *pRspAuthenticateField, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspAuthenticate_;
	virtual void OnRspAuthenticate(CThostFtdcRspAuthenticateField *pRspAuthenticateField, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspAuthenticate_) ((FP_OnRspAuthenticate)OnRspAuthenticate_)(pRspAuthenticateField, pRspInfo, nRequestID, bIsLast); }
    
	// 登录请求响应
	typedef int (WPCTP *FP_OnRspUserLogin)(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspUserLogin_;
	virtual void OnRspUserLogin(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspUserLogin_) ((FP_OnRspUserLogin)OnRspUserLogin_)(pRspUserLogin, pRspInfo, nRequestID, bIsLast); }
    
	// 登出请求响应
	typedef int (WPCTP *FP_OnRspUserLogout)(CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspUserLogout_;
	virtual void OnRspUserLogout(CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspUserLogout_) ((FP_OnRspUserLogout)OnRspUserLogout_)(pUserLogout, pRspInfo, nRequestID, bIsLast); }
    
	// 用户口令更新请求响应
	typedef int (WPCTP *FP_OnRspUserPasswordUpdate)(CThostFtdcUserPasswordUpdateField *pUserPasswordUpdate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspUserPasswordUpdate_;
	virtual void OnRspUserPasswordUpdate(CThostFtdcUserPasswordUpdateField *pUserPasswordUpdate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspUserPasswordUpdate_) ((FP_OnRspUserPasswordUpdate)OnRspUserPasswordUpdate_)(pUserPasswordUpdate, pRspInfo, nRequestID, bIsLast); }
    
	// 资金账户口令更新请求响应
	typedef int (WPCTP *FP_OnRspTradingAccountPasswordUpdate)(CThostFtdcTradingAccountPasswordUpdateField *pTradingAccountPasswordUpdate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspTradingAccountPasswordUpdate_;
	virtual void OnRspTradingAccountPasswordUpdate(CThostFtdcTradingAccountPasswordUpdateField *pTradingAccountPasswordUpdate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspTradingAccountPasswordUpdate_) ((FP_OnRspTradingAccountPasswordUpdate)OnRspTradingAccountPasswordUpdate_)(pTradingAccountPasswordUpdate, pRspInfo, nRequestID, bIsLast); }
    
	// 查询用户当前支持的认证模式的回复
	typedef int (WPCTP *FP_OnRspUserAuthMethod)(CThostFtdcRspUserAuthMethodField *pRspUserAuthMethod, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspUserAuthMethod_;
	virtual void OnRspUserAuthMethod(CThostFtdcRspUserAuthMethodField *pRspUserAuthMethod, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspUserAuthMethod_) ((FP_OnRspUserAuthMethod)OnRspUserAuthMethod_)(pRspUserAuthMethod, pRspInfo, nRequestID, bIsLast); }
    
	// 获取图形验证码请求的回复
	typedef int (WPCTP *FP_OnRspGenUserCaptcha)(CThostFtdcRspGenUserCaptchaField *pRspGenUserCaptcha, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspGenUserCaptcha_;
	virtual void OnRspGenUserCaptcha(CThostFtdcRspGenUserCaptchaField *pRspGenUserCaptcha, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspGenUserCaptcha_) ((FP_OnRspGenUserCaptcha)OnRspGenUserCaptcha_)(pRspGenUserCaptcha, pRspInfo, nRequestID, bIsLast); }
    
	// 获取短信验证码请求的回复
	typedef int (WPCTP *FP_OnRspGenUserText)(CThostFtdcRspGenUserTextField *pRspGenUserText, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspGenUserText_;
	virtual void OnRspGenUserText(CThostFtdcRspGenUserTextField *pRspGenUserText, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspGenUserText_) ((FP_OnRspGenUserText)OnRspGenUserText_)(pRspGenUserText, pRspInfo, nRequestID, bIsLast); }
    
	// 报单录入请求响应
	typedef int (WPCTP *FP_OnRspOrderInsert)(CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspOrderInsert_;
	virtual void OnRspOrderInsert(CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspOrderInsert_) ((FP_OnRspOrderInsert)OnRspOrderInsert_)(pInputOrder, pRspInfo, nRequestID, bIsLast); }
    
	// 预埋单录入请求响应
	typedef int (WPCTP *FP_OnRspParkedOrderInsert)(CThostFtdcParkedOrderField *pParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspParkedOrderInsert_;
	virtual void OnRspParkedOrderInsert(CThostFtdcParkedOrderField *pParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspParkedOrderInsert_) ((FP_OnRspParkedOrderInsert)OnRspParkedOrderInsert_)(pParkedOrder, pRspInfo, nRequestID, bIsLast); }
    
	// 预埋撤单录入请求响应
	typedef int (WPCTP *FP_OnRspParkedOrderAction)(CThostFtdcParkedOrderActionField *pParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspParkedOrderAction_;
	virtual void OnRspParkedOrderAction(CThostFtdcParkedOrderActionField *pParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspParkedOrderAction_) ((FP_OnRspParkedOrderAction)OnRspParkedOrderAction_)(pParkedOrderAction, pRspInfo, nRequestID, bIsLast); }
    
	// 报单操作请求响应
	typedef int (WPCTP *FP_OnRspOrderAction)(CThostFtdcInputOrderActionField *pInputOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspOrderAction_;
	virtual void OnRspOrderAction(CThostFtdcInputOrderActionField *pInputOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspOrderAction_) ((FP_OnRspOrderAction)OnRspOrderAction_)(pInputOrderAction, pRspInfo, nRequestID, bIsLast); }
    
	// 查询最大报单数量响应
	typedef int (WPCTP *FP_OnRspQryMaxOrderVolume)(CThostFtdcQryMaxOrderVolumeField *pQryMaxOrderVolume, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryMaxOrderVolume_;
	virtual void OnRspQryMaxOrderVolume(CThostFtdcQryMaxOrderVolumeField *pQryMaxOrderVolume, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryMaxOrderVolume_) ((FP_OnRspQryMaxOrderVolume)OnRspQryMaxOrderVolume_)(pQryMaxOrderVolume, pRspInfo, nRequestID, bIsLast); }
    
	// 投资者结算结果确认响应
	typedef int (WPCTP *FP_OnRspSettlementInfoConfirm)(CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspSettlementInfoConfirm_;
	virtual void OnRspSettlementInfoConfirm(CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspSettlementInfoConfirm_) ((FP_OnRspSettlementInfoConfirm)OnRspSettlementInfoConfirm_)(pSettlementInfoConfirm, pRspInfo, nRequestID, bIsLast); }
    
	// 删除预埋单响应
	typedef int (WPCTP *FP_OnRspRemoveParkedOrder)(CThostFtdcRemoveParkedOrderField *pRemoveParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspRemoveParkedOrder_;
	virtual void OnRspRemoveParkedOrder(CThostFtdcRemoveParkedOrderField *pRemoveParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspRemoveParkedOrder_) ((FP_OnRspRemoveParkedOrder)OnRspRemoveParkedOrder_)(pRemoveParkedOrder, pRspInfo, nRequestID, bIsLast); }
    
	// 删除预埋撤单响应
	typedef int (WPCTP *FP_OnRspRemoveParkedOrderAction)(CThostFtdcRemoveParkedOrderActionField *pRemoveParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspRemoveParkedOrderAction_;
	virtual void OnRspRemoveParkedOrderAction(CThostFtdcRemoveParkedOrderActionField *pRemoveParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspRemoveParkedOrderAction_) ((FP_OnRspRemoveParkedOrderAction)OnRspRemoveParkedOrderAction_)(pRemoveParkedOrderAction, pRspInfo, nRequestID, bIsLast); }
    
	// 执行宣告录入请求响应
	typedef int (WPCTP *FP_OnRspExecOrderInsert)(CThostFtdcInputExecOrderField *pInputExecOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspExecOrderInsert_;
	virtual void OnRspExecOrderInsert(CThostFtdcInputExecOrderField *pInputExecOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspExecOrderInsert_) ((FP_OnRspExecOrderInsert)OnRspExecOrderInsert_)(pInputExecOrder, pRspInfo, nRequestID, bIsLast); }
    
	// 执行宣告操作请求响应
	typedef int (WPCTP *FP_OnRspExecOrderAction)(CThostFtdcInputExecOrderActionField *pInputExecOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspExecOrderAction_;
	virtual void OnRspExecOrderAction(CThostFtdcInputExecOrderActionField *pInputExecOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspExecOrderAction_) ((FP_OnRspExecOrderAction)OnRspExecOrderAction_)(pInputExecOrderAction, pRspInfo, nRequestID, bIsLast); }
    
	// 询价录入请求响应
	typedef int (WPCTP *FP_OnRspForQuoteInsert)(CThostFtdcInputForQuoteField *pInputForQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspForQuoteInsert_;
	virtual void OnRspForQuoteInsert(CThostFtdcInputForQuoteField *pInputForQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspForQuoteInsert_) ((FP_OnRspForQuoteInsert)OnRspForQuoteInsert_)(pInputForQuote, pRspInfo, nRequestID, bIsLast); }
    
	// 报价录入请求响应
	typedef int (WPCTP *FP_OnRspQuoteInsert)(CThostFtdcInputQuoteField *pInputQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQuoteInsert_;
	virtual void OnRspQuoteInsert(CThostFtdcInputQuoteField *pInputQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQuoteInsert_) ((FP_OnRspQuoteInsert)OnRspQuoteInsert_)(pInputQuote, pRspInfo, nRequestID, bIsLast); }
    
	// 报价操作请求响应
	typedef int (WPCTP *FP_OnRspQuoteAction)(CThostFtdcInputQuoteActionField *pInputQuoteAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQuoteAction_;
	virtual void OnRspQuoteAction(CThostFtdcInputQuoteActionField *pInputQuoteAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQuoteAction_) ((FP_OnRspQuoteAction)OnRspQuoteAction_)(pInputQuoteAction, pRspInfo, nRequestID, bIsLast); }
    
	// 批量报单操作请求响应
	typedef int (WPCTP *FP_OnRspBatchOrderAction)(CThostFtdcInputBatchOrderActionField *pInputBatchOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspBatchOrderAction_;
	virtual void OnRspBatchOrderAction(CThostFtdcInputBatchOrderActionField *pInputBatchOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspBatchOrderAction_) ((FP_OnRspBatchOrderAction)OnRspBatchOrderAction_)(pInputBatchOrderAction, pRspInfo, nRequestID, bIsLast); }
    
	// 期权自对冲录入请求响应
	typedef int (WPCTP *FP_OnRspOptionSelfCloseInsert)(CThostFtdcInputOptionSelfCloseField *pInputOptionSelfClose, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspOptionSelfCloseInsert_;
	virtual void OnRspOptionSelfCloseInsert(CThostFtdcInputOptionSelfCloseField *pInputOptionSelfClose, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspOptionSelfCloseInsert_) ((FP_OnRspOptionSelfCloseInsert)OnRspOptionSelfCloseInsert_)(pInputOptionSelfClose, pRspInfo, nRequestID, bIsLast); }
    
	// 期权自对冲操作请求响应
	typedef int (WPCTP *FP_OnRspOptionSelfCloseAction)(CThostFtdcInputOptionSelfCloseActionField *pInputOptionSelfCloseAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspOptionSelfCloseAction_;
	virtual void OnRspOptionSelfCloseAction(CThostFtdcInputOptionSelfCloseActionField *pInputOptionSelfCloseAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspOptionSelfCloseAction_) ((FP_OnRspOptionSelfCloseAction)OnRspOptionSelfCloseAction_)(pInputOptionSelfCloseAction, pRspInfo, nRequestID, bIsLast); }
    
	// 申请组合录入请求响应
	typedef int (WPCTP *FP_OnRspCombActionInsert)(CThostFtdcInputCombActionField *pInputCombAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspCombActionInsert_;
	virtual void OnRspCombActionInsert(CThostFtdcInputCombActionField *pInputCombAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspCombActionInsert_) ((FP_OnRspCombActionInsert)OnRspCombActionInsert_)(pInputCombAction, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询报单响应
	typedef int (WPCTP *FP_OnRspQryOrder)(CThostFtdcOrderField *pOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryOrder_;
	virtual void OnRspQryOrder(CThostFtdcOrderField *pOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryOrder_) ((FP_OnRspQryOrder)OnRspQryOrder_)(pOrder, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询成交响应
	typedef int (WPCTP *FP_OnRspQryTrade)(CThostFtdcTradeField *pTrade, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryTrade_;
	virtual void OnRspQryTrade(CThostFtdcTradeField *pTrade, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryTrade_) ((FP_OnRspQryTrade)OnRspQryTrade_)(pTrade, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询投资者持仓响应
	typedef int (WPCTP *FP_OnRspQryInvestorPosition)(CThostFtdcInvestorPositionField *pInvestorPosition, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryInvestorPosition_;
	virtual void OnRspQryInvestorPosition(CThostFtdcInvestorPositionField *pInvestorPosition, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryInvestorPosition_) ((FP_OnRspQryInvestorPosition)OnRspQryInvestorPosition_)(pInvestorPosition, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询资金账户响应
	typedef int (WPCTP *FP_OnRspQryTradingAccount)(CThostFtdcTradingAccountField *pTradingAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryTradingAccount_;
	virtual void OnRspQryTradingAccount(CThostFtdcTradingAccountField *pTradingAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryTradingAccount_) ((FP_OnRspQryTradingAccount)OnRspQryTradingAccount_)(pTradingAccount, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询投资者响应
	typedef int (WPCTP *FP_OnRspQryInvestor)(CThostFtdcInvestorField *pInvestor, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryInvestor_;
	virtual void OnRspQryInvestor(CThostFtdcInvestorField *pInvestor, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryInvestor_) ((FP_OnRspQryInvestor)OnRspQryInvestor_)(pInvestor, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询交易编码响应
	typedef int (WPCTP *FP_OnRspQryTradingCode)(CThostFtdcTradingCodeField *pTradingCode, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryTradingCode_;
	virtual void OnRspQryTradingCode(CThostFtdcTradingCodeField *pTradingCode, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryTradingCode_) ((FP_OnRspQryTradingCode)OnRspQryTradingCode_)(pTradingCode, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询合约保证金率响应
	typedef int (WPCTP *FP_OnRspQryInstrumentMarginRate)(CThostFtdcInstrumentMarginRateField *pInstrumentMarginRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryInstrumentMarginRate_;
	virtual void OnRspQryInstrumentMarginRate(CThostFtdcInstrumentMarginRateField *pInstrumentMarginRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryInstrumentMarginRate_) ((FP_OnRspQryInstrumentMarginRate)OnRspQryInstrumentMarginRate_)(pInstrumentMarginRate, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询合约手续费率响应
	typedef int (WPCTP *FP_OnRspQryInstrumentCommissionRate)(CThostFtdcInstrumentCommissionRateField *pInstrumentCommissionRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryInstrumentCommissionRate_;
	virtual void OnRspQryInstrumentCommissionRate(CThostFtdcInstrumentCommissionRateField *pInstrumentCommissionRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryInstrumentCommissionRate_) ((FP_OnRspQryInstrumentCommissionRate)OnRspQryInstrumentCommissionRate_)(pInstrumentCommissionRate, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询交易所响应
	typedef int (WPCTP *FP_OnRspQryExchange)(CThostFtdcExchangeField *pExchange, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryExchange_;
	virtual void OnRspQryExchange(CThostFtdcExchangeField *pExchange, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryExchange_) ((FP_OnRspQryExchange)OnRspQryExchange_)(pExchange, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询产品响应
	typedef int (WPCTP *FP_OnRspQryProduct)(CThostFtdcProductField *pProduct, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryProduct_;
	virtual void OnRspQryProduct(CThostFtdcProductField *pProduct, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryProduct_) ((FP_OnRspQryProduct)OnRspQryProduct_)(pProduct, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询合约响应
	typedef int (WPCTP *FP_OnRspQryInstrument)(CThostFtdcInstrumentField *pInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryInstrument_;
	virtual void OnRspQryInstrument(CThostFtdcInstrumentField *pInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryInstrument_) ((FP_OnRspQryInstrument)OnRspQryInstrument_)(pInstrument, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询行情响应
	typedef int (WPCTP *FP_OnRspQryDepthMarketData)(CThostFtdcDepthMarketDataField *pDepthMarketData, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryDepthMarketData_;
	virtual void OnRspQryDepthMarketData(CThostFtdcDepthMarketDataField *pDepthMarketData, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryDepthMarketData_) ((FP_OnRspQryDepthMarketData)OnRspQryDepthMarketData_)(pDepthMarketData, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询交易员报盘机响应
	typedef int (WPCTP *FP_OnRspQryTraderOffer)(CThostFtdcTraderOfferField *pTraderOffer, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryTraderOffer_;
	virtual void OnRspQryTraderOffer(CThostFtdcTraderOfferField *pTraderOffer, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryTraderOffer_) ((FP_OnRspQryTraderOffer)OnRspQryTraderOffer_)(pTraderOffer, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询投资者结算结果响应
	typedef int (WPCTP *FP_OnRspQrySettlementInfo)(CThostFtdcSettlementInfoField *pSettlementInfo, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQrySettlementInfo_;
	virtual void OnRspQrySettlementInfo(CThostFtdcSettlementInfoField *pSettlementInfo, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQrySettlementInfo_) ((FP_OnRspQrySettlementInfo)OnRspQrySettlementInfo_)(pSettlementInfo, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询转帐银行响应
	typedef int (WPCTP *FP_OnRspQryTransferBank)(CThostFtdcTransferBankField *pTransferBank, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryTransferBank_;
	virtual void OnRspQryTransferBank(CThostFtdcTransferBankField *pTransferBank, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryTransferBank_) ((FP_OnRspQryTransferBank)OnRspQryTransferBank_)(pTransferBank, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询投资者持仓明细响应
	typedef int (WPCTP *FP_OnRspQryInvestorPositionDetail)(CThostFtdcInvestorPositionDetailField *pInvestorPositionDetail, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryInvestorPositionDetail_;
	virtual void OnRspQryInvestorPositionDetail(CThostFtdcInvestorPositionDetailField *pInvestorPositionDetail, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryInvestorPositionDetail_) ((FP_OnRspQryInvestorPositionDetail)OnRspQryInvestorPositionDetail_)(pInvestorPositionDetail, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询客户通知响应
	typedef int (WPCTP *FP_OnRspQryNotice)(CThostFtdcNoticeField *pNotice, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryNotice_;
	virtual void OnRspQryNotice(CThostFtdcNoticeField *pNotice, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryNotice_) ((FP_OnRspQryNotice)OnRspQryNotice_)(pNotice, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询结算信息确认响应
	typedef int (WPCTP *FP_OnRspQrySettlementInfoConfirm)(CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQrySettlementInfoConfirm_;
	virtual void OnRspQrySettlementInfoConfirm(CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQrySettlementInfoConfirm_) ((FP_OnRspQrySettlementInfoConfirm)OnRspQrySettlementInfoConfirm_)(pSettlementInfoConfirm, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询投资者持仓明细响应
	typedef int (WPCTP *FP_OnRspQryInvestorPositionCombineDetail)(CThostFtdcInvestorPositionCombineDetailField *pInvestorPositionCombineDetail, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryInvestorPositionCombineDetail_;
	virtual void OnRspQryInvestorPositionCombineDetail(CThostFtdcInvestorPositionCombineDetailField *pInvestorPositionCombineDetail, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryInvestorPositionCombineDetail_) ((FP_OnRspQryInvestorPositionCombineDetail)OnRspQryInvestorPositionCombineDetail_)(pInvestorPositionCombineDetail, pRspInfo, nRequestID, bIsLast); }
    
	// 查询保证金监管系统经纪公司资金账户密钥响应
	typedef int (WPCTP *FP_OnRspQryCFMMCTradingAccountKey)(CThostFtdcCFMMCTradingAccountKeyField *pCFMMCTradingAccountKey, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryCFMMCTradingAccountKey_;
	virtual void OnRspQryCFMMCTradingAccountKey(CThostFtdcCFMMCTradingAccountKeyField *pCFMMCTradingAccountKey, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryCFMMCTradingAccountKey_) ((FP_OnRspQryCFMMCTradingAccountKey)OnRspQryCFMMCTradingAccountKey_)(pCFMMCTradingAccountKey, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询仓单折抵信息响应
	typedef int (WPCTP *FP_OnRspQryEWarrantOffset)(CThostFtdcEWarrantOffsetField *pEWarrantOffset, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryEWarrantOffset_;
	virtual void OnRspQryEWarrantOffset(CThostFtdcEWarrantOffsetField *pEWarrantOffset, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryEWarrantOffset_) ((FP_OnRspQryEWarrantOffset)OnRspQryEWarrantOffset_)(pEWarrantOffset, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询投资者品种/跨品种保证金响应
	typedef int (WPCTP *FP_OnRspQryInvestorProductGroupMargin)(CThostFtdcInvestorProductGroupMarginField *pInvestorProductGroupMargin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryInvestorProductGroupMargin_;
	virtual void OnRspQryInvestorProductGroupMargin(CThostFtdcInvestorProductGroupMarginField *pInvestorProductGroupMargin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryInvestorProductGroupMargin_) ((FP_OnRspQryInvestorProductGroupMargin)OnRspQryInvestorProductGroupMargin_)(pInvestorProductGroupMargin, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询交易所保证金率响应
	typedef int (WPCTP *FP_OnRspQryExchangeMarginRate)(CThostFtdcExchangeMarginRateField *pExchangeMarginRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryExchangeMarginRate_;
	virtual void OnRspQryExchangeMarginRate(CThostFtdcExchangeMarginRateField *pExchangeMarginRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryExchangeMarginRate_) ((FP_OnRspQryExchangeMarginRate)OnRspQryExchangeMarginRate_)(pExchangeMarginRate, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询交易所调整保证金率响应
	typedef int (WPCTP *FP_OnRspQryExchangeMarginRateAdjust)(CThostFtdcExchangeMarginRateAdjustField *pExchangeMarginRateAdjust, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryExchangeMarginRateAdjust_;
	virtual void OnRspQryExchangeMarginRateAdjust(CThostFtdcExchangeMarginRateAdjustField *pExchangeMarginRateAdjust, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryExchangeMarginRateAdjust_) ((FP_OnRspQryExchangeMarginRateAdjust)OnRspQryExchangeMarginRateAdjust_)(pExchangeMarginRateAdjust, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询汇率响应
	typedef int (WPCTP *FP_OnRspQryExchangeRate)(CThostFtdcExchangeRateField *pExchangeRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryExchangeRate_;
	virtual void OnRspQryExchangeRate(CThostFtdcExchangeRateField *pExchangeRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryExchangeRate_) ((FP_OnRspQryExchangeRate)OnRspQryExchangeRate_)(pExchangeRate, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询二级代理操作员银期权限响应
	typedef int (WPCTP *FP_OnRspQrySecAgentACIDMap)(CThostFtdcSecAgentACIDMapField *pSecAgentACIDMap, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQrySecAgentACIDMap_;
	virtual void OnRspQrySecAgentACIDMap(CThostFtdcSecAgentACIDMapField *pSecAgentACIDMap, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQrySecAgentACIDMap_) ((FP_OnRspQrySecAgentACIDMap)OnRspQrySecAgentACIDMap_)(pSecAgentACIDMap, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询产品报价汇率
	typedef int (WPCTP *FP_OnRspQryProductExchRate)(CThostFtdcProductExchRateField *pProductExchRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryProductExchRate_;
	virtual void OnRspQryProductExchRate(CThostFtdcProductExchRateField *pProductExchRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryProductExchRate_) ((FP_OnRspQryProductExchRate)OnRspQryProductExchRate_)(pProductExchRate, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询产品组
	typedef int (WPCTP *FP_OnRspQryProductGroup)(CThostFtdcProductGroupField *pProductGroup, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryProductGroup_;
	virtual void OnRspQryProductGroup(CThostFtdcProductGroupField *pProductGroup, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryProductGroup_) ((FP_OnRspQryProductGroup)OnRspQryProductGroup_)(pProductGroup, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询做市商合约手续费率响应
	typedef int (WPCTP *FP_OnRspQryMMInstrumentCommissionRate)(CThostFtdcMMInstrumentCommissionRateField *pMMInstrumentCommissionRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryMMInstrumentCommissionRate_;
	virtual void OnRspQryMMInstrumentCommissionRate(CThostFtdcMMInstrumentCommissionRateField *pMMInstrumentCommissionRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryMMInstrumentCommissionRate_) ((FP_OnRspQryMMInstrumentCommissionRate)OnRspQryMMInstrumentCommissionRate_)(pMMInstrumentCommissionRate, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询做市商期权合约手续费响应
	typedef int (WPCTP *FP_OnRspQryMMOptionInstrCommRate)(CThostFtdcMMOptionInstrCommRateField *pMMOptionInstrCommRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryMMOptionInstrCommRate_;
	virtual void OnRspQryMMOptionInstrCommRate(CThostFtdcMMOptionInstrCommRateField *pMMOptionInstrCommRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryMMOptionInstrCommRate_) ((FP_OnRspQryMMOptionInstrCommRate)OnRspQryMMOptionInstrCommRate_)(pMMOptionInstrCommRate, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询报单手续费响应
	typedef int (WPCTP *FP_OnRspQryInstrumentOrderCommRate)(CThostFtdcInstrumentOrderCommRateField *pInstrumentOrderCommRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryInstrumentOrderCommRate_;
	virtual void OnRspQryInstrumentOrderCommRate(CThostFtdcInstrumentOrderCommRateField *pInstrumentOrderCommRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryInstrumentOrderCommRate_) ((FP_OnRspQryInstrumentOrderCommRate)OnRspQryInstrumentOrderCommRate_)(pInstrumentOrderCommRate, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询资金账户响应
	typedef int (WPCTP *FP_OnRspQrySecAgentTradingAccount)(CThostFtdcTradingAccountField *pTradingAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQrySecAgentTradingAccount_;
	virtual void OnRspQrySecAgentTradingAccount(CThostFtdcTradingAccountField *pTradingAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQrySecAgentTradingAccount_) ((FP_OnRspQrySecAgentTradingAccount)OnRspQrySecAgentTradingAccount_)(pTradingAccount, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询二级代理商资金校验模式响应
	typedef int (WPCTP *FP_OnRspQrySecAgentCheckMode)(CThostFtdcSecAgentCheckModeField *pSecAgentCheckMode, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQrySecAgentCheckMode_;
	virtual void OnRspQrySecAgentCheckMode(CThostFtdcSecAgentCheckModeField *pSecAgentCheckMode, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQrySecAgentCheckMode_) ((FP_OnRspQrySecAgentCheckMode)OnRspQrySecAgentCheckMode_)(pSecAgentCheckMode, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询二级代理商信息响应
	typedef int (WPCTP *FP_OnRspQrySecAgentTradeInfo)(CThostFtdcSecAgentTradeInfoField *pSecAgentTradeInfo, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQrySecAgentTradeInfo_;
	virtual void OnRspQrySecAgentTradeInfo(CThostFtdcSecAgentTradeInfoField *pSecAgentTradeInfo, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQrySecAgentTradeInfo_) ((FP_OnRspQrySecAgentTradeInfo)OnRspQrySecAgentTradeInfo_)(pSecAgentTradeInfo, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询期权交易成本响应
	typedef int (WPCTP *FP_OnRspQryOptionInstrTradeCost)(CThostFtdcOptionInstrTradeCostField *pOptionInstrTradeCost, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryOptionInstrTradeCost_;
	virtual void OnRspQryOptionInstrTradeCost(CThostFtdcOptionInstrTradeCostField *pOptionInstrTradeCost, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryOptionInstrTradeCost_) ((FP_OnRspQryOptionInstrTradeCost)OnRspQryOptionInstrTradeCost_)(pOptionInstrTradeCost, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询期权合约手续费响应
	typedef int (WPCTP *FP_OnRspQryOptionInstrCommRate)(CThostFtdcOptionInstrCommRateField *pOptionInstrCommRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryOptionInstrCommRate_;
	virtual void OnRspQryOptionInstrCommRate(CThostFtdcOptionInstrCommRateField *pOptionInstrCommRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryOptionInstrCommRate_) ((FP_OnRspQryOptionInstrCommRate)OnRspQryOptionInstrCommRate_)(pOptionInstrCommRate, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询执行宣告响应
	typedef int (WPCTP *FP_OnRspQryExecOrder)(CThostFtdcExecOrderField *pExecOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryExecOrder_;
	virtual void OnRspQryExecOrder(CThostFtdcExecOrderField *pExecOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryExecOrder_) ((FP_OnRspQryExecOrder)OnRspQryExecOrder_)(pExecOrder, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询询价响应
	typedef int (WPCTP *FP_OnRspQryForQuote)(CThostFtdcForQuoteField *pForQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryForQuote_;
	virtual void OnRspQryForQuote(CThostFtdcForQuoteField *pForQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryForQuote_) ((FP_OnRspQryForQuote)OnRspQryForQuote_)(pForQuote, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询报价响应
	typedef int (WPCTP *FP_OnRspQryQuote)(CThostFtdcQuoteField *pQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryQuote_;
	virtual void OnRspQryQuote(CThostFtdcQuoteField *pQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryQuote_) ((FP_OnRspQryQuote)OnRspQryQuote_)(pQuote, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询期权自对冲响应
	typedef int (WPCTP *FP_OnRspQryOptionSelfClose)(CThostFtdcOptionSelfCloseField *pOptionSelfClose, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryOptionSelfClose_;
	virtual void OnRspQryOptionSelfClose(CThostFtdcOptionSelfCloseField *pOptionSelfClose, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryOptionSelfClose_) ((FP_OnRspQryOptionSelfClose)OnRspQryOptionSelfClose_)(pOptionSelfClose, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询投资单元响应
	typedef int (WPCTP *FP_OnRspQryInvestUnit)(CThostFtdcInvestUnitField *pInvestUnit, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryInvestUnit_;
	virtual void OnRspQryInvestUnit(CThostFtdcInvestUnitField *pInvestUnit, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryInvestUnit_) ((FP_OnRspQryInvestUnit)OnRspQryInvestUnit_)(pInvestUnit, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询组合合约安全系数响应
	typedef int (WPCTP *FP_OnRspQryCombInstrumentGuard)(CThostFtdcCombInstrumentGuardField *pCombInstrumentGuard, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryCombInstrumentGuard_;
	virtual void OnRspQryCombInstrumentGuard(CThostFtdcCombInstrumentGuardField *pCombInstrumentGuard, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryCombInstrumentGuard_) ((FP_OnRspQryCombInstrumentGuard)OnRspQryCombInstrumentGuard_)(pCombInstrumentGuard, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询申请组合响应
	typedef int (WPCTP *FP_OnRspQryCombAction)(CThostFtdcCombActionField *pCombAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryCombAction_;
	virtual void OnRspQryCombAction(CThostFtdcCombActionField *pCombAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryCombAction_) ((FP_OnRspQryCombAction)OnRspQryCombAction_)(pCombAction, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询转帐流水响应
	typedef int (WPCTP *FP_OnRspQryTransferSerial)(CThostFtdcTransferSerialField *pTransferSerial, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryTransferSerial_;
	virtual void OnRspQryTransferSerial(CThostFtdcTransferSerialField *pTransferSerial, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryTransferSerial_) ((FP_OnRspQryTransferSerial)OnRspQryTransferSerial_)(pTransferSerial, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询银期签约关系响应
	typedef int (WPCTP *FP_OnRspQryAccountregister)(CThostFtdcAccountregisterField *pAccountregister, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryAccountregister_;
	virtual void OnRspQryAccountregister(CThostFtdcAccountregisterField *pAccountregister, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryAccountregister_) ((FP_OnRspQryAccountregister)OnRspQryAccountregister_)(pAccountregister, pRspInfo, nRequestID, bIsLast); }
    
	// 错误应答
	typedef int (WPCTP *FP_OnRspError)(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspError_;
	virtual void OnRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspError_) ((FP_OnRspError)OnRspError_)(pRspInfo, nRequestID, bIsLast); }
    
	// 报单通知
	typedef int (WPCTP *FP_OnRtnOrder)(CThostFtdcOrderField *pOrder);
	void *OnRtnOrder_;
	virtual void OnRtnOrder(CThostFtdcOrderField *pOrder){ if(OnRtnOrder_) ((FP_OnRtnOrder)OnRtnOrder_)(pOrder); }
    
	// 成交通知
	typedef int (WPCTP *FP_OnRtnTrade)(CThostFtdcTradeField *pTrade);
	void *OnRtnTrade_;
	virtual void OnRtnTrade(CThostFtdcTradeField *pTrade){ if(OnRtnTrade_) ((FP_OnRtnTrade)OnRtnTrade_)(pTrade); }
    
	// 报单录入错误回报
	typedef int (WPCTP *FP_OnErrRtnOrderInsert)(CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo);
	void *OnErrRtnOrderInsert_;
	virtual void OnErrRtnOrderInsert(CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo){ if(OnErrRtnOrderInsert_) ((FP_OnErrRtnOrderInsert)OnErrRtnOrderInsert_)(pInputOrder, pRspInfo); }
    
	// 报单操作错误回报
	typedef int (WPCTP *FP_OnErrRtnOrderAction)(CThostFtdcOrderActionField *pOrderAction, CThostFtdcRspInfoField *pRspInfo);
	void *OnErrRtnOrderAction_;
	virtual void OnErrRtnOrderAction(CThostFtdcOrderActionField *pOrderAction, CThostFtdcRspInfoField *pRspInfo){ if(OnErrRtnOrderAction_) ((FP_OnErrRtnOrderAction)OnErrRtnOrderAction_)(pOrderAction, pRspInfo); }
    
	// 合约交易状态通知
	typedef int (WPCTP *FP_OnRtnInstrumentStatus)(CThostFtdcInstrumentStatusField *pInstrumentStatus);
	void *OnRtnInstrumentStatus_;
	virtual void OnRtnInstrumentStatus(CThostFtdcInstrumentStatusField *pInstrumentStatus){ if(OnRtnInstrumentStatus_) ((FP_OnRtnInstrumentStatus)OnRtnInstrumentStatus_)(pInstrumentStatus); }
    
	// 交易所公告通知
	typedef int (WPCTP *FP_OnRtnBulletin)(CThostFtdcBulletinField *pBulletin);
	void *OnRtnBulletin_;
	virtual void OnRtnBulletin(CThostFtdcBulletinField *pBulletin){ if(OnRtnBulletin_) ((FP_OnRtnBulletin)OnRtnBulletin_)(pBulletin); }
    
	// 交易通知
	typedef int (WPCTP *FP_OnRtnTradingNotice)(CThostFtdcTradingNoticeInfoField *pTradingNoticeInfo);
	void *OnRtnTradingNotice_;
	virtual void OnRtnTradingNotice(CThostFtdcTradingNoticeInfoField *pTradingNoticeInfo){ if(OnRtnTradingNotice_) ((FP_OnRtnTradingNotice)OnRtnTradingNotice_)(pTradingNoticeInfo); }
    
	// 提示条件单校验错误
	typedef int (WPCTP *FP_OnRtnErrorConditionalOrder)(CThostFtdcErrorConditionalOrderField *pErrorConditionalOrder);
	void *OnRtnErrorConditionalOrder_;
	virtual void OnRtnErrorConditionalOrder(CThostFtdcErrorConditionalOrderField *pErrorConditionalOrder){ if(OnRtnErrorConditionalOrder_) ((FP_OnRtnErrorConditionalOrder)OnRtnErrorConditionalOrder_)(pErrorConditionalOrder); }
    
	// 执行宣告通知
	typedef int (WPCTP *FP_OnRtnExecOrder)(CThostFtdcExecOrderField *pExecOrder);
	void *OnRtnExecOrder_;
	virtual void OnRtnExecOrder(CThostFtdcExecOrderField *pExecOrder){ if(OnRtnExecOrder_) ((FP_OnRtnExecOrder)OnRtnExecOrder_)(pExecOrder); }
    
	// 执行宣告录入错误回报
	typedef int (WPCTP *FP_OnErrRtnExecOrderInsert)(CThostFtdcInputExecOrderField *pInputExecOrder, CThostFtdcRspInfoField *pRspInfo);
	void *OnErrRtnExecOrderInsert_;
	virtual void OnErrRtnExecOrderInsert(CThostFtdcInputExecOrderField *pInputExecOrder, CThostFtdcRspInfoField *pRspInfo){ if(OnErrRtnExecOrderInsert_) ((FP_OnErrRtnExecOrderInsert)OnErrRtnExecOrderInsert_)(pInputExecOrder, pRspInfo); }
    
	// 执行宣告操作错误回报
	typedef int (WPCTP *FP_OnErrRtnExecOrderAction)(CThostFtdcExecOrderActionField *pExecOrderAction, CThostFtdcRspInfoField *pRspInfo);
	void *OnErrRtnExecOrderAction_;
	virtual void OnErrRtnExecOrderAction(CThostFtdcExecOrderActionField *pExecOrderAction, CThostFtdcRspInfoField *pRspInfo){ if(OnErrRtnExecOrderAction_) ((FP_OnErrRtnExecOrderAction)OnErrRtnExecOrderAction_)(pExecOrderAction, pRspInfo); }
    
	// 询价录入错误回报
	typedef int (WPCTP *FP_OnErrRtnForQuoteInsert)(CThostFtdcInputForQuoteField *pInputForQuote, CThostFtdcRspInfoField *pRspInfo);
	void *OnErrRtnForQuoteInsert_;
	virtual void OnErrRtnForQuoteInsert(CThostFtdcInputForQuoteField *pInputForQuote, CThostFtdcRspInfoField *pRspInfo){ if(OnErrRtnForQuoteInsert_) ((FP_OnErrRtnForQuoteInsert)OnErrRtnForQuoteInsert_)(pInputForQuote, pRspInfo); }
    
	// 报价通知
	typedef int (WPCTP *FP_OnRtnQuote)(CThostFtdcQuoteField *pQuote);
	void *OnRtnQuote_;
	virtual void OnRtnQuote(CThostFtdcQuoteField *pQuote){ if(OnRtnQuote_) ((FP_OnRtnQuote)OnRtnQuote_)(pQuote); }
    
	// 报价录入错误回报
	typedef int (WPCTP *FP_OnErrRtnQuoteInsert)(CThostFtdcInputQuoteField *pInputQuote, CThostFtdcRspInfoField *pRspInfo);
	void *OnErrRtnQuoteInsert_;
	virtual void OnErrRtnQuoteInsert(CThostFtdcInputQuoteField *pInputQuote, CThostFtdcRspInfoField *pRspInfo){ if(OnErrRtnQuoteInsert_) ((FP_OnErrRtnQuoteInsert)OnErrRtnQuoteInsert_)(pInputQuote, pRspInfo); }
    
	// 报价操作错误回报
	typedef int (WPCTP *FP_OnErrRtnQuoteAction)(CThostFtdcQuoteActionField *pQuoteAction, CThostFtdcRspInfoField *pRspInfo);
	void *OnErrRtnQuoteAction_;
	virtual void OnErrRtnQuoteAction(CThostFtdcQuoteActionField *pQuoteAction, CThostFtdcRspInfoField *pRspInfo){ if(OnErrRtnQuoteAction_) ((FP_OnErrRtnQuoteAction)OnErrRtnQuoteAction_)(pQuoteAction, pRspInfo); }
    
	// 询价通知
	typedef int (WPCTP *FP_OnRtnForQuoteRsp)(CThostFtdcForQuoteRspField *pForQuoteRsp);
	void *OnRtnForQuoteRsp_;
	virtual void OnRtnForQuoteRsp(CThostFtdcForQuoteRspField *pForQuoteRsp){ if(OnRtnForQuoteRsp_) ((FP_OnRtnForQuoteRsp)OnRtnForQuoteRsp_)(pForQuoteRsp); }
    
	// 保证金监控中心用户令牌
	typedef int (WPCTP *FP_OnRtnCFMMCTradingAccountToken)(CThostFtdcCFMMCTradingAccountTokenField *pCFMMCTradingAccountToken);
	void *OnRtnCFMMCTradingAccountToken_;
	virtual void OnRtnCFMMCTradingAccountToken(CThostFtdcCFMMCTradingAccountTokenField *pCFMMCTradingAccountToken){ if(OnRtnCFMMCTradingAccountToken_) ((FP_OnRtnCFMMCTradingAccountToken)OnRtnCFMMCTradingAccountToken_)(pCFMMCTradingAccountToken); }
    
	// 批量报单操作错误回报
	typedef int (WPCTP *FP_OnErrRtnBatchOrderAction)(CThostFtdcBatchOrderActionField *pBatchOrderAction, CThostFtdcRspInfoField *pRspInfo);
	void *OnErrRtnBatchOrderAction_;
	virtual void OnErrRtnBatchOrderAction(CThostFtdcBatchOrderActionField *pBatchOrderAction, CThostFtdcRspInfoField *pRspInfo){ if(OnErrRtnBatchOrderAction_) ((FP_OnErrRtnBatchOrderAction)OnErrRtnBatchOrderAction_)(pBatchOrderAction, pRspInfo); }
    
	// 期权自对冲通知
	typedef int (WPCTP *FP_OnRtnOptionSelfClose)(CThostFtdcOptionSelfCloseField *pOptionSelfClose);
	void *OnRtnOptionSelfClose_;
	virtual void OnRtnOptionSelfClose(CThostFtdcOptionSelfCloseField *pOptionSelfClose){ if(OnRtnOptionSelfClose_) ((FP_OnRtnOptionSelfClose)OnRtnOptionSelfClose_)(pOptionSelfClose); }
    
	// 期权自对冲录入错误回报
	typedef int (WPCTP *FP_OnErrRtnOptionSelfCloseInsert)(CThostFtdcInputOptionSelfCloseField *pInputOptionSelfClose, CThostFtdcRspInfoField *pRspInfo);
	void *OnErrRtnOptionSelfCloseInsert_;
	virtual void OnErrRtnOptionSelfCloseInsert(CThostFtdcInputOptionSelfCloseField *pInputOptionSelfClose, CThostFtdcRspInfoField *pRspInfo){ if(OnErrRtnOptionSelfCloseInsert_) ((FP_OnErrRtnOptionSelfCloseInsert)OnErrRtnOptionSelfCloseInsert_)(pInputOptionSelfClose, pRspInfo); }
    
	// 期权自对冲操作错误回报
	typedef int (WPCTP *FP_OnErrRtnOptionSelfCloseAction)(CThostFtdcOptionSelfCloseActionField *pOptionSelfCloseAction, CThostFtdcRspInfoField *pRspInfo);
	void *OnErrRtnOptionSelfCloseAction_;
	virtual void OnErrRtnOptionSelfCloseAction(CThostFtdcOptionSelfCloseActionField *pOptionSelfCloseAction, CThostFtdcRspInfoField *pRspInfo){ if(OnErrRtnOptionSelfCloseAction_) ((FP_OnErrRtnOptionSelfCloseAction)OnErrRtnOptionSelfCloseAction_)(pOptionSelfCloseAction, pRspInfo); }
    
	// 申请组合通知
	typedef int (WPCTP *FP_OnRtnCombAction)(CThostFtdcCombActionField *pCombAction);
	void *OnRtnCombAction_;
	virtual void OnRtnCombAction(CThostFtdcCombActionField *pCombAction){ if(OnRtnCombAction_) ((FP_OnRtnCombAction)OnRtnCombAction_)(pCombAction); }
    
	// 申请组合录入错误回报
	typedef int (WPCTP *FP_OnErrRtnCombActionInsert)(CThostFtdcInputCombActionField *pInputCombAction, CThostFtdcRspInfoField *pRspInfo);
	void *OnErrRtnCombActionInsert_;
	virtual void OnErrRtnCombActionInsert(CThostFtdcInputCombActionField *pInputCombAction, CThostFtdcRspInfoField *pRspInfo){ if(OnErrRtnCombActionInsert_) ((FP_OnErrRtnCombActionInsert)OnErrRtnCombActionInsert_)(pInputCombAction, pRspInfo); }
    
	// 请求查询签约银行响应
	typedef int (WPCTP *FP_OnRspQryContractBank)(CThostFtdcContractBankField *pContractBank, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryContractBank_;
	virtual void OnRspQryContractBank(CThostFtdcContractBankField *pContractBank, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryContractBank_) ((FP_OnRspQryContractBank)OnRspQryContractBank_)(pContractBank, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询预埋单响应
	typedef int (WPCTP *FP_OnRspQryParkedOrder)(CThostFtdcParkedOrderField *pParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryParkedOrder_;
	virtual void OnRspQryParkedOrder(CThostFtdcParkedOrderField *pParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryParkedOrder_) ((FP_OnRspQryParkedOrder)OnRspQryParkedOrder_)(pParkedOrder, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询预埋撤单响应
	typedef int (WPCTP *FP_OnRspQryParkedOrderAction)(CThostFtdcParkedOrderActionField *pParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryParkedOrderAction_;
	virtual void OnRspQryParkedOrderAction(CThostFtdcParkedOrderActionField *pParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryParkedOrderAction_) ((FP_OnRspQryParkedOrderAction)OnRspQryParkedOrderAction_)(pParkedOrderAction, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询交易通知响应
	typedef int (WPCTP *FP_OnRspQryTradingNotice)(CThostFtdcTradingNoticeField *pTradingNotice, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryTradingNotice_;
	virtual void OnRspQryTradingNotice(CThostFtdcTradingNoticeField *pTradingNotice, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryTradingNotice_) ((FP_OnRspQryTradingNotice)OnRspQryTradingNotice_)(pTradingNotice, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询经纪公司交易参数响应
	typedef int (WPCTP *FP_OnRspQryBrokerTradingParams)(CThostFtdcBrokerTradingParamsField *pBrokerTradingParams, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryBrokerTradingParams_;
	virtual void OnRspQryBrokerTradingParams(CThostFtdcBrokerTradingParamsField *pBrokerTradingParams, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryBrokerTradingParams_) ((FP_OnRspQryBrokerTradingParams)OnRspQryBrokerTradingParams_)(pBrokerTradingParams, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询经纪公司交易算法响应
	typedef int (WPCTP *FP_OnRspQryBrokerTradingAlgos)(CThostFtdcBrokerTradingAlgosField *pBrokerTradingAlgos, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryBrokerTradingAlgos_;
	virtual void OnRspQryBrokerTradingAlgos(CThostFtdcBrokerTradingAlgosField *pBrokerTradingAlgos, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryBrokerTradingAlgos_) ((FP_OnRspQryBrokerTradingAlgos)OnRspQryBrokerTradingAlgos_)(pBrokerTradingAlgos, pRspInfo, nRequestID, bIsLast); }
    
	// 请求查询监控中心用户令牌
	typedef int (WPCTP *FP_OnRspQueryCFMMCTradingAccountToken)(CThostFtdcQueryCFMMCTradingAccountTokenField *pQueryCFMMCTradingAccountToken, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQueryCFMMCTradingAccountToken_;
	virtual void OnRspQueryCFMMCTradingAccountToken(CThostFtdcQueryCFMMCTradingAccountTokenField *pQueryCFMMCTradingAccountToken, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQueryCFMMCTradingAccountToken_) ((FP_OnRspQueryCFMMCTradingAccountToken)OnRspQueryCFMMCTradingAccountToken_)(pQueryCFMMCTradingAccountToken, pRspInfo, nRequestID, bIsLast); }
    
	// 银行发起银行资金转期货通知
	typedef int (WPCTP *FP_OnRtnFromBankToFutureByBank)(CThostFtdcRspTransferField *pRspTransfer);
	void *OnRtnFromBankToFutureByBank_;
	virtual void OnRtnFromBankToFutureByBank(CThostFtdcRspTransferField *pRspTransfer){ if(OnRtnFromBankToFutureByBank_) ((FP_OnRtnFromBankToFutureByBank)OnRtnFromBankToFutureByBank_)(pRspTransfer); }
    
	// 银行发起期货资金转银行通知
	typedef int (WPCTP *FP_OnRtnFromFutureToBankByBank)(CThostFtdcRspTransferField *pRspTransfer);
	void *OnRtnFromFutureToBankByBank_;
	virtual void OnRtnFromFutureToBankByBank(CThostFtdcRspTransferField *pRspTransfer){ if(OnRtnFromFutureToBankByBank_) ((FP_OnRtnFromFutureToBankByBank)OnRtnFromFutureToBankByBank_)(pRspTransfer); }
    
	// 银行发起冲正银行转期货通知
	typedef int (WPCTP *FP_OnRtnRepealFromBankToFutureByBank)(CThostFtdcRspRepealField *pRspRepeal);
	void *OnRtnRepealFromBankToFutureByBank_;
	virtual void OnRtnRepealFromBankToFutureByBank(CThostFtdcRspRepealField *pRspRepeal){ if(OnRtnRepealFromBankToFutureByBank_) ((FP_OnRtnRepealFromBankToFutureByBank)OnRtnRepealFromBankToFutureByBank_)(pRspRepeal); }
    
	// 银行发起冲正期货转银行通知
	typedef int (WPCTP *FP_OnRtnRepealFromFutureToBankByBank)(CThostFtdcRspRepealField *pRspRepeal);
	void *OnRtnRepealFromFutureToBankByBank_;
	virtual void OnRtnRepealFromFutureToBankByBank(CThostFtdcRspRepealField *pRspRepeal){ if(OnRtnRepealFromFutureToBankByBank_) ((FP_OnRtnRepealFromFutureToBankByBank)OnRtnRepealFromFutureToBankByBank_)(pRspRepeal); }
    
	// 期货发起银行资金转期货通知
	typedef int (WPCTP *FP_OnRtnFromBankToFutureByFuture)(CThostFtdcRspTransferField *pRspTransfer);
	void *OnRtnFromBankToFutureByFuture_;
	virtual void OnRtnFromBankToFutureByFuture(CThostFtdcRspTransferField *pRspTransfer){ if(OnRtnFromBankToFutureByFuture_) ((FP_OnRtnFromBankToFutureByFuture)OnRtnFromBankToFutureByFuture_)(pRspTransfer); }
    
	// 期货发起期货资金转银行通知
	typedef int (WPCTP *FP_OnRtnFromFutureToBankByFuture)(CThostFtdcRspTransferField *pRspTransfer);
	void *OnRtnFromFutureToBankByFuture_;
	virtual void OnRtnFromFutureToBankByFuture(CThostFtdcRspTransferField *pRspTransfer){ if(OnRtnFromFutureToBankByFuture_) ((FP_OnRtnFromFutureToBankByFuture)OnRtnFromFutureToBankByFuture_)(pRspTransfer); }
    
	// 系统运行时期货端手工发起冲正银行转期货请求，银行处理完毕后报盘发回的通知
	typedef int (WPCTP *FP_OnRtnRepealFromBankToFutureByFutureManual)(CThostFtdcRspRepealField *pRspRepeal);
	void *OnRtnRepealFromBankToFutureByFutureManual_;
	virtual void OnRtnRepealFromBankToFutureByFutureManual(CThostFtdcRspRepealField *pRspRepeal){ if(OnRtnRepealFromBankToFutureByFutureManual_) ((FP_OnRtnRepealFromBankToFutureByFutureManual)OnRtnRepealFromBankToFutureByFutureManual_)(pRspRepeal); }
    
	// 系统运行时期货端手工发起冲正期货转银行请求，银行处理完毕后报盘发回的通知
	typedef int (WPCTP *FP_OnRtnRepealFromFutureToBankByFutureManual)(CThostFtdcRspRepealField *pRspRepeal);
	void *OnRtnRepealFromFutureToBankByFutureManual_;
	virtual void OnRtnRepealFromFutureToBankByFutureManual(CThostFtdcRspRepealField *pRspRepeal){ if(OnRtnRepealFromFutureToBankByFutureManual_) ((FP_OnRtnRepealFromFutureToBankByFutureManual)OnRtnRepealFromFutureToBankByFutureManual_)(pRspRepeal); }
    
	// 期货发起查询银行余额通知
	typedef int (WPCTP *FP_OnRtnQueryBankBalanceByFuture)(CThostFtdcNotifyQueryAccountField *pNotifyQueryAccount);
	void *OnRtnQueryBankBalanceByFuture_;
	virtual void OnRtnQueryBankBalanceByFuture(CThostFtdcNotifyQueryAccountField *pNotifyQueryAccount){ if(OnRtnQueryBankBalanceByFuture_) ((FP_OnRtnQueryBankBalanceByFuture)OnRtnQueryBankBalanceByFuture_)(pNotifyQueryAccount); }
    
	// 期货发起银行资金转期货错误回报
	typedef int (WPCTP *FP_OnErrRtnBankToFutureByFuture)(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo);
	void *OnErrRtnBankToFutureByFuture_;
	virtual void OnErrRtnBankToFutureByFuture(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo){ if(OnErrRtnBankToFutureByFuture_) ((FP_OnErrRtnBankToFutureByFuture)OnErrRtnBankToFutureByFuture_)(pReqTransfer, pRspInfo); }
    
	// 期货发起期货资金转银行错误回报
	typedef int (WPCTP *FP_OnErrRtnFutureToBankByFuture)(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo);
	void *OnErrRtnFutureToBankByFuture_;
	virtual void OnErrRtnFutureToBankByFuture(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo){ if(OnErrRtnFutureToBankByFuture_) ((FP_OnErrRtnFutureToBankByFuture)OnErrRtnFutureToBankByFuture_)(pReqTransfer, pRspInfo); }
    
	// 系统运行时期货端手工发起冲正银行转期货错误回报
	typedef int (WPCTP *FP_OnErrRtnRepealBankToFutureByFutureManual)(CThostFtdcReqRepealField *pReqRepeal, CThostFtdcRspInfoField *pRspInfo);
	void *OnErrRtnRepealBankToFutureByFutureManual_;
	virtual void OnErrRtnRepealBankToFutureByFutureManual(CThostFtdcReqRepealField *pReqRepeal, CThostFtdcRspInfoField *pRspInfo){ if(OnErrRtnRepealBankToFutureByFutureManual_) ((FP_OnErrRtnRepealBankToFutureByFutureManual)OnErrRtnRepealBankToFutureByFutureManual_)(pReqRepeal, pRspInfo); }
    
	// 系统运行时期货端手工发起冲正期货转银行错误回报
	typedef int (WPCTP *FP_OnErrRtnRepealFutureToBankByFutureManual)(CThostFtdcReqRepealField *pReqRepeal, CThostFtdcRspInfoField *pRspInfo);
	void *OnErrRtnRepealFutureToBankByFutureManual_;
	virtual void OnErrRtnRepealFutureToBankByFutureManual(CThostFtdcReqRepealField *pReqRepeal, CThostFtdcRspInfoField *pRspInfo){ if(OnErrRtnRepealFutureToBankByFutureManual_) ((FP_OnErrRtnRepealFutureToBankByFutureManual)OnErrRtnRepealFutureToBankByFutureManual_)(pReqRepeal, pRspInfo); }
    
	// 期货发起查询银行余额错误回报
	typedef int (WPCTP *FP_OnErrRtnQueryBankBalanceByFuture)(CThostFtdcReqQueryAccountField *pReqQueryAccount, CThostFtdcRspInfoField *pRspInfo);
	void *OnErrRtnQueryBankBalanceByFuture_;
	virtual void OnErrRtnQueryBankBalanceByFuture(CThostFtdcReqQueryAccountField *pReqQueryAccount, CThostFtdcRspInfoField *pRspInfo){ if(OnErrRtnQueryBankBalanceByFuture_) ((FP_OnErrRtnQueryBankBalanceByFuture)OnErrRtnQueryBankBalanceByFuture_)(pReqQueryAccount, pRspInfo); }
    
	// 期货发起冲正银行转期货请求，银行处理完毕后报盘发回的通知
	typedef int (WPCTP *FP_OnRtnRepealFromBankToFutureByFuture)(CThostFtdcRspRepealField *pRspRepeal);
	void *OnRtnRepealFromBankToFutureByFuture_;
	virtual void OnRtnRepealFromBankToFutureByFuture(CThostFtdcRspRepealField *pRspRepeal){ if(OnRtnRepealFromBankToFutureByFuture_) ((FP_OnRtnRepealFromBankToFutureByFuture)OnRtnRepealFromBankToFutureByFuture_)(pRspRepeal); }
    
	// 期货发起冲正期货转银行请求，银行处理完毕后报盘发回的通知
	typedef int (WPCTP *FP_OnRtnRepealFromFutureToBankByFuture)(CThostFtdcRspRepealField *pRspRepeal);
	void *OnRtnRepealFromFutureToBankByFuture_;
	virtual void OnRtnRepealFromFutureToBankByFuture(CThostFtdcRspRepealField *pRspRepeal){ if(OnRtnRepealFromFutureToBankByFuture_) ((FP_OnRtnRepealFromFutureToBankByFuture)OnRtnRepealFromFutureToBankByFuture_)(pRspRepeal); }
    
	// 期货发起银行资金转期货应答
	typedef int (WPCTP *FP_OnRspFromBankToFutureByFuture)(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspFromBankToFutureByFuture_;
	virtual void OnRspFromBankToFutureByFuture(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspFromBankToFutureByFuture_) ((FP_OnRspFromBankToFutureByFuture)OnRspFromBankToFutureByFuture_)(pReqTransfer, pRspInfo, nRequestID, bIsLast); }
    
	// 期货发起期货资金转银行应答
	typedef int (WPCTP *FP_OnRspFromFutureToBankByFuture)(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspFromFutureToBankByFuture_;
	virtual void OnRspFromFutureToBankByFuture(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspFromFutureToBankByFuture_) ((FP_OnRspFromFutureToBankByFuture)OnRspFromFutureToBankByFuture_)(pReqTransfer, pRspInfo, nRequestID, bIsLast); }
    
	// 期货发起查询银行余额应答
	typedef int (WPCTP *FP_OnRspQueryBankAccountMoneyByFuture)(CThostFtdcReqQueryAccountField *pReqQueryAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQueryBankAccountMoneyByFuture_;
	virtual void OnRspQueryBankAccountMoneyByFuture(CThostFtdcReqQueryAccountField *pReqQueryAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQueryBankAccountMoneyByFuture_) ((FP_OnRspQueryBankAccountMoneyByFuture)OnRspQueryBankAccountMoneyByFuture_)(pReqQueryAccount, pRspInfo, nRequestID, bIsLast); }
    
	// 银行发起银期开户通知
	typedef int (WPCTP *FP_OnRtnOpenAccountByBank)(CThostFtdcOpenAccountField *pOpenAccount);
	void *OnRtnOpenAccountByBank_;
	virtual void OnRtnOpenAccountByBank(CThostFtdcOpenAccountField *pOpenAccount){ if(OnRtnOpenAccountByBank_) ((FP_OnRtnOpenAccountByBank)OnRtnOpenAccountByBank_)(pOpenAccount); }
    
	// 银行发起银期销户通知
	typedef int (WPCTP *FP_OnRtnCancelAccountByBank)(CThostFtdcCancelAccountField *pCancelAccount);
	void *OnRtnCancelAccountByBank_;
	virtual void OnRtnCancelAccountByBank(CThostFtdcCancelAccountField *pCancelAccount){ if(OnRtnCancelAccountByBank_) ((FP_OnRtnCancelAccountByBank)OnRtnCancelAccountByBank_)(pCancelAccount); }
    
	// 银行发起变更银行账号通知
	typedef int (WPCTP *FP_OnRtnChangeAccountByBank)(CThostFtdcChangeAccountField *pChangeAccount);
	void *OnRtnChangeAccountByBank_;
	virtual void OnRtnChangeAccountByBank(CThostFtdcChangeAccountField *pChangeAccount){ if(OnRtnChangeAccountByBank_) ((FP_OnRtnChangeAccountByBank)OnRtnChangeAccountByBank_)(pChangeAccount); }
    
	// 请求查询分类合约响应
	typedef int (WPCTP *FP_OnRspQryClassifiedInstrument)(CThostFtdcInstrumentField *pInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryClassifiedInstrument_;
	virtual void OnRspQryClassifiedInstrument(CThostFtdcInstrumentField *pInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryClassifiedInstrument_) ((FP_OnRspQryClassifiedInstrument)OnRspQryClassifiedInstrument_)(pInstrument, pRspInfo, nRequestID, bIsLast); }
    
	// 请求组合优惠比例响应
	typedef int (WPCTP *FP_OnRspQryCombPromotionParam)(CThostFtdcCombPromotionParamField *pCombPromotionParam, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryCombPromotionParam_;
	virtual void OnRspQryCombPromotionParam(CThostFtdcCombPromotionParamField *pCombPromotionParam, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryCombPromotionParam_) ((FP_OnRspQryCombPromotionParam)OnRspQryCombPromotionParam_)(pCombPromotionParam, pRspInfo, nRequestID, bIsLast); }
    
	// 投资者风险结算持仓查询响应
	typedef int (WPCTP *FP_OnRspQryRiskSettleInvstPosition)(CThostFtdcRiskSettleInvstPositionField *pRiskSettleInvstPosition, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryRiskSettleInvstPosition_;
	virtual void OnRspQryRiskSettleInvstPosition(CThostFtdcRiskSettleInvstPositionField *pRiskSettleInvstPosition, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryRiskSettleInvstPosition_) ((FP_OnRspQryRiskSettleInvstPosition)OnRspQryRiskSettleInvstPosition_)(pRiskSettleInvstPosition, pRspInfo, nRequestID, bIsLast); }
    
	// 风险结算产品查询响应
	typedef int (WPCTP *FP_OnRspQryRiskSettleProductStatus)(CThostFtdcRiskSettleProductStatusField *pRiskSettleProductStatus, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryRiskSettleProductStatus_;
	virtual void OnRspQryRiskSettleProductStatus(CThostFtdcRiskSettleProductStatusField *pRiskSettleProductStatus, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryRiskSettleProductStatus_) ((FP_OnRspQryRiskSettleProductStatus)OnRspQryRiskSettleProductStatus_)(pRiskSettleProductStatus, pRspInfo, nRequestID, bIsLast); }
    
	// SPBM期货合约参数查询响应
	typedef int (WPCTP *FP_OnRspQrySPBMFutureParameter)(CThostFtdcSPBMFutureParameterField *pSPBMFutureParameter, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQrySPBMFutureParameter_;
	virtual void OnRspQrySPBMFutureParameter(CThostFtdcSPBMFutureParameterField *pSPBMFutureParameter, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQrySPBMFutureParameter_) ((FP_OnRspQrySPBMFutureParameter)OnRspQrySPBMFutureParameter_)(pSPBMFutureParameter, pRspInfo, nRequestID, bIsLast); }
    
	// SPBM期权合约参数查询响应
	typedef int (WPCTP *FP_OnRspQrySPBMOptionParameter)(CThostFtdcSPBMOptionParameterField *pSPBMOptionParameter, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQrySPBMOptionParameter_;
	virtual void OnRspQrySPBMOptionParameter(CThostFtdcSPBMOptionParameterField *pSPBMOptionParameter, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQrySPBMOptionParameter_) ((FP_OnRspQrySPBMOptionParameter)OnRspQrySPBMOptionParameter_)(pSPBMOptionParameter, pRspInfo, nRequestID, bIsLast); }
    
	// SPBM品种内对锁仓折扣参数查询响应
	typedef int (WPCTP *FP_OnRspQrySPBMIntraParameter)(CThostFtdcSPBMIntraParameterField *pSPBMIntraParameter, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQrySPBMIntraParameter_;
	virtual void OnRspQrySPBMIntraParameter(CThostFtdcSPBMIntraParameterField *pSPBMIntraParameter, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQrySPBMIntraParameter_) ((FP_OnRspQrySPBMIntraParameter)OnRspQrySPBMIntraParameter_)(pSPBMIntraParameter, pRspInfo, nRequestID, bIsLast); }
    
	// SPBM跨品种抵扣参数查询响应
	typedef int (WPCTP *FP_OnRspQrySPBMInterParameter)(CThostFtdcSPBMInterParameterField *pSPBMInterParameter, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQrySPBMInterParameter_;
	virtual void OnRspQrySPBMInterParameter(CThostFtdcSPBMInterParameterField *pSPBMInterParameter, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQrySPBMInterParameter_) ((FP_OnRspQrySPBMInterParameter)OnRspQrySPBMInterParameter_)(pSPBMInterParameter, pRspInfo, nRequestID, bIsLast); }
    
	// SPBM组合保证金套餐查询响应
	typedef int (WPCTP *FP_OnRspQrySPBMPortfDefinition)(CThostFtdcSPBMPortfDefinitionField *pSPBMPortfDefinition, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQrySPBMPortfDefinition_;
	virtual void OnRspQrySPBMPortfDefinition(CThostFtdcSPBMPortfDefinitionField *pSPBMPortfDefinition, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQrySPBMPortfDefinition_) ((FP_OnRspQrySPBMPortfDefinition)OnRspQrySPBMPortfDefinition_)(pSPBMPortfDefinition, pRspInfo, nRequestID, bIsLast); }
    
	// 投资者SPBM套餐选择查询响应
	typedef int (WPCTP *FP_OnRspQrySPBMInvestorPortfDef)(CThostFtdcSPBMInvestorPortfDefField *pSPBMInvestorPortfDef, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQrySPBMInvestorPortfDef_;
	virtual void OnRspQrySPBMInvestorPortfDef(CThostFtdcSPBMInvestorPortfDefField *pSPBMInvestorPortfDef, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQrySPBMInvestorPortfDef_) ((FP_OnRspQrySPBMInvestorPortfDef)OnRspQrySPBMInvestorPortfDef_)(pSPBMInvestorPortfDef, pRspInfo, nRequestID, bIsLast); }
    
	// 投资者新型组合保证金系数查询响应
	typedef int (WPCTP *FP_OnRspQryInvestorPortfMarginRatio)(CThostFtdcInvestorPortfMarginRatioField *pInvestorPortfMarginRatio, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryInvestorPortfMarginRatio_;
	virtual void OnRspQryInvestorPortfMarginRatio(CThostFtdcInvestorPortfMarginRatioField *pInvestorPortfMarginRatio, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryInvestorPortfMarginRatio_) ((FP_OnRspQryInvestorPortfMarginRatio)OnRspQryInvestorPortfMarginRatio_)(pInvestorPortfMarginRatio, pRspInfo, nRequestID, bIsLast); }
    
	// 投资者产品SPBM明细查询响应
	typedef int (WPCTP *FP_OnRspQryInvestorProdSPBMDetail)(CThostFtdcInvestorProdSPBMDetailField *pInvestorProdSPBMDetail, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *OnRspQryInvestorProdSPBMDetail_;
	virtual void OnRspQryInvestorProdSPBMDetail(CThostFtdcInvestorProdSPBMDetailField *pInvestorProdSPBMDetail, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast){ if(OnRspQryInvestorProdSPBMDetail_) ((FP_OnRspQryInvestorProdSPBMDetail)OnRspQryInvestorProdSPBMDetail_)(pInvestorProdSPBMDetail, pRspInfo, nRequestID, bIsLast); }
    
};

DLL_EXPORT_C_DECL void* WPCTP tCreateApi(const char *pszFlowPath);
DLL_EXPORT_C_DECL void* WPCTP tCreateSpi();
DLL_EXPORT_C_DECL void* WPCTP tGetApiVersion();
DLL_EXPORT_C_DECL void* WPCTP tGetTradingDay(CThostFtdcTraderApi *api);

// 当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。
DLL_EXPORT_C_DECL void WPCTP tOnFrontConnected(Trade* spi, void* func);

// 当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。
DLL_EXPORT_C_DECL void WPCTP tOnFrontDisconnected(Trade* spi, void* func);

// 心跳超时警告。当长时间未收到报文时，该方法被调用。
DLL_EXPORT_C_DECL void WPCTP tOnHeartBeatWarning(Trade* spi, void* func);

// 客户端认证响应
DLL_EXPORT_C_DECL void WPCTP tOnRspAuthenticate(Trade* spi, void* func);

// 登录请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspUserLogin(Trade* spi, void* func);

// 登出请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspUserLogout(Trade* spi, void* func);

// 用户口令更新请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspUserPasswordUpdate(Trade* spi, void* func);

// 资金账户口令更新请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspTradingAccountPasswordUpdate(Trade* spi, void* func);

// 查询用户当前支持的认证模式的回复
DLL_EXPORT_C_DECL void WPCTP tOnRspUserAuthMethod(Trade* spi, void* func);

// 获取图形验证码请求的回复
DLL_EXPORT_C_DECL void WPCTP tOnRspGenUserCaptcha(Trade* spi, void* func);

// 获取短信验证码请求的回复
DLL_EXPORT_C_DECL void WPCTP tOnRspGenUserText(Trade* spi, void* func);

// 报单录入请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspOrderInsert(Trade* spi, void* func);

// 预埋单录入请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspParkedOrderInsert(Trade* spi, void* func);

// 预埋撤单录入请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspParkedOrderAction(Trade* spi, void* func);

// 报单操作请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspOrderAction(Trade* spi, void* func);

// 查询最大报单数量响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryMaxOrderVolume(Trade* spi, void* func);

// 投资者结算结果确认响应
DLL_EXPORT_C_DECL void WPCTP tOnRspSettlementInfoConfirm(Trade* spi, void* func);

// 删除预埋单响应
DLL_EXPORT_C_DECL void WPCTP tOnRspRemoveParkedOrder(Trade* spi, void* func);

// 删除预埋撤单响应
DLL_EXPORT_C_DECL void WPCTP tOnRspRemoveParkedOrderAction(Trade* spi, void* func);

// 执行宣告录入请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspExecOrderInsert(Trade* spi, void* func);

// 执行宣告操作请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspExecOrderAction(Trade* spi, void* func);

// 询价录入请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspForQuoteInsert(Trade* spi, void* func);

// 报价录入请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQuoteInsert(Trade* spi, void* func);

// 报价操作请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQuoteAction(Trade* spi, void* func);

// 批量报单操作请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspBatchOrderAction(Trade* spi, void* func);

// 期权自对冲录入请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspOptionSelfCloseInsert(Trade* spi, void* func);

// 期权自对冲操作请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspOptionSelfCloseAction(Trade* spi, void* func);

// 申请组合录入请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspCombActionInsert(Trade* spi, void* func);

// 请求查询报单响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryOrder(Trade* spi, void* func);

// 请求查询成交响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryTrade(Trade* spi, void* func);

// 请求查询投资者持仓响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryInvestorPosition(Trade* spi, void* func);

// 请求查询资金账户响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryTradingAccount(Trade* spi, void* func);

// 请求查询投资者响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryInvestor(Trade* spi, void* func);

// 请求查询交易编码响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryTradingCode(Trade* spi, void* func);

// 请求查询合约保证金率响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryInstrumentMarginRate(Trade* spi, void* func);

// 请求查询合约手续费率响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryInstrumentCommissionRate(Trade* spi, void* func);

// 请求查询交易所响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryExchange(Trade* spi, void* func);

// 请求查询产品响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryProduct(Trade* spi, void* func);

// 请求查询合约响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryInstrument(Trade* spi, void* func);

// 请求查询行情响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryDepthMarketData(Trade* spi, void* func);

// 请求查询交易员报盘机响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryTraderOffer(Trade* spi, void* func);

// 请求查询投资者结算结果响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQrySettlementInfo(Trade* spi, void* func);

// 请求查询转帐银行响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryTransferBank(Trade* spi, void* func);

// 请求查询投资者持仓明细响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryInvestorPositionDetail(Trade* spi, void* func);

// 请求查询客户通知响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryNotice(Trade* spi, void* func);

// 请求查询结算信息确认响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQrySettlementInfoConfirm(Trade* spi, void* func);

// 请求查询投资者持仓明细响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryInvestorPositionCombineDetail(Trade* spi, void* func);

// 查询保证金监管系统经纪公司资金账户密钥响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryCFMMCTradingAccountKey(Trade* spi, void* func);

// 请求查询仓单折抵信息响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryEWarrantOffset(Trade* spi, void* func);

// 请求查询投资者品种/跨品种保证金响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryInvestorProductGroupMargin(Trade* spi, void* func);

// 请求查询交易所保证金率响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryExchangeMarginRate(Trade* spi, void* func);

// 请求查询交易所调整保证金率响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryExchangeMarginRateAdjust(Trade* spi, void* func);

// 请求查询汇率响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryExchangeRate(Trade* spi, void* func);

// 请求查询二级代理操作员银期权限响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQrySecAgentACIDMap(Trade* spi, void* func);

// 请求查询产品报价汇率
DLL_EXPORT_C_DECL void WPCTP tOnRspQryProductExchRate(Trade* spi, void* func);

// 请求查询产品组
DLL_EXPORT_C_DECL void WPCTP tOnRspQryProductGroup(Trade* spi, void* func);

// 请求查询做市商合约手续费率响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryMMInstrumentCommissionRate(Trade* spi, void* func);

// 请求查询做市商期权合约手续费响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryMMOptionInstrCommRate(Trade* spi, void* func);

// 请求查询报单手续费响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryInstrumentOrderCommRate(Trade* spi, void* func);

// 请求查询资金账户响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQrySecAgentTradingAccount(Trade* spi, void* func);

// 请求查询二级代理商资金校验模式响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQrySecAgentCheckMode(Trade* spi, void* func);

// 请求查询二级代理商信息响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQrySecAgentTradeInfo(Trade* spi, void* func);

// 请求查询期权交易成本响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryOptionInstrTradeCost(Trade* spi, void* func);

// 请求查询期权合约手续费响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryOptionInstrCommRate(Trade* spi, void* func);

// 请求查询执行宣告响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryExecOrder(Trade* spi, void* func);

// 请求查询询价响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryForQuote(Trade* spi, void* func);

// 请求查询报价响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryQuote(Trade* spi, void* func);

// 请求查询期权自对冲响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryOptionSelfClose(Trade* spi, void* func);

// 请求查询投资单元响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryInvestUnit(Trade* spi, void* func);

// 请求查询组合合约安全系数响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryCombInstrumentGuard(Trade* spi, void* func);

// 请求查询申请组合响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryCombAction(Trade* spi, void* func);

// 请求查询转帐流水响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryTransferSerial(Trade* spi, void* func);

// 请求查询银期签约关系响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryAccountregister(Trade* spi, void* func);

// 错误应答
DLL_EXPORT_C_DECL void WPCTP tOnRspError(Trade* spi, void* func);

// 报单通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnOrder(Trade* spi, void* func);

// 成交通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnTrade(Trade* spi, void* func);

// 报单录入错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnOrderInsert(Trade* spi, void* func);

// 报单操作错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnOrderAction(Trade* spi, void* func);

// 合约交易状态通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnInstrumentStatus(Trade* spi, void* func);

// 交易所公告通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnBulletin(Trade* spi, void* func);

// 交易通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnTradingNotice(Trade* spi, void* func);

// 提示条件单校验错误
DLL_EXPORT_C_DECL void WPCTP tOnRtnErrorConditionalOrder(Trade* spi, void* func);

// 执行宣告通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnExecOrder(Trade* spi, void* func);

// 执行宣告录入错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnExecOrderInsert(Trade* spi, void* func);

// 执行宣告操作错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnExecOrderAction(Trade* spi, void* func);

// 询价录入错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnForQuoteInsert(Trade* spi, void* func);

// 报价通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnQuote(Trade* spi, void* func);

// 报价录入错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnQuoteInsert(Trade* spi, void* func);

// 报价操作错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnQuoteAction(Trade* spi, void* func);

// 询价通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnForQuoteRsp(Trade* spi, void* func);

// 保证金监控中心用户令牌
DLL_EXPORT_C_DECL void WPCTP tOnRtnCFMMCTradingAccountToken(Trade* spi, void* func);

// 批量报单操作错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnBatchOrderAction(Trade* spi, void* func);

// 期权自对冲通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnOptionSelfClose(Trade* spi, void* func);

// 期权自对冲录入错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnOptionSelfCloseInsert(Trade* spi, void* func);

// 期权自对冲操作错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnOptionSelfCloseAction(Trade* spi, void* func);

// 申请组合通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnCombAction(Trade* spi, void* func);

// 申请组合录入错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnCombActionInsert(Trade* spi, void* func);

// 请求查询签约银行响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryContractBank(Trade* spi, void* func);

// 请求查询预埋单响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryParkedOrder(Trade* spi, void* func);

// 请求查询预埋撤单响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryParkedOrderAction(Trade* spi, void* func);

// 请求查询交易通知响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryTradingNotice(Trade* spi, void* func);

// 请求查询经纪公司交易参数响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryBrokerTradingParams(Trade* spi, void* func);

// 请求查询经纪公司交易算法响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryBrokerTradingAlgos(Trade* spi, void* func);

// 请求查询监控中心用户令牌
DLL_EXPORT_C_DECL void WPCTP tOnRspQueryCFMMCTradingAccountToken(Trade* spi, void* func);

// 银行发起银行资金转期货通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnFromBankToFutureByBank(Trade* spi, void* func);

// 银行发起期货资金转银行通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnFromFutureToBankByBank(Trade* spi, void* func);

// 银行发起冲正银行转期货通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnRepealFromBankToFutureByBank(Trade* spi, void* func);

// 银行发起冲正期货转银行通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnRepealFromFutureToBankByBank(Trade* spi, void* func);

// 期货发起银行资金转期货通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnFromBankToFutureByFuture(Trade* spi, void* func);

// 期货发起期货资金转银行通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnFromFutureToBankByFuture(Trade* spi, void* func);

// 系统运行时期货端手工发起冲正银行转期货请求，银行处理完毕后报盘发回的通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnRepealFromBankToFutureByFutureManual(Trade* spi, void* func);

// 系统运行时期货端手工发起冲正期货转银行请求，银行处理完毕后报盘发回的通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnRepealFromFutureToBankByFutureManual(Trade* spi, void* func);

// 期货发起查询银行余额通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnQueryBankBalanceByFuture(Trade* spi, void* func);

// 期货发起银行资金转期货错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnBankToFutureByFuture(Trade* spi, void* func);

// 期货发起期货资金转银行错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnFutureToBankByFuture(Trade* spi, void* func);

// 系统运行时期货端手工发起冲正银行转期货错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnRepealBankToFutureByFutureManual(Trade* spi, void* func);

// 系统运行时期货端手工发起冲正期货转银行错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnRepealFutureToBankByFutureManual(Trade* spi, void* func);

// 期货发起查询银行余额错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnQueryBankBalanceByFuture(Trade* spi, void* func);

// 期货发起冲正银行转期货请求，银行处理完毕后报盘发回的通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnRepealFromBankToFutureByFuture(Trade* spi, void* func);

// 期货发起冲正期货转银行请求，银行处理完毕后报盘发回的通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnRepealFromFutureToBankByFuture(Trade* spi, void* func);

// 期货发起银行资金转期货应答
DLL_EXPORT_C_DECL void WPCTP tOnRspFromBankToFutureByFuture(Trade* spi, void* func);

// 期货发起期货资金转银行应答
DLL_EXPORT_C_DECL void WPCTP tOnRspFromFutureToBankByFuture(Trade* spi, void* func);

// 期货发起查询银行余额应答
DLL_EXPORT_C_DECL void WPCTP tOnRspQueryBankAccountMoneyByFuture(Trade* spi, void* func);

// 银行发起银期开户通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnOpenAccountByBank(Trade* spi, void* func);

// 银行发起银期销户通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnCancelAccountByBank(Trade* spi, void* func);

// 银行发起变更银行账号通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnChangeAccountByBank(Trade* spi, void* func);

// 请求查询分类合约响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryClassifiedInstrument(Trade* spi, void* func);

// 请求组合优惠比例响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryCombPromotionParam(Trade* spi, void* func);

// 投资者风险结算持仓查询响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryRiskSettleInvstPosition(Trade* spi, void* func);

// 风险结算产品查询响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryRiskSettleProductStatus(Trade* spi, void* func);

// SPBM期货合约参数查询响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQrySPBMFutureParameter(Trade* spi, void* func);

// SPBM期权合约参数查询响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQrySPBMOptionParameter(Trade* spi, void* func);

// SPBM品种内对锁仓折扣参数查询响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQrySPBMIntraParameter(Trade* spi, void* func);

// SPBM跨品种抵扣参数查询响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQrySPBMInterParameter(Trade* spi, void* func);

// SPBM组合保证金套餐查询响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQrySPBMPortfDefinition(Trade* spi, void* func);

// 投资者SPBM套餐选择查询响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQrySPBMInvestorPortfDef(Trade* spi, void* func);

// 投资者新型组合保证金系数查询响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryInvestorPortfMarginRatio(Trade* spi, void* func);

// 投资者产品SPBM明细查询响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryInvestorProdSPBMDetail(Trade* spi, void* func);


// 创建TraderApi
DLL_EXPORT_C_DECL void WPCTP tRelease(CThostFtdcTraderApi *api);

// 初始化
DLL_EXPORT_C_DECL void WPCTP tInit(CThostFtdcTraderApi *api);

// 等待接口线程结束运行
DLL_EXPORT_C_DECL int WPCTP tJoin(CThostFtdcTraderApi *api);

// 注册前置机网络地址
DLL_EXPORT_C_DECL void WPCTP tRegisterFront(CThostFtdcTraderApi *api, char *pszFrontAddress);

// @remark RegisterNameServer优先于RegisterFront
DLL_EXPORT_C_DECL void WPCTP tRegisterNameServer(CThostFtdcTraderApi *api, char *pszNsAddress);

// 注册名字服务器用户信息
DLL_EXPORT_C_DECL void WPCTP tRegisterFensUserInfo(CThostFtdcTraderApi *api, CThostFtdcFensUserInfoField * pFensUserInfo);

// 注册回调接口
DLL_EXPORT_C_DECL void WPCTP tRegisterSpi(CThostFtdcTraderApi *api, CThostFtdcTraderSpi *pSpi);

// 订阅私有流。
DLL_EXPORT_C_DECL void WPCTP tSubscribePrivateTopic(CThostFtdcTraderApi *api, THOST_TE_RESUME_TYPE nResumeType);

// 订阅公共流。
DLL_EXPORT_C_DECL void WPCTP tSubscribePublicTopic(CThostFtdcTraderApi *api, THOST_TE_RESUME_TYPE nResumeType);

// 客户端认证请求
DLL_EXPORT_C_DECL int WPCTP tReqAuthenticate(CThostFtdcTraderApi *api, CThostFtdcReqAuthenticateField *pReqAuthenticateField, int nRequestID);

// 注册用户终端信息，用于中继服务器多连接模式
DLL_EXPORT_C_DECL int WPCTP tRegisterUserSystemInfo(CThostFtdcTraderApi *api, CThostFtdcUserSystemInfoField *pUserSystemInfo);

// 上报用户终端信息，用于中继服务器操作员登录模式
DLL_EXPORT_C_DECL int WPCTP tSubmitUserSystemInfo(CThostFtdcTraderApi *api, CThostFtdcUserSystemInfoField *pUserSystemInfo);

// 用户登录请求
DLL_EXPORT_C_DECL int WPCTP tReqUserLogin(CThostFtdcTraderApi *api, CThostFtdcReqUserLoginField *pReqUserLoginField, int nRequestID);

// 登出请求
DLL_EXPORT_C_DECL int WPCTP tReqUserLogout(CThostFtdcTraderApi *api, CThostFtdcUserLogoutField *pUserLogout, int nRequestID);

// 用户口令更新请求
DLL_EXPORT_C_DECL int WPCTP tReqUserPasswordUpdate(CThostFtdcTraderApi *api, CThostFtdcUserPasswordUpdateField *pUserPasswordUpdate, int nRequestID);

// 资金账户口令更新请求
DLL_EXPORT_C_DECL int WPCTP tReqTradingAccountPasswordUpdate(CThostFtdcTraderApi *api, CThostFtdcTradingAccountPasswordUpdateField *pTradingAccountPasswordUpdate, int nRequestID);

// 查询用户当前支持的认证模式
DLL_EXPORT_C_DECL int WPCTP tReqUserAuthMethod(CThostFtdcTraderApi *api, CThostFtdcReqUserAuthMethodField *pReqUserAuthMethod, int nRequestID);

// 用户发出获取图形验证码请求
DLL_EXPORT_C_DECL int WPCTP tReqGenUserCaptcha(CThostFtdcTraderApi *api, CThostFtdcReqGenUserCaptchaField *pReqGenUserCaptcha, int nRequestID);

// 用户发出获取短信验证码请求
DLL_EXPORT_C_DECL int WPCTP tReqGenUserText(CThostFtdcTraderApi *api, CThostFtdcReqGenUserTextField *pReqGenUserText, int nRequestID);

// 用户发出带有图片验证码的登陆请求
DLL_EXPORT_C_DECL int WPCTP tReqUserLoginWithCaptcha(CThostFtdcTraderApi *api, CThostFtdcReqUserLoginWithCaptchaField *pReqUserLoginWithCaptcha, int nRequestID);

// 用户发出带有短信验证码的登陆请求
DLL_EXPORT_C_DECL int WPCTP tReqUserLoginWithText(CThostFtdcTraderApi *api, CThostFtdcReqUserLoginWithTextField *pReqUserLoginWithText, int nRequestID);

// 用户发出带有动态口令的登陆请求
DLL_EXPORT_C_DECL int WPCTP tReqUserLoginWithOTP(CThostFtdcTraderApi *api, CThostFtdcReqUserLoginWithOTPField *pReqUserLoginWithOTP, int nRequestID);

// 报单录入请求
DLL_EXPORT_C_DECL int WPCTP tReqOrderInsert(CThostFtdcTraderApi *api, CThostFtdcInputOrderField *pInputOrder, int nRequestID);

// 预埋单录入请求
DLL_EXPORT_C_DECL int WPCTP tReqParkedOrderInsert(CThostFtdcTraderApi *api, CThostFtdcParkedOrderField *pParkedOrder, int nRequestID);

// 预埋撤单录入请求
DLL_EXPORT_C_DECL int WPCTP tReqParkedOrderAction(CThostFtdcTraderApi *api, CThostFtdcParkedOrderActionField *pParkedOrderAction, int nRequestID);

// 报单操作请求
DLL_EXPORT_C_DECL int WPCTP tReqOrderAction(CThostFtdcTraderApi *api, CThostFtdcInputOrderActionField *pInputOrderAction, int nRequestID);

// 查询最大报单数量请求
DLL_EXPORT_C_DECL int WPCTP tReqQryMaxOrderVolume(CThostFtdcTraderApi *api, CThostFtdcQryMaxOrderVolumeField *pQryMaxOrderVolume, int nRequestID);

// 投资者结算结果确认
DLL_EXPORT_C_DECL int WPCTP tReqSettlementInfoConfirm(CThostFtdcTraderApi *api, CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, int nRequestID);

// 请求删除预埋单
DLL_EXPORT_C_DECL int WPCTP tReqRemoveParkedOrder(CThostFtdcTraderApi *api, CThostFtdcRemoveParkedOrderField *pRemoveParkedOrder, int nRequestID);

// 请求删除预埋撤单
DLL_EXPORT_C_DECL int WPCTP tReqRemoveParkedOrderAction(CThostFtdcTraderApi *api, CThostFtdcRemoveParkedOrderActionField *pRemoveParkedOrderAction, int nRequestID);

// 执行宣告录入请求
DLL_EXPORT_C_DECL int WPCTP tReqExecOrderInsert(CThostFtdcTraderApi *api, CThostFtdcInputExecOrderField *pInputExecOrder, int nRequestID);

// 执行宣告操作请求
DLL_EXPORT_C_DECL int WPCTP tReqExecOrderAction(CThostFtdcTraderApi *api, CThostFtdcInputExecOrderActionField *pInputExecOrderAction, int nRequestID);

// 询价录入请求
DLL_EXPORT_C_DECL int WPCTP tReqForQuoteInsert(CThostFtdcTraderApi *api, CThostFtdcInputForQuoteField *pInputForQuote, int nRequestID);

// 报价录入请求
DLL_EXPORT_C_DECL int WPCTP tReqQuoteInsert(CThostFtdcTraderApi *api, CThostFtdcInputQuoteField *pInputQuote, int nRequestID);

// 报价操作请求
DLL_EXPORT_C_DECL int WPCTP tReqQuoteAction(CThostFtdcTraderApi *api, CThostFtdcInputQuoteActionField *pInputQuoteAction, int nRequestID);

// 批量报单操作请求
DLL_EXPORT_C_DECL int WPCTP tReqBatchOrderAction(CThostFtdcTraderApi *api, CThostFtdcInputBatchOrderActionField *pInputBatchOrderAction, int nRequestID);

// 期权自对冲录入请求
DLL_EXPORT_C_DECL int WPCTP tReqOptionSelfCloseInsert(CThostFtdcTraderApi *api, CThostFtdcInputOptionSelfCloseField *pInputOptionSelfClose, int nRequestID);

// 期权自对冲操作请求
DLL_EXPORT_C_DECL int WPCTP tReqOptionSelfCloseAction(CThostFtdcTraderApi *api, CThostFtdcInputOptionSelfCloseActionField *pInputOptionSelfCloseAction, int nRequestID);

// 申请组合录入请求
DLL_EXPORT_C_DECL int WPCTP tReqCombActionInsert(CThostFtdcTraderApi *api, CThostFtdcInputCombActionField *pInputCombAction, int nRequestID);

// 请求查询报单
DLL_EXPORT_C_DECL int WPCTP tReqQryOrder(CThostFtdcTraderApi *api, CThostFtdcQryOrderField *pQryOrder, int nRequestID);

// 请求查询成交
DLL_EXPORT_C_DECL int WPCTP tReqQryTrade(CThostFtdcTraderApi *api, CThostFtdcQryTradeField *pQryTrade, int nRequestID);

// 请求查询投资者持仓
DLL_EXPORT_C_DECL int WPCTP tReqQryInvestorPosition(CThostFtdcTraderApi *api, CThostFtdcQryInvestorPositionField *pQryInvestorPosition, int nRequestID);

// 请求查询资金账户
DLL_EXPORT_C_DECL int WPCTP tReqQryTradingAccount(CThostFtdcTraderApi *api, CThostFtdcQryTradingAccountField *pQryTradingAccount, int nRequestID);

// 请求查询投资者
DLL_EXPORT_C_DECL int WPCTP tReqQryInvestor(CThostFtdcTraderApi *api, CThostFtdcQryInvestorField *pQryInvestor, int nRequestID);

// 请求查询交易编码
DLL_EXPORT_C_DECL int WPCTP tReqQryTradingCode(CThostFtdcTraderApi *api, CThostFtdcQryTradingCodeField *pQryTradingCode, int nRequestID);

// 请求查询合约保证金率
DLL_EXPORT_C_DECL int WPCTP tReqQryInstrumentMarginRate(CThostFtdcTraderApi *api, CThostFtdcQryInstrumentMarginRateField *pQryInstrumentMarginRate, int nRequestID);

// 请求查询合约手续费率
DLL_EXPORT_C_DECL int WPCTP tReqQryInstrumentCommissionRate(CThostFtdcTraderApi *api, CThostFtdcQryInstrumentCommissionRateField *pQryInstrumentCommissionRate, int nRequestID);

// 请求查询交易所
DLL_EXPORT_C_DECL int WPCTP tReqQryExchange(CThostFtdcTraderApi *api, CThostFtdcQryExchangeField *pQryExchange, int nRequestID);

// 请求查询产品
DLL_EXPORT_C_DECL int WPCTP tReqQryProduct(CThostFtdcTraderApi *api, CThostFtdcQryProductField *pQryProduct, int nRequestID);

// 请求查询合约
DLL_EXPORT_C_DECL int WPCTP tReqQryInstrument(CThostFtdcTraderApi *api, CThostFtdcQryInstrumentField *pQryInstrument, int nRequestID);

// 请求查询行情
DLL_EXPORT_C_DECL int WPCTP tReqQryDepthMarketData(CThostFtdcTraderApi *api, CThostFtdcQryDepthMarketDataField *pQryDepthMarketData, int nRequestID);

// 请求查询交易员报盘机
DLL_EXPORT_C_DECL int WPCTP tReqQryTraderOffer(CThostFtdcTraderApi *api, CThostFtdcQryTraderOfferField *pQryTraderOffer, int nRequestID);

// 请求查询投资者结算结果
DLL_EXPORT_C_DECL int WPCTP tReqQrySettlementInfo(CThostFtdcTraderApi *api, CThostFtdcQrySettlementInfoField *pQrySettlementInfo, int nRequestID);

// 请求查询转帐银行
DLL_EXPORT_C_DECL int WPCTP tReqQryTransferBank(CThostFtdcTraderApi *api, CThostFtdcQryTransferBankField *pQryTransferBank, int nRequestID);

// 请求查询投资者持仓明细
DLL_EXPORT_C_DECL int WPCTP tReqQryInvestorPositionDetail(CThostFtdcTraderApi *api, CThostFtdcQryInvestorPositionDetailField *pQryInvestorPositionDetail, int nRequestID);

// 请求查询客户通知
DLL_EXPORT_C_DECL int WPCTP tReqQryNotice(CThostFtdcTraderApi *api, CThostFtdcQryNoticeField *pQryNotice, int nRequestID);

// 请求查询结算信息确认
DLL_EXPORT_C_DECL int WPCTP tReqQrySettlementInfoConfirm(CThostFtdcTraderApi *api, CThostFtdcQrySettlementInfoConfirmField *pQrySettlementInfoConfirm, int nRequestID);

// 请求查询投资者持仓明细
DLL_EXPORT_C_DECL int WPCTP tReqQryInvestorPositionCombineDetail(CThostFtdcTraderApi *api, CThostFtdcQryInvestorPositionCombineDetailField *pQryInvestorPositionCombineDetail, int nRequestID);

// 请求查询保证金监管系统经纪公司资金账户密钥
DLL_EXPORT_C_DECL int WPCTP tReqQryCFMMCTradingAccountKey(CThostFtdcTraderApi *api, CThostFtdcQryCFMMCTradingAccountKeyField *pQryCFMMCTradingAccountKey, int nRequestID);

// 请求查询仓单折抵信息
DLL_EXPORT_C_DECL int WPCTP tReqQryEWarrantOffset(CThostFtdcTraderApi *api, CThostFtdcQryEWarrantOffsetField *pQryEWarrantOffset, int nRequestID);

// 请求查询投资者品种/跨品种保证金
DLL_EXPORT_C_DECL int WPCTP tReqQryInvestorProductGroupMargin(CThostFtdcTraderApi *api, CThostFtdcQryInvestorProductGroupMarginField *pQryInvestorProductGroupMargin, int nRequestID);

// 请求查询交易所保证金率
DLL_EXPORT_C_DECL int WPCTP tReqQryExchangeMarginRate(CThostFtdcTraderApi *api, CThostFtdcQryExchangeMarginRateField *pQryExchangeMarginRate, int nRequestID);

// 请求查询交易所调整保证金率
DLL_EXPORT_C_DECL int WPCTP tReqQryExchangeMarginRateAdjust(CThostFtdcTraderApi *api, CThostFtdcQryExchangeMarginRateAdjustField *pQryExchangeMarginRateAdjust, int nRequestID);

// 请求查询汇率
DLL_EXPORT_C_DECL int WPCTP tReqQryExchangeRate(CThostFtdcTraderApi *api, CThostFtdcQryExchangeRateField *pQryExchangeRate, int nRequestID);

// 请求查询二级代理操作员银期权限
DLL_EXPORT_C_DECL int WPCTP tReqQrySecAgentACIDMap(CThostFtdcTraderApi *api, CThostFtdcQrySecAgentACIDMapField *pQrySecAgentACIDMap, int nRequestID);

// 请求查询产品报价汇率
DLL_EXPORT_C_DECL int WPCTP tReqQryProductExchRate(CThostFtdcTraderApi *api, CThostFtdcQryProductExchRateField *pQryProductExchRate, int nRequestID);

// 请求查询产品组
DLL_EXPORT_C_DECL int WPCTP tReqQryProductGroup(CThostFtdcTraderApi *api, CThostFtdcQryProductGroupField *pQryProductGroup, int nRequestID);

// 请求查询做市商合约手续费率
DLL_EXPORT_C_DECL int WPCTP tReqQryMMInstrumentCommissionRate(CThostFtdcTraderApi *api, CThostFtdcQryMMInstrumentCommissionRateField *pQryMMInstrumentCommissionRate, int nRequestID);

// 请求查询做市商期权合约手续费
DLL_EXPORT_C_DECL int WPCTP tReqQryMMOptionInstrCommRate(CThostFtdcTraderApi *api, CThostFtdcQryMMOptionInstrCommRateField *pQryMMOptionInstrCommRate, int nRequestID);

// 请求查询报单手续费
DLL_EXPORT_C_DECL int WPCTP tReqQryInstrumentOrderCommRate(CThostFtdcTraderApi *api, CThostFtdcQryInstrumentOrderCommRateField *pQryInstrumentOrderCommRate, int nRequestID);

// 请求查询资金账户
DLL_EXPORT_C_DECL int WPCTP tReqQrySecAgentTradingAccount(CThostFtdcTraderApi *api, CThostFtdcQryTradingAccountField *pQryTradingAccount, int nRequestID);

// 请求查询二级代理商资金校验模式
DLL_EXPORT_C_DECL int WPCTP tReqQrySecAgentCheckMode(CThostFtdcTraderApi *api, CThostFtdcQrySecAgentCheckModeField *pQrySecAgentCheckMode, int nRequestID);

// 请求查询二级代理商信息
DLL_EXPORT_C_DECL int WPCTP tReqQrySecAgentTradeInfo(CThostFtdcTraderApi *api, CThostFtdcQrySecAgentTradeInfoField *pQrySecAgentTradeInfo, int nRequestID);

// 请求查询期权交易成本
DLL_EXPORT_C_DECL int WPCTP tReqQryOptionInstrTradeCost(CThostFtdcTraderApi *api, CThostFtdcQryOptionInstrTradeCostField *pQryOptionInstrTradeCost, int nRequestID);

// 请求查询期权合约手续费
DLL_EXPORT_C_DECL int WPCTP tReqQryOptionInstrCommRate(CThostFtdcTraderApi *api, CThostFtdcQryOptionInstrCommRateField *pQryOptionInstrCommRate, int nRequestID);

// 请求查询执行宣告
DLL_EXPORT_C_DECL int WPCTP tReqQryExecOrder(CThostFtdcTraderApi *api, CThostFtdcQryExecOrderField *pQryExecOrder, int nRequestID);

// 请求查询询价
DLL_EXPORT_C_DECL int WPCTP tReqQryForQuote(CThostFtdcTraderApi *api, CThostFtdcQryForQuoteField *pQryForQuote, int nRequestID);

// 请求查询报价
DLL_EXPORT_C_DECL int WPCTP tReqQryQuote(CThostFtdcTraderApi *api, CThostFtdcQryQuoteField *pQryQuote, int nRequestID);

// 请求查询期权自对冲
DLL_EXPORT_C_DECL int WPCTP tReqQryOptionSelfClose(CThostFtdcTraderApi *api, CThostFtdcQryOptionSelfCloseField *pQryOptionSelfClose, int nRequestID);

// 请求查询投资单元
DLL_EXPORT_C_DECL int WPCTP tReqQryInvestUnit(CThostFtdcTraderApi *api, CThostFtdcQryInvestUnitField *pQryInvestUnit, int nRequestID);

// 请求查询组合合约安全系数
DLL_EXPORT_C_DECL int WPCTP tReqQryCombInstrumentGuard(CThostFtdcTraderApi *api, CThostFtdcQryCombInstrumentGuardField *pQryCombInstrumentGuard, int nRequestID);

// 请求查询申请组合
DLL_EXPORT_C_DECL int WPCTP tReqQryCombAction(CThostFtdcTraderApi *api, CThostFtdcQryCombActionField *pQryCombAction, int nRequestID);

// 请求查询转帐流水
DLL_EXPORT_C_DECL int WPCTP tReqQryTransferSerial(CThostFtdcTraderApi *api, CThostFtdcQryTransferSerialField *pQryTransferSerial, int nRequestID);

// 请求查询银期签约关系
DLL_EXPORT_C_DECL int WPCTP tReqQryAccountregister(CThostFtdcTraderApi *api, CThostFtdcQryAccountregisterField *pQryAccountregister, int nRequestID);

// 请求查询签约银行
DLL_EXPORT_C_DECL int WPCTP tReqQryContractBank(CThostFtdcTraderApi *api, CThostFtdcQryContractBankField *pQryContractBank, int nRequestID);

// 请求查询预埋单
DLL_EXPORT_C_DECL int WPCTP tReqQryParkedOrder(CThostFtdcTraderApi *api, CThostFtdcQryParkedOrderField *pQryParkedOrder, int nRequestID);

// 请求查询预埋撤单
DLL_EXPORT_C_DECL int WPCTP tReqQryParkedOrderAction(CThostFtdcTraderApi *api, CThostFtdcQryParkedOrderActionField *pQryParkedOrderAction, int nRequestID);

// 请求查询交易通知
DLL_EXPORT_C_DECL int WPCTP tReqQryTradingNotice(CThostFtdcTraderApi *api, CThostFtdcQryTradingNoticeField *pQryTradingNotice, int nRequestID);

// 请求查询经纪公司交易参数
DLL_EXPORT_C_DECL int WPCTP tReqQryBrokerTradingParams(CThostFtdcTraderApi *api, CThostFtdcQryBrokerTradingParamsField *pQryBrokerTradingParams, int nRequestID);

// 请求查询经纪公司交易算法
DLL_EXPORT_C_DECL int WPCTP tReqQryBrokerTradingAlgos(CThostFtdcTraderApi *api, CThostFtdcQryBrokerTradingAlgosField *pQryBrokerTradingAlgos, int nRequestID);

// 请求查询监控中心用户令牌
DLL_EXPORT_C_DECL int WPCTP tReqQueryCFMMCTradingAccountToken(CThostFtdcTraderApi *api, CThostFtdcQueryCFMMCTradingAccountTokenField *pQueryCFMMCTradingAccountToken, int nRequestID);

// 期货发起银行资金转期货请求
DLL_EXPORT_C_DECL int WPCTP tReqFromBankToFutureByFuture(CThostFtdcTraderApi *api, CThostFtdcReqTransferField *pReqTransfer, int nRequestID);

// 期货发起期货资金转银行请求
DLL_EXPORT_C_DECL int WPCTP tReqFromFutureToBankByFuture(CThostFtdcTraderApi *api, CThostFtdcReqTransferField *pReqTransfer, int nRequestID);

// 期货发起查询银行余额请求
DLL_EXPORT_C_DECL int WPCTP tReqQueryBankAccountMoneyByFuture(CThostFtdcTraderApi *api, CThostFtdcReqQueryAccountField *pReqQueryAccount, int nRequestID);

// 请求查询分类合约
DLL_EXPORT_C_DECL int WPCTP tReqQryClassifiedInstrument(CThostFtdcTraderApi *api, CThostFtdcQryClassifiedInstrumentField *pQryClassifiedInstrument, int nRequestID);

// 请求组合优惠比例
DLL_EXPORT_C_DECL int WPCTP tReqQryCombPromotionParam(CThostFtdcTraderApi *api, CThostFtdcQryCombPromotionParamField *pQryCombPromotionParam, int nRequestID);

// 投资者风险结算持仓查询
DLL_EXPORT_C_DECL int WPCTP tReqQryRiskSettleInvstPosition(CThostFtdcTraderApi *api, CThostFtdcQryRiskSettleInvstPositionField *pQryRiskSettleInvstPosition, int nRequestID);

// 风险结算产品查询
DLL_EXPORT_C_DECL int WPCTP tReqQryRiskSettleProductStatus(CThostFtdcTraderApi *api, CThostFtdcQryRiskSettleProductStatusField *pQryRiskSettleProductStatus, int nRequestID);

// SPBM期货合约参数查询
DLL_EXPORT_C_DECL int WPCTP tReqQrySPBMFutureParameter(CThostFtdcTraderApi *api, CThostFtdcQrySPBMFutureParameterField *pQrySPBMFutureParameter, int nRequestID);

// SPBM期权合约参数查询
DLL_EXPORT_C_DECL int WPCTP tReqQrySPBMOptionParameter(CThostFtdcTraderApi *api, CThostFtdcQrySPBMOptionParameterField *pQrySPBMOptionParameter, int nRequestID);

// SPBM品种内对锁仓折扣参数查询
DLL_EXPORT_C_DECL int WPCTP tReqQrySPBMIntraParameter(CThostFtdcTraderApi *api, CThostFtdcQrySPBMIntraParameterField *pQrySPBMIntraParameter, int nRequestID);

// SPBM跨品种抵扣参数查询
DLL_EXPORT_C_DECL int WPCTP tReqQrySPBMInterParameter(CThostFtdcTraderApi *api, CThostFtdcQrySPBMInterParameterField *pQrySPBMInterParameter, int nRequestID);

// SPBM组合保证金套餐查询
DLL_EXPORT_C_DECL int WPCTP tReqQrySPBMPortfDefinition(CThostFtdcTraderApi *api, CThostFtdcQrySPBMPortfDefinitionField *pQrySPBMPortfDefinition, int nRequestID);

// 投资者SPBM套餐选择查询
DLL_EXPORT_C_DECL int WPCTP tReqQrySPBMInvestorPortfDef(CThostFtdcTraderApi *api, CThostFtdcQrySPBMInvestorPortfDefField *pQrySPBMInvestorPortfDef, int nRequestID);

// 投资者新型组合保证金系数查询
DLL_EXPORT_C_DECL int WPCTP tReqQryInvestorPortfMarginRatio(CThostFtdcTraderApi *api, CThostFtdcQryInvestorPortfMarginRatioField *pQryInvestorPortfMarginRatio, int nRequestID);

// 投资者产品SPBM明细查询
DLL_EXPORT_C_DECL int WPCTP tReqQryInvestorProdSPBMDetail(CThostFtdcTraderApi *api, CThostFtdcQryInvestorProdSPBMDetailField *pQryInvestorProdSPBMDetail, int nRequestID);
