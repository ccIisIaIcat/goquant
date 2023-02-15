#include "ctptrade_api.h"
#include <string.h>

DLL_EXPORT_C_DECL int WPCTP dCTP_GetSystemInfo(char* pSystemInfo, int nLen) { return CTP_GetSystemInfo(pSystemInfo, nLen); };

DLL_EXPORT_C_DECL void* WPCTP dCTP_GetDataCollectApiVersion() { return (void*)CTP_GetDataCollectApiVersion();};

Trade::Trade()
{
	OnFrontConnected_ = NULL;
	OnFrontDisconnected_ = NULL;
	OnHeartBeatWarning_ = NULL;
	OnRspAuthenticate_ = NULL;
	OnRspUserLogin_ = NULL;
	OnRspUserLogout_ = NULL;
	OnRspUserPasswordUpdate_ = NULL;
	OnRspTradingAccountPasswordUpdate_ = NULL;
	OnRspUserAuthMethod_ = NULL;
	OnRspGenUserCaptcha_ = NULL;
	OnRspGenUserText_ = NULL;
	OnRspOrderInsert_ = NULL;
	OnRspParkedOrderInsert_ = NULL;
	OnRspParkedOrderAction_ = NULL;
	OnRspOrderAction_ = NULL;
	OnRspQryMaxOrderVolume_ = NULL;
	OnRspSettlementInfoConfirm_ = NULL;
	OnRspRemoveParkedOrder_ = NULL;
	OnRspRemoveParkedOrderAction_ = NULL;
	OnRspExecOrderInsert_ = NULL;
	OnRspExecOrderAction_ = NULL;
	OnRspForQuoteInsert_ = NULL;
	OnRspQuoteInsert_ = NULL;
	OnRspQuoteAction_ = NULL;
	OnRspBatchOrderAction_ = NULL;
	OnRspOptionSelfCloseInsert_ = NULL;
	OnRspOptionSelfCloseAction_ = NULL;
	OnRspCombActionInsert_ = NULL;
	OnRspQryOrder_ = NULL;
	OnRspQryTrade_ = NULL;
	OnRspQryInvestorPosition_ = NULL;
	OnRspQryTradingAccount_ = NULL;
	OnRspQryInvestor_ = NULL;
	OnRspQryTradingCode_ = NULL;
	OnRspQryInstrumentMarginRate_ = NULL;
	OnRspQryInstrumentCommissionRate_ = NULL;
	OnRspQryExchange_ = NULL;
	OnRspQryProduct_ = NULL;
	OnRspQryInstrument_ = NULL;
	OnRspQryDepthMarketData_ = NULL;
	OnRspQryTraderOffer_ = NULL;
	OnRspQrySettlementInfo_ = NULL;
	OnRspQryTransferBank_ = NULL;
	OnRspQryInvestorPositionDetail_ = NULL;
	OnRspQryNotice_ = NULL;
	OnRspQrySettlementInfoConfirm_ = NULL;
	OnRspQryInvestorPositionCombineDetail_ = NULL;
	OnRspQryCFMMCTradingAccountKey_ = NULL;
	OnRspQryEWarrantOffset_ = NULL;
	OnRspQryInvestorProductGroupMargin_ = NULL;
	OnRspQryExchangeMarginRate_ = NULL;
	OnRspQryExchangeMarginRateAdjust_ = NULL;
	OnRspQryExchangeRate_ = NULL;
	OnRspQrySecAgentACIDMap_ = NULL;
	OnRspQryProductExchRate_ = NULL;
	OnRspQryProductGroup_ = NULL;
	OnRspQryMMInstrumentCommissionRate_ = NULL;
	OnRspQryMMOptionInstrCommRate_ = NULL;
	OnRspQryInstrumentOrderCommRate_ = NULL;
	OnRspQrySecAgentTradingAccount_ = NULL;
	OnRspQrySecAgentCheckMode_ = NULL;
	OnRspQrySecAgentTradeInfo_ = NULL;
	OnRspQryOptionInstrTradeCost_ = NULL;
	OnRspQryOptionInstrCommRate_ = NULL;
	OnRspQryExecOrder_ = NULL;
	OnRspQryForQuote_ = NULL;
	OnRspQryQuote_ = NULL;
	OnRspQryOptionSelfClose_ = NULL;
	OnRspQryInvestUnit_ = NULL;
	OnRspQryCombInstrumentGuard_ = NULL;
	OnRspQryCombAction_ = NULL;
	OnRspQryTransferSerial_ = NULL;
	OnRspQryAccountregister_ = NULL;
	OnRspError_ = NULL;
	OnRtnOrder_ = NULL;
	OnRtnTrade_ = NULL;
	OnErrRtnOrderInsert_ = NULL;
	OnErrRtnOrderAction_ = NULL;
	OnRtnInstrumentStatus_ = NULL;
	OnRtnBulletin_ = NULL;
	OnRtnTradingNotice_ = NULL;
	OnRtnErrorConditionalOrder_ = NULL;
	OnRtnExecOrder_ = NULL;
	OnErrRtnExecOrderInsert_ = NULL;
	OnErrRtnExecOrderAction_ = NULL;
	OnErrRtnForQuoteInsert_ = NULL;
	OnRtnQuote_ = NULL;
	OnErrRtnQuoteInsert_ = NULL;
	OnErrRtnQuoteAction_ = NULL;
	OnRtnForQuoteRsp_ = NULL;
	OnRtnCFMMCTradingAccountToken_ = NULL;
	OnErrRtnBatchOrderAction_ = NULL;
	OnRtnOptionSelfClose_ = NULL;
	OnErrRtnOptionSelfCloseInsert_ = NULL;
	OnErrRtnOptionSelfCloseAction_ = NULL;
	OnRtnCombAction_ = NULL;
	OnErrRtnCombActionInsert_ = NULL;
	OnRspQryContractBank_ = NULL;
	OnRspQryParkedOrder_ = NULL;
	OnRspQryParkedOrderAction_ = NULL;
	OnRspQryTradingNotice_ = NULL;
	OnRspQryBrokerTradingParams_ = NULL;
	OnRspQryBrokerTradingAlgos_ = NULL;
	OnRspQueryCFMMCTradingAccountToken_ = NULL;
	OnRtnFromBankToFutureByBank_ = NULL;
	OnRtnFromFutureToBankByBank_ = NULL;
	OnRtnRepealFromBankToFutureByBank_ = NULL;
	OnRtnRepealFromFutureToBankByBank_ = NULL;
	OnRtnFromBankToFutureByFuture_ = NULL;
	OnRtnFromFutureToBankByFuture_ = NULL;
	OnRtnRepealFromBankToFutureByFutureManual_ = NULL;
	OnRtnRepealFromFutureToBankByFutureManual_ = NULL;
	OnRtnQueryBankBalanceByFuture_ = NULL;
	OnErrRtnBankToFutureByFuture_ = NULL;
	OnErrRtnFutureToBankByFuture_ = NULL;
	OnErrRtnRepealBankToFutureByFutureManual_ = NULL;
	OnErrRtnRepealFutureToBankByFutureManual_ = NULL;
	OnErrRtnQueryBankBalanceByFuture_ = NULL;
	OnRtnRepealFromBankToFutureByFuture_ = NULL;
	OnRtnRepealFromFutureToBankByFuture_ = NULL;
	OnRspFromBankToFutureByFuture_ = NULL;
	OnRspFromFutureToBankByFuture_ = NULL;
	OnRspQueryBankAccountMoneyByFuture_ = NULL;
	OnRtnOpenAccountByBank_ = NULL;
	OnRtnCancelAccountByBank_ = NULL;
	OnRtnChangeAccountByBank_ = NULL;
	OnRspQryClassifiedInstrument_ = NULL;
	OnRspQryCombPromotionParam_ = NULL;
	OnRspQryRiskSettleInvstPosition_ = NULL;
	OnRspQryRiskSettleProductStatus_ = NULL;
	OnRspQrySPBMFutureParameter_ = NULL;
	OnRspQrySPBMOptionParameter_ = NULL;
	OnRspQrySPBMIntraParameter_ = NULL;
	OnRspQrySPBMInterParameter_ = NULL;
	OnRspQrySPBMPortfDefinition_ = NULL;
	OnRspQrySPBMInvestorPortfDef_ = NULL;
	OnRspQryInvestorPortfMarginRatio_ = NULL;
	OnRspQryInvestorProdSPBMDetail_ = NULL;
	
}


DLL_EXPORT_C_DECL void* WPCTP tCreateApi(const char *pszFlowPath = "") { return CThostFtdcTraderApi::CreateFtdcTraderApi(pszFlowPath); }
DLL_EXPORT_C_DECL void* WPCTP tCreateSpi() { return new Trade(); }
DLL_EXPORT_C_DECL void* WPCTP tGetApiVersion() { return (void*)CThostFtdcTraderApi::GetApiVersion(); }
DLL_EXPORT_C_DECL void* WPCTP tGetTradingDay(CThostFtdcTraderApi *api) { return (void*)api->GetTradingDay(); }


// 当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。
DLL_EXPORT_C_DECL void WPCTP tOnFrontConnected(Trade* spi, void* func){ spi->OnFrontConnected_ = func; }

// 当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。
DLL_EXPORT_C_DECL void WPCTP tOnFrontDisconnected(Trade* spi, void* func){ spi->OnFrontDisconnected_ = func; }

// 心跳超时警告。当长时间未收到报文时，该方法被调用。
DLL_EXPORT_C_DECL void WPCTP tOnHeartBeatWarning(Trade* spi, void* func){ spi->OnHeartBeatWarning_ = func; }

// 客户端认证响应
DLL_EXPORT_C_DECL void WPCTP tOnRspAuthenticate(Trade* spi, void* func){ spi->OnRspAuthenticate_ = func; }

// 登录请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspUserLogin(Trade* spi, void* func){ spi->OnRspUserLogin_ = func; }

// 登出请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspUserLogout(Trade* spi, void* func){ spi->OnRspUserLogout_ = func; }

// 用户口令更新请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspUserPasswordUpdate(Trade* spi, void* func){ spi->OnRspUserPasswordUpdate_ = func; }

// 资金账户口令更新请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspTradingAccountPasswordUpdate(Trade* spi, void* func){ spi->OnRspTradingAccountPasswordUpdate_ = func; }

// 查询用户当前支持的认证模式的回复
DLL_EXPORT_C_DECL void WPCTP tOnRspUserAuthMethod(Trade* spi, void* func){ spi->OnRspUserAuthMethod_ = func; }

// 获取图形验证码请求的回复
DLL_EXPORT_C_DECL void WPCTP tOnRspGenUserCaptcha(Trade* spi, void* func){ spi->OnRspGenUserCaptcha_ = func; }

// 获取短信验证码请求的回复
DLL_EXPORT_C_DECL void WPCTP tOnRspGenUserText(Trade* spi, void* func){ spi->OnRspGenUserText_ = func; }

// 报单录入请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspOrderInsert(Trade* spi, void* func){ spi->OnRspOrderInsert_ = func; }

// 预埋单录入请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspParkedOrderInsert(Trade* spi, void* func){ spi->OnRspParkedOrderInsert_ = func; }

// 预埋撤单录入请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspParkedOrderAction(Trade* spi, void* func){ spi->OnRspParkedOrderAction_ = func; }

// 报单操作请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspOrderAction(Trade* spi, void* func){ spi->OnRspOrderAction_ = func; }

// 查询最大报单数量响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryMaxOrderVolume(Trade* spi, void* func){ spi->OnRspQryMaxOrderVolume_ = func; }

// 投资者结算结果确认响应
DLL_EXPORT_C_DECL void WPCTP tOnRspSettlementInfoConfirm(Trade* spi, void* func){ spi->OnRspSettlementInfoConfirm_ = func; }

// 删除预埋单响应
DLL_EXPORT_C_DECL void WPCTP tOnRspRemoveParkedOrder(Trade* spi, void* func){ spi->OnRspRemoveParkedOrder_ = func; }

// 删除预埋撤单响应
DLL_EXPORT_C_DECL void WPCTP tOnRspRemoveParkedOrderAction(Trade* spi, void* func){ spi->OnRspRemoveParkedOrderAction_ = func; }

// 执行宣告录入请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspExecOrderInsert(Trade* spi, void* func){ spi->OnRspExecOrderInsert_ = func; }

// 执行宣告操作请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspExecOrderAction(Trade* spi, void* func){ spi->OnRspExecOrderAction_ = func; }

// 询价录入请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspForQuoteInsert(Trade* spi, void* func){ spi->OnRspForQuoteInsert_ = func; }

// 报价录入请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQuoteInsert(Trade* spi, void* func){ spi->OnRspQuoteInsert_ = func; }

// 报价操作请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQuoteAction(Trade* spi, void* func){ spi->OnRspQuoteAction_ = func; }

// 批量报单操作请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspBatchOrderAction(Trade* spi, void* func){ spi->OnRspBatchOrderAction_ = func; }

// 期权自对冲录入请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspOptionSelfCloseInsert(Trade* spi, void* func){ spi->OnRspOptionSelfCloseInsert_ = func; }

// 期权自对冲操作请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspOptionSelfCloseAction(Trade* spi, void* func){ spi->OnRspOptionSelfCloseAction_ = func; }

// 申请组合录入请求响应
DLL_EXPORT_C_DECL void WPCTP tOnRspCombActionInsert(Trade* spi, void* func){ spi->OnRspCombActionInsert_ = func; }

// 请求查询报单响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryOrder(Trade* spi, void* func){ spi->OnRspQryOrder_ = func; }

// 请求查询成交响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryTrade(Trade* spi, void* func){ spi->OnRspQryTrade_ = func; }

// 请求查询投资者持仓响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryInvestorPosition(Trade* spi, void* func){ spi->OnRspQryInvestorPosition_ = func; }

// 请求查询资金账户响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryTradingAccount(Trade* spi, void* func){ spi->OnRspQryTradingAccount_ = func; }

// 请求查询投资者响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryInvestor(Trade* spi, void* func){ spi->OnRspQryInvestor_ = func; }

// 请求查询交易编码响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryTradingCode(Trade* spi, void* func){ spi->OnRspQryTradingCode_ = func; }

// 请求查询合约保证金率响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryInstrumentMarginRate(Trade* spi, void* func){ spi->OnRspQryInstrumentMarginRate_ = func; }

// 请求查询合约手续费率响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryInstrumentCommissionRate(Trade* spi, void* func){ spi->OnRspQryInstrumentCommissionRate_ = func; }

// 请求查询交易所响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryExchange(Trade* spi, void* func){ spi->OnRspQryExchange_ = func; }

// 请求查询产品响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryProduct(Trade* spi, void* func){ spi->OnRspQryProduct_ = func; }

// 请求查询合约响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryInstrument(Trade* spi, void* func){ spi->OnRspQryInstrument_ = func; }

// 请求查询行情响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryDepthMarketData(Trade* spi, void* func){ spi->OnRspQryDepthMarketData_ = func; }

// 请求查询交易员报盘机响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryTraderOffer(Trade* spi, void* func){ spi->OnRspQryTraderOffer_ = func; }

// 请求查询投资者结算结果响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQrySettlementInfo(Trade* spi, void* func){ spi->OnRspQrySettlementInfo_ = func; }

// 请求查询转帐银行响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryTransferBank(Trade* spi, void* func){ spi->OnRspQryTransferBank_ = func; }

// 请求查询投资者持仓明细响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryInvestorPositionDetail(Trade* spi, void* func){ spi->OnRspQryInvestorPositionDetail_ = func; }

// 请求查询客户通知响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryNotice(Trade* spi, void* func){ spi->OnRspQryNotice_ = func; }

// 请求查询结算信息确认响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQrySettlementInfoConfirm(Trade* spi, void* func){ spi->OnRspQrySettlementInfoConfirm_ = func; }

// 请求查询投资者持仓明细响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryInvestorPositionCombineDetail(Trade* spi, void* func){ spi->OnRspQryInvestorPositionCombineDetail_ = func; }

// 查询保证金监管系统经纪公司资金账户密钥响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryCFMMCTradingAccountKey(Trade* spi, void* func){ spi->OnRspQryCFMMCTradingAccountKey_ = func; }

// 请求查询仓单折抵信息响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryEWarrantOffset(Trade* spi, void* func){ spi->OnRspQryEWarrantOffset_ = func; }

// 请求查询投资者品种/跨品种保证金响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryInvestorProductGroupMargin(Trade* spi, void* func){ spi->OnRspQryInvestorProductGroupMargin_ = func; }

// 请求查询交易所保证金率响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryExchangeMarginRate(Trade* spi, void* func){ spi->OnRspQryExchangeMarginRate_ = func; }

// 请求查询交易所调整保证金率响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryExchangeMarginRateAdjust(Trade* spi, void* func){ spi->OnRspQryExchangeMarginRateAdjust_ = func; }

// 请求查询汇率响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryExchangeRate(Trade* spi, void* func){ spi->OnRspQryExchangeRate_ = func; }

// 请求查询二级代理操作员银期权限响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQrySecAgentACIDMap(Trade* spi, void* func){ spi->OnRspQrySecAgentACIDMap_ = func; }

// 请求查询产品报价汇率
DLL_EXPORT_C_DECL void WPCTP tOnRspQryProductExchRate(Trade* spi, void* func){ spi->OnRspQryProductExchRate_ = func; }

// 请求查询产品组
DLL_EXPORT_C_DECL void WPCTP tOnRspQryProductGroup(Trade* spi, void* func){ spi->OnRspQryProductGroup_ = func; }

// 请求查询做市商合约手续费率响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryMMInstrumentCommissionRate(Trade* spi, void* func){ spi->OnRspQryMMInstrumentCommissionRate_ = func; }

// 请求查询做市商期权合约手续费响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryMMOptionInstrCommRate(Trade* spi, void* func){ spi->OnRspQryMMOptionInstrCommRate_ = func; }

// 请求查询报单手续费响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryInstrumentOrderCommRate(Trade* spi, void* func){ spi->OnRspQryInstrumentOrderCommRate_ = func; }

// 请求查询资金账户响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQrySecAgentTradingAccount(Trade* spi, void* func){ spi->OnRspQrySecAgentTradingAccount_ = func; }

// 请求查询二级代理商资金校验模式响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQrySecAgentCheckMode(Trade* spi, void* func){ spi->OnRspQrySecAgentCheckMode_ = func; }

// 请求查询二级代理商信息响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQrySecAgentTradeInfo(Trade* spi, void* func){ spi->OnRspQrySecAgentTradeInfo_ = func; }

// 请求查询期权交易成本响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryOptionInstrTradeCost(Trade* spi, void* func){ spi->OnRspQryOptionInstrTradeCost_ = func; }

// 请求查询期权合约手续费响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryOptionInstrCommRate(Trade* spi, void* func){ spi->OnRspQryOptionInstrCommRate_ = func; }

// 请求查询执行宣告响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryExecOrder(Trade* spi, void* func){ spi->OnRspQryExecOrder_ = func; }

// 请求查询询价响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryForQuote(Trade* spi, void* func){ spi->OnRspQryForQuote_ = func; }

// 请求查询报价响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryQuote(Trade* spi, void* func){ spi->OnRspQryQuote_ = func; }

// 请求查询期权自对冲响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryOptionSelfClose(Trade* spi, void* func){ spi->OnRspQryOptionSelfClose_ = func; }

// 请求查询投资单元响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryInvestUnit(Trade* spi, void* func){ spi->OnRspQryInvestUnit_ = func; }

// 请求查询组合合约安全系数响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryCombInstrumentGuard(Trade* spi, void* func){ spi->OnRspQryCombInstrumentGuard_ = func; }

// 请求查询申请组合响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryCombAction(Trade* spi, void* func){ spi->OnRspQryCombAction_ = func; }

// 请求查询转帐流水响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryTransferSerial(Trade* spi, void* func){ spi->OnRspQryTransferSerial_ = func; }

// 请求查询银期签约关系响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryAccountregister(Trade* spi, void* func){ spi->OnRspQryAccountregister_ = func; }

// 错误应答
DLL_EXPORT_C_DECL void WPCTP tOnRspError(Trade* spi, void* func){ spi->OnRspError_ = func; }

// 报单通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnOrder(Trade* spi, void* func){ spi->OnRtnOrder_ = func; }

// 成交通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnTrade(Trade* spi, void* func){ spi->OnRtnTrade_ = func; }

// 报单录入错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnOrderInsert(Trade* spi, void* func){ spi->OnErrRtnOrderInsert_ = func; }

// 报单操作错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnOrderAction(Trade* spi, void* func){ spi->OnErrRtnOrderAction_ = func; }

// 合约交易状态通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnInstrumentStatus(Trade* spi, void* func){ spi->OnRtnInstrumentStatus_ = func; }

// 交易所公告通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnBulletin(Trade* spi, void* func){ spi->OnRtnBulletin_ = func; }

// 交易通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnTradingNotice(Trade* spi, void* func){ spi->OnRtnTradingNotice_ = func; }

// 提示条件单校验错误
DLL_EXPORT_C_DECL void WPCTP tOnRtnErrorConditionalOrder(Trade* spi, void* func){ spi->OnRtnErrorConditionalOrder_ = func; }

// 执行宣告通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnExecOrder(Trade* spi, void* func){ spi->OnRtnExecOrder_ = func; }

// 执行宣告录入错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnExecOrderInsert(Trade* spi, void* func){ spi->OnErrRtnExecOrderInsert_ = func; }

// 执行宣告操作错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnExecOrderAction(Trade* spi, void* func){ spi->OnErrRtnExecOrderAction_ = func; }

// 询价录入错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnForQuoteInsert(Trade* spi, void* func){ spi->OnErrRtnForQuoteInsert_ = func; }

// 报价通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnQuote(Trade* spi, void* func){ spi->OnRtnQuote_ = func; }

// 报价录入错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnQuoteInsert(Trade* spi, void* func){ spi->OnErrRtnQuoteInsert_ = func; }

// 报价操作错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnQuoteAction(Trade* spi, void* func){ spi->OnErrRtnQuoteAction_ = func; }

// 询价通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnForQuoteRsp(Trade* spi, void* func){ spi->OnRtnForQuoteRsp_ = func; }

// 保证金监控中心用户令牌
DLL_EXPORT_C_DECL void WPCTP tOnRtnCFMMCTradingAccountToken(Trade* spi, void* func){ spi->OnRtnCFMMCTradingAccountToken_ = func; }

// 批量报单操作错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnBatchOrderAction(Trade* spi, void* func){ spi->OnErrRtnBatchOrderAction_ = func; }

// 期权自对冲通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnOptionSelfClose(Trade* spi, void* func){ spi->OnRtnOptionSelfClose_ = func; }

// 期权自对冲录入错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnOptionSelfCloseInsert(Trade* spi, void* func){ spi->OnErrRtnOptionSelfCloseInsert_ = func; }

// 期权自对冲操作错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnOptionSelfCloseAction(Trade* spi, void* func){ spi->OnErrRtnOptionSelfCloseAction_ = func; }

// 申请组合通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnCombAction(Trade* spi, void* func){ spi->OnRtnCombAction_ = func; }

// 申请组合录入错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnCombActionInsert(Trade* spi, void* func){ spi->OnErrRtnCombActionInsert_ = func; }

// 请求查询签约银行响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryContractBank(Trade* spi, void* func){ spi->OnRspQryContractBank_ = func; }

// 请求查询预埋单响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryParkedOrder(Trade* spi, void* func){ spi->OnRspQryParkedOrder_ = func; }

// 请求查询预埋撤单响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryParkedOrderAction(Trade* spi, void* func){ spi->OnRspQryParkedOrderAction_ = func; }

// 请求查询交易通知响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryTradingNotice(Trade* spi, void* func){ spi->OnRspQryTradingNotice_ = func; }

// 请求查询经纪公司交易参数响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryBrokerTradingParams(Trade* spi, void* func){ spi->OnRspQryBrokerTradingParams_ = func; }

// 请求查询经纪公司交易算法响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryBrokerTradingAlgos(Trade* spi, void* func){ spi->OnRspQryBrokerTradingAlgos_ = func; }

// 请求查询监控中心用户令牌
DLL_EXPORT_C_DECL void WPCTP tOnRspQueryCFMMCTradingAccountToken(Trade* spi, void* func){ spi->OnRspQueryCFMMCTradingAccountToken_ = func; }

// 银行发起银行资金转期货通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnFromBankToFutureByBank(Trade* spi, void* func){ spi->OnRtnFromBankToFutureByBank_ = func; }

// 银行发起期货资金转银行通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnFromFutureToBankByBank(Trade* spi, void* func){ spi->OnRtnFromFutureToBankByBank_ = func; }

// 银行发起冲正银行转期货通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnRepealFromBankToFutureByBank(Trade* spi, void* func){ spi->OnRtnRepealFromBankToFutureByBank_ = func; }

// 银行发起冲正期货转银行通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnRepealFromFutureToBankByBank(Trade* spi, void* func){ spi->OnRtnRepealFromFutureToBankByBank_ = func; }

// 期货发起银行资金转期货通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnFromBankToFutureByFuture(Trade* spi, void* func){ spi->OnRtnFromBankToFutureByFuture_ = func; }

// 期货发起期货资金转银行通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnFromFutureToBankByFuture(Trade* spi, void* func){ spi->OnRtnFromFutureToBankByFuture_ = func; }

// 系统运行时期货端手工发起冲正银行转期货请求，银行处理完毕后报盘发回的通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnRepealFromBankToFutureByFutureManual(Trade* spi, void* func){ spi->OnRtnRepealFromBankToFutureByFutureManual_ = func; }

// 系统运行时期货端手工发起冲正期货转银行请求，银行处理完毕后报盘发回的通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnRepealFromFutureToBankByFutureManual(Trade* spi, void* func){ spi->OnRtnRepealFromFutureToBankByFutureManual_ = func; }

// 期货发起查询银行余额通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnQueryBankBalanceByFuture(Trade* spi, void* func){ spi->OnRtnQueryBankBalanceByFuture_ = func; }

// 期货发起银行资金转期货错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnBankToFutureByFuture(Trade* spi, void* func){ spi->OnErrRtnBankToFutureByFuture_ = func; }

// 期货发起期货资金转银行错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnFutureToBankByFuture(Trade* spi, void* func){ spi->OnErrRtnFutureToBankByFuture_ = func; }

// 系统运行时期货端手工发起冲正银行转期货错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnRepealBankToFutureByFutureManual(Trade* spi, void* func){ spi->OnErrRtnRepealBankToFutureByFutureManual_ = func; }

// 系统运行时期货端手工发起冲正期货转银行错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnRepealFutureToBankByFutureManual(Trade* spi, void* func){ spi->OnErrRtnRepealFutureToBankByFutureManual_ = func; }

// 期货发起查询银行余额错误回报
DLL_EXPORT_C_DECL void WPCTP tOnErrRtnQueryBankBalanceByFuture(Trade* spi, void* func){ spi->OnErrRtnQueryBankBalanceByFuture_ = func; }

// 期货发起冲正银行转期货请求，银行处理完毕后报盘发回的通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnRepealFromBankToFutureByFuture(Trade* spi, void* func){ spi->OnRtnRepealFromBankToFutureByFuture_ = func; }

// 期货发起冲正期货转银行请求，银行处理完毕后报盘发回的通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnRepealFromFutureToBankByFuture(Trade* spi, void* func){ spi->OnRtnRepealFromFutureToBankByFuture_ = func; }

// 期货发起银行资金转期货应答
DLL_EXPORT_C_DECL void WPCTP tOnRspFromBankToFutureByFuture(Trade* spi, void* func){ spi->OnRspFromBankToFutureByFuture_ = func; }

// 期货发起期货资金转银行应答
DLL_EXPORT_C_DECL void WPCTP tOnRspFromFutureToBankByFuture(Trade* spi, void* func){ spi->OnRspFromFutureToBankByFuture_ = func; }

// 期货发起查询银行余额应答
DLL_EXPORT_C_DECL void WPCTP tOnRspQueryBankAccountMoneyByFuture(Trade* spi, void* func){ spi->OnRspQueryBankAccountMoneyByFuture_ = func; }

// 银行发起银期开户通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnOpenAccountByBank(Trade* spi, void* func){ spi->OnRtnOpenAccountByBank_ = func; }

// 银行发起银期销户通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnCancelAccountByBank(Trade* spi, void* func){ spi->OnRtnCancelAccountByBank_ = func; }

// 银行发起变更银行账号通知
DLL_EXPORT_C_DECL void WPCTP tOnRtnChangeAccountByBank(Trade* spi, void* func){ spi->OnRtnChangeAccountByBank_ = func; }

// 请求查询分类合约响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryClassifiedInstrument(Trade* spi, void* func){ spi->OnRspQryClassifiedInstrument_ = func; }

// 请求组合优惠比例响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryCombPromotionParam(Trade* spi, void* func){ spi->OnRspQryCombPromotionParam_ = func; }

// 投资者风险结算持仓查询响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryRiskSettleInvstPosition(Trade* spi, void* func){ spi->OnRspQryRiskSettleInvstPosition_ = func; }

// 风险结算产品查询响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryRiskSettleProductStatus(Trade* spi, void* func){ spi->OnRspQryRiskSettleProductStatus_ = func; }

// SPBM期货合约参数查询响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQrySPBMFutureParameter(Trade* spi, void* func){ spi->OnRspQrySPBMFutureParameter_ = func; }

// SPBM期权合约参数查询响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQrySPBMOptionParameter(Trade* spi, void* func){ spi->OnRspQrySPBMOptionParameter_ = func; }

// SPBM品种内对锁仓折扣参数查询响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQrySPBMIntraParameter(Trade* spi, void* func){ spi->OnRspQrySPBMIntraParameter_ = func; }

// SPBM跨品种抵扣参数查询响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQrySPBMInterParameter(Trade* spi, void* func){ spi->OnRspQrySPBMInterParameter_ = func; }

// SPBM组合保证金套餐查询响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQrySPBMPortfDefinition(Trade* spi, void* func){ spi->OnRspQrySPBMPortfDefinition_ = func; }

// 投资者SPBM套餐选择查询响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQrySPBMInvestorPortfDef(Trade* spi, void* func){ spi->OnRspQrySPBMInvestorPortfDef_ = func; }

// 投资者新型组合保证金系数查询响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryInvestorPortfMarginRatio(Trade* spi, void* func){ spi->OnRspQryInvestorPortfMarginRatio_ = func; }

// 投资者产品SPBM明细查询响应
DLL_EXPORT_C_DECL void WPCTP tOnRspQryInvestorProdSPBMDetail(Trade* spi, void* func){ spi->OnRspQryInvestorProdSPBMDetail_ = func; }


// 创建TraderApi
DLL_EXPORT_C_DECL void WPCTP tRelease(CThostFtdcTraderApi *api){ api->Release(); return; }

// 初始化
DLL_EXPORT_C_DECL void WPCTP tInit(CThostFtdcTraderApi *api){ api->Init(); return; }

// 等待接口线程结束运行
DLL_EXPORT_C_DECL int WPCTP tJoin(CThostFtdcTraderApi *api){ return api->Join(); }

// 注册前置机网络地址
DLL_EXPORT_C_DECL void WPCTP tRegisterFront(CThostFtdcTraderApi *api, char *pszFrontAddress){ api->RegisterFront(pszFrontAddress); return; }

// @remark RegisterNameServer优先于RegisterFront
DLL_EXPORT_C_DECL void WPCTP tRegisterNameServer(CThostFtdcTraderApi *api, char *pszNsAddress){ api->RegisterNameServer(pszNsAddress); return; }

// 注册名字服务器用户信息
DLL_EXPORT_C_DECL void WPCTP tRegisterFensUserInfo(CThostFtdcTraderApi *api, CThostFtdcFensUserInfoField * pFensUserInfo){ api->RegisterFensUserInfo( pFensUserInfo); return; }

// 注册回调接口
DLL_EXPORT_C_DECL void WPCTP tRegisterSpi(CThostFtdcTraderApi *api, CThostFtdcTraderSpi *pSpi){ api->RegisterSpi(pSpi); return; }

// 订阅私有流。
DLL_EXPORT_C_DECL void WPCTP tSubscribePrivateTopic(CThostFtdcTraderApi *api, THOST_TE_RESUME_TYPE nResumeType){ api->SubscribePrivateTopic(nResumeType); return; }

// 订阅公共流。
DLL_EXPORT_C_DECL void WPCTP tSubscribePublicTopic(CThostFtdcTraderApi *api, THOST_TE_RESUME_TYPE nResumeType){ api->SubscribePublicTopic(nResumeType); return; }

// 客户端认证请求
DLL_EXPORT_C_DECL int WPCTP tReqAuthenticate(CThostFtdcTraderApi *api, CThostFtdcReqAuthenticateField *pReqAuthenticateField, int nRequestID){ return api->ReqAuthenticate(pReqAuthenticateField, nRequestID); }

// 注册用户终端信息，用于中继服务器多连接模式
DLL_EXPORT_C_DECL int WPCTP tRegisterUserSystemInfo(CThostFtdcTraderApi *api, CThostFtdcUserSystemInfoField *pUserSystemInfo){ return api->RegisterUserSystemInfo(pUserSystemInfo); }

// 上报用户终端信息，用于中继服务器操作员登录模式
DLL_EXPORT_C_DECL int WPCTP tSubmitUserSystemInfo(CThostFtdcTraderApi *api, CThostFtdcUserSystemInfoField *pUserSystemInfo){ return api->SubmitUserSystemInfo(pUserSystemInfo); }

// 用户登录请求
DLL_EXPORT_C_DECL int WPCTP tReqUserLogin(CThostFtdcTraderApi *api, CThostFtdcReqUserLoginField *pReqUserLoginField, int nRequestID){ return api->ReqUserLogin(pReqUserLoginField, nRequestID); }

// 登出请求
DLL_EXPORT_C_DECL int WPCTP tReqUserLogout(CThostFtdcTraderApi *api, CThostFtdcUserLogoutField *pUserLogout, int nRequestID){ return api->ReqUserLogout(pUserLogout, nRequestID); }

// 用户口令更新请求
DLL_EXPORT_C_DECL int WPCTP tReqUserPasswordUpdate(CThostFtdcTraderApi *api, CThostFtdcUserPasswordUpdateField *pUserPasswordUpdate, int nRequestID){ return api->ReqUserPasswordUpdate(pUserPasswordUpdate, nRequestID); }

// 资金账户口令更新请求
DLL_EXPORT_C_DECL int WPCTP tReqTradingAccountPasswordUpdate(CThostFtdcTraderApi *api, CThostFtdcTradingAccountPasswordUpdateField *pTradingAccountPasswordUpdate, int nRequestID){ return api->ReqTradingAccountPasswordUpdate(pTradingAccountPasswordUpdate, nRequestID); }

// 查询用户当前支持的认证模式
DLL_EXPORT_C_DECL int WPCTP tReqUserAuthMethod(CThostFtdcTraderApi *api, CThostFtdcReqUserAuthMethodField *pReqUserAuthMethod, int nRequestID){ return api->ReqUserAuthMethod(pReqUserAuthMethod, nRequestID); }

// 用户发出获取图形验证码请求
DLL_EXPORT_C_DECL int WPCTP tReqGenUserCaptcha(CThostFtdcTraderApi *api, CThostFtdcReqGenUserCaptchaField *pReqGenUserCaptcha, int nRequestID){ return api->ReqGenUserCaptcha(pReqGenUserCaptcha, nRequestID); }

// 用户发出获取短信验证码请求
DLL_EXPORT_C_DECL int WPCTP tReqGenUserText(CThostFtdcTraderApi *api, CThostFtdcReqGenUserTextField *pReqGenUserText, int nRequestID){ return api->ReqGenUserText(pReqGenUserText, nRequestID); }

// 用户发出带有图片验证码的登陆请求
DLL_EXPORT_C_DECL int WPCTP tReqUserLoginWithCaptcha(CThostFtdcTraderApi *api, CThostFtdcReqUserLoginWithCaptchaField *pReqUserLoginWithCaptcha, int nRequestID){ return api->ReqUserLoginWithCaptcha(pReqUserLoginWithCaptcha, nRequestID); }

// 用户发出带有短信验证码的登陆请求
DLL_EXPORT_C_DECL int WPCTP tReqUserLoginWithText(CThostFtdcTraderApi *api, CThostFtdcReqUserLoginWithTextField *pReqUserLoginWithText, int nRequestID){ return api->ReqUserLoginWithText(pReqUserLoginWithText, nRequestID); }

// 用户发出带有动态口令的登陆请求
DLL_EXPORT_C_DECL int WPCTP tReqUserLoginWithOTP(CThostFtdcTraderApi *api, CThostFtdcReqUserLoginWithOTPField *pReqUserLoginWithOTP, int nRequestID){ return api->ReqUserLoginWithOTP(pReqUserLoginWithOTP, nRequestID); }

// 报单录入请求
DLL_EXPORT_C_DECL int WPCTP tReqOrderInsert(CThostFtdcTraderApi *api, CThostFtdcInputOrderField *pInputOrder, int nRequestID){ return api->ReqOrderInsert(pInputOrder, nRequestID); }

// 预埋单录入请求
DLL_EXPORT_C_DECL int WPCTP tReqParkedOrderInsert(CThostFtdcTraderApi *api, CThostFtdcParkedOrderField *pParkedOrder, int nRequestID){ return api->ReqParkedOrderInsert(pParkedOrder, nRequestID); }

// 预埋撤单录入请求
DLL_EXPORT_C_DECL int WPCTP tReqParkedOrderAction(CThostFtdcTraderApi *api, CThostFtdcParkedOrderActionField *pParkedOrderAction, int nRequestID){ return api->ReqParkedOrderAction(pParkedOrderAction, nRequestID); }

// 报单操作请求
DLL_EXPORT_C_DECL int WPCTP tReqOrderAction(CThostFtdcTraderApi *api, CThostFtdcInputOrderActionField *pInputOrderAction, int nRequestID){ return api->ReqOrderAction(pInputOrderAction, nRequestID); }

// 查询最大报单数量请求
DLL_EXPORT_C_DECL int WPCTP tReqQryMaxOrderVolume(CThostFtdcTraderApi *api, CThostFtdcQryMaxOrderVolumeField *pQryMaxOrderVolume, int nRequestID){ return api->ReqQryMaxOrderVolume(pQryMaxOrderVolume, nRequestID); }

// 投资者结算结果确认
DLL_EXPORT_C_DECL int WPCTP tReqSettlementInfoConfirm(CThostFtdcTraderApi *api, CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, int nRequestID){ return api->ReqSettlementInfoConfirm(pSettlementInfoConfirm, nRequestID); }

// 请求删除预埋单
DLL_EXPORT_C_DECL int WPCTP tReqRemoveParkedOrder(CThostFtdcTraderApi *api, CThostFtdcRemoveParkedOrderField *pRemoveParkedOrder, int nRequestID){ return api->ReqRemoveParkedOrder(pRemoveParkedOrder, nRequestID); }

// 请求删除预埋撤单
DLL_EXPORT_C_DECL int WPCTP tReqRemoveParkedOrderAction(CThostFtdcTraderApi *api, CThostFtdcRemoveParkedOrderActionField *pRemoveParkedOrderAction, int nRequestID){ return api->ReqRemoveParkedOrderAction(pRemoveParkedOrderAction, nRequestID); }

// 执行宣告录入请求
DLL_EXPORT_C_DECL int WPCTP tReqExecOrderInsert(CThostFtdcTraderApi *api, CThostFtdcInputExecOrderField *pInputExecOrder, int nRequestID){ return api->ReqExecOrderInsert(pInputExecOrder, nRequestID); }

// 执行宣告操作请求
DLL_EXPORT_C_DECL int WPCTP tReqExecOrderAction(CThostFtdcTraderApi *api, CThostFtdcInputExecOrderActionField *pInputExecOrderAction, int nRequestID){ return api->ReqExecOrderAction(pInputExecOrderAction, nRequestID); }

// 询价录入请求
DLL_EXPORT_C_DECL int WPCTP tReqForQuoteInsert(CThostFtdcTraderApi *api, CThostFtdcInputForQuoteField *pInputForQuote, int nRequestID){ return api->ReqForQuoteInsert(pInputForQuote, nRequestID); }

// 报价录入请求
DLL_EXPORT_C_DECL int WPCTP tReqQuoteInsert(CThostFtdcTraderApi *api, CThostFtdcInputQuoteField *pInputQuote, int nRequestID){ return api->ReqQuoteInsert(pInputQuote, nRequestID); }

// 报价操作请求
DLL_EXPORT_C_DECL int WPCTP tReqQuoteAction(CThostFtdcTraderApi *api, CThostFtdcInputQuoteActionField *pInputQuoteAction, int nRequestID){ return api->ReqQuoteAction(pInputQuoteAction, nRequestID); }

// 批量报单操作请求
DLL_EXPORT_C_DECL int WPCTP tReqBatchOrderAction(CThostFtdcTraderApi *api, CThostFtdcInputBatchOrderActionField *pInputBatchOrderAction, int nRequestID){ return api->ReqBatchOrderAction(pInputBatchOrderAction, nRequestID); }

// 期权自对冲录入请求
DLL_EXPORT_C_DECL int WPCTP tReqOptionSelfCloseInsert(CThostFtdcTraderApi *api, CThostFtdcInputOptionSelfCloseField *pInputOptionSelfClose, int nRequestID){ return api->ReqOptionSelfCloseInsert(pInputOptionSelfClose, nRequestID); }

// 期权自对冲操作请求
DLL_EXPORT_C_DECL int WPCTP tReqOptionSelfCloseAction(CThostFtdcTraderApi *api, CThostFtdcInputOptionSelfCloseActionField *pInputOptionSelfCloseAction, int nRequestID){ return api->ReqOptionSelfCloseAction(pInputOptionSelfCloseAction, nRequestID); }

// 申请组合录入请求
DLL_EXPORT_C_DECL int WPCTP tReqCombActionInsert(CThostFtdcTraderApi *api, CThostFtdcInputCombActionField *pInputCombAction, int nRequestID){ return api->ReqCombActionInsert(pInputCombAction, nRequestID); }

// 请求查询报单
DLL_EXPORT_C_DECL int WPCTP tReqQryOrder(CThostFtdcTraderApi *api, CThostFtdcQryOrderField *pQryOrder, int nRequestID){ return api->ReqQryOrder(pQryOrder, nRequestID); }

// 请求查询成交
DLL_EXPORT_C_DECL int WPCTP tReqQryTrade(CThostFtdcTraderApi *api, CThostFtdcQryTradeField *pQryTrade, int nRequestID){ return api->ReqQryTrade(pQryTrade, nRequestID); }

// 请求查询投资者持仓
DLL_EXPORT_C_DECL int WPCTP tReqQryInvestorPosition(CThostFtdcTraderApi *api, CThostFtdcQryInvestorPositionField *pQryInvestorPosition, int nRequestID){ return api->ReqQryInvestorPosition(pQryInvestorPosition, nRequestID); }

// 请求查询资金账户
DLL_EXPORT_C_DECL int WPCTP tReqQryTradingAccount(CThostFtdcTraderApi *api, CThostFtdcQryTradingAccountField *pQryTradingAccount, int nRequestID){ return api->ReqQryTradingAccount(pQryTradingAccount, nRequestID); }

// 请求查询投资者
DLL_EXPORT_C_DECL int WPCTP tReqQryInvestor(CThostFtdcTraderApi *api, CThostFtdcQryInvestorField *pQryInvestor, int nRequestID){ return api->ReqQryInvestor(pQryInvestor, nRequestID); }

// 请求查询交易编码
DLL_EXPORT_C_DECL int WPCTP tReqQryTradingCode(CThostFtdcTraderApi *api, CThostFtdcQryTradingCodeField *pQryTradingCode, int nRequestID){ return api->ReqQryTradingCode(pQryTradingCode, nRequestID); }

// 请求查询合约保证金率
DLL_EXPORT_C_DECL int WPCTP tReqQryInstrumentMarginRate(CThostFtdcTraderApi *api, CThostFtdcQryInstrumentMarginRateField *pQryInstrumentMarginRate, int nRequestID){ return api->ReqQryInstrumentMarginRate(pQryInstrumentMarginRate, nRequestID); }

// 请求查询合约手续费率
DLL_EXPORT_C_DECL int WPCTP tReqQryInstrumentCommissionRate(CThostFtdcTraderApi *api, CThostFtdcQryInstrumentCommissionRateField *pQryInstrumentCommissionRate, int nRequestID){ return api->ReqQryInstrumentCommissionRate(pQryInstrumentCommissionRate, nRequestID); }

// 请求查询交易所
DLL_EXPORT_C_DECL int WPCTP tReqQryExchange(CThostFtdcTraderApi *api, CThostFtdcQryExchangeField *pQryExchange, int nRequestID){ return api->ReqQryExchange(pQryExchange, nRequestID); }

// 请求查询产品
DLL_EXPORT_C_DECL int WPCTP tReqQryProduct(CThostFtdcTraderApi *api, CThostFtdcQryProductField *pQryProduct, int nRequestID){ return api->ReqQryProduct(pQryProduct, nRequestID); }

// 请求查询合约
DLL_EXPORT_C_DECL int WPCTP tReqQryInstrument(CThostFtdcTraderApi *api, CThostFtdcQryInstrumentField *pQryInstrument, int nRequestID){ return api->ReqQryInstrument(pQryInstrument, nRequestID); }

// 请求查询行情
DLL_EXPORT_C_DECL int WPCTP tReqQryDepthMarketData(CThostFtdcTraderApi *api, CThostFtdcQryDepthMarketDataField *pQryDepthMarketData, int nRequestID){ return api->ReqQryDepthMarketData(pQryDepthMarketData, nRequestID); }

// 请求查询交易员报盘机
DLL_EXPORT_C_DECL int WPCTP tReqQryTraderOffer(CThostFtdcTraderApi *api, CThostFtdcQryTraderOfferField *pQryTraderOffer, int nRequestID){ return api->ReqQryTraderOffer(pQryTraderOffer, nRequestID); }

// 请求查询投资者结算结果
DLL_EXPORT_C_DECL int WPCTP tReqQrySettlementInfo(CThostFtdcTraderApi *api, CThostFtdcQrySettlementInfoField *pQrySettlementInfo, int nRequestID){ return api->ReqQrySettlementInfo(pQrySettlementInfo, nRequestID); }

// 请求查询转帐银行
DLL_EXPORT_C_DECL int WPCTP tReqQryTransferBank(CThostFtdcTraderApi *api, CThostFtdcQryTransferBankField *pQryTransferBank, int nRequestID){ return api->ReqQryTransferBank(pQryTransferBank, nRequestID); }

// 请求查询投资者持仓明细
DLL_EXPORT_C_DECL int WPCTP tReqQryInvestorPositionDetail(CThostFtdcTraderApi *api, CThostFtdcQryInvestorPositionDetailField *pQryInvestorPositionDetail, int nRequestID){ return api->ReqQryInvestorPositionDetail(pQryInvestorPositionDetail, nRequestID); }

// 请求查询客户通知
DLL_EXPORT_C_DECL int WPCTP tReqQryNotice(CThostFtdcTraderApi *api, CThostFtdcQryNoticeField *pQryNotice, int nRequestID){ return api->ReqQryNotice(pQryNotice, nRequestID); }

// 请求查询结算信息确认
DLL_EXPORT_C_DECL int WPCTP tReqQrySettlementInfoConfirm(CThostFtdcTraderApi *api, CThostFtdcQrySettlementInfoConfirmField *pQrySettlementInfoConfirm, int nRequestID){ return api->ReqQrySettlementInfoConfirm(pQrySettlementInfoConfirm, nRequestID); }

// 请求查询投资者持仓明细
DLL_EXPORT_C_DECL int WPCTP tReqQryInvestorPositionCombineDetail(CThostFtdcTraderApi *api, CThostFtdcQryInvestorPositionCombineDetailField *pQryInvestorPositionCombineDetail, int nRequestID){ return api->ReqQryInvestorPositionCombineDetail(pQryInvestorPositionCombineDetail, nRequestID); }

// 请求查询保证金监管系统经纪公司资金账户密钥
DLL_EXPORT_C_DECL int WPCTP tReqQryCFMMCTradingAccountKey(CThostFtdcTraderApi *api, CThostFtdcQryCFMMCTradingAccountKeyField *pQryCFMMCTradingAccountKey, int nRequestID){ return api->ReqQryCFMMCTradingAccountKey(pQryCFMMCTradingAccountKey, nRequestID); }

// 请求查询仓单折抵信息
DLL_EXPORT_C_DECL int WPCTP tReqQryEWarrantOffset(CThostFtdcTraderApi *api, CThostFtdcQryEWarrantOffsetField *pQryEWarrantOffset, int nRequestID){ return api->ReqQryEWarrantOffset(pQryEWarrantOffset, nRequestID); }

// 请求查询投资者品种/跨品种保证金
DLL_EXPORT_C_DECL int WPCTP tReqQryInvestorProductGroupMargin(CThostFtdcTraderApi *api, CThostFtdcQryInvestorProductGroupMarginField *pQryInvestorProductGroupMargin, int nRequestID){ return api->ReqQryInvestorProductGroupMargin(pQryInvestorProductGroupMargin, nRequestID); }

// 请求查询交易所保证金率
DLL_EXPORT_C_DECL int WPCTP tReqQryExchangeMarginRate(CThostFtdcTraderApi *api, CThostFtdcQryExchangeMarginRateField *pQryExchangeMarginRate, int nRequestID){ return api->ReqQryExchangeMarginRate(pQryExchangeMarginRate, nRequestID); }

// 请求查询交易所调整保证金率
DLL_EXPORT_C_DECL int WPCTP tReqQryExchangeMarginRateAdjust(CThostFtdcTraderApi *api, CThostFtdcQryExchangeMarginRateAdjustField *pQryExchangeMarginRateAdjust, int nRequestID){ return api->ReqQryExchangeMarginRateAdjust(pQryExchangeMarginRateAdjust, nRequestID); }

// 请求查询汇率
DLL_EXPORT_C_DECL int WPCTP tReqQryExchangeRate(CThostFtdcTraderApi *api, CThostFtdcQryExchangeRateField *pQryExchangeRate, int nRequestID){ return api->ReqQryExchangeRate(pQryExchangeRate, nRequestID); }

// 请求查询二级代理操作员银期权限
DLL_EXPORT_C_DECL int WPCTP tReqQrySecAgentACIDMap(CThostFtdcTraderApi *api, CThostFtdcQrySecAgentACIDMapField *pQrySecAgentACIDMap, int nRequestID){ return api->ReqQrySecAgentACIDMap(pQrySecAgentACIDMap, nRequestID); }

// 请求查询产品报价汇率
DLL_EXPORT_C_DECL int WPCTP tReqQryProductExchRate(CThostFtdcTraderApi *api, CThostFtdcQryProductExchRateField *pQryProductExchRate, int nRequestID){ return api->ReqQryProductExchRate(pQryProductExchRate, nRequestID); }

// 请求查询产品组
DLL_EXPORT_C_DECL int WPCTP tReqQryProductGroup(CThostFtdcTraderApi *api, CThostFtdcQryProductGroupField *pQryProductGroup, int nRequestID){ return api->ReqQryProductGroup(pQryProductGroup, nRequestID); }

// 请求查询做市商合约手续费率
DLL_EXPORT_C_DECL int WPCTP tReqQryMMInstrumentCommissionRate(CThostFtdcTraderApi *api, CThostFtdcQryMMInstrumentCommissionRateField *pQryMMInstrumentCommissionRate, int nRequestID){ return api->ReqQryMMInstrumentCommissionRate(pQryMMInstrumentCommissionRate, nRequestID); }

// 请求查询做市商期权合约手续费
DLL_EXPORT_C_DECL int WPCTP tReqQryMMOptionInstrCommRate(CThostFtdcTraderApi *api, CThostFtdcQryMMOptionInstrCommRateField *pQryMMOptionInstrCommRate, int nRequestID){ return api->ReqQryMMOptionInstrCommRate(pQryMMOptionInstrCommRate, nRequestID); }

// 请求查询报单手续费
DLL_EXPORT_C_DECL int WPCTP tReqQryInstrumentOrderCommRate(CThostFtdcTraderApi *api, CThostFtdcQryInstrumentOrderCommRateField *pQryInstrumentOrderCommRate, int nRequestID){ return api->ReqQryInstrumentOrderCommRate(pQryInstrumentOrderCommRate, nRequestID); }

// 请求查询资金账户
DLL_EXPORT_C_DECL int WPCTP tReqQrySecAgentTradingAccount(CThostFtdcTraderApi *api, CThostFtdcQryTradingAccountField *pQryTradingAccount, int nRequestID){ return api->ReqQrySecAgentTradingAccount(pQryTradingAccount, nRequestID); }

// 请求查询二级代理商资金校验模式
DLL_EXPORT_C_DECL int WPCTP tReqQrySecAgentCheckMode(CThostFtdcTraderApi *api, CThostFtdcQrySecAgentCheckModeField *pQrySecAgentCheckMode, int nRequestID){ return api->ReqQrySecAgentCheckMode(pQrySecAgentCheckMode, nRequestID); }

// 请求查询二级代理商信息
DLL_EXPORT_C_DECL int WPCTP tReqQrySecAgentTradeInfo(CThostFtdcTraderApi *api, CThostFtdcQrySecAgentTradeInfoField *pQrySecAgentTradeInfo, int nRequestID){ return api->ReqQrySecAgentTradeInfo(pQrySecAgentTradeInfo, nRequestID); }

// 请求查询期权交易成本
DLL_EXPORT_C_DECL int WPCTP tReqQryOptionInstrTradeCost(CThostFtdcTraderApi *api, CThostFtdcQryOptionInstrTradeCostField *pQryOptionInstrTradeCost, int nRequestID){ return api->ReqQryOptionInstrTradeCost(pQryOptionInstrTradeCost, nRequestID); }

// 请求查询期权合约手续费
DLL_EXPORT_C_DECL int WPCTP tReqQryOptionInstrCommRate(CThostFtdcTraderApi *api, CThostFtdcQryOptionInstrCommRateField *pQryOptionInstrCommRate, int nRequestID){ return api->ReqQryOptionInstrCommRate(pQryOptionInstrCommRate, nRequestID); }

// 请求查询执行宣告
DLL_EXPORT_C_DECL int WPCTP tReqQryExecOrder(CThostFtdcTraderApi *api, CThostFtdcQryExecOrderField *pQryExecOrder, int nRequestID){ return api->ReqQryExecOrder(pQryExecOrder, nRequestID); }

// 请求查询询价
DLL_EXPORT_C_DECL int WPCTP tReqQryForQuote(CThostFtdcTraderApi *api, CThostFtdcQryForQuoteField *pQryForQuote, int nRequestID){ return api->ReqQryForQuote(pQryForQuote, nRequestID); }

// 请求查询报价
DLL_EXPORT_C_DECL int WPCTP tReqQryQuote(CThostFtdcTraderApi *api, CThostFtdcQryQuoteField *pQryQuote, int nRequestID){ return api->ReqQryQuote(pQryQuote, nRequestID); }

// 请求查询期权自对冲
DLL_EXPORT_C_DECL int WPCTP tReqQryOptionSelfClose(CThostFtdcTraderApi *api, CThostFtdcQryOptionSelfCloseField *pQryOptionSelfClose, int nRequestID){ return api->ReqQryOptionSelfClose(pQryOptionSelfClose, nRequestID); }

// 请求查询投资单元
DLL_EXPORT_C_DECL int WPCTP tReqQryInvestUnit(CThostFtdcTraderApi *api, CThostFtdcQryInvestUnitField *pQryInvestUnit, int nRequestID){ return api->ReqQryInvestUnit(pQryInvestUnit, nRequestID); }

// 请求查询组合合约安全系数
DLL_EXPORT_C_DECL int WPCTP tReqQryCombInstrumentGuard(CThostFtdcTraderApi *api, CThostFtdcQryCombInstrumentGuardField *pQryCombInstrumentGuard, int nRequestID){ return api->ReqQryCombInstrumentGuard(pQryCombInstrumentGuard, nRequestID); }

// 请求查询申请组合
DLL_EXPORT_C_DECL int WPCTP tReqQryCombAction(CThostFtdcTraderApi *api, CThostFtdcQryCombActionField *pQryCombAction, int nRequestID){ return api->ReqQryCombAction(pQryCombAction, nRequestID); }

// 请求查询转帐流水
DLL_EXPORT_C_DECL int WPCTP tReqQryTransferSerial(CThostFtdcTraderApi *api, CThostFtdcQryTransferSerialField *pQryTransferSerial, int nRequestID){ return api->ReqQryTransferSerial(pQryTransferSerial, nRequestID); }

// 请求查询银期签约关系
DLL_EXPORT_C_DECL int WPCTP tReqQryAccountregister(CThostFtdcTraderApi *api, CThostFtdcQryAccountregisterField *pQryAccountregister, int nRequestID){ return api->ReqQryAccountregister(pQryAccountregister, nRequestID); }

// 请求查询签约银行
DLL_EXPORT_C_DECL int WPCTP tReqQryContractBank(CThostFtdcTraderApi *api, CThostFtdcQryContractBankField *pQryContractBank, int nRequestID){ return api->ReqQryContractBank(pQryContractBank, nRequestID); }

// 请求查询预埋单
DLL_EXPORT_C_DECL int WPCTP tReqQryParkedOrder(CThostFtdcTraderApi *api, CThostFtdcQryParkedOrderField *pQryParkedOrder, int nRequestID){ return api->ReqQryParkedOrder(pQryParkedOrder, nRequestID); }

// 请求查询预埋撤单
DLL_EXPORT_C_DECL int WPCTP tReqQryParkedOrderAction(CThostFtdcTraderApi *api, CThostFtdcQryParkedOrderActionField *pQryParkedOrderAction, int nRequestID){ return api->ReqQryParkedOrderAction(pQryParkedOrderAction, nRequestID); }

// 请求查询交易通知
DLL_EXPORT_C_DECL int WPCTP tReqQryTradingNotice(CThostFtdcTraderApi *api, CThostFtdcQryTradingNoticeField *pQryTradingNotice, int nRequestID){ return api->ReqQryTradingNotice(pQryTradingNotice, nRequestID); }

// 请求查询经纪公司交易参数
DLL_EXPORT_C_DECL int WPCTP tReqQryBrokerTradingParams(CThostFtdcTraderApi *api, CThostFtdcQryBrokerTradingParamsField *pQryBrokerTradingParams, int nRequestID){ return api->ReqQryBrokerTradingParams(pQryBrokerTradingParams, nRequestID); }

// 请求查询经纪公司交易算法
DLL_EXPORT_C_DECL int WPCTP tReqQryBrokerTradingAlgos(CThostFtdcTraderApi *api, CThostFtdcQryBrokerTradingAlgosField *pQryBrokerTradingAlgos, int nRequestID){ return api->ReqQryBrokerTradingAlgos(pQryBrokerTradingAlgos, nRequestID); }

// 请求查询监控中心用户令牌
DLL_EXPORT_C_DECL int WPCTP tReqQueryCFMMCTradingAccountToken(CThostFtdcTraderApi *api, CThostFtdcQueryCFMMCTradingAccountTokenField *pQueryCFMMCTradingAccountToken, int nRequestID){ return api->ReqQueryCFMMCTradingAccountToken(pQueryCFMMCTradingAccountToken, nRequestID); }

// 期货发起银行资金转期货请求
DLL_EXPORT_C_DECL int WPCTP tReqFromBankToFutureByFuture(CThostFtdcTraderApi *api, CThostFtdcReqTransferField *pReqTransfer, int nRequestID){ return api->ReqFromBankToFutureByFuture(pReqTransfer, nRequestID); }

// 期货发起期货资金转银行请求
DLL_EXPORT_C_DECL int WPCTP tReqFromFutureToBankByFuture(CThostFtdcTraderApi *api, CThostFtdcReqTransferField *pReqTransfer, int nRequestID){ return api->ReqFromFutureToBankByFuture(pReqTransfer, nRequestID); }

// 期货发起查询银行余额请求
DLL_EXPORT_C_DECL int WPCTP tReqQueryBankAccountMoneyByFuture(CThostFtdcTraderApi *api, CThostFtdcReqQueryAccountField *pReqQueryAccount, int nRequestID){ return api->ReqQueryBankAccountMoneyByFuture(pReqQueryAccount, nRequestID); }

// 请求查询分类合约
DLL_EXPORT_C_DECL int WPCTP tReqQryClassifiedInstrument(CThostFtdcTraderApi *api, CThostFtdcQryClassifiedInstrumentField *pQryClassifiedInstrument, int nRequestID){ return api->ReqQryClassifiedInstrument(pQryClassifiedInstrument, nRequestID); }

// 请求组合优惠比例
DLL_EXPORT_C_DECL int WPCTP tReqQryCombPromotionParam(CThostFtdcTraderApi *api, CThostFtdcQryCombPromotionParamField *pQryCombPromotionParam, int nRequestID){ return api->ReqQryCombPromotionParam(pQryCombPromotionParam, nRequestID); }

// 投资者风险结算持仓查询
DLL_EXPORT_C_DECL int WPCTP tReqQryRiskSettleInvstPosition(CThostFtdcTraderApi *api, CThostFtdcQryRiskSettleInvstPositionField *pQryRiskSettleInvstPosition, int nRequestID){ return api->ReqQryRiskSettleInvstPosition(pQryRiskSettleInvstPosition, nRequestID); }

// 风险结算产品查询
DLL_EXPORT_C_DECL int WPCTP tReqQryRiskSettleProductStatus(CThostFtdcTraderApi *api, CThostFtdcQryRiskSettleProductStatusField *pQryRiskSettleProductStatus, int nRequestID){ return api->ReqQryRiskSettleProductStatus(pQryRiskSettleProductStatus, nRequestID); }

// SPBM期货合约参数查询
DLL_EXPORT_C_DECL int WPCTP tReqQrySPBMFutureParameter(CThostFtdcTraderApi *api, CThostFtdcQrySPBMFutureParameterField *pQrySPBMFutureParameter, int nRequestID){ return api->ReqQrySPBMFutureParameter(pQrySPBMFutureParameter, nRequestID); }

// SPBM期权合约参数查询
DLL_EXPORT_C_DECL int WPCTP tReqQrySPBMOptionParameter(CThostFtdcTraderApi *api, CThostFtdcQrySPBMOptionParameterField *pQrySPBMOptionParameter, int nRequestID){ return api->ReqQrySPBMOptionParameter(pQrySPBMOptionParameter, nRequestID); }

// SPBM品种内对锁仓折扣参数查询
DLL_EXPORT_C_DECL int WPCTP tReqQrySPBMIntraParameter(CThostFtdcTraderApi *api, CThostFtdcQrySPBMIntraParameterField *pQrySPBMIntraParameter, int nRequestID){ return api->ReqQrySPBMIntraParameter(pQrySPBMIntraParameter, nRequestID); }

// SPBM跨品种抵扣参数查询
DLL_EXPORT_C_DECL int WPCTP tReqQrySPBMInterParameter(CThostFtdcTraderApi *api, CThostFtdcQrySPBMInterParameterField *pQrySPBMInterParameter, int nRequestID){ return api->ReqQrySPBMInterParameter(pQrySPBMInterParameter, nRequestID); }

// SPBM组合保证金套餐查询
DLL_EXPORT_C_DECL int WPCTP tReqQrySPBMPortfDefinition(CThostFtdcTraderApi *api, CThostFtdcQrySPBMPortfDefinitionField *pQrySPBMPortfDefinition, int nRequestID){ return api->ReqQrySPBMPortfDefinition(pQrySPBMPortfDefinition, nRequestID); }

// 投资者SPBM套餐选择查询
DLL_EXPORT_C_DECL int WPCTP tReqQrySPBMInvestorPortfDef(CThostFtdcTraderApi *api, CThostFtdcQrySPBMInvestorPortfDefField *pQrySPBMInvestorPortfDef, int nRequestID){ return api->ReqQrySPBMInvestorPortfDef(pQrySPBMInvestorPortfDef, nRequestID); }

// 投资者新型组合保证金系数查询
DLL_EXPORT_C_DECL int WPCTP tReqQryInvestorPortfMarginRatio(CThostFtdcTraderApi *api, CThostFtdcQryInvestorPortfMarginRatioField *pQryInvestorPortfMarginRatio, int nRequestID){ return api->ReqQryInvestorPortfMarginRatio(pQryInvestorPortfMarginRatio, nRequestID); }

// 投资者产品SPBM明细查询
DLL_EXPORT_C_DECL int WPCTP tReqQryInvestorProdSPBMDetail(CThostFtdcTraderApi *api, CThostFtdcQryInvestorProdSPBMDetailField *pQryInvestorProdSPBMDetail, int nRequestID){ return api->ReqQryInvestorProdSPBMDetail(pQryInvestorProdSPBMDetail, nRequestID); }
