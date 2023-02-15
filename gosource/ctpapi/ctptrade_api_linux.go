package ctpapi

/*
#cgo LDFLAGS: -L${SRCDIR}/../../libs/ctpapi -lctptrade_api
#include "cctptrade_api_linux.h"
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

    // 当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。
    OnFrontConnected_ func()
    // 当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。
    OnFrontDisconnected_ func(nReason int)
    // 心跳超时警告。当长时间未收到报文时，该方法被调用。
    OnHeartBeatWarning_ func(nTimeLapse int)
    // 客户端认证响应
    OnRspAuthenticate_ func(pRspAuthenticateField *CThostFtdcRspAuthenticateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 登录请求响应
    OnRspUserLogin_ func(pRspUserLogin *CThostFtdcRspUserLoginField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 登出请求响应
    OnRspUserLogout_ func(pUserLogout *CThostFtdcUserLogoutField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 用户口令更新请求响应
    OnRspUserPasswordUpdate_ func(pUserPasswordUpdate *CThostFtdcUserPasswordUpdateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 资金账户口令更新请求响应
    OnRspTradingAccountPasswordUpdate_ func(pTradingAccountPasswordUpdate *CThostFtdcTradingAccountPasswordUpdateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 查询用户当前支持的认证模式的回复
    OnRspUserAuthMethod_ func(pRspUserAuthMethod *CThostFtdcRspUserAuthMethodField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 获取图形验证码请求的回复
    OnRspGenUserCaptcha_ func(pRspGenUserCaptcha *CThostFtdcRspGenUserCaptchaField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 获取短信验证码请求的回复
    OnRspGenUserText_ func(pRspGenUserText *CThostFtdcRspGenUserTextField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 报单录入请求响应
    OnRspOrderInsert_ func(pInputOrder *CThostFtdcInputOrderField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 预埋单录入请求响应
    OnRspParkedOrderInsert_ func(pParkedOrder *CThostFtdcParkedOrderField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 预埋撤单录入请求响应
    OnRspParkedOrderAction_ func(pParkedOrderAction *CThostFtdcParkedOrderActionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 报单操作请求响应
    OnRspOrderAction_ func(pInputOrderAction *CThostFtdcInputOrderActionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 查询最大报单数量响应
    OnRspQryMaxOrderVolume_ func(pQryMaxOrderVolume *CThostFtdcQryMaxOrderVolumeField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 投资者结算结果确认响应
    OnRspSettlementInfoConfirm_ func(pSettlementInfoConfirm *CThostFtdcSettlementInfoConfirmField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 删除预埋单响应
    OnRspRemoveParkedOrder_ func(pRemoveParkedOrder *CThostFtdcRemoveParkedOrderField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 删除预埋撤单响应
    OnRspRemoveParkedOrderAction_ func(pRemoveParkedOrderAction *CThostFtdcRemoveParkedOrderActionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 执行宣告录入请求响应
    OnRspExecOrderInsert_ func(pInputExecOrder *CThostFtdcInputExecOrderField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 执行宣告操作请求响应
    OnRspExecOrderAction_ func(pInputExecOrderAction *CThostFtdcInputExecOrderActionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 询价录入请求响应
    OnRspForQuoteInsert_ func(pInputForQuote *CThostFtdcInputForQuoteField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 报价录入请求响应
    OnRspQuoteInsert_ func(pInputQuote *CThostFtdcInputQuoteField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 报价操作请求响应
    OnRspQuoteAction_ func(pInputQuoteAction *CThostFtdcInputQuoteActionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 批量报单操作请求响应
    OnRspBatchOrderAction_ func(pInputBatchOrderAction *CThostFtdcInputBatchOrderActionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 期权自对冲录入请求响应
    OnRspOptionSelfCloseInsert_ func(pInputOptionSelfClose *CThostFtdcInputOptionSelfCloseField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 期权自对冲操作请求响应
    OnRspOptionSelfCloseAction_ func(pInputOptionSelfCloseAction *CThostFtdcInputOptionSelfCloseActionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 申请组合录入请求响应
    OnRspCombActionInsert_ func(pInputCombAction *CThostFtdcInputCombActionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询报单响应
    OnRspQryOrder_ func(pOrder *CThostFtdcOrderField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询成交响应
    OnRspQryTrade_ func(pTrade *CThostFtdcTradeField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询投资者持仓响应
    OnRspQryInvestorPosition_ func(pInvestorPosition *CThostFtdcInvestorPositionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询资金账户响应
    OnRspQryTradingAccount_ func(pTradingAccount *CThostFtdcTradingAccountField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询投资者响应
    OnRspQryInvestor_ func(pInvestor *CThostFtdcInvestorField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询交易编码响应
    OnRspQryTradingCode_ func(pTradingCode *CThostFtdcTradingCodeField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询合约保证金率响应
    OnRspQryInstrumentMarginRate_ func(pInstrumentMarginRate *CThostFtdcInstrumentMarginRateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询合约手续费率响应
    OnRspQryInstrumentCommissionRate_ func(pInstrumentCommissionRate *CThostFtdcInstrumentCommissionRateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询交易所响应
    OnRspQryExchange_ func(pExchange *CThostFtdcExchangeField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询产品响应
    OnRspQryProduct_ func(pProduct *CThostFtdcProductField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询合约响应
    OnRspQryInstrument_ func(pInstrument *CThostFtdcInstrumentField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询行情响应
    OnRspQryDepthMarketData_ func(pDepthMarketData *CThostFtdcDepthMarketDataField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询交易员报盘机响应
    OnRspQryTraderOffer_ func(pTraderOffer *CThostFtdcTraderOfferField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询投资者结算结果响应
    OnRspQrySettlementInfo_ func(pSettlementInfo *CThostFtdcSettlementInfoField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询转帐银行响应
    OnRspQryTransferBank_ func(pTransferBank *CThostFtdcTransferBankField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询投资者持仓明细响应
    OnRspQryInvestorPositionDetail_ func(pInvestorPositionDetail *CThostFtdcInvestorPositionDetailField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询客户通知响应
    OnRspQryNotice_ func(pNotice *CThostFtdcNoticeField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询结算信息确认响应
    OnRspQrySettlementInfoConfirm_ func(pSettlementInfoConfirm *CThostFtdcSettlementInfoConfirmField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询投资者持仓明细响应
    OnRspQryInvestorPositionCombineDetail_ func(pInvestorPositionCombineDetail *CThostFtdcInvestorPositionCombineDetailField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 查询保证金监管系统经纪公司资金账户密钥响应
    OnRspQryCFMMCTradingAccountKey_ func(pCFMMCTradingAccountKey *CThostFtdcCFMMCTradingAccountKeyField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询仓单折抵信息响应
    OnRspQryEWarrantOffset_ func(pEWarrantOffset *CThostFtdcEWarrantOffsetField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询投资者品种/跨品种保证金响应
    OnRspQryInvestorProductGroupMargin_ func(pInvestorProductGroupMargin *CThostFtdcInvestorProductGroupMarginField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询交易所保证金率响应
    OnRspQryExchangeMarginRate_ func(pExchangeMarginRate *CThostFtdcExchangeMarginRateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询交易所调整保证金率响应
    OnRspQryExchangeMarginRateAdjust_ func(pExchangeMarginRateAdjust *CThostFtdcExchangeMarginRateAdjustField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询汇率响应
    OnRspQryExchangeRate_ func(pExchangeRate *CThostFtdcExchangeRateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询二级代理操作员银期权限响应
    OnRspQrySecAgentACIDMap_ func(pSecAgentACIDMap *CThostFtdcSecAgentACIDMapField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询产品报价汇率
    OnRspQryProductExchRate_ func(pProductExchRate *CThostFtdcProductExchRateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询产品组
    OnRspQryProductGroup_ func(pProductGroup *CThostFtdcProductGroupField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询做市商合约手续费率响应
    OnRspQryMMInstrumentCommissionRate_ func(pMMInstrumentCommissionRate *CThostFtdcMMInstrumentCommissionRateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询做市商期权合约手续费响应
    OnRspQryMMOptionInstrCommRate_ func(pMMOptionInstrCommRate *CThostFtdcMMOptionInstrCommRateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询报单手续费响应
    OnRspQryInstrumentOrderCommRate_ func(pInstrumentOrderCommRate *CThostFtdcInstrumentOrderCommRateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询资金账户响应
    OnRspQrySecAgentTradingAccount_ func(pTradingAccount *CThostFtdcTradingAccountField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询二级代理商资金校验模式响应
    OnRspQrySecAgentCheckMode_ func(pSecAgentCheckMode *CThostFtdcSecAgentCheckModeField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询二级代理商信息响应
    OnRspQrySecAgentTradeInfo_ func(pSecAgentTradeInfo *CThostFtdcSecAgentTradeInfoField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询期权交易成本响应
    OnRspQryOptionInstrTradeCost_ func(pOptionInstrTradeCost *CThostFtdcOptionInstrTradeCostField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询期权合约手续费响应
    OnRspQryOptionInstrCommRate_ func(pOptionInstrCommRate *CThostFtdcOptionInstrCommRateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询执行宣告响应
    OnRspQryExecOrder_ func(pExecOrder *CThostFtdcExecOrderField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询询价响应
    OnRspQryForQuote_ func(pForQuote *CThostFtdcForQuoteField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询报价响应
    OnRspQryQuote_ func(pQuote *CThostFtdcQuoteField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询期权自对冲响应
    OnRspQryOptionSelfClose_ func(pOptionSelfClose *CThostFtdcOptionSelfCloseField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询投资单元响应
    OnRspQryInvestUnit_ func(pInvestUnit *CThostFtdcInvestUnitField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询组合合约安全系数响应
    OnRspQryCombInstrumentGuard_ func(pCombInstrumentGuard *CThostFtdcCombInstrumentGuardField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询申请组合响应
    OnRspQryCombAction_ func(pCombAction *CThostFtdcCombActionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询转帐流水响应
    OnRspQryTransferSerial_ func(pTransferSerial *CThostFtdcTransferSerialField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询银期签约关系响应
    OnRspQryAccountregister_ func(pAccountregister *CThostFtdcAccountregisterField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 错误应答
    OnRspError_ func(pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 报单通知
    OnRtnOrder_ func(pOrder *CThostFtdcOrderField)
    // 成交通知
    OnRtnTrade_ func(pTrade *CThostFtdcTradeField)
    // 报单录入错误回报
    OnErrRtnOrderInsert_ func(pInputOrder *CThostFtdcInputOrderField, pRspInfo *CThostFtdcRspInfoField)
    // 报单操作错误回报
    OnErrRtnOrderAction_ func(pOrderAction *CThostFtdcOrderActionField, pRspInfo *CThostFtdcRspInfoField)
    // 合约交易状态通知
    OnRtnInstrumentStatus_ func(pInstrumentStatus *CThostFtdcInstrumentStatusField)
    // 交易所公告通知
    OnRtnBulletin_ func(pBulletin *CThostFtdcBulletinField)
    // 交易通知
    OnRtnTradingNotice_ func(pTradingNoticeInfo *CThostFtdcTradingNoticeInfoField)
    // 提示条件单校验错误
    OnRtnErrorConditionalOrder_ func(pErrorConditionalOrder *CThostFtdcErrorConditionalOrderField)
    // 执行宣告通知
    OnRtnExecOrder_ func(pExecOrder *CThostFtdcExecOrderField)
    // 执行宣告录入错误回报
    OnErrRtnExecOrderInsert_ func(pInputExecOrder *CThostFtdcInputExecOrderField, pRspInfo *CThostFtdcRspInfoField)
    // 执行宣告操作错误回报
    OnErrRtnExecOrderAction_ func(pExecOrderAction *CThostFtdcExecOrderActionField, pRspInfo *CThostFtdcRspInfoField)
    // 询价录入错误回报
    OnErrRtnForQuoteInsert_ func(pInputForQuote *CThostFtdcInputForQuoteField, pRspInfo *CThostFtdcRspInfoField)
    // 报价通知
    OnRtnQuote_ func(pQuote *CThostFtdcQuoteField)
    // 报价录入错误回报
    OnErrRtnQuoteInsert_ func(pInputQuote *CThostFtdcInputQuoteField, pRspInfo *CThostFtdcRspInfoField)
    // 报价操作错误回报
    OnErrRtnQuoteAction_ func(pQuoteAction *CThostFtdcQuoteActionField, pRspInfo *CThostFtdcRspInfoField)
    // 询价通知
    OnRtnForQuoteRsp_ func(pForQuoteRsp *CThostFtdcForQuoteRspField)
    // 保证金监控中心用户令牌
    OnRtnCFMMCTradingAccountToken_ func(pCFMMCTradingAccountToken *CThostFtdcCFMMCTradingAccountTokenField)
    // 批量报单操作错误回报
    OnErrRtnBatchOrderAction_ func(pBatchOrderAction *CThostFtdcBatchOrderActionField, pRspInfo *CThostFtdcRspInfoField)
    // 期权自对冲通知
    OnRtnOptionSelfClose_ func(pOptionSelfClose *CThostFtdcOptionSelfCloseField)
    // 期权自对冲录入错误回报
    OnErrRtnOptionSelfCloseInsert_ func(pInputOptionSelfClose *CThostFtdcInputOptionSelfCloseField, pRspInfo *CThostFtdcRspInfoField)
    // 期权自对冲操作错误回报
    OnErrRtnOptionSelfCloseAction_ func(pOptionSelfCloseAction *CThostFtdcOptionSelfCloseActionField, pRspInfo *CThostFtdcRspInfoField)
    // 申请组合通知
    OnRtnCombAction_ func(pCombAction *CThostFtdcCombActionField)
    // 申请组合录入错误回报
    OnErrRtnCombActionInsert_ func(pInputCombAction *CThostFtdcInputCombActionField, pRspInfo *CThostFtdcRspInfoField)
    // 请求查询签约银行响应
    OnRspQryContractBank_ func(pContractBank *CThostFtdcContractBankField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询预埋单响应
    OnRspQryParkedOrder_ func(pParkedOrder *CThostFtdcParkedOrderField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询预埋撤单响应
    OnRspQryParkedOrderAction_ func(pParkedOrderAction *CThostFtdcParkedOrderActionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询交易通知响应
    OnRspQryTradingNotice_ func(pTradingNotice *CThostFtdcTradingNoticeField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询经纪公司交易参数响应
    OnRspQryBrokerTradingParams_ func(pBrokerTradingParams *CThostFtdcBrokerTradingParamsField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询经纪公司交易算法响应
    OnRspQryBrokerTradingAlgos_ func(pBrokerTradingAlgos *CThostFtdcBrokerTradingAlgosField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求查询监控中心用户令牌
    OnRspQueryCFMMCTradingAccountToken_ func(pQueryCFMMCTradingAccountToken *CThostFtdcQueryCFMMCTradingAccountTokenField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 银行发起银行资金转期货通知
    OnRtnFromBankToFutureByBank_ func(pRspTransfer *CThostFtdcRspTransferField)
    // 银行发起期货资金转银行通知
    OnRtnFromFutureToBankByBank_ func(pRspTransfer *CThostFtdcRspTransferField)
    // 银行发起冲正银行转期货通知
    OnRtnRepealFromBankToFutureByBank_ func(pRspRepeal *CThostFtdcRspRepealField)
    // 银行发起冲正期货转银行通知
    OnRtnRepealFromFutureToBankByBank_ func(pRspRepeal *CThostFtdcRspRepealField)
    // 期货发起银行资金转期货通知
    OnRtnFromBankToFutureByFuture_ func(pRspTransfer *CThostFtdcRspTransferField)
    // 期货发起期货资金转银行通知
    OnRtnFromFutureToBankByFuture_ func(pRspTransfer *CThostFtdcRspTransferField)
    // 系统运行时期货端手工发起冲正银行转期货请求，银行处理完毕后报盘发回的通知
    OnRtnRepealFromBankToFutureByFutureManual_ func(pRspRepeal *CThostFtdcRspRepealField)
    // 系统运行时期货端手工发起冲正期货转银行请求，银行处理完毕后报盘发回的通知
    OnRtnRepealFromFutureToBankByFutureManual_ func(pRspRepeal *CThostFtdcRspRepealField)
    // 期货发起查询银行余额通知
    OnRtnQueryBankBalanceByFuture_ func(pNotifyQueryAccount *CThostFtdcNotifyQueryAccountField)
    // 期货发起银行资金转期货错误回报
    OnErrRtnBankToFutureByFuture_ func(pReqTransfer *CThostFtdcReqTransferField, pRspInfo *CThostFtdcRspInfoField)
    // 期货发起期货资金转银行错误回报
    OnErrRtnFutureToBankByFuture_ func(pReqTransfer *CThostFtdcReqTransferField, pRspInfo *CThostFtdcRspInfoField)
    // 系统运行时期货端手工发起冲正银行转期货错误回报
    OnErrRtnRepealBankToFutureByFutureManual_ func(pReqRepeal *CThostFtdcReqRepealField, pRspInfo *CThostFtdcRspInfoField)
    // 系统运行时期货端手工发起冲正期货转银行错误回报
    OnErrRtnRepealFutureToBankByFutureManual_ func(pReqRepeal *CThostFtdcReqRepealField, pRspInfo *CThostFtdcRspInfoField)
    // 期货发起查询银行余额错误回报
    OnErrRtnQueryBankBalanceByFuture_ func(pReqQueryAccount *CThostFtdcReqQueryAccountField, pRspInfo *CThostFtdcRspInfoField)
    // 期货发起冲正银行转期货请求，银行处理完毕后报盘发回的通知
    OnRtnRepealFromBankToFutureByFuture_ func(pRspRepeal *CThostFtdcRspRepealField)
    // 期货发起冲正期货转银行请求，银行处理完毕后报盘发回的通知
    OnRtnRepealFromFutureToBankByFuture_ func(pRspRepeal *CThostFtdcRspRepealField)
    // 期货发起银行资金转期货应答
    OnRspFromBankToFutureByFuture_ func(pReqTransfer *CThostFtdcReqTransferField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 期货发起期货资金转银行应答
    OnRspFromFutureToBankByFuture_ func(pReqTransfer *CThostFtdcReqTransferField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 期货发起查询银行余额应答
    OnRspQueryBankAccountMoneyByFuture_ func(pReqQueryAccount *CThostFtdcReqQueryAccountField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 银行发起银期开户通知
    OnRtnOpenAccountByBank_ func(pOpenAccount *CThostFtdcOpenAccountField)
    // 银行发起银期销户通知
    OnRtnCancelAccountByBank_ func(pCancelAccount *CThostFtdcCancelAccountField)
    // 银行发起变更银行账号通知
    OnRtnChangeAccountByBank_ func(pChangeAccount *CThostFtdcChangeAccountField)
    // 请求查询分类合约响应
    OnRspQryClassifiedInstrument_ func(pInstrument *CThostFtdcInstrumentField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 请求组合优惠比例响应
    OnRspQryCombPromotionParam_ func(pCombPromotionParam *CThostFtdcCombPromotionParamField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 投资者风险结算持仓查询响应
    OnRspQryRiskSettleInvstPosition_ func(pRiskSettleInvstPosition *CThostFtdcRiskSettleInvstPositionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 风险结算产品查询响应
    OnRspQryRiskSettleProductStatus_ func(pRiskSettleProductStatus *CThostFtdcRiskSettleProductStatusField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // SPBM期货合约参数查询响应
    OnRspQrySPBMFutureParameter_ func(pSPBMFutureParameter *CThostFtdcSPBMFutureParameterField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // SPBM期权合约参数查询响应
    OnRspQrySPBMOptionParameter_ func(pSPBMOptionParameter *CThostFtdcSPBMOptionParameterField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // SPBM品种内对锁仓折扣参数查询响应
    OnRspQrySPBMIntraParameter_ func(pSPBMIntraParameter *CThostFtdcSPBMIntraParameterField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // SPBM跨品种抵扣参数查询响应
    OnRspQrySPBMInterParameter_ func(pSPBMInterParameter *CThostFtdcSPBMInterParameterField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // SPBM组合保证金套餐查询响应
    OnRspQrySPBMPortfDefinition_ func(pSPBMPortfDefinition *CThostFtdcSPBMPortfDefinitionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 投资者SPBM套餐选择查询响应
    OnRspQrySPBMInvestorPortfDef_ func(pSPBMInvestorPortfDef *CThostFtdcSPBMInvestorPortfDefField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 投资者新型组合保证金系数查询响应
    OnRspQryInvestorPortfMarginRatio_ func(pInvestorPortfMarginRatio *CThostFtdcInvestorPortfMarginRatioField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    // 投资者产品SPBM明细查询响应
    OnRspQryInvestorProdSPBMDetail_ func(pInvestorProdSPBMDetail *CThostFtdcInvestorProdSPBMDetailField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)
    
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



func (t *Trade) CTP_GetDataCollectApiVersion() string {
	return C.GoString((*C.char)(C.dCTP_GetDataCollectApiVersion()))
}

func (t *Trade) Release() { 
	  
	C.tRelease(t.api)
}

func (t *Trade) Init() { 
	  
	C.tInit(t.api)
}

func (t *Trade) Join() int32 {
	  
	res := C.tJoin(t.api)
	return int32(res)
}

func (t *Trade) RegisterFront(pszFrontAddress []byte) { 
	    
	C.tRegisterFront(t.api, (*C.char)(unsafe.Pointer(C.CBytes(pszFrontAddress))))
}

func (t *Trade) RegisterNameServer(pszNsAddress []byte) { 
	    
	C.tRegisterNameServer(t.api, (*C.char)(unsafe.Pointer(C.CBytes(pszNsAddress))))
}

func (t *Trade) RegisterFensUserInfo( pFensUserInfo *CThostFtdcFensUserInfoField) { 
	    
	C.tRegisterFensUserInfo(t.api, (*C.struct_CThostFtdcFensUserInfoField)(unsafe.Pointer( pFensUserInfo)))
}

func (t *Trade) RegisterSpi() { 
	    
	C.tRegisterSpi(t.api, t.pSpi)
}

func (t *Trade) SubscribePrivateTopic(nResumeType THOST_TE_RESUME_TYPE) { 
	    
	C.tSubscribePrivateTopic(t.api, C.int(nResumeType))
}

func (t *Trade) SubscribePublicTopic(nResumeType THOST_TE_RESUME_TYPE) { 
	    
	C.tSubscribePublicTopic(t.api, C.int(nResumeType))
}

func (t *Trade) ReqAuthenticate(pReqAuthenticateField *CThostFtdcReqAuthenticateField, nRequestID int) int32 {
	      
	res := C.tReqAuthenticate(t.api, (*C.struct_CThostFtdcReqAuthenticateField)(unsafe.Pointer(pReqAuthenticateField)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) RegisterUserSystemInfo(pUserSystemInfo *CThostFtdcUserSystemInfoField) int32 {
	    
	res := C.tRegisterUserSystemInfo(t.api, (*C.struct_CThostFtdcUserSystemInfoField)(unsafe.Pointer(pUserSystemInfo)))
	return int32(res)
}

func (t *Trade) SubmitUserSystemInfo(pUserSystemInfo *CThostFtdcUserSystemInfoField) int32 {
	    
	res := C.tSubmitUserSystemInfo(t.api, (*C.struct_CThostFtdcUserSystemInfoField)(unsafe.Pointer(pUserSystemInfo)))
	return int32(res)
}

func (t *Trade) ReqUserLogin(pReqUserLoginField *CThostFtdcReqUserLoginField, nRequestID int) int32 {
	      
	res := C.tReqUserLogin(t.api, (*C.struct_CThostFtdcReqUserLoginField)(unsafe.Pointer(pReqUserLoginField)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqUserLogout(pUserLogout *CThostFtdcUserLogoutField, nRequestID int) int32 {
	      
	res := C.tReqUserLogout(t.api, (*C.struct_CThostFtdcUserLogoutField)(unsafe.Pointer(pUserLogout)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqUserPasswordUpdate(pUserPasswordUpdate *CThostFtdcUserPasswordUpdateField, nRequestID int) int32 {
	      
	res := C.tReqUserPasswordUpdate(t.api, (*C.struct_CThostFtdcUserPasswordUpdateField)(unsafe.Pointer(pUserPasswordUpdate)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqTradingAccountPasswordUpdate(pTradingAccountPasswordUpdate *CThostFtdcTradingAccountPasswordUpdateField, nRequestID int) int32 {
	      
	res := C.tReqTradingAccountPasswordUpdate(t.api, (*C.struct_CThostFtdcTradingAccountPasswordUpdateField)(unsafe.Pointer(pTradingAccountPasswordUpdate)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqUserAuthMethod(pReqUserAuthMethod *CThostFtdcReqUserAuthMethodField, nRequestID int) int32 {
	      
	res := C.tReqUserAuthMethod(t.api, (*C.struct_CThostFtdcReqUserAuthMethodField)(unsafe.Pointer(pReqUserAuthMethod)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqGenUserCaptcha(pReqGenUserCaptcha *CThostFtdcReqGenUserCaptchaField, nRequestID int) int32 {
	      
	res := C.tReqGenUserCaptcha(t.api, (*C.struct_CThostFtdcReqGenUserCaptchaField)(unsafe.Pointer(pReqGenUserCaptcha)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqGenUserText(pReqGenUserText *CThostFtdcReqGenUserTextField, nRequestID int) int32 {
	      
	res := C.tReqGenUserText(t.api, (*C.struct_CThostFtdcReqGenUserTextField)(unsafe.Pointer(pReqGenUserText)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqUserLoginWithCaptcha(pReqUserLoginWithCaptcha *CThostFtdcReqUserLoginWithCaptchaField, nRequestID int) int32 {
	      
	res := C.tReqUserLoginWithCaptcha(t.api, (*C.struct_CThostFtdcReqUserLoginWithCaptchaField)(unsafe.Pointer(pReqUserLoginWithCaptcha)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqUserLoginWithText(pReqUserLoginWithText *CThostFtdcReqUserLoginWithTextField, nRequestID int) int32 {
	      
	res := C.tReqUserLoginWithText(t.api, (*C.struct_CThostFtdcReqUserLoginWithTextField)(unsafe.Pointer(pReqUserLoginWithText)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqUserLoginWithOTP(pReqUserLoginWithOTP *CThostFtdcReqUserLoginWithOTPField, nRequestID int) int32 {
	      
	res := C.tReqUserLoginWithOTP(t.api, (*C.struct_CThostFtdcReqUserLoginWithOTPField)(unsafe.Pointer(pReqUserLoginWithOTP)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqOrderInsert(pInputOrder *CThostFtdcInputOrderField, nRequestID int) int32 {
	      
	res := C.tReqOrderInsert(t.api, (*C.struct_CThostFtdcInputOrderField)(unsafe.Pointer(pInputOrder)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqParkedOrderInsert(pParkedOrder *CThostFtdcParkedOrderField, nRequestID int) int32 {
	      
	res := C.tReqParkedOrderInsert(t.api, (*C.struct_CThostFtdcParkedOrderField)(unsafe.Pointer(pParkedOrder)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqParkedOrderAction(pParkedOrderAction *CThostFtdcParkedOrderActionField, nRequestID int) int32 {
	      
	res := C.tReqParkedOrderAction(t.api, (*C.struct_CThostFtdcParkedOrderActionField)(unsafe.Pointer(pParkedOrderAction)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqOrderAction(pInputOrderAction *CThostFtdcInputOrderActionField, nRequestID int) int32 {
	      
	res := C.tReqOrderAction(t.api, (*C.struct_CThostFtdcInputOrderActionField)(unsafe.Pointer(pInputOrderAction)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryMaxOrderVolume(pQryMaxOrderVolume *CThostFtdcQryMaxOrderVolumeField, nRequestID int) int32 {
	      
	res := C.tReqQryMaxOrderVolume(t.api, (*C.struct_CThostFtdcQryMaxOrderVolumeField)(unsafe.Pointer(pQryMaxOrderVolume)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqSettlementInfoConfirm(pSettlementInfoConfirm *CThostFtdcSettlementInfoConfirmField, nRequestID int) int32 {
	      
	res := C.tReqSettlementInfoConfirm(t.api, (*C.struct_CThostFtdcSettlementInfoConfirmField)(unsafe.Pointer(pSettlementInfoConfirm)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqRemoveParkedOrder(pRemoveParkedOrder *CThostFtdcRemoveParkedOrderField, nRequestID int) int32 {
	      
	res := C.tReqRemoveParkedOrder(t.api, (*C.struct_CThostFtdcRemoveParkedOrderField)(unsafe.Pointer(pRemoveParkedOrder)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqRemoveParkedOrderAction(pRemoveParkedOrderAction *CThostFtdcRemoveParkedOrderActionField, nRequestID int) int32 {
	      
	res := C.tReqRemoveParkedOrderAction(t.api, (*C.struct_CThostFtdcRemoveParkedOrderActionField)(unsafe.Pointer(pRemoveParkedOrderAction)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqExecOrderInsert(pInputExecOrder *CThostFtdcInputExecOrderField, nRequestID int) int32 {
	      
	res := C.tReqExecOrderInsert(t.api, (*C.struct_CThostFtdcInputExecOrderField)(unsafe.Pointer(pInputExecOrder)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqExecOrderAction(pInputExecOrderAction *CThostFtdcInputExecOrderActionField, nRequestID int) int32 {
	      
	res := C.tReqExecOrderAction(t.api, (*C.struct_CThostFtdcInputExecOrderActionField)(unsafe.Pointer(pInputExecOrderAction)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqForQuoteInsert(pInputForQuote *CThostFtdcInputForQuoteField, nRequestID int) int32 {
	      
	res := C.tReqForQuoteInsert(t.api, (*C.struct_CThostFtdcInputForQuoteField)(unsafe.Pointer(pInputForQuote)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQuoteInsert(pInputQuote *CThostFtdcInputQuoteField, nRequestID int) int32 {
	      
	res := C.tReqQuoteInsert(t.api, (*C.struct_CThostFtdcInputQuoteField)(unsafe.Pointer(pInputQuote)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQuoteAction(pInputQuoteAction *CThostFtdcInputQuoteActionField, nRequestID int) int32 {
	      
	res := C.tReqQuoteAction(t.api, (*C.struct_CThostFtdcInputQuoteActionField)(unsafe.Pointer(pInputQuoteAction)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqBatchOrderAction(pInputBatchOrderAction *CThostFtdcInputBatchOrderActionField, nRequestID int) int32 {
	      
	res := C.tReqBatchOrderAction(t.api, (*C.struct_CThostFtdcInputBatchOrderActionField)(unsafe.Pointer(pInputBatchOrderAction)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqOptionSelfCloseInsert(pInputOptionSelfClose *CThostFtdcInputOptionSelfCloseField, nRequestID int) int32 {
	      
	res := C.tReqOptionSelfCloseInsert(t.api, (*C.struct_CThostFtdcInputOptionSelfCloseField)(unsafe.Pointer(pInputOptionSelfClose)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqOptionSelfCloseAction(pInputOptionSelfCloseAction *CThostFtdcInputOptionSelfCloseActionField, nRequestID int) int32 {
	      
	res := C.tReqOptionSelfCloseAction(t.api, (*C.struct_CThostFtdcInputOptionSelfCloseActionField)(unsafe.Pointer(pInputOptionSelfCloseAction)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqCombActionInsert(pInputCombAction *CThostFtdcInputCombActionField, nRequestID int) int32 {
	      
	res := C.tReqCombActionInsert(t.api, (*C.struct_CThostFtdcInputCombActionField)(unsafe.Pointer(pInputCombAction)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryOrder(pQryOrder *CThostFtdcQryOrderField, nRequestID int) int32 {
	      
	res := C.tReqQryOrder(t.api, (*C.struct_CThostFtdcQryOrderField)(unsafe.Pointer(pQryOrder)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryTrade(pQryTrade *CThostFtdcQryTradeField, nRequestID int) int32 {
	      
	res := C.tReqQryTrade(t.api, (*C.struct_CThostFtdcQryTradeField)(unsafe.Pointer(pQryTrade)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryInvestorPosition(pQryInvestorPosition *CThostFtdcQryInvestorPositionField, nRequestID int) int32 {
	      
	res := C.tReqQryInvestorPosition(t.api, (*C.struct_CThostFtdcQryInvestorPositionField)(unsafe.Pointer(pQryInvestorPosition)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryTradingAccount(pQryTradingAccount *CThostFtdcQryTradingAccountField, nRequestID int) int32 {
	      
	res := C.tReqQryTradingAccount(t.api, (*C.struct_CThostFtdcQryTradingAccountField)(unsafe.Pointer(pQryTradingAccount)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryInvestor(pQryInvestor *CThostFtdcQryInvestorField, nRequestID int) int32 {
	      
	res := C.tReqQryInvestor(t.api, (*C.struct_CThostFtdcQryInvestorField)(unsafe.Pointer(pQryInvestor)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryTradingCode(pQryTradingCode *CThostFtdcQryTradingCodeField, nRequestID int) int32 {
	      
	res := C.tReqQryTradingCode(t.api, (*C.struct_CThostFtdcQryTradingCodeField)(unsafe.Pointer(pQryTradingCode)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryInstrumentMarginRate(pQryInstrumentMarginRate *CThostFtdcQryInstrumentMarginRateField, nRequestID int) int32 {
	      
	res := C.tReqQryInstrumentMarginRate(t.api, (*C.struct_CThostFtdcQryInstrumentMarginRateField)(unsafe.Pointer(pQryInstrumentMarginRate)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryInstrumentCommissionRate(pQryInstrumentCommissionRate *CThostFtdcQryInstrumentCommissionRateField, nRequestID int) int32 {
	      
	res := C.tReqQryInstrumentCommissionRate(t.api, (*C.struct_CThostFtdcQryInstrumentCommissionRateField)(unsafe.Pointer(pQryInstrumentCommissionRate)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryExchange(pQryExchange *CThostFtdcQryExchangeField, nRequestID int) int32 {
	      
	res := C.tReqQryExchange(t.api, (*C.struct_CThostFtdcQryExchangeField)(unsafe.Pointer(pQryExchange)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryProduct(pQryProduct *CThostFtdcQryProductField, nRequestID int) int32 {
	      
	res := C.tReqQryProduct(t.api, (*C.struct_CThostFtdcQryProductField)(unsafe.Pointer(pQryProduct)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryInstrument(pQryInstrument *CThostFtdcQryInstrumentField, nRequestID int) int32 {
	      
	res := C.tReqQryInstrument(t.api, (*C.struct_CThostFtdcQryInstrumentField)(unsafe.Pointer(pQryInstrument)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryDepthMarketData(pQryDepthMarketData *CThostFtdcQryDepthMarketDataField, nRequestID int) int32 {
	      
	res := C.tReqQryDepthMarketData(t.api, (*C.struct_CThostFtdcQryDepthMarketDataField)(unsafe.Pointer(pQryDepthMarketData)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryTraderOffer(pQryTraderOffer *CThostFtdcQryTraderOfferField, nRequestID int) int32 {
	      
	res := C.tReqQryTraderOffer(t.api, (*C.struct_CThostFtdcQryTraderOfferField)(unsafe.Pointer(pQryTraderOffer)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQrySettlementInfo(pQrySettlementInfo *CThostFtdcQrySettlementInfoField, nRequestID int) int32 {
	      
	res := C.tReqQrySettlementInfo(t.api, (*C.struct_CThostFtdcQrySettlementInfoField)(unsafe.Pointer(pQrySettlementInfo)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryTransferBank(pQryTransferBank *CThostFtdcQryTransferBankField, nRequestID int) int32 {
	      
	res := C.tReqQryTransferBank(t.api, (*C.struct_CThostFtdcQryTransferBankField)(unsafe.Pointer(pQryTransferBank)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryInvestorPositionDetail(pQryInvestorPositionDetail *CThostFtdcQryInvestorPositionDetailField, nRequestID int) int32 {
	      
	res := C.tReqQryInvestorPositionDetail(t.api, (*C.struct_CThostFtdcQryInvestorPositionDetailField)(unsafe.Pointer(pQryInvestorPositionDetail)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryNotice(pQryNotice *CThostFtdcQryNoticeField, nRequestID int) int32 {
	      
	res := C.tReqQryNotice(t.api, (*C.struct_CThostFtdcQryNoticeField)(unsafe.Pointer(pQryNotice)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQrySettlementInfoConfirm(pQrySettlementInfoConfirm *CThostFtdcQrySettlementInfoConfirmField, nRequestID int) int32 {
	      
	res := C.tReqQrySettlementInfoConfirm(t.api, (*C.struct_CThostFtdcQrySettlementInfoConfirmField)(unsafe.Pointer(pQrySettlementInfoConfirm)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryInvestorPositionCombineDetail(pQryInvestorPositionCombineDetail *CThostFtdcQryInvestorPositionCombineDetailField, nRequestID int) int32 {
	      
	res := C.tReqQryInvestorPositionCombineDetail(t.api, (*C.struct_CThostFtdcQryInvestorPositionCombineDetailField)(unsafe.Pointer(pQryInvestorPositionCombineDetail)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryCFMMCTradingAccountKey(pQryCFMMCTradingAccountKey *CThostFtdcQryCFMMCTradingAccountKeyField, nRequestID int) int32 {
	      
	res := C.tReqQryCFMMCTradingAccountKey(t.api, (*C.struct_CThostFtdcQryCFMMCTradingAccountKeyField)(unsafe.Pointer(pQryCFMMCTradingAccountKey)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryEWarrantOffset(pQryEWarrantOffset *CThostFtdcQryEWarrantOffsetField, nRequestID int) int32 {
	      
	res := C.tReqQryEWarrantOffset(t.api, (*C.struct_CThostFtdcQryEWarrantOffsetField)(unsafe.Pointer(pQryEWarrantOffset)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryInvestorProductGroupMargin(pQryInvestorProductGroupMargin *CThostFtdcQryInvestorProductGroupMarginField, nRequestID int) int32 {
	      
	res := C.tReqQryInvestorProductGroupMargin(t.api, (*C.struct_CThostFtdcQryInvestorProductGroupMarginField)(unsafe.Pointer(pQryInvestorProductGroupMargin)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryExchangeMarginRate(pQryExchangeMarginRate *CThostFtdcQryExchangeMarginRateField, nRequestID int) int32 {
	      
	res := C.tReqQryExchangeMarginRate(t.api, (*C.struct_CThostFtdcQryExchangeMarginRateField)(unsafe.Pointer(pQryExchangeMarginRate)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryExchangeMarginRateAdjust(pQryExchangeMarginRateAdjust *CThostFtdcQryExchangeMarginRateAdjustField, nRequestID int) int32 {
	      
	res := C.tReqQryExchangeMarginRateAdjust(t.api, (*C.struct_CThostFtdcQryExchangeMarginRateAdjustField)(unsafe.Pointer(pQryExchangeMarginRateAdjust)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryExchangeRate(pQryExchangeRate *CThostFtdcQryExchangeRateField, nRequestID int) int32 {
	      
	res := C.tReqQryExchangeRate(t.api, (*C.struct_CThostFtdcQryExchangeRateField)(unsafe.Pointer(pQryExchangeRate)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQrySecAgentACIDMap(pQrySecAgentACIDMap *CThostFtdcQrySecAgentACIDMapField, nRequestID int) int32 {
	      
	res := C.tReqQrySecAgentACIDMap(t.api, (*C.struct_CThostFtdcQrySecAgentACIDMapField)(unsafe.Pointer(pQrySecAgentACIDMap)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryProductExchRate(pQryProductExchRate *CThostFtdcQryProductExchRateField, nRequestID int) int32 {
	      
	res := C.tReqQryProductExchRate(t.api, (*C.struct_CThostFtdcQryProductExchRateField)(unsafe.Pointer(pQryProductExchRate)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryProductGroup(pQryProductGroup *CThostFtdcQryProductGroupField, nRequestID int) int32 {
	      
	res := C.tReqQryProductGroup(t.api, (*C.struct_CThostFtdcQryProductGroupField)(unsafe.Pointer(pQryProductGroup)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryMMInstrumentCommissionRate(pQryMMInstrumentCommissionRate *CThostFtdcQryMMInstrumentCommissionRateField, nRequestID int) int32 {
	      
	res := C.tReqQryMMInstrumentCommissionRate(t.api, (*C.struct_CThostFtdcQryMMInstrumentCommissionRateField)(unsafe.Pointer(pQryMMInstrumentCommissionRate)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryMMOptionInstrCommRate(pQryMMOptionInstrCommRate *CThostFtdcQryMMOptionInstrCommRateField, nRequestID int) int32 {
	      
	res := C.tReqQryMMOptionInstrCommRate(t.api, (*C.struct_CThostFtdcQryMMOptionInstrCommRateField)(unsafe.Pointer(pQryMMOptionInstrCommRate)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryInstrumentOrderCommRate(pQryInstrumentOrderCommRate *CThostFtdcQryInstrumentOrderCommRateField, nRequestID int) int32 {
	      
	res := C.tReqQryInstrumentOrderCommRate(t.api, (*C.struct_CThostFtdcQryInstrumentOrderCommRateField)(unsafe.Pointer(pQryInstrumentOrderCommRate)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQrySecAgentTradingAccount(pQryTradingAccount *CThostFtdcQryTradingAccountField, nRequestID int) int32 {
	      
	res := C.tReqQrySecAgentTradingAccount(t.api, (*C.struct_CThostFtdcQryTradingAccountField)(unsafe.Pointer(pQryTradingAccount)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQrySecAgentCheckMode(pQrySecAgentCheckMode *CThostFtdcQrySecAgentCheckModeField, nRequestID int) int32 {
	      
	res := C.tReqQrySecAgentCheckMode(t.api, (*C.struct_CThostFtdcQrySecAgentCheckModeField)(unsafe.Pointer(pQrySecAgentCheckMode)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQrySecAgentTradeInfo(pQrySecAgentTradeInfo *CThostFtdcQrySecAgentTradeInfoField, nRequestID int) int32 {
	      
	res := C.tReqQrySecAgentTradeInfo(t.api, (*C.struct_CThostFtdcQrySecAgentTradeInfoField)(unsafe.Pointer(pQrySecAgentTradeInfo)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryOptionInstrTradeCost(pQryOptionInstrTradeCost *CThostFtdcQryOptionInstrTradeCostField, nRequestID int) int32 {
	      
	res := C.tReqQryOptionInstrTradeCost(t.api, (*C.struct_CThostFtdcQryOptionInstrTradeCostField)(unsafe.Pointer(pQryOptionInstrTradeCost)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryOptionInstrCommRate(pQryOptionInstrCommRate *CThostFtdcQryOptionInstrCommRateField, nRequestID int) int32 {
	      
	res := C.tReqQryOptionInstrCommRate(t.api, (*C.struct_CThostFtdcQryOptionInstrCommRateField)(unsafe.Pointer(pQryOptionInstrCommRate)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryExecOrder(pQryExecOrder *CThostFtdcQryExecOrderField, nRequestID int) int32 {
	      
	res := C.tReqQryExecOrder(t.api, (*C.struct_CThostFtdcQryExecOrderField)(unsafe.Pointer(pQryExecOrder)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryForQuote(pQryForQuote *CThostFtdcQryForQuoteField, nRequestID int) int32 {
	      
	res := C.tReqQryForQuote(t.api, (*C.struct_CThostFtdcQryForQuoteField)(unsafe.Pointer(pQryForQuote)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryQuote(pQryQuote *CThostFtdcQryQuoteField, nRequestID int) int32 {
	      
	res := C.tReqQryQuote(t.api, (*C.struct_CThostFtdcQryQuoteField)(unsafe.Pointer(pQryQuote)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryOptionSelfClose(pQryOptionSelfClose *CThostFtdcQryOptionSelfCloseField, nRequestID int) int32 {
	      
	res := C.tReqQryOptionSelfClose(t.api, (*C.struct_CThostFtdcQryOptionSelfCloseField)(unsafe.Pointer(pQryOptionSelfClose)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryInvestUnit(pQryInvestUnit *CThostFtdcQryInvestUnitField, nRequestID int) int32 {
	      
	res := C.tReqQryInvestUnit(t.api, (*C.struct_CThostFtdcQryInvestUnitField)(unsafe.Pointer(pQryInvestUnit)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryCombInstrumentGuard(pQryCombInstrumentGuard *CThostFtdcQryCombInstrumentGuardField, nRequestID int) int32 {
	      
	res := C.tReqQryCombInstrumentGuard(t.api, (*C.struct_CThostFtdcQryCombInstrumentGuardField)(unsafe.Pointer(pQryCombInstrumentGuard)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryCombAction(pQryCombAction *CThostFtdcQryCombActionField, nRequestID int) int32 {
	      
	res := C.tReqQryCombAction(t.api, (*C.struct_CThostFtdcQryCombActionField)(unsafe.Pointer(pQryCombAction)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryTransferSerial(pQryTransferSerial *CThostFtdcQryTransferSerialField, nRequestID int) int32 {
	      
	res := C.tReqQryTransferSerial(t.api, (*C.struct_CThostFtdcQryTransferSerialField)(unsafe.Pointer(pQryTransferSerial)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryAccountregister(pQryAccountregister *CThostFtdcQryAccountregisterField, nRequestID int) int32 {
	      
	res := C.tReqQryAccountregister(t.api, (*C.struct_CThostFtdcQryAccountregisterField)(unsafe.Pointer(pQryAccountregister)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryContractBank(pQryContractBank *CThostFtdcQryContractBankField, nRequestID int) int32 {
	      
	res := C.tReqQryContractBank(t.api, (*C.struct_CThostFtdcQryContractBankField)(unsafe.Pointer(pQryContractBank)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryParkedOrder(pQryParkedOrder *CThostFtdcQryParkedOrderField, nRequestID int) int32 {
	      
	res := C.tReqQryParkedOrder(t.api, (*C.struct_CThostFtdcQryParkedOrderField)(unsafe.Pointer(pQryParkedOrder)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryParkedOrderAction(pQryParkedOrderAction *CThostFtdcQryParkedOrderActionField, nRequestID int) int32 {
	      
	res := C.tReqQryParkedOrderAction(t.api, (*C.struct_CThostFtdcQryParkedOrderActionField)(unsafe.Pointer(pQryParkedOrderAction)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryTradingNotice(pQryTradingNotice *CThostFtdcQryTradingNoticeField, nRequestID int) int32 {
	      
	res := C.tReqQryTradingNotice(t.api, (*C.struct_CThostFtdcQryTradingNoticeField)(unsafe.Pointer(pQryTradingNotice)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryBrokerTradingParams(pQryBrokerTradingParams *CThostFtdcQryBrokerTradingParamsField, nRequestID int) int32 {
	      
	res := C.tReqQryBrokerTradingParams(t.api, (*C.struct_CThostFtdcQryBrokerTradingParamsField)(unsafe.Pointer(pQryBrokerTradingParams)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryBrokerTradingAlgos(pQryBrokerTradingAlgos *CThostFtdcQryBrokerTradingAlgosField, nRequestID int) int32 {
	      
	res := C.tReqQryBrokerTradingAlgos(t.api, (*C.struct_CThostFtdcQryBrokerTradingAlgosField)(unsafe.Pointer(pQryBrokerTradingAlgos)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQueryCFMMCTradingAccountToken(pQueryCFMMCTradingAccountToken *CThostFtdcQueryCFMMCTradingAccountTokenField, nRequestID int) int32 {
	      
	res := C.tReqQueryCFMMCTradingAccountToken(t.api, (*C.struct_CThostFtdcQueryCFMMCTradingAccountTokenField)(unsafe.Pointer(pQueryCFMMCTradingAccountToken)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqFromBankToFutureByFuture(pReqTransfer *CThostFtdcReqTransferField, nRequestID int) int32 {
	      
	res := C.tReqFromBankToFutureByFuture(t.api, (*C.struct_CThostFtdcReqTransferField)(unsafe.Pointer(pReqTransfer)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqFromFutureToBankByFuture(pReqTransfer *CThostFtdcReqTransferField, nRequestID int) int32 {
	      
	res := C.tReqFromFutureToBankByFuture(t.api, (*C.struct_CThostFtdcReqTransferField)(unsafe.Pointer(pReqTransfer)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQueryBankAccountMoneyByFuture(pReqQueryAccount *CThostFtdcReqQueryAccountField, nRequestID int) int32 {
	      
	res := C.tReqQueryBankAccountMoneyByFuture(t.api, (*C.struct_CThostFtdcReqQueryAccountField)(unsafe.Pointer(pReqQueryAccount)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryClassifiedInstrument(pQryClassifiedInstrument *CThostFtdcQryClassifiedInstrumentField, nRequestID int) int32 {
	      
	res := C.tReqQryClassifiedInstrument(t.api, (*C.struct_CThostFtdcQryClassifiedInstrumentField)(unsafe.Pointer(pQryClassifiedInstrument)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryCombPromotionParam(pQryCombPromotionParam *CThostFtdcQryCombPromotionParamField, nRequestID int) int32 {
	      
	res := C.tReqQryCombPromotionParam(t.api, (*C.struct_CThostFtdcQryCombPromotionParamField)(unsafe.Pointer(pQryCombPromotionParam)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryRiskSettleInvstPosition(pQryRiskSettleInvstPosition *CThostFtdcQryRiskSettleInvstPositionField, nRequestID int) int32 {
	      
	res := C.tReqQryRiskSettleInvstPosition(t.api, (*C.struct_CThostFtdcQryRiskSettleInvstPositionField)(unsafe.Pointer(pQryRiskSettleInvstPosition)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryRiskSettleProductStatus(pQryRiskSettleProductStatus *CThostFtdcQryRiskSettleProductStatusField, nRequestID int) int32 {
	      
	res := C.tReqQryRiskSettleProductStatus(t.api, (*C.struct_CThostFtdcQryRiskSettleProductStatusField)(unsafe.Pointer(pQryRiskSettleProductStatus)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQrySPBMFutureParameter(pQrySPBMFutureParameter *CThostFtdcQrySPBMFutureParameterField, nRequestID int) int32 {
	      
	res := C.tReqQrySPBMFutureParameter(t.api, (*C.struct_CThostFtdcQrySPBMFutureParameterField)(unsafe.Pointer(pQrySPBMFutureParameter)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQrySPBMOptionParameter(pQrySPBMOptionParameter *CThostFtdcQrySPBMOptionParameterField, nRequestID int) int32 {
	      
	res := C.tReqQrySPBMOptionParameter(t.api, (*C.struct_CThostFtdcQrySPBMOptionParameterField)(unsafe.Pointer(pQrySPBMOptionParameter)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQrySPBMIntraParameter(pQrySPBMIntraParameter *CThostFtdcQrySPBMIntraParameterField, nRequestID int) int32 {
	      
	res := C.tReqQrySPBMIntraParameter(t.api, (*C.struct_CThostFtdcQrySPBMIntraParameterField)(unsafe.Pointer(pQrySPBMIntraParameter)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQrySPBMInterParameter(pQrySPBMInterParameter *CThostFtdcQrySPBMInterParameterField, nRequestID int) int32 {
	      
	res := C.tReqQrySPBMInterParameter(t.api, (*C.struct_CThostFtdcQrySPBMInterParameterField)(unsafe.Pointer(pQrySPBMInterParameter)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQrySPBMPortfDefinition(pQrySPBMPortfDefinition *CThostFtdcQrySPBMPortfDefinitionField, nRequestID int) int32 {
	      
	res := C.tReqQrySPBMPortfDefinition(t.api, (*C.struct_CThostFtdcQrySPBMPortfDefinitionField)(unsafe.Pointer(pQrySPBMPortfDefinition)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQrySPBMInvestorPortfDef(pQrySPBMInvestorPortfDef *CThostFtdcQrySPBMInvestorPortfDefField, nRequestID int) int32 {
	      
	res := C.tReqQrySPBMInvestorPortfDef(t.api, (*C.struct_CThostFtdcQrySPBMInvestorPortfDefField)(unsafe.Pointer(pQrySPBMInvestorPortfDef)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryInvestorPortfMarginRatio(pQryInvestorPortfMarginRatio *CThostFtdcQryInvestorPortfMarginRatioField, nRequestID int) int32 {
	      
	res := C.tReqQryInvestorPortfMarginRatio(t.api, (*C.struct_CThostFtdcQryInvestorPortfMarginRatioField)(unsafe.Pointer(pQryInvestorPortfMarginRatio)), C.int(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryInvestorProdSPBMDetail(pQryInvestorProdSPBMDetail *CThostFtdcQryInvestorProdSPBMDetailField, nRequestID int) int32 {
	      
	res := C.tReqQryInvestorProdSPBMDetail(t.api, (*C.struct_CThostFtdcQryInvestorProdSPBMDetailField)(unsafe.Pointer(pQryInvestorProdSPBMDetail)), C.int(nRequestID))
	return int32(res)
}

// 当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。
func (t *Trade) OnFrontConnected (fn func()) {
	t.OnFrontConnected_ = fn
	C.tOnFrontConnected(t.pSpi, C.tOnFrontConnected_)
}
// 当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。
func (t *Trade) OnFrontDisconnected (fn func(nReason int)) {
	t.OnFrontDisconnected_ = fn
	C.tOnFrontDisconnected(t.pSpi, C.tOnFrontDisconnected_)
}
// 心跳超时警告。当长时间未收到报文时，该方法被调用。
func (t *Trade) OnHeartBeatWarning (fn func(nTimeLapse int)) {
	t.OnHeartBeatWarning_ = fn
	C.tOnHeartBeatWarning(t.pSpi, C.tOnHeartBeatWarning_)
}
// 客户端认证响应
func (t *Trade) OnRspAuthenticate (fn func(pRspAuthenticateField *CThostFtdcRspAuthenticateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspAuthenticate_ = fn
	C.tOnRspAuthenticate(t.pSpi, C.tOnRspAuthenticate_)
}
// 登录请求响应
func (t *Trade) OnRspUserLogin (fn func(pRspUserLogin *CThostFtdcRspUserLoginField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspUserLogin_ = fn
	C.tOnRspUserLogin(t.pSpi, C.tOnRspUserLogin_)
}
// 登出请求响应
func (t *Trade) OnRspUserLogout (fn func(pUserLogout *CThostFtdcUserLogoutField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspUserLogout_ = fn
	C.tOnRspUserLogout(t.pSpi, C.tOnRspUserLogout_)
}
// 用户口令更新请求响应
func (t *Trade) OnRspUserPasswordUpdate (fn func(pUserPasswordUpdate *CThostFtdcUserPasswordUpdateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspUserPasswordUpdate_ = fn
	C.tOnRspUserPasswordUpdate(t.pSpi, C.tOnRspUserPasswordUpdate_)
}
// 资金账户口令更新请求响应
func (t *Trade) OnRspTradingAccountPasswordUpdate (fn func(pTradingAccountPasswordUpdate *CThostFtdcTradingAccountPasswordUpdateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspTradingAccountPasswordUpdate_ = fn
	C.tOnRspTradingAccountPasswordUpdate(t.pSpi, C.tOnRspTradingAccountPasswordUpdate_)
}
// 查询用户当前支持的认证模式的回复
func (t *Trade) OnRspUserAuthMethod (fn func(pRspUserAuthMethod *CThostFtdcRspUserAuthMethodField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspUserAuthMethod_ = fn
	C.tOnRspUserAuthMethod(t.pSpi, C.tOnRspUserAuthMethod_)
}
// 获取图形验证码请求的回复
func (t *Trade) OnRspGenUserCaptcha (fn func(pRspGenUserCaptcha *CThostFtdcRspGenUserCaptchaField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspGenUserCaptcha_ = fn
	C.tOnRspGenUserCaptcha(t.pSpi, C.tOnRspGenUserCaptcha_)
}
// 获取短信验证码请求的回复
func (t *Trade) OnRspGenUserText (fn func(pRspGenUserText *CThostFtdcRspGenUserTextField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspGenUserText_ = fn
	C.tOnRspGenUserText(t.pSpi, C.tOnRspGenUserText_)
}
// 报单录入请求响应
func (t *Trade) OnRspOrderInsert (fn func(pInputOrder *CThostFtdcInputOrderField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspOrderInsert_ = fn
	C.tOnRspOrderInsert(t.pSpi, C.tOnRspOrderInsert_)
}
// 预埋单录入请求响应
func (t *Trade) OnRspParkedOrderInsert (fn func(pParkedOrder *CThostFtdcParkedOrderField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspParkedOrderInsert_ = fn
	C.tOnRspParkedOrderInsert(t.pSpi, C.tOnRspParkedOrderInsert_)
}
// 预埋撤单录入请求响应
func (t *Trade) OnRspParkedOrderAction (fn func(pParkedOrderAction *CThostFtdcParkedOrderActionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspParkedOrderAction_ = fn
	C.tOnRspParkedOrderAction(t.pSpi, C.tOnRspParkedOrderAction_)
}
// 报单操作请求响应
func (t *Trade) OnRspOrderAction (fn func(pInputOrderAction *CThostFtdcInputOrderActionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspOrderAction_ = fn
	C.tOnRspOrderAction(t.pSpi, C.tOnRspOrderAction_)
}
// 查询最大报单数量响应
func (t *Trade) OnRspQryMaxOrderVolume (fn func(pQryMaxOrderVolume *CThostFtdcQryMaxOrderVolumeField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryMaxOrderVolume_ = fn
	C.tOnRspQryMaxOrderVolume(t.pSpi, C.tOnRspQryMaxOrderVolume_)
}
// 投资者结算结果确认响应
func (t *Trade) OnRspSettlementInfoConfirm (fn func(pSettlementInfoConfirm *CThostFtdcSettlementInfoConfirmField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspSettlementInfoConfirm_ = fn
	C.tOnRspSettlementInfoConfirm(t.pSpi, C.tOnRspSettlementInfoConfirm_)
}
// 删除预埋单响应
func (t *Trade) OnRspRemoveParkedOrder (fn func(pRemoveParkedOrder *CThostFtdcRemoveParkedOrderField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspRemoveParkedOrder_ = fn
	C.tOnRspRemoveParkedOrder(t.pSpi, C.tOnRspRemoveParkedOrder_)
}
// 删除预埋撤单响应
func (t *Trade) OnRspRemoveParkedOrderAction (fn func(pRemoveParkedOrderAction *CThostFtdcRemoveParkedOrderActionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspRemoveParkedOrderAction_ = fn
	C.tOnRspRemoveParkedOrderAction(t.pSpi, C.tOnRspRemoveParkedOrderAction_)
}
// 执行宣告录入请求响应
func (t *Trade) OnRspExecOrderInsert (fn func(pInputExecOrder *CThostFtdcInputExecOrderField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspExecOrderInsert_ = fn
	C.tOnRspExecOrderInsert(t.pSpi, C.tOnRspExecOrderInsert_)
}
// 执行宣告操作请求响应
func (t *Trade) OnRspExecOrderAction (fn func(pInputExecOrderAction *CThostFtdcInputExecOrderActionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspExecOrderAction_ = fn
	C.tOnRspExecOrderAction(t.pSpi, C.tOnRspExecOrderAction_)
}
// 询价录入请求响应
func (t *Trade) OnRspForQuoteInsert (fn func(pInputForQuote *CThostFtdcInputForQuoteField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspForQuoteInsert_ = fn
	C.tOnRspForQuoteInsert(t.pSpi, C.tOnRspForQuoteInsert_)
}
// 报价录入请求响应
func (t *Trade) OnRspQuoteInsert (fn func(pInputQuote *CThostFtdcInputQuoteField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQuoteInsert_ = fn
	C.tOnRspQuoteInsert(t.pSpi, C.tOnRspQuoteInsert_)
}
// 报价操作请求响应
func (t *Trade) OnRspQuoteAction (fn func(pInputQuoteAction *CThostFtdcInputQuoteActionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQuoteAction_ = fn
	C.tOnRspQuoteAction(t.pSpi, C.tOnRspQuoteAction_)
}
// 批量报单操作请求响应
func (t *Trade) OnRspBatchOrderAction (fn func(pInputBatchOrderAction *CThostFtdcInputBatchOrderActionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspBatchOrderAction_ = fn
	C.tOnRspBatchOrderAction(t.pSpi, C.tOnRspBatchOrderAction_)
}
// 期权自对冲录入请求响应
func (t *Trade) OnRspOptionSelfCloseInsert (fn func(pInputOptionSelfClose *CThostFtdcInputOptionSelfCloseField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspOptionSelfCloseInsert_ = fn
	C.tOnRspOptionSelfCloseInsert(t.pSpi, C.tOnRspOptionSelfCloseInsert_)
}
// 期权自对冲操作请求响应
func (t *Trade) OnRspOptionSelfCloseAction (fn func(pInputOptionSelfCloseAction *CThostFtdcInputOptionSelfCloseActionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspOptionSelfCloseAction_ = fn
	C.tOnRspOptionSelfCloseAction(t.pSpi, C.tOnRspOptionSelfCloseAction_)
}
// 申请组合录入请求响应
func (t *Trade) OnRspCombActionInsert (fn func(pInputCombAction *CThostFtdcInputCombActionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspCombActionInsert_ = fn
	C.tOnRspCombActionInsert(t.pSpi, C.tOnRspCombActionInsert_)
}
// 请求查询报单响应
func (t *Trade) OnRspQryOrder (fn func(pOrder *CThostFtdcOrderField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryOrder_ = fn
	C.tOnRspQryOrder(t.pSpi, C.tOnRspQryOrder_)
}
// 请求查询成交响应
func (t *Trade) OnRspQryTrade (fn func(pTrade *CThostFtdcTradeField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryTrade_ = fn
	C.tOnRspQryTrade(t.pSpi, C.tOnRspQryTrade_)
}
// 请求查询投资者持仓响应
func (t *Trade) OnRspQryInvestorPosition (fn func(pInvestorPosition *CThostFtdcInvestorPositionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryInvestorPosition_ = fn
	C.tOnRspQryInvestorPosition(t.pSpi, C.tOnRspQryInvestorPosition_)
}
// 请求查询资金账户响应
func (t *Trade) OnRspQryTradingAccount (fn func(pTradingAccount *CThostFtdcTradingAccountField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryTradingAccount_ = fn
	C.tOnRspQryTradingAccount(t.pSpi, C.tOnRspQryTradingAccount_)
}
// 请求查询投资者响应
func (t *Trade) OnRspQryInvestor (fn func(pInvestor *CThostFtdcInvestorField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryInvestor_ = fn
	C.tOnRspQryInvestor(t.pSpi, C.tOnRspQryInvestor_)
}
// 请求查询交易编码响应
func (t *Trade) OnRspQryTradingCode (fn func(pTradingCode *CThostFtdcTradingCodeField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryTradingCode_ = fn
	C.tOnRspQryTradingCode(t.pSpi, C.tOnRspQryTradingCode_)
}
// 请求查询合约保证金率响应
func (t *Trade) OnRspQryInstrumentMarginRate (fn func(pInstrumentMarginRate *CThostFtdcInstrumentMarginRateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryInstrumentMarginRate_ = fn
	C.tOnRspQryInstrumentMarginRate(t.pSpi, C.tOnRspQryInstrumentMarginRate_)
}
// 请求查询合约手续费率响应
func (t *Trade) OnRspQryInstrumentCommissionRate (fn func(pInstrumentCommissionRate *CThostFtdcInstrumentCommissionRateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryInstrumentCommissionRate_ = fn
	C.tOnRspQryInstrumentCommissionRate(t.pSpi, C.tOnRspQryInstrumentCommissionRate_)
}
// 请求查询交易所响应
func (t *Trade) OnRspQryExchange (fn func(pExchange *CThostFtdcExchangeField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryExchange_ = fn
	C.tOnRspQryExchange(t.pSpi, C.tOnRspQryExchange_)
}
// 请求查询产品响应
func (t *Trade) OnRspQryProduct (fn func(pProduct *CThostFtdcProductField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryProduct_ = fn
	C.tOnRspQryProduct(t.pSpi, C.tOnRspQryProduct_)
}
// 请求查询合约响应
func (t *Trade) OnRspQryInstrument (fn func(pInstrument *CThostFtdcInstrumentField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryInstrument_ = fn
	C.tOnRspQryInstrument(t.pSpi, C.tOnRspQryInstrument_)
}
// 请求查询行情响应
func (t *Trade) OnRspQryDepthMarketData (fn func(pDepthMarketData *CThostFtdcDepthMarketDataField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryDepthMarketData_ = fn
	C.tOnRspQryDepthMarketData(t.pSpi, C.tOnRspQryDepthMarketData_)
}
// 请求查询交易员报盘机响应
func (t *Trade) OnRspQryTraderOffer (fn func(pTraderOffer *CThostFtdcTraderOfferField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryTraderOffer_ = fn
	C.tOnRspQryTraderOffer(t.pSpi, C.tOnRspQryTraderOffer_)
}
// 请求查询投资者结算结果响应
func (t *Trade) OnRspQrySettlementInfo (fn func(pSettlementInfo *CThostFtdcSettlementInfoField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQrySettlementInfo_ = fn
	C.tOnRspQrySettlementInfo(t.pSpi, C.tOnRspQrySettlementInfo_)
}
// 请求查询转帐银行响应
func (t *Trade) OnRspQryTransferBank (fn func(pTransferBank *CThostFtdcTransferBankField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryTransferBank_ = fn
	C.tOnRspQryTransferBank(t.pSpi, C.tOnRspQryTransferBank_)
}
// 请求查询投资者持仓明细响应
func (t *Trade) OnRspQryInvestorPositionDetail (fn func(pInvestorPositionDetail *CThostFtdcInvestorPositionDetailField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryInvestorPositionDetail_ = fn
	C.tOnRspQryInvestorPositionDetail(t.pSpi, C.tOnRspQryInvestorPositionDetail_)
}
// 请求查询客户通知响应
func (t *Trade) OnRspQryNotice (fn func(pNotice *CThostFtdcNoticeField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryNotice_ = fn
	C.tOnRspQryNotice(t.pSpi, C.tOnRspQryNotice_)
}
// 请求查询结算信息确认响应
func (t *Trade) OnRspQrySettlementInfoConfirm (fn func(pSettlementInfoConfirm *CThostFtdcSettlementInfoConfirmField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQrySettlementInfoConfirm_ = fn
	C.tOnRspQrySettlementInfoConfirm(t.pSpi, C.tOnRspQrySettlementInfoConfirm_)
}
// 请求查询投资者持仓明细响应
func (t *Trade) OnRspQryInvestorPositionCombineDetail (fn func(pInvestorPositionCombineDetail *CThostFtdcInvestorPositionCombineDetailField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryInvestorPositionCombineDetail_ = fn
	C.tOnRspQryInvestorPositionCombineDetail(t.pSpi, C.tOnRspQryInvestorPositionCombineDetail_)
}
// 查询保证金监管系统经纪公司资金账户密钥响应
func (t *Trade) OnRspQryCFMMCTradingAccountKey (fn func(pCFMMCTradingAccountKey *CThostFtdcCFMMCTradingAccountKeyField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryCFMMCTradingAccountKey_ = fn
	C.tOnRspQryCFMMCTradingAccountKey(t.pSpi, C.tOnRspQryCFMMCTradingAccountKey_)
}
// 请求查询仓单折抵信息响应
func (t *Trade) OnRspQryEWarrantOffset (fn func(pEWarrantOffset *CThostFtdcEWarrantOffsetField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryEWarrantOffset_ = fn
	C.tOnRspQryEWarrantOffset(t.pSpi, C.tOnRspQryEWarrantOffset_)
}
// 请求查询投资者品种/跨品种保证金响应
func (t *Trade) OnRspQryInvestorProductGroupMargin (fn func(pInvestorProductGroupMargin *CThostFtdcInvestorProductGroupMarginField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryInvestorProductGroupMargin_ = fn
	C.tOnRspQryInvestorProductGroupMargin(t.pSpi, C.tOnRspQryInvestorProductGroupMargin_)
}
// 请求查询交易所保证金率响应
func (t *Trade) OnRspQryExchangeMarginRate (fn func(pExchangeMarginRate *CThostFtdcExchangeMarginRateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryExchangeMarginRate_ = fn
	C.tOnRspQryExchangeMarginRate(t.pSpi, C.tOnRspQryExchangeMarginRate_)
}
// 请求查询交易所调整保证金率响应
func (t *Trade) OnRspQryExchangeMarginRateAdjust (fn func(pExchangeMarginRateAdjust *CThostFtdcExchangeMarginRateAdjustField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryExchangeMarginRateAdjust_ = fn
	C.tOnRspQryExchangeMarginRateAdjust(t.pSpi, C.tOnRspQryExchangeMarginRateAdjust_)
}
// 请求查询汇率响应
func (t *Trade) OnRspQryExchangeRate (fn func(pExchangeRate *CThostFtdcExchangeRateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryExchangeRate_ = fn
	C.tOnRspQryExchangeRate(t.pSpi, C.tOnRspQryExchangeRate_)
}
// 请求查询二级代理操作员银期权限响应
func (t *Trade) OnRspQrySecAgentACIDMap (fn func(pSecAgentACIDMap *CThostFtdcSecAgentACIDMapField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQrySecAgentACIDMap_ = fn
	C.tOnRspQrySecAgentACIDMap(t.pSpi, C.tOnRspQrySecAgentACIDMap_)
}
// 请求查询产品报价汇率
func (t *Trade) OnRspQryProductExchRate (fn func(pProductExchRate *CThostFtdcProductExchRateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryProductExchRate_ = fn
	C.tOnRspQryProductExchRate(t.pSpi, C.tOnRspQryProductExchRate_)
}
// 请求查询产品组
func (t *Trade) OnRspQryProductGroup (fn func(pProductGroup *CThostFtdcProductGroupField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryProductGroup_ = fn
	C.tOnRspQryProductGroup(t.pSpi, C.tOnRspQryProductGroup_)
}
// 请求查询做市商合约手续费率响应
func (t *Trade) OnRspQryMMInstrumentCommissionRate (fn func(pMMInstrumentCommissionRate *CThostFtdcMMInstrumentCommissionRateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryMMInstrumentCommissionRate_ = fn
	C.tOnRspQryMMInstrumentCommissionRate(t.pSpi, C.tOnRspQryMMInstrumentCommissionRate_)
}
// 请求查询做市商期权合约手续费响应
func (t *Trade) OnRspQryMMOptionInstrCommRate (fn func(pMMOptionInstrCommRate *CThostFtdcMMOptionInstrCommRateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryMMOptionInstrCommRate_ = fn
	C.tOnRspQryMMOptionInstrCommRate(t.pSpi, C.tOnRspQryMMOptionInstrCommRate_)
}
// 请求查询报单手续费响应
func (t *Trade) OnRspQryInstrumentOrderCommRate (fn func(pInstrumentOrderCommRate *CThostFtdcInstrumentOrderCommRateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryInstrumentOrderCommRate_ = fn
	C.tOnRspQryInstrumentOrderCommRate(t.pSpi, C.tOnRspQryInstrumentOrderCommRate_)
}
// 请求查询资金账户响应
func (t *Trade) OnRspQrySecAgentTradingAccount (fn func(pTradingAccount *CThostFtdcTradingAccountField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQrySecAgentTradingAccount_ = fn
	C.tOnRspQrySecAgentTradingAccount(t.pSpi, C.tOnRspQrySecAgentTradingAccount_)
}
// 请求查询二级代理商资金校验模式响应
func (t *Trade) OnRspQrySecAgentCheckMode (fn func(pSecAgentCheckMode *CThostFtdcSecAgentCheckModeField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQrySecAgentCheckMode_ = fn
	C.tOnRspQrySecAgentCheckMode(t.pSpi, C.tOnRspQrySecAgentCheckMode_)
}
// 请求查询二级代理商信息响应
func (t *Trade) OnRspQrySecAgentTradeInfo (fn func(pSecAgentTradeInfo *CThostFtdcSecAgentTradeInfoField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQrySecAgentTradeInfo_ = fn
	C.tOnRspQrySecAgentTradeInfo(t.pSpi, C.tOnRspQrySecAgentTradeInfo_)
}
// 请求查询期权交易成本响应
func (t *Trade) OnRspQryOptionInstrTradeCost (fn func(pOptionInstrTradeCost *CThostFtdcOptionInstrTradeCostField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryOptionInstrTradeCost_ = fn
	C.tOnRspQryOptionInstrTradeCost(t.pSpi, C.tOnRspQryOptionInstrTradeCost_)
}
// 请求查询期权合约手续费响应
func (t *Trade) OnRspQryOptionInstrCommRate (fn func(pOptionInstrCommRate *CThostFtdcOptionInstrCommRateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryOptionInstrCommRate_ = fn
	C.tOnRspQryOptionInstrCommRate(t.pSpi, C.tOnRspQryOptionInstrCommRate_)
}
// 请求查询执行宣告响应
func (t *Trade) OnRspQryExecOrder (fn func(pExecOrder *CThostFtdcExecOrderField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryExecOrder_ = fn
	C.tOnRspQryExecOrder(t.pSpi, C.tOnRspQryExecOrder_)
}
// 请求查询询价响应
func (t *Trade) OnRspQryForQuote (fn func(pForQuote *CThostFtdcForQuoteField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryForQuote_ = fn
	C.tOnRspQryForQuote(t.pSpi, C.tOnRspQryForQuote_)
}
// 请求查询报价响应
func (t *Trade) OnRspQryQuote (fn func(pQuote *CThostFtdcQuoteField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryQuote_ = fn
	C.tOnRspQryQuote(t.pSpi, C.tOnRspQryQuote_)
}
// 请求查询期权自对冲响应
func (t *Trade) OnRspQryOptionSelfClose (fn func(pOptionSelfClose *CThostFtdcOptionSelfCloseField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryOptionSelfClose_ = fn
	C.tOnRspQryOptionSelfClose(t.pSpi, C.tOnRspQryOptionSelfClose_)
}
// 请求查询投资单元响应
func (t *Trade) OnRspQryInvestUnit (fn func(pInvestUnit *CThostFtdcInvestUnitField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryInvestUnit_ = fn
	C.tOnRspQryInvestUnit(t.pSpi, C.tOnRspQryInvestUnit_)
}
// 请求查询组合合约安全系数响应
func (t *Trade) OnRspQryCombInstrumentGuard (fn func(pCombInstrumentGuard *CThostFtdcCombInstrumentGuardField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryCombInstrumentGuard_ = fn
	C.tOnRspQryCombInstrumentGuard(t.pSpi, C.tOnRspQryCombInstrumentGuard_)
}
// 请求查询申请组合响应
func (t *Trade) OnRspQryCombAction (fn func(pCombAction *CThostFtdcCombActionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryCombAction_ = fn
	C.tOnRspQryCombAction(t.pSpi, C.tOnRspQryCombAction_)
}
// 请求查询转帐流水响应
func (t *Trade) OnRspQryTransferSerial (fn func(pTransferSerial *CThostFtdcTransferSerialField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryTransferSerial_ = fn
	C.tOnRspQryTransferSerial(t.pSpi, C.tOnRspQryTransferSerial_)
}
// 请求查询银期签约关系响应
func (t *Trade) OnRspQryAccountregister (fn func(pAccountregister *CThostFtdcAccountregisterField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryAccountregister_ = fn
	C.tOnRspQryAccountregister(t.pSpi, C.tOnRspQryAccountregister_)
}
// 错误应答
func (t *Trade) OnRspError (fn func(pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspError_ = fn
	C.tOnRspError(t.pSpi, C.tOnRspError_)
}
// 报单通知
func (t *Trade) OnRtnOrder (fn func(pOrder *CThostFtdcOrderField)) {
	t.OnRtnOrder_ = fn
	C.tOnRtnOrder(t.pSpi, C.tOnRtnOrder_)
}
// 成交通知
func (t *Trade) OnRtnTrade (fn func(pTrade *CThostFtdcTradeField)) {
	t.OnRtnTrade_ = fn
	C.tOnRtnTrade(t.pSpi, C.tOnRtnTrade_)
}
// 报单录入错误回报
func (t *Trade) OnErrRtnOrderInsert (fn func(pInputOrder *CThostFtdcInputOrderField, pRspInfo *CThostFtdcRspInfoField)) {
	t.OnErrRtnOrderInsert_ = fn
	C.tOnErrRtnOrderInsert(t.pSpi, C.tOnErrRtnOrderInsert_)
}
// 报单操作错误回报
func (t *Trade) OnErrRtnOrderAction (fn func(pOrderAction *CThostFtdcOrderActionField, pRspInfo *CThostFtdcRspInfoField)) {
	t.OnErrRtnOrderAction_ = fn
	C.tOnErrRtnOrderAction(t.pSpi, C.tOnErrRtnOrderAction_)
}
// 合约交易状态通知
func (t *Trade) OnRtnInstrumentStatus (fn func(pInstrumentStatus *CThostFtdcInstrumentStatusField)) {
	t.OnRtnInstrumentStatus_ = fn
	C.tOnRtnInstrumentStatus(t.pSpi, C.tOnRtnInstrumentStatus_)
}
// 交易所公告通知
func (t *Trade) OnRtnBulletin (fn func(pBulletin *CThostFtdcBulletinField)) {
	t.OnRtnBulletin_ = fn
	C.tOnRtnBulletin(t.pSpi, C.tOnRtnBulletin_)
}
// 交易通知
func (t *Trade) OnRtnTradingNotice (fn func(pTradingNoticeInfo *CThostFtdcTradingNoticeInfoField)) {
	t.OnRtnTradingNotice_ = fn
	C.tOnRtnTradingNotice(t.pSpi, C.tOnRtnTradingNotice_)
}
// 提示条件单校验错误
func (t *Trade) OnRtnErrorConditionalOrder (fn func(pErrorConditionalOrder *CThostFtdcErrorConditionalOrderField)) {
	t.OnRtnErrorConditionalOrder_ = fn
	C.tOnRtnErrorConditionalOrder(t.pSpi, C.tOnRtnErrorConditionalOrder_)
}
// 执行宣告通知
func (t *Trade) OnRtnExecOrder (fn func(pExecOrder *CThostFtdcExecOrderField)) {
	t.OnRtnExecOrder_ = fn
	C.tOnRtnExecOrder(t.pSpi, C.tOnRtnExecOrder_)
}
// 执行宣告录入错误回报
func (t *Trade) OnErrRtnExecOrderInsert (fn func(pInputExecOrder *CThostFtdcInputExecOrderField, pRspInfo *CThostFtdcRspInfoField)) {
	t.OnErrRtnExecOrderInsert_ = fn
	C.tOnErrRtnExecOrderInsert(t.pSpi, C.tOnErrRtnExecOrderInsert_)
}
// 执行宣告操作错误回报
func (t *Trade) OnErrRtnExecOrderAction (fn func(pExecOrderAction *CThostFtdcExecOrderActionField, pRspInfo *CThostFtdcRspInfoField)) {
	t.OnErrRtnExecOrderAction_ = fn
	C.tOnErrRtnExecOrderAction(t.pSpi, C.tOnErrRtnExecOrderAction_)
}
// 询价录入错误回报
func (t *Trade) OnErrRtnForQuoteInsert (fn func(pInputForQuote *CThostFtdcInputForQuoteField, pRspInfo *CThostFtdcRspInfoField)) {
	t.OnErrRtnForQuoteInsert_ = fn
	C.tOnErrRtnForQuoteInsert(t.pSpi, C.tOnErrRtnForQuoteInsert_)
}
// 报价通知
func (t *Trade) OnRtnQuote (fn func(pQuote *CThostFtdcQuoteField)) {
	t.OnRtnQuote_ = fn
	C.tOnRtnQuote(t.pSpi, C.tOnRtnQuote_)
}
// 报价录入错误回报
func (t *Trade) OnErrRtnQuoteInsert (fn func(pInputQuote *CThostFtdcInputQuoteField, pRspInfo *CThostFtdcRspInfoField)) {
	t.OnErrRtnQuoteInsert_ = fn
	C.tOnErrRtnQuoteInsert(t.pSpi, C.tOnErrRtnQuoteInsert_)
}
// 报价操作错误回报
func (t *Trade) OnErrRtnQuoteAction (fn func(pQuoteAction *CThostFtdcQuoteActionField, pRspInfo *CThostFtdcRspInfoField)) {
	t.OnErrRtnQuoteAction_ = fn
	C.tOnErrRtnQuoteAction(t.pSpi, C.tOnErrRtnQuoteAction_)
}
// 询价通知
func (t *Trade) OnRtnForQuoteRsp (fn func(pForQuoteRsp *CThostFtdcForQuoteRspField)) {
	t.OnRtnForQuoteRsp_ = fn
	C.tOnRtnForQuoteRsp(t.pSpi, C.tOnRtnForQuoteRsp_)
}
// 保证金监控中心用户令牌
func (t *Trade) OnRtnCFMMCTradingAccountToken (fn func(pCFMMCTradingAccountToken *CThostFtdcCFMMCTradingAccountTokenField)) {
	t.OnRtnCFMMCTradingAccountToken_ = fn
	C.tOnRtnCFMMCTradingAccountToken(t.pSpi, C.tOnRtnCFMMCTradingAccountToken_)
}
// 批量报单操作错误回报
func (t *Trade) OnErrRtnBatchOrderAction (fn func(pBatchOrderAction *CThostFtdcBatchOrderActionField, pRspInfo *CThostFtdcRspInfoField)) {
	t.OnErrRtnBatchOrderAction_ = fn
	C.tOnErrRtnBatchOrderAction(t.pSpi, C.tOnErrRtnBatchOrderAction_)
}
// 期权自对冲通知
func (t *Trade) OnRtnOptionSelfClose (fn func(pOptionSelfClose *CThostFtdcOptionSelfCloseField)) {
	t.OnRtnOptionSelfClose_ = fn
	C.tOnRtnOptionSelfClose(t.pSpi, C.tOnRtnOptionSelfClose_)
}
// 期权自对冲录入错误回报
func (t *Trade) OnErrRtnOptionSelfCloseInsert (fn func(pInputOptionSelfClose *CThostFtdcInputOptionSelfCloseField, pRspInfo *CThostFtdcRspInfoField)) {
	t.OnErrRtnOptionSelfCloseInsert_ = fn
	C.tOnErrRtnOptionSelfCloseInsert(t.pSpi, C.tOnErrRtnOptionSelfCloseInsert_)
}
// 期权自对冲操作错误回报
func (t *Trade) OnErrRtnOptionSelfCloseAction (fn func(pOptionSelfCloseAction *CThostFtdcOptionSelfCloseActionField, pRspInfo *CThostFtdcRspInfoField)) {
	t.OnErrRtnOptionSelfCloseAction_ = fn
	C.tOnErrRtnOptionSelfCloseAction(t.pSpi, C.tOnErrRtnOptionSelfCloseAction_)
}
// 申请组合通知
func (t *Trade) OnRtnCombAction (fn func(pCombAction *CThostFtdcCombActionField)) {
	t.OnRtnCombAction_ = fn
	C.tOnRtnCombAction(t.pSpi, C.tOnRtnCombAction_)
}
// 申请组合录入错误回报
func (t *Trade) OnErrRtnCombActionInsert (fn func(pInputCombAction *CThostFtdcInputCombActionField, pRspInfo *CThostFtdcRspInfoField)) {
	t.OnErrRtnCombActionInsert_ = fn
	C.tOnErrRtnCombActionInsert(t.pSpi, C.tOnErrRtnCombActionInsert_)
}
// 请求查询签约银行响应
func (t *Trade) OnRspQryContractBank (fn func(pContractBank *CThostFtdcContractBankField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryContractBank_ = fn
	C.tOnRspQryContractBank(t.pSpi, C.tOnRspQryContractBank_)
}
// 请求查询预埋单响应
func (t *Trade) OnRspQryParkedOrder (fn func(pParkedOrder *CThostFtdcParkedOrderField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryParkedOrder_ = fn
	C.tOnRspQryParkedOrder(t.pSpi, C.tOnRspQryParkedOrder_)
}
// 请求查询预埋撤单响应
func (t *Trade) OnRspQryParkedOrderAction (fn func(pParkedOrderAction *CThostFtdcParkedOrderActionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryParkedOrderAction_ = fn
	C.tOnRspQryParkedOrderAction(t.pSpi, C.tOnRspQryParkedOrderAction_)
}
// 请求查询交易通知响应
func (t *Trade) OnRspQryTradingNotice (fn func(pTradingNotice *CThostFtdcTradingNoticeField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryTradingNotice_ = fn
	C.tOnRspQryTradingNotice(t.pSpi, C.tOnRspQryTradingNotice_)
}
// 请求查询经纪公司交易参数响应
func (t *Trade) OnRspQryBrokerTradingParams (fn func(pBrokerTradingParams *CThostFtdcBrokerTradingParamsField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryBrokerTradingParams_ = fn
	C.tOnRspQryBrokerTradingParams(t.pSpi, C.tOnRspQryBrokerTradingParams_)
}
// 请求查询经纪公司交易算法响应
func (t *Trade) OnRspQryBrokerTradingAlgos (fn func(pBrokerTradingAlgos *CThostFtdcBrokerTradingAlgosField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryBrokerTradingAlgos_ = fn
	C.tOnRspQryBrokerTradingAlgos(t.pSpi, C.tOnRspQryBrokerTradingAlgos_)
}
// 请求查询监控中心用户令牌
func (t *Trade) OnRspQueryCFMMCTradingAccountToken (fn func(pQueryCFMMCTradingAccountToken *CThostFtdcQueryCFMMCTradingAccountTokenField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQueryCFMMCTradingAccountToken_ = fn
	C.tOnRspQueryCFMMCTradingAccountToken(t.pSpi, C.tOnRspQueryCFMMCTradingAccountToken_)
}
// 银行发起银行资金转期货通知
func (t *Trade) OnRtnFromBankToFutureByBank (fn func(pRspTransfer *CThostFtdcRspTransferField)) {
	t.OnRtnFromBankToFutureByBank_ = fn
	C.tOnRtnFromBankToFutureByBank(t.pSpi, C.tOnRtnFromBankToFutureByBank_)
}
// 银行发起期货资金转银行通知
func (t *Trade) OnRtnFromFutureToBankByBank (fn func(pRspTransfer *CThostFtdcRspTransferField)) {
	t.OnRtnFromFutureToBankByBank_ = fn
	C.tOnRtnFromFutureToBankByBank(t.pSpi, C.tOnRtnFromFutureToBankByBank_)
}
// 银行发起冲正银行转期货通知
func (t *Trade) OnRtnRepealFromBankToFutureByBank (fn func(pRspRepeal *CThostFtdcRspRepealField)) {
	t.OnRtnRepealFromBankToFutureByBank_ = fn
	C.tOnRtnRepealFromBankToFutureByBank(t.pSpi, C.tOnRtnRepealFromBankToFutureByBank_)
}
// 银行发起冲正期货转银行通知
func (t *Trade) OnRtnRepealFromFutureToBankByBank (fn func(pRspRepeal *CThostFtdcRspRepealField)) {
	t.OnRtnRepealFromFutureToBankByBank_ = fn
	C.tOnRtnRepealFromFutureToBankByBank(t.pSpi, C.tOnRtnRepealFromFutureToBankByBank_)
}
// 期货发起银行资金转期货通知
func (t *Trade) OnRtnFromBankToFutureByFuture (fn func(pRspTransfer *CThostFtdcRspTransferField)) {
	t.OnRtnFromBankToFutureByFuture_ = fn
	C.tOnRtnFromBankToFutureByFuture(t.pSpi, C.tOnRtnFromBankToFutureByFuture_)
}
// 期货发起期货资金转银行通知
func (t *Trade) OnRtnFromFutureToBankByFuture (fn func(pRspTransfer *CThostFtdcRspTransferField)) {
	t.OnRtnFromFutureToBankByFuture_ = fn
	C.tOnRtnFromFutureToBankByFuture(t.pSpi, C.tOnRtnFromFutureToBankByFuture_)
}
// 系统运行时期货端手工发起冲正银行转期货请求，银行处理完毕后报盘发回的通知
func (t *Trade) OnRtnRepealFromBankToFutureByFutureManual (fn func(pRspRepeal *CThostFtdcRspRepealField)) {
	t.OnRtnRepealFromBankToFutureByFutureManual_ = fn
	C.tOnRtnRepealFromBankToFutureByFutureManual(t.pSpi, C.tOnRtnRepealFromBankToFutureByFutureManual_)
}
// 系统运行时期货端手工发起冲正期货转银行请求，银行处理完毕后报盘发回的通知
func (t *Trade) OnRtnRepealFromFutureToBankByFutureManual (fn func(pRspRepeal *CThostFtdcRspRepealField)) {
	t.OnRtnRepealFromFutureToBankByFutureManual_ = fn
	C.tOnRtnRepealFromFutureToBankByFutureManual(t.pSpi, C.tOnRtnRepealFromFutureToBankByFutureManual_)
}
// 期货发起查询银行余额通知
func (t *Trade) OnRtnQueryBankBalanceByFuture (fn func(pNotifyQueryAccount *CThostFtdcNotifyQueryAccountField)) {
	t.OnRtnQueryBankBalanceByFuture_ = fn
	C.tOnRtnQueryBankBalanceByFuture(t.pSpi, C.tOnRtnQueryBankBalanceByFuture_)
}
// 期货发起银行资金转期货错误回报
func (t *Trade) OnErrRtnBankToFutureByFuture (fn func(pReqTransfer *CThostFtdcReqTransferField, pRspInfo *CThostFtdcRspInfoField)) {
	t.OnErrRtnBankToFutureByFuture_ = fn
	C.tOnErrRtnBankToFutureByFuture(t.pSpi, C.tOnErrRtnBankToFutureByFuture_)
}
// 期货发起期货资金转银行错误回报
func (t *Trade) OnErrRtnFutureToBankByFuture (fn func(pReqTransfer *CThostFtdcReqTransferField, pRspInfo *CThostFtdcRspInfoField)) {
	t.OnErrRtnFutureToBankByFuture_ = fn
	C.tOnErrRtnFutureToBankByFuture(t.pSpi, C.tOnErrRtnFutureToBankByFuture_)
}
// 系统运行时期货端手工发起冲正银行转期货错误回报
func (t *Trade) OnErrRtnRepealBankToFutureByFutureManual (fn func(pReqRepeal *CThostFtdcReqRepealField, pRspInfo *CThostFtdcRspInfoField)) {
	t.OnErrRtnRepealBankToFutureByFutureManual_ = fn
	C.tOnErrRtnRepealBankToFutureByFutureManual(t.pSpi, C.tOnErrRtnRepealBankToFutureByFutureManual_)
}
// 系统运行时期货端手工发起冲正期货转银行错误回报
func (t *Trade) OnErrRtnRepealFutureToBankByFutureManual (fn func(pReqRepeal *CThostFtdcReqRepealField, pRspInfo *CThostFtdcRspInfoField)) {
	t.OnErrRtnRepealFutureToBankByFutureManual_ = fn
	C.tOnErrRtnRepealFutureToBankByFutureManual(t.pSpi, C.tOnErrRtnRepealFutureToBankByFutureManual_)
}
// 期货发起查询银行余额错误回报
func (t *Trade) OnErrRtnQueryBankBalanceByFuture (fn func(pReqQueryAccount *CThostFtdcReqQueryAccountField, pRspInfo *CThostFtdcRspInfoField)) {
	t.OnErrRtnQueryBankBalanceByFuture_ = fn
	C.tOnErrRtnQueryBankBalanceByFuture(t.pSpi, C.tOnErrRtnQueryBankBalanceByFuture_)
}
// 期货发起冲正银行转期货请求，银行处理完毕后报盘发回的通知
func (t *Trade) OnRtnRepealFromBankToFutureByFuture (fn func(pRspRepeal *CThostFtdcRspRepealField)) {
	t.OnRtnRepealFromBankToFutureByFuture_ = fn
	C.tOnRtnRepealFromBankToFutureByFuture(t.pSpi, C.tOnRtnRepealFromBankToFutureByFuture_)
}
// 期货发起冲正期货转银行请求，银行处理完毕后报盘发回的通知
func (t *Trade) OnRtnRepealFromFutureToBankByFuture (fn func(pRspRepeal *CThostFtdcRspRepealField)) {
	t.OnRtnRepealFromFutureToBankByFuture_ = fn
	C.tOnRtnRepealFromFutureToBankByFuture(t.pSpi, C.tOnRtnRepealFromFutureToBankByFuture_)
}
// 期货发起银行资金转期货应答
func (t *Trade) OnRspFromBankToFutureByFuture (fn func(pReqTransfer *CThostFtdcReqTransferField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspFromBankToFutureByFuture_ = fn
	C.tOnRspFromBankToFutureByFuture(t.pSpi, C.tOnRspFromBankToFutureByFuture_)
}
// 期货发起期货资金转银行应答
func (t *Trade) OnRspFromFutureToBankByFuture (fn func(pReqTransfer *CThostFtdcReqTransferField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspFromFutureToBankByFuture_ = fn
	C.tOnRspFromFutureToBankByFuture(t.pSpi, C.tOnRspFromFutureToBankByFuture_)
}
// 期货发起查询银行余额应答
func (t *Trade) OnRspQueryBankAccountMoneyByFuture (fn func(pReqQueryAccount *CThostFtdcReqQueryAccountField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQueryBankAccountMoneyByFuture_ = fn
	C.tOnRspQueryBankAccountMoneyByFuture(t.pSpi, C.tOnRspQueryBankAccountMoneyByFuture_)
}
// 银行发起银期开户通知
func (t *Trade) OnRtnOpenAccountByBank (fn func(pOpenAccount *CThostFtdcOpenAccountField)) {
	t.OnRtnOpenAccountByBank_ = fn
	C.tOnRtnOpenAccountByBank(t.pSpi, C.tOnRtnOpenAccountByBank_)
}
// 银行发起银期销户通知
func (t *Trade) OnRtnCancelAccountByBank (fn func(pCancelAccount *CThostFtdcCancelAccountField)) {
	t.OnRtnCancelAccountByBank_ = fn
	C.tOnRtnCancelAccountByBank(t.pSpi, C.tOnRtnCancelAccountByBank_)
}
// 银行发起变更银行账号通知
func (t *Trade) OnRtnChangeAccountByBank (fn func(pChangeAccount *CThostFtdcChangeAccountField)) {
	t.OnRtnChangeAccountByBank_ = fn
	C.tOnRtnChangeAccountByBank(t.pSpi, C.tOnRtnChangeAccountByBank_)
}
// 请求查询分类合约响应
func (t *Trade) OnRspQryClassifiedInstrument (fn func(pInstrument *CThostFtdcInstrumentField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryClassifiedInstrument_ = fn
	C.tOnRspQryClassifiedInstrument(t.pSpi, C.tOnRspQryClassifiedInstrument_)
}
// 请求组合优惠比例响应
func (t *Trade) OnRspQryCombPromotionParam (fn func(pCombPromotionParam *CThostFtdcCombPromotionParamField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryCombPromotionParam_ = fn
	C.tOnRspQryCombPromotionParam(t.pSpi, C.tOnRspQryCombPromotionParam_)
}
// 投资者风险结算持仓查询响应
func (t *Trade) OnRspQryRiskSettleInvstPosition (fn func(pRiskSettleInvstPosition *CThostFtdcRiskSettleInvstPositionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryRiskSettleInvstPosition_ = fn
	C.tOnRspQryRiskSettleInvstPosition(t.pSpi, C.tOnRspQryRiskSettleInvstPosition_)
}
// 风险结算产品查询响应
func (t *Trade) OnRspQryRiskSettleProductStatus (fn func(pRiskSettleProductStatus *CThostFtdcRiskSettleProductStatusField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryRiskSettleProductStatus_ = fn
	C.tOnRspQryRiskSettleProductStatus(t.pSpi, C.tOnRspQryRiskSettleProductStatus_)
}
// SPBM期货合约参数查询响应
func (t *Trade) OnRspQrySPBMFutureParameter (fn func(pSPBMFutureParameter *CThostFtdcSPBMFutureParameterField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQrySPBMFutureParameter_ = fn
	C.tOnRspQrySPBMFutureParameter(t.pSpi, C.tOnRspQrySPBMFutureParameter_)
}
// SPBM期权合约参数查询响应
func (t *Trade) OnRspQrySPBMOptionParameter (fn func(pSPBMOptionParameter *CThostFtdcSPBMOptionParameterField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQrySPBMOptionParameter_ = fn
	C.tOnRspQrySPBMOptionParameter(t.pSpi, C.tOnRspQrySPBMOptionParameter_)
}
// SPBM品种内对锁仓折扣参数查询响应
func (t *Trade) OnRspQrySPBMIntraParameter (fn func(pSPBMIntraParameter *CThostFtdcSPBMIntraParameterField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQrySPBMIntraParameter_ = fn
	C.tOnRspQrySPBMIntraParameter(t.pSpi, C.tOnRspQrySPBMIntraParameter_)
}
// SPBM跨品种抵扣参数查询响应
func (t *Trade) OnRspQrySPBMInterParameter (fn func(pSPBMInterParameter *CThostFtdcSPBMInterParameterField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQrySPBMInterParameter_ = fn
	C.tOnRspQrySPBMInterParameter(t.pSpi, C.tOnRspQrySPBMInterParameter_)
}
// SPBM组合保证金套餐查询响应
func (t *Trade) OnRspQrySPBMPortfDefinition (fn func(pSPBMPortfDefinition *CThostFtdcSPBMPortfDefinitionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQrySPBMPortfDefinition_ = fn
	C.tOnRspQrySPBMPortfDefinition(t.pSpi, C.tOnRspQrySPBMPortfDefinition_)
}
// 投资者SPBM套餐选择查询响应
func (t *Trade) OnRspQrySPBMInvestorPortfDef (fn func(pSPBMInvestorPortfDef *CThostFtdcSPBMInvestorPortfDefField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQrySPBMInvestorPortfDef_ = fn
	C.tOnRspQrySPBMInvestorPortfDef(t.pSpi, C.tOnRspQrySPBMInvestorPortfDef_)
}
// 投资者新型组合保证金系数查询响应
func (t *Trade) OnRspQryInvestorPortfMarginRatio (fn func(pInvestorPortfMarginRatio *CThostFtdcInvestorPortfMarginRatioField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryInvestorPortfMarginRatio_ = fn
	C.tOnRspQryInvestorPortfMarginRatio(t.pSpi, C.tOnRspQryInvestorPortfMarginRatio_)
}
// 投资者产品SPBM明细查询响应
func (t *Trade) OnRspQryInvestorProdSPBMDetail (fn func(pInvestorProdSPBMDetail *CThostFtdcInvestorProdSPBMDetailField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
	t.OnRspQryInvestorProdSPBMDetail_ = fn
	C.tOnRspQryInvestorProdSPBMDetail(t.pSpi, C.tOnRspQryInvestorProdSPBMDetail_)
}



//export tOnFrontConnected_
func tOnFrontConnected_() C.int {
    if t.OnFrontConnected_ != nil{
        t.OnFrontConnected_()
    }
	return 0
}

//export tOnFrontDisconnected_
func tOnFrontDisconnected_(nReason C.int) C.int {
    if t.OnFrontDisconnected_ != nil{
        t.OnFrontDisconnected_(int(nReason))
    }
	return 0
}

//export tOnHeartBeatWarning_
func tOnHeartBeatWarning_(nTimeLapse C.int) C.int {
    if t.OnHeartBeatWarning_ != nil{
        t.OnHeartBeatWarning_(int(nTimeLapse))
    }
	return 0
}

//export tOnRspAuthenticate_
func tOnRspAuthenticate_(pRspAuthenticateField *C.struct_CThostFtdcRspAuthenticateField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspAuthenticate_ != nil{
        t.OnRspAuthenticate_((*CThostFtdcRspAuthenticateField)(unsafe.Pointer(pRspAuthenticateField)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspUserLogin_
func tOnRspUserLogin_(pRspUserLogin *C.struct_CThostFtdcRspUserLoginField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspUserLogin_ != nil{
        t.OnRspUserLogin_((*CThostFtdcRspUserLoginField)(unsafe.Pointer(pRspUserLogin)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspUserLogout_
func tOnRspUserLogout_(pUserLogout *C.struct_CThostFtdcUserLogoutField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspUserLogout_ != nil{
        t.OnRspUserLogout_((*CThostFtdcUserLogoutField)(unsafe.Pointer(pUserLogout)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspUserPasswordUpdate_
func tOnRspUserPasswordUpdate_(pUserPasswordUpdate *C.struct_CThostFtdcUserPasswordUpdateField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspUserPasswordUpdate_ != nil{
        t.OnRspUserPasswordUpdate_((*CThostFtdcUserPasswordUpdateField)(unsafe.Pointer(pUserPasswordUpdate)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspTradingAccountPasswordUpdate_
func tOnRspTradingAccountPasswordUpdate_(pTradingAccountPasswordUpdate *C.struct_CThostFtdcTradingAccountPasswordUpdateField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspTradingAccountPasswordUpdate_ != nil{
        t.OnRspTradingAccountPasswordUpdate_((*CThostFtdcTradingAccountPasswordUpdateField)(unsafe.Pointer(pTradingAccountPasswordUpdate)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspUserAuthMethod_
func tOnRspUserAuthMethod_(pRspUserAuthMethod *C.struct_CThostFtdcRspUserAuthMethodField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspUserAuthMethod_ != nil{
        t.OnRspUserAuthMethod_((*CThostFtdcRspUserAuthMethodField)(unsafe.Pointer(pRspUserAuthMethod)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspGenUserCaptcha_
func tOnRspGenUserCaptcha_(pRspGenUserCaptcha *C.struct_CThostFtdcRspGenUserCaptchaField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspGenUserCaptcha_ != nil{
        t.OnRspGenUserCaptcha_((*CThostFtdcRspGenUserCaptchaField)(unsafe.Pointer(pRspGenUserCaptcha)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspGenUserText_
func tOnRspGenUserText_(pRspGenUserText *C.struct_CThostFtdcRspGenUserTextField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspGenUserText_ != nil{
        t.OnRspGenUserText_((*CThostFtdcRspGenUserTextField)(unsafe.Pointer(pRspGenUserText)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspOrderInsert_
func tOnRspOrderInsert_(pInputOrder *C.struct_CThostFtdcInputOrderField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspOrderInsert_ != nil{
        t.OnRspOrderInsert_((*CThostFtdcInputOrderField)(unsafe.Pointer(pInputOrder)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspParkedOrderInsert_
func tOnRspParkedOrderInsert_(pParkedOrder *C.struct_CThostFtdcParkedOrderField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspParkedOrderInsert_ != nil{
        t.OnRspParkedOrderInsert_((*CThostFtdcParkedOrderField)(unsafe.Pointer(pParkedOrder)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspParkedOrderAction_
func tOnRspParkedOrderAction_(pParkedOrderAction *C.struct_CThostFtdcParkedOrderActionField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspParkedOrderAction_ != nil{
        t.OnRspParkedOrderAction_((*CThostFtdcParkedOrderActionField)(unsafe.Pointer(pParkedOrderAction)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspOrderAction_
func tOnRspOrderAction_(pInputOrderAction *C.struct_CThostFtdcInputOrderActionField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspOrderAction_ != nil{
        t.OnRspOrderAction_((*CThostFtdcInputOrderActionField)(unsafe.Pointer(pInputOrderAction)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryMaxOrderVolume_
func tOnRspQryMaxOrderVolume_(pQryMaxOrderVolume *C.struct_CThostFtdcQryMaxOrderVolumeField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryMaxOrderVolume_ != nil{
        t.OnRspQryMaxOrderVolume_((*CThostFtdcQryMaxOrderVolumeField)(unsafe.Pointer(pQryMaxOrderVolume)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspSettlementInfoConfirm_
func tOnRspSettlementInfoConfirm_(pSettlementInfoConfirm *C.struct_CThostFtdcSettlementInfoConfirmField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspSettlementInfoConfirm_ != nil{
        t.OnRspSettlementInfoConfirm_((*CThostFtdcSettlementInfoConfirmField)(unsafe.Pointer(pSettlementInfoConfirm)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspRemoveParkedOrder_
func tOnRspRemoveParkedOrder_(pRemoveParkedOrder *C.struct_CThostFtdcRemoveParkedOrderField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspRemoveParkedOrder_ != nil{
        t.OnRspRemoveParkedOrder_((*CThostFtdcRemoveParkedOrderField)(unsafe.Pointer(pRemoveParkedOrder)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspRemoveParkedOrderAction_
func tOnRspRemoveParkedOrderAction_(pRemoveParkedOrderAction *C.struct_CThostFtdcRemoveParkedOrderActionField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspRemoveParkedOrderAction_ != nil{
        t.OnRspRemoveParkedOrderAction_((*CThostFtdcRemoveParkedOrderActionField)(unsafe.Pointer(pRemoveParkedOrderAction)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspExecOrderInsert_
func tOnRspExecOrderInsert_(pInputExecOrder *C.struct_CThostFtdcInputExecOrderField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspExecOrderInsert_ != nil{
        t.OnRspExecOrderInsert_((*CThostFtdcInputExecOrderField)(unsafe.Pointer(pInputExecOrder)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspExecOrderAction_
func tOnRspExecOrderAction_(pInputExecOrderAction *C.struct_CThostFtdcInputExecOrderActionField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspExecOrderAction_ != nil{
        t.OnRspExecOrderAction_((*CThostFtdcInputExecOrderActionField)(unsafe.Pointer(pInputExecOrderAction)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspForQuoteInsert_
func tOnRspForQuoteInsert_(pInputForQuote *C.struct_CThostFtdcInputForQuoteField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspForQuoteInsert_ != nil{
        t.OnRspForQuoteInsert_((*CThostFtdcInputForQuoteField)(unsafe.Pointer(pInputForQuote)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQuoteInsert_
func tOnRspQuoteInsert_(pInputQuote *C.struct_CThostFtdcInputQuoteField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQuoteInsert_ != nil{
        t.OnRspQuoteInsert_((*CThostFtdcInputQuoteField)(unsafe.Pointer(pInputQuote)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQuoteAction_
func tOnRspQuoteAction_(pInputQuoteAction *C.struct_CThostFtdcInputQuoteActionField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQuoteAction_ != nil{
        t.OnRspQuoteAction_((*CThostFtdcInputQuoteActionField)(unsafe.Pointer(pInputQuoteAction)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspBatchOrderAction_
func tOnRspBatchOrderAction_(pInputBatchOrderAction *C.struct_CThostFtdcInputBatchOrderActionField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspBatchOrderAction_ != nil{
        t.OnRspBatchOrderAction_((*CThostFtdcInputBatchOrderActionField)(unsafe.Pointer(pInputBatchOrderAction)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspOptionSelfCloseInsert_
func tOnRspOptionSelfCloseInsert_(pInputOptionSelfClose *C.struct_CThostFtdcInputOptionSelfCloseField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspOptionSelfCloseInsert_ != nil{
        t.OnRspOptionSelfCloseInsert_((*CThostFtdcInputOptionSelfCloseField)(unsafe.Pointer(pInputOptionSelfClose)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspOptionSelfCloseAction_
func tOnRspOptionSelfCloseAction_(pInputOptionSelfCloseAction *C.struct_CThostFtdcInputOptionSelfCloseActionField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspOptionSelfCloseAction_ != nil{
        t.OnRspOptionSelfCloseAction_((*CThostFtdcInputOptionSelfCloseActionField)(unsafe.Pointer(pInputOptionSelfCloseAction)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspCombActionInsert_
func tOnRspCombActionInsert_(pInputCombAction *C.struct_CThostFtdcInputCombActionField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspCombActionInsert_ != nil{
        t.OnRspCombActionInsert_((*CThostFtdcInputCombActionField)(unsafe.Pointer(pInputCombAction)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryOrder_
func tOnRspQryOrder_(pOrder *C.struct_CThostFtdcOrderField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryOrder_ != nil{
        t.OnRspQryOrder_((*CThostFtdcOrderField)(unsafe.Pointer(pOrder)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryTrade_
func tOnRspQryTrade_(pTrade *C.struct_CThostFtdcTradeField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryTrade_ != nil{
        t.OnRspQryTrade_((*CThostFtdcTradeField)(unsafe.Pointer(pTrade)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryInvestorPosition_
func tOnRspQryInvestorPosition_(pInvestorPosition *C.struct_CThostFtdcInvestorPositionField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryInvestorPosition_ != nil{
        t.OnRspQryInvestorPosition_((*CThostFtdcInvestorPositionField)(unsafe.Pointer(pInvestorPosition)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryTradingAccount_
func tOnRspQryTradingAccount_(pTradingAccount *C.struct_CThostFtdcTradingAccountField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryTradingAccount_ != nil{
        t.OnRspQryTradingAccount_((*CThostFtdcTradingAccountField)(unsafe.Pointer(pTradingAccount)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryInvestor_
func tOnRspQryInvestor_(pInvestor *C.struct_CThostFtdcInvestorField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryInvestor_ != nil{
        t.OnRspQryInvestor_((*CThostFtdcInvestorField)(unsafe.Pointer(pInvestor)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryTradingCode_
func tOnRspQryTradingCode_(pTradingCode *C.struct_CThostFtdcTradingCodeField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryTradingCode_ != nil{
        t.OnRspQryTradingCode_((*CThostFtdcTradingCodeField)(unsafe.Pointer(pTradingCode)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryInstrumentMarginRate_
func tOnRspQryInstrumentMarginRate_(pInstrumentMarginRate *C.struct_CThostFtdcInstrumentMarginRateField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryInstrumentMarginRate_ != nil{
        t.OnRspQryInstrumentMarginRate_((*CThostFtdcInstrumentMarginRateField)(unsafe.Pointer(pInstrumentMarginRate)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryInstrumentCommissionRate_
func tOnRspQryInstrumentCommissionRate_(pInstrumentCommissionRate *C.struct_CThostFtdcInstrumentCommissionRateField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryInstrumentCommissionRate_ != nil{
        t.OnRspQryInstrumentCommissionRate_((*CThostFtdcInstrumentCommissionRateField)(unsafe.Pointer(pInstrumentCommissionRate)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryExchange_
func tOnRspQryExchange_(pExchange *C.struct_CThostFtdcExchangeField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryExchange_ != nil{
        t.OnRspQryExchange_((*CThostFtdcExchangeField)(unsafe.Pointer(pExchange)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryProduct_
func tOnRspQryProduct_(pProduct *C.struct_CThostFtdcProductField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryProduct_ != nil{
        t.OnRspQryProduct_((*CThostFtdcProductField)(unsafe.Pointer(pProduct)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryInstrument_
func tOnRspQryInstrument_(pInstrument *C.struct_CThostFtdcInstrumentField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryInstrument_ != nil{
        t.OnRspQryInstrument_((*CThostFtdcInstrumentField)(unsafe.Pointer(pInstrument)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryDepthMarketData_
func tOnRspQryDepthMarketData_(pDepthMarketData *C.struct_CThostFtdcDepthMarketDataField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryDepthMarketData_ != nil{
        t.OnRspQryDepthMarketData_((*CThostFtdcDepthMarketDataField)(unsafe.Pointer(pDepthMarketData)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryTraderOffer_
func tOnRspQryTraderOffer_(pTraderOffer *C.struct_CThostFtdcTraderOfferField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryTraderOffer_ != nil{
        t.OnRspQryTraderOffer_((*CThostFtdcTraderOfferField)(unsafe.Pointer(pTraderOffer)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQrySettlementInfo_
func tOnRspQrySettlementInfo_(pSettlementInfo *C.struct_CThostFtdcSettlementInfoField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQrySettlementInfo_ != nil{
        t.OnRspQrySettlementInfo_((*CThostFtdcSettlementInfoField)(unsafe.Pointer(pSettlementInfo)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryTransferBank_
func tOnRspQryTransferBank_(pTransferBank *C.struct_CThostFtdcTransferBankField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryTransferBank_ != nil{
        t.OnRspQryTransferBank_((*CThostFtdcTransferBankField)(unsafe.Pointer(pTransferBank)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryInvestorPositionDetail_
func tOnRspQryInvestorPositionDetail_(pInvestorPositionDetail *C.struct_CThostFtdcInvestorPositionDetailField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryInvestorPositionDetail_ != nil{
        t.OnRspQryInvestorPositionDetail_((*CThostFtdcInvestorPositionDetailField)(unsafe.Pointer(pInvestorPositionDetail)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryNotice_
func tOnRspQryNotice_(pNotice *C.struct_CThostFtdcNoticeField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryNotice_ != nil{
        t.OnRspQryNotice_((*CThostFtdcNoticeField)(unsafe.Pointer(pNotice)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQrySettlementInfoConfirm_
func tOnRspQrySettlementInfoConfirm_(pSettlementInfoConfirm *C.struct_CThostFtdcSettlementInfoConfirmField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQrySettlementInfoConfirm_ != nil{
        t.OnRspQrySettlementInfoConfirm_((*CThostFtdcSettlementInfoConfirmField)(unsafe.Pointer(pSettlementInfoConfirm)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryInvestorPositionCombineDetail_
func tOnRspQryInvestorPositionCombineDetail_(pInvestorPositionCombineDetail *C.struct_CThostFtdcInvestorPositionCombineDetailField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryInvestorPositionCombineDetail_ != nil{
        t.OnRspQryInvestorPositionCombineDetail_((*CThostFtdcInvestorPositionCombineDetailField)(unsafe.Pointer(pInvestorPositionCombineDetail)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryCFMMCTradingAccountKey_
func tOnRspQryCFMMCTradingAccountKey_(pCFMMCTradingAccountKey *C.struct_CThostFtdcCFMMCTradingAccountKeyField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryCFMMCTradingAccountKey_ != nil{
        t.OnRspQryCFMMCTradingAccountKey_((*CThostFtdcCFMMCTradingAccountKeyField)(unsafe.Pointer(pCFMMCTradingAccountKey)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryEWarrantOffset_
func tOnRspQryEWarrantOffset_(pEWarrantOffset *C.struct_CThostFtdcEWarrantOffsetField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryEWarrantOffset_ != nil{
        t.OnRspQryEWarrantOffset_((*CThostFtdcEWarrantOffsetField)(unsafe.Pointer(pEWarrantOffset)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryInvestorProductGroupMargin_
func tOnRspQryInvestorProductGroupMargin_(pInvestorProductGroupMargin *C.struct_CThostFtdcInvestorProductGroupMarginField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryInvestorProductGroupMargin_ != nil{
        t.OnRspQryInvestorProductGroupMargin_((*CThostFtdcInvestorProductGroupMarginField)(unsafe.Pointer(pInvestorProductGroupMargin)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryExchangeMarginRate_
func tOnRspQryExchangeMarginRate_(pExchangeMarginRate *C.struct_CThostFtdcExchangeMarginRateField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryExchangeMarginRate_ != nil{
        t.OnRspQryExchangeMarginRate_((*CThostFtdcExchangeMarginRateField)(unsafe.Pointer(pExchangeMarginRate)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryExchangeMarginRateAdjust_
func tOnRspQryExchangeMarginRateAdjust_(pExchangeMarginRateAdjust *C.struct_CThostFtdcExchangeMarginRateAdjustField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryExchangeMarginRateAdjust_ != nil{
        t.OnRspQryExchangeMarginRateAdjust_((*CThostFtdcExchangeMarginRateAdjustField)(unsafe.Pointer(pExchangeMarginRateAdjust)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryExchangeRate_
func tOnRspQryExchangeRate_(pExchangeRate *C.struct_CThostFtdcExchangeRateField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryExchangeRate_ != nil{
        t.OnRspQryExchangeRate_((*CThostFtdcExchangeRateField)(unsafe.Pointer(pExchangeRate)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQrySecAgentACIDMap_
func tOnRspQrySecAgentACIDMap_(pSecAgentACIDMap *C.struct_CThostFtdcSecAgentACIDMapField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQrySecAgentACIDMap_ != nil{
        t.OnRspQrySecAgentACIDMap_((*CThostFtdcSecAgentACIDMapField)(unsafe.Pointer(pSecAgentACIDMap)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryProductExchRate_
func tOnRspQryProductExchRate_(pProductExchRate *C.struct_CThostFtdcProductExchRateField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryProductExchRate_ != nil{
        t.OnRspQryProductExchRate_((*CThostFtdcProductExchRateField)(unsafe.Pointer(pProductExchRate)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryProductGroup_
func tOnRspQryProductGroup_(pProductGroup *C.struct_CThostFtdcProductGroupField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryProductGroup_ != nil{
        t.OnRspQryProductGroup_((*CThostFtdcProductGroupField)(unsafe.Pointer(pProductGroup)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryMMInstrumentCommissionRate_
func tOnRspQryMMInstrumentCommissionRate_(pMMInstrumentCommissionRate *C.struct_CThostFtdcMMInstrumentCommissionRateField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryMMInstrumentCommissionRate_ != nil{
        t.OnRspQryMMInstrumentCommissionRate_((*CThostFtdcMMInstrumentCommissionRateField)(unsafe.Pointer(pMMInstrumentCommissionRate)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryMMOptionInstrCommRate_
func tOnRspQryMMOptionInstrCommRate_(pMMOptionInstrCommRate *C.struct_CThostFtdcMMOptionInstrCommRateField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryMMOptionInstrCommRate_ != nil{
        t.OnRspQryMMOptionInstrCommRate_((*CThostFtdcMMOptionInstrCommRateField)(unsafe.Pointer(pMMOptionInstrCommRate)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryInstrumentOrderCommRate_
func tOnRspQryInstrumentOrderCommRate_(pInstrumentOrderCommRate *C.struct_CThostFtdcInstrumentOrderCommRateField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryInstrumentOrderCommRate_ != nil{
        t.OnRspQryInstrumentOrderCommRate_((*CThostFtdcInstrumentOrderCommRateField)(unsafe.Pointer(pInstrumentOrderCommRate)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQrySecAgentTradingAccount_
func tOnRspQrySecAgentTradingAccount_(pTradingAccount *C.struct_CThostFtdcTradingAccountField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQrySecAgentTradingAccount_ != nil{
        t.OnRspQrySecAgentTradingAccount_((*CThostFtdcTradingAccountField)(unsafe.Pointer(pTradingAccount)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQrySecAgentCheckMode_
func tOnRspQrySecAgentCheckMode_(pSecAgentCheckMode *C.struct_CThostFtdcSecAgentCheckModeField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQrySecAgentCheckMode_ != nil{
        t.OnRspQrySecAgentCheckMode_((*CThostFtdcSecAgentCheckModeField)(unsafe.Pointer(pSecAgentCheckMode)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQrySecAgentTradeInfo_
func tOnRspQrySecAgentTradeInfo_(pSecAgentTradeInfo *C.struct_CThostFtdcSecAgentTradeInfoField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQrySecAgentTradeInfo_ != nil{
        t.OnRspQrySecAgentTradeInfo_((*CThostFtdcSecAgentTradeInfoField)(unsafe.Pointer(pSecAgentTradeInfo)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryOptionInstrTradeCost_
func tOnRspQryOptionInstrTradeCost_(pOptionInstrTradeCost *C.struct_CThostFtdcOptionInstrTradeCostField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryOptionInstrTradeCost_ != nil{
        t.OnRspQryOptionInstrTradeCost_((*CThostFtdcOptionInstrTradeCostField)(unsafe.Pointer(pOptionInstrTradeCost)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryOptionInstrCommRate_
func tOnRspQryOptionInstrCommRate_(pOptionInstrCommRate *C.struct_CThostFtdcOptionInstrCommRateField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryOptionInstrCommRate_ != nil{
        t.OnRspQryOptionInstrCommRate_((*CThostFtdcOptionInstrCommRateField)(unsafe.Pointer(pOptionInstrCommRate)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryExecOrder_
func tOnRspQryExecOrder_(pExecOrder *C.struct_CThostFtdcExecOrderField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryExecOrder_ != nil{
        t.OnRspQryExecOrder_((*CThostFtdcExecOrderField)(unsafe.Pointer(pExecOrder)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryForQuote_
func tOnRspQryForQuote_(pForQuote *C.struct_CThostFtdcForQuoteField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryForQuote_ != nil{
        t.OnRspQryForQuote_((*CThostFtdcForQuoteField)(unsafe.Pointer(pForQuote)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryQuote_
func tOnRspQryQuote_(pQuote *C.struct_CThostFtdcQuoteField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryQuote_ != nil{
        t.OnRspQryQuote_((*CThostFtdcQuoteField)(unsafe.Pointer(pQuote)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryOptionSelfClose_
func tOnRspQryOptionSelfClose_(pOptionSelfClose *C.struct_CThostFtdcOptionSelfCloseField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryOptionSelfClose_ != nil{
        t.OnRspQryOptionSelfClose_((*CThostFtdcOptionSelfCloseField)(unsafe.Pointer(pOptionSelfClose)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryInvestUnit_
func tOnRspQryInvestUnit_(pInvestUnit *C.struct_CThostFtdcInvestUnitField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryInvestUnit_ != nil{
        t.OnRspQryInvestUnit_((*CThostFtdcInvestUnitField)(unsafe.Pointer(pInvestUnit)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryCombInstrumentGuard_
func tOnRspQryCombInstrumentGuard_(pCombInstrumentGuard *C.struct_CThostFtdcCombInstrumentGuardField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryCombInstrumentGuard_ != nil{
        t.OnRspQryCombInstrumentGuard_((*CThostFtdcCombInstrumentGuardField)(unsafe.Pointer(pCombInstrumentGuard)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryCombAction_
func tOnRspQryCombAction_(pCombAction *C.struct_CThostFtdcCombActionField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryCombAction_ != nil{
        t.OnRspQryCombAction_((*CThostFtdcCombActionField)(unsafe.Pointer(pCombAction)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryTransferSerial_
func tOnRspQryTransferSerial_(pTransferSerial *C.struct_CThostFtdcTransferSerialField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryTransferSerial_ != nil{
        t.OnRspQryTransferSerial_((*CThostFtdcTransferSerialField)(unsafe.Pointer(pTransferSerial)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryAccountregister_
func tOnRspQryAccountregister_(pAccountregister *C.struct_CThostFtdcAccountregisterField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryAccountregister_ != nil{
        t.OnRspQryAccountregister_((*CThostFtdcAccountregisterField)(unsafe.Pointer(pAccountregister)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspError_
func tOnRspError_(pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspError_ != nil{
        t.OnRspError_((*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRtnOrder_
func tOnRtnOrder_(pOrder *C.struct_CThostFtdcOrderField) C.int {
    if t.OnRtnOrder_ != nil{
        t.OnRtnOrder_((*CThostFtdcOrderField)(unsafe.Pointer(pOrder)))
    }
	return 0
}

//export tOnRtnTrade_
func tOnRtnTrade_(pTrade *C.struct_CThostFtdcTradeField) C.int {
    if t.OnRtnTrade_ != nil{
        t.OnRtnTrade_((*CThostFtdcTradeField)(unsafe.Pointer(pTrade)))
    }
	return 0
}

//export tOnErrRtnOrderInsert_
func tOnErrRtnOrderInsert_(pInputOrder *C.struct_CThostFtdcInputOrderField, pRspInfo *C.struct_CThostFtdcRspInfoField) C.int {
    if t.OnErrRtnOrderInsert_ != nil{
        t.OnErrRtnOrderInsert_((*CThostFtdcInputOrderField)(unsafe.Pointer(pInputOrder)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)))
    }
	return 0
}

//export tOnErrRtnOrderAction_
func tOnErrRtnOrderAction_(pOrderAction *C.struct_CThostFtdcOrderActionField, pRspInfo *C.struct_CThostFtdcRspInfoField) C.int {
    if t.OnErrRtnOrderAction_ != nil{
        t.OnErrRtnOrderAction_((*CThostFtdcOrderActionField)(unsafe.Pointer(pOrderAction)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)))
    }
	return 0
}

//export tOnRtnInstrumentStatus_
func tOnRtnInstrumentStatus_(pInstrumentStatus *C.struct_CThostFtdcInstrumentStatusField) C.int {
    if t.OnRtnInstrumentStatus_ != nil{
        t.OnRtnInstrumentStatus_((*CThostFtdcInstrumentStatusField)(unsafe.Pointer(pInstrumentStatus)))
    }
	return 0
}

//export tOnRtnBulletin_
func tOnRtnBulletin_(pBulletin *C.struct_CThostFtdcBulletinField) C.int {
    if t.OnRtnBulletin_ != nil{
        t.OnRtnBulletin_((*CThostFtdcBulletinField)(unsafe.Pointer(pBulletin)))
    }
	return 0
}

//export tOnRtnTradingNotice_
func tOnRtnTradingNotice_(pTradingNoticeInfo *C.struct_CThostFtdcTradingNoticeInfoField) C.int {
    if t.OnRtnTradingNotice_ != nil{
        t.OnRtnTradingNotice_((*CThostFtdcTradingNoticeInfoField)(unsafe.Pointer(pTradingNoticeInfo)))
    }
	return 0
}

//export tOnRtnErrorConditionalOrder_
func tOnRtnErrorConditionalOrder_(pErrorConditionalOrder *C.struct_CThostFtdcErrorConditionalOrderField) C.int {
    if t.OnRtnErrorConditionalOrder_ != nil{
        t.OnRtnErrorConditionalOrder_((*CThostFtdcErrorConditionalOrderField)(unsafe.Pointer(pErrorConditionalOrder)))
    }
	return 0
}

//export tOnRtnExecOrder_
func tOnRtnExecOrder_(pExecOrder *C.struct_CThostFtdcExecOrderField) C.int {
    if t.OnRtnExecOrder_ != nil{
        t.OnRtnExecOrder_((*CThostFtdcExecOrderField)(unsafe.Pointer(pExecOrder)))
    }
	return 0
}

//export tOnErrRtnExecOrderInsert_
func tOnErrRtnExecOrderInsert_(pInputExecOrder *C.struct_CThostFtdcInputExecOrderField, pRspInfo *C.struct_CThostFtdcRspInfoField) C.int {
    if t.OnErrRtnExecOrderInsert_ != nil{
        t.OnErrRtnExecOrderInsert_((*CThostFtdcInputExecOrderField)(unsafe.Pointer(pInputExecOrder)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)))
    }
	return 0
}

//export tOnErrRtnExecOrderAction_
func tOnErrRtnExecOrderAction_(pExecOrderAction *C.struct_CThostFtdcExecOrderActionField, pRspInfo *C.struct_CThostFtdcRspInfoField) C.int {
    if t.OnErrRtnExecOrderAction_ != nil{
        t.OnErrRtnExecOrderAction_((*CThostFtdcExecOrderActionField)(unsafe.Pointer(pExecOrderAction)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)))
    }
	return 0
}

//export tOnErrRtnForQuoteInsert_
func tOnErrRtnForQuoteInsert_(pInputForQuote *C.struct_CThostFtdcInputForQuoteField, pRspInfo *C.struct_CThostFtdcRspInfoField) C.int {
    if t.OnErrRtnForQuoteInsert_ != nil{
        t.OnErrRtnForQuoteInsert_((*CThostFtdcInputForQuoteField)(unsafe.Pointer(pInputForQuote)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)))
    }
	return 0
}

//export tOnRtnQuote_
func tOnRtnQuote_(pQuote *C.struct_CThostFtdcQuoteField) C.int {
    if t.OnRtnQuote_ != nil{
        t.OnRtnQuote_((*CThostFtdcQuoteField)(unsafe.Pointer(pQuote)))
    }
	return 0
}

//export tOnErrRtnQuoteInsert_
func tOnErrRtnQuoteInsert_(pInputQuote *C.struct_CThostFtdcInputQuoteField, pRspInfo *C.struct_CThostFtdcRspInfoField) C.int {
    if t.OnErrRtnQuoteInsert_ != nil{
        t.OnErrRtnQuoteInsert_((*CThostFtdcInputQuoteField)(unsafe.Pointer(pInputQuote)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)))
    }
	return 0
}

//export tOnErrRtnQuoteAction_
func tOnErrRtnQuoteAction_(pQuoteAction *C.struct_CThostFtdcQuoteActionField, pRspInfo *C.struct_CThostFtdcRspInfoField) C.int {
    if t.OnErrRtnQuoteAction_ != nil{
        t.OnErrRtnQuoteAction_((*CThostFtdcQuoteActionField)(unsafe.Pointer(pQuoteAction)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)))
    }
	return 0
}

//export tOnRtnForQuoteRsp_
func tOnRtnForQuoteRsp_(pForQuoteRsp *C.struct_CThostFtdcForQuoteRspField) C.int {
    if t.OnRtnForQuoteRsp_ != nil{
        t.OnRtnForQuoteRsp_((*CThostFtdcForQuoteRspField)(unsafe.Pointer(pForQuoteRsp)))
    }
	return 0
}

//export tOnRtnCFMMCTradingAccountToken_
func tOnRtnCFMMCTradingAccountToken_(pCFMMCTradingAccountToken *C.struct_CThostFtdcCFMMCTradingAccountTokenField) C.int {
    if t.OnRtnCFMMCTradingAccountToken_ != nil{
        t.OnRtnCFMMCTradingAccountToken_((*CThostFtdcCFMMCTradingAccountTokenField)(unsafe.Pointer(pCFMMCTradingAccountToken)))
    }
	return 0
}

//export tOnErrRtnBatchOrderAction_
func tOnErrRtnBatchOrderAction_(pBatchOrderAction *C.struct_CThostFtdcBatchOrderActionField, pRspInfo *C.struct_CThostFtdcRspInfoField) C.int {
    if t.OnErrRtnBatchOrderAction_ != nil{
        t.OnErrRtnBatchOrderAction_((*CThostFtdcBatchOrderActionField)(unsafe.Pointer(pBatchOrderAction)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)))
    }
	return 0
}

//export tOnRtnOptionSelfClose_
func tOnRtnOptionSelfClose_(pOptionSelfClose *C.struct_CThostFtdcOptionSelfCloseField) C.int {
    if t.OnRtnOptionSelfClose_ != nil{
        t.OnRtnOptionSelfClose_((*CThostFtdcOptionSelfCloseField)(unsafe.Pointer(pOptionSelfClose)))
    }
	return 0
}

//export tOnErrRtnOptionSelfCloseInsert_
func tOnErrRtnOptionSelfCloseInsert_(pInputOptionSelfClose *C.struct_CThostFtdcInputOptionSelfCloseField, pRspInfo *C.struct_CThostFtdcRspInfoField) C.int {
    if t.OnErrRtnOptionSelfCloseInsert_ != nil{
        t.OnErrRtnOptionSelfCloseInsert_((*CThostFtdcInputOptionSelfCloseField)(unsafe.Pointer(pInputOptionSelfClose)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)))
    }
	return 0
}

//export tOnErrRtnOptionSelfCloseAction_
func tOnErrRtnOptionSelfCloseAction_(pOptionSelfCloseAction *C.struct_CThostFtdcOptionSelfCloseActionField, pRspInfo *C.struct_CThostFtdcRspInfoField) C.int {
    if t.OnErrRtnOptionSelfCloseAction_ != nil{
        t.OnErrRtnOptionSelfCloseAction_((*CThostFtdcOptionSelfCloseActionField)(unsafe.Pointer(pOptionSelfCloseAction)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)))
    }
	return 0
}

//export tOnRtnCombAction_
func tOnRtnCombAction_(pCombAction *C.struct_CThostFtdcCombActionField) C.int {
    if t.OnRtnCombAction_ != nil{
        t.OnRtnCombAction_((*CThostFtdcCombActionField)(unsafe.Pointer(pCombAction)))
    }
	return 0
}

//export tOnErrRtnCombActionInsert_
func tOnErrRtnCombActionInsert_(pInputCombAction *C.struct_CThostFtdcInputCombActionField, pRspInfo *C.struct_CThostFtdcRspInfoField) C.int {
    if t.OnErrRtnCombActionInsert_ != nil{
        t.OnErrRtnCombActionInsert_((*CThostFtdcInputCombActionField)(unsafe.Pointer(pInputCombAction)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)))
    }
	return 0
}

//export tOnRspQryContractBank_
func tOnRspQryContractBank_(pContractBank *C.struct_CThostFtdcContractBankField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryContractBank_ != nil{
        t.OnRspQryContractBank_((*CThostFtdcContractBankField)(unsafe.Pointer(pContractBank)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryParkedOrder_
func tOnRspQryParkedOrder_(pParkedOrder *C.struct_CThostFtdcParkedOrderField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryParkedOrder_ != nil{
        t.OnRspQryParkedOrder_((*CThostFtdcParkedOrderField)(unsafe.Pointer(pParkedOrder)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryParkedOrderAction_
func tOnRspQryParkedOrderAction_(pParkedOrderAction *C.struct_CThostFtdcParkedOrderActionField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryParkedOrderAction_ != nil{
        t.OnRspQryParkedOrderAction_((*CThostFtdcParkedOrderActionField)(unsafe.Pointer(pParkedOrderAction)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryTradingNotice_
func tOnRspQryTradingNotice_(pTradingNotice *C.struct_CThostFtdcTradingNoticeField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryTradingNotice_ != nil{
        t.OnRspQryTradingNotice_((*CThostFtdcTradingNoticeField)(unsafe.Pointer(pTradingNotice)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryBrokerTradingParams_
func tOnRspQryBrokerTradingParams_(pBrokerTradingParams *C.struct_CThostFtdcBrokerTradingParamsField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryBrokerTradingParams_ != nil{
        t.OnRspQryBrokerTradingParams_((*CThostFtdcBrokerTradingParamsField)(unsafe.Pointer(pBrokerTradingParams)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryBrokerTradingAlgos_
func tOnRspQryBrokerTradingAlgos_(pBrokerTradingAlgos *C.struct_CThostFtdcBrokerTradingAlgosField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryBrokerTradingAlgos_ != nil{
        t.OnRspQryBrokerTradingAlgos_((*CThostFtdcBrokerTradingAlgosField)(unsafe.Pointer(pBrokerTradingAlgos)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQueryCFMMCTradingAccountToken_
func tOnRspQueryCFMMCTradingAccountToken_(pQueryCFMMCTradingAccountToken *C.struct_CThostFtdcQueryCFMMCTradingAccountTokenField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQueryCFMMCTradingAccountToken_ != nil{
        t.OnRspQueryCFMMCTradingAccountToken_((*CThostFtdcQueryCFMMCTradingAccountTokenField)(unsafe.Pointer(pQueryCFMMCTradingAccountToken)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRtnFromBankToFutureByBank_
func tOnRtnFromBankToFutureByBank_(pRspTransfer *C.struct_CThostFtdcRspTransferField) C.int {
    if t.OnRtnFromBankToFutureByBank_ != nil{
        t.OnRtnFromBankToFutureByBank_((*CThostFtdcRspTransferField)(unsafe.Pointer(pRspTransfer)))
    }
	return 0
}

//export tOnRtnFromFutureToBankByBank_
func tOnRtnFromFutureToBankByBank_(pRspTransfer *C.struct_CThostFtdcRspTransferField) C.int {
    if t.OnRtnFromFutureToBankByBank_ != nil{
        t.OnRtnFromFutureToBankByBank_((*CThostFtdcRspTransferField)(unsafe.Pointer(pRspTransfer)))
    }
	return 0
}

//export tOnRtnRepealFromBankToFutureByBank_
func tOnRtnRepealFromBankToFutureByBank_(pRspRepeal *C.struct_CThostFtdcRspRepealField) C.int {
    if t.OnRtnRepealFromBankToFutureByBank_ != nil{
        t.OnRtnRepealFromBankToFutureByBank_((*CThostFtdcRspRepealField)(unsafe.Pointer(pRspRepeal)))
    }
	return 0
}

//export tOnRtnRepealFromFutureToBankByBank_
func tOnRtnRepealFromFutureToBankByBank_(pRspRepeal *C.struct_CThostFtdcRspRepealField) C.int {
    if t.OnRtnRepealFromFutureToBankByBank_ != nil{
        t.OnRtnRepealFromFutureToBankByBank_((*CThostFtdcRspRepealField)(unsafe.Pointer(pRspRepeal)))
    }
	return 0
}

//export tOnRtnFromBankToFutureByFuture_
func tOnRtnFromBankToFutureByFuture_(pRspTransfer *C.struct_CThostFtdcRspTransferField) C.int {
    if t.OnRtnFromBankToFutureByFuture_ != nil{
        t.OnRtnFromBankToFutureByFuture_((*CThostFtdcRspTransferField)(unsafe.Pointer(pRspTransfer)))
    }
	return 0
}

//export tOnRtnFromFutureToBankByFuture_
func tOnRtnFromFutureToBankByFuture_(pRspTransfer *C.struct_CThostFtdcRspTransferField) C.int {
    if t.OnRtnFromFutureToBankByFuture_ != nil{
        t.OnRtnFromFutureToBankByFuture_((*CThostFtdcRspTransferField)(unsafe.Pointer(pRspTransfer)))
    }
	return 0
}

//export tOnRtnRepealFromBankToFutureByFutureManual_
func tOnRtnRepealFromBankToFutureByFutureManual_(pRspRepeal *C.struct_CThostFtdcRspRepealField) C.int {
    if t.OnRtnRepealFromBankToFutureByFutureManual_ != nil{
        t.OnRtnRepealFromBankToFutureByFutureManual_((*CThostFtdcRspRepealField)(unsafe.Pointer(pRspRepeal)))
    }
	return 0
}

//export tOnRtnRepealFromFutureToBankByFutureManual_
func tOnRtnRepealFromFutureToBankByFutureManual_(pRspRepeal *C.struct_CThostFtdcRspRepealField) C.int {
    if t.OnRtnRepealFromFutureToBankByFutureManual_ != nil{
        t.OnRtnRepealFromFutureToBankByFutureManual_((*CThostFtdcRspRepealField)(unsafe.Pointer(pRspRepeal)))
    }
	return 0
}

//export tOnRtnQueryBankBalanceByFuture_
func tOnRtnQueryBankBalanceByFuture_(pNotifyQueryAccount *C.struct_CThostFtdcNotifyQueryAccountField) C.int {
    if t.OnRtnQueryBankBalanceByFuture_ != nil{
        t.OnRtnQueryBankBalanceByFuture_((*CThostFtdcNotifyQueryAccountField)(unsafe.Pointer(pNotifyQueryAccount)))
    }
	return 0
}

//export tOnErrRtnBankToFutureByFuture_
func tOnErrRtnBankToFutureByFuture_(pReqTransfer *C.struct_CThostFtdcReqTransferField, pRspInfo *C.struct_CThostFtdcRspInfoField) C.int {
    if t.OnErrRtnBankToFutureByFuture_ != nil{
        t.OnErrRtnBankToFutureByFuture_((*CThostFtdcReqTransferField)(unsafe.Pointer(pReqTransfer)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)))
    }
	return 0
}

//export tOnErrRtnFutureToBankByFuture_
func tOnErrRtnFutureToBankByFuture_(pReqTransfer *C.struct_CThostFtdcReqTransferField, pRspInfo *C.struct_CThostFtdcRspInfoField) C.int {
    if t.OnErrRtnFutureToBankByFuture_ != nil{
        t.OnErrRtnFutureToBankByFuture_((*CThostFtdcReqTransferField)(unsafe.Pointer(pReqTransfer)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)))
    }
	return 0
}

//export tOnErrRtnRepealBankToFutureByFutureManual_
func tOnErrRtnRepealBankToFutureByFutureManual_(pReqRepeal *C.struct_CThostFtdcReqRepealField, pRspInfo *C.struct_CThostFtdcRspInfoField) C.int {
    if t.OnErrRtnRepealBankToFutureByFutureManual_ != nil{
        t.OnErrRtnRepealBankToFutureByFutureManual_((*CThostFtdcReqRepealField)(unsafe.Pointer(pReqRepeal)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)))
    }
	return 0
}

//export tOnErrRtnRepealFutureToBankByFutureManual_
func tOnErrRtnRepealFutureToBankByFutureManual_(pReqRepeal *C.struct_CThostFtdcReqRepealField, pRspInfo *C.struct_CThostFtdcRspInfoField) C.int {
    if t.OnErrRtnRepealFutureToBankByFutureManual_ != nil{
        t.OnErrRtnRepealFutureToBankByFutureManual_((*CThostFtdcReqRepealField)(unsafe.Pointer(pReqRepeal)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)))
    }
	return 0
}

//export tOnErrRtnQueryBankBalanceByFuture_
func tOnErrRtnQueryBankBalanceByFuture_(pReqQueryAccount *C.struct_CThostFtdcReqQueryAccountField, pRspInfo *C.struct_CThostFtdcRspInfoField) C.int {
    if t.OnErrRtnQueryBankBalanceByFuture_ != nil{
        t.OnErrRtnQueryBankBalanceByFuture_((*CThostFtdcReqQueryAccountField)(unsafe.Pointer(pReqQueryAccount)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)))
    }
	return 0
}

//export tOnRtnRepealFromBankToFutureByFuture_
func tOnRtnRepealFromBankToFutureByFuture_(pRspRepeal *C.struct_CThostFtdcRspRepealField) C.int {
    if t.OnRtnRepealFromBankToFutureByFuture_ != nil{
        t.OnRtnRepealFromBankToFutureByFuture_((*CThostFtdcRspRepealField)(unsafe.Pointer(pRspRepeal)))
    }
	return 0
}

//export tOnRtnRepealFromFutureToBankByFuture_
func tOnRtnRepealFromFutureToBankByFuture_(pRspRepeal *C.struct_CThostFtdcRspRepealField) C.int {
    if t.OnRtnRepealFromFutureToBankByFuture_ != nil{
        t.OnRtnRepealFromFutureToBankByFuture_((*CThostFtdcRspRepealField)(unsafe.Pointer(pRspRepeal)))
    }
	return 0
}

//export tOnRspFromBankToFutureByFuture_
func tOnRspFromBankToFutureByFuture_(pReqTransfer *C.struct_CThostFtdcReqTransferField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspFromBankToFutureByFuture_ != nil{
        t.OnRspFromBankToFutureByFuture_((*CThostFtdcReqTransferField)(unsafe.Pointer(pReqTransfer)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspFromFutureToBankByFuture_
func tOnRspFromFutureToBankByFuture_(pReqTransfer *C.struct_CThostFtdcReqTransferField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspFromFutureToBankByFuture_ != nil{
        t.OnRspFromFutureToBankByFuture_((*CThostFtdcReqTransferField)(unsafe.Pointer(pReqTransfer)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQueryBankAccountMoneyByFuture_
func tOnRspQueryBankAccountMoneyByFuture_(pReqQueryAccount *C.struct_CThostFtdcReqQueryAccountField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQueryBankAccountMoneyByFuture_ != nil{
        t.OnRspQueryBankAccountMoneyByFuture_((*CThostFtdcReqQueryAccountField)(unsafe.Pointer(pReqQueryAccount)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRtnOpenAccountByBank_
func tOnRtnOpenAccountByBank_(pOpenAccount *C.struct_CThostFtdcOpenAccountField) C.int {
    if t.OnRtnOpenAccountByBank_ != nil{
        t.OnRtnOpenAccountByBank_((*CThostFtdcOpenAccountField)(unsafe.Pointer(pOpenAccount)))
    }
	return 0
}

//export tOnRtnCancelAccountByBank_
func tOnRtnCancelAccountByBank_(pCancelAccount *C.struct_CThostFtdcCancelAccountField) C.int {
    if t.OnRtnCancelAccountByBank_ != nil{
        t.OnRtnCancelAccountByBank_((*CThostFtdcCancelAccountField)(unsafe.Pointer(pCancelAccount)))
    }
	return 0
}

//export tOnRtnChangeAccountByBank_
func tOnRtnChangeAccountByBank_(pChangeAccount *C.struct_CThostFtdcChangeAccountField) C.int {
    if t.OnRtnChangeAccountByBank_ != nil{
        t.OnRtnChangeAccountByBank_((*CThostFtdcChangeAccountField)(unsafe.Pointer(pChangeAccount)))
    }
	return 0
}

//export tOnRspQryClassifiedInstrument_
func tOnRspQryClassifiedInstrument_(pInstrument *C.struct_CThostFtdcInstrumentField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryClassifiedInstrument_ != nil{
        t.OnRspQryClassifiedInstrument_((*CThostFtdcInstrumentField)(unsafe.Pointer(pInstrument)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryCombPromotionParam_
func tOnRspQryCombPromotionParam_(pCombPromotionParam *C.struct_CThostFtdcCombPromotionParamField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryCombPromotionParam_ != nil{
        t.OnRspQryCombPromotionParam_((*CThostFtdcCombPromotionParamField)(unsafe.Pointer(pCombPromotionParam)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryRiskSettleInvstPosition_
func tOnRspQryRiskSettleInvstPosition_(pRiskSettleInvstPosition *C.struct_CThostFtdcRiskSettleInvstPositionField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryRiskSettleInvstPosition_ != nil{
        t.OnRspQryRiskSettleInvstPosition_((*CThostFtdcRiskSettleInvstPositionField)(unsafe.Pointer(pRiskSettleInvstPosition)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryRiskSettleProductStatus_
func tOnRspQryRiskSettleProductStatus_(pRiskSettleProductStatus *C.struct_CThostFtdcRiskSettleProductStatusField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryRiskSettleProductStatus_ != nil{
        t.OnRspQryRiskSettleProductStatus_((*CThostFtdcRiskSettleProductStatusField)(unsafe.Pointer(pRiskSettleProductStatus)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQrySPBMFutureParameter_
func tOnRspQrySPBMFutureParameter_(pSPBMFutureParameter *C.struct_CThostFtdcSPBMFutureParameterField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQrySPBMFutureParameter_ != nil{
        t.OnRspQrySPBMFutureParameter_((*CThostFtdcSPBMFutureParameterField)(unsafe.Pointer(pSPBMFutureParameter)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQrySPBMOptionParameter_
func tOnRspQrySPBMOptionParameter_(pSPBMOptionParameter *C.struct_CThostFtdcSPBMOptionParameterField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQrySPBMOptionParameter_ != nil{
        t.OnRspQrySPBMOptionParameter_((*CThostFtdcSPBMOptionParameterField)(unsafe.Pointer(pSPBMOptionParameter)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQrySPBMIntraParameter_
func tOnRspQrySPBMIntraParameter_(pSPBMIntraParameter *C.struct_CThostFtdcSPBMIntraParameterField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQrySPBMIntraParameter_ != nil{
        t.OnRspQrySPBMIntraParameter_((*CThostFtdcSPBMIntraParameterField)(unsafe.Pointer(pSPBMIntraParameter)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQrySPBMInterParameter_
func tOnRspQrySPBMInterParameter_(pSPBMInterParameter *C.struct_CThostFtdcSPBMInterParameterField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQrySPBMInterParameter_ != nil{
        t.OnRspQrySPBMInterParameter_((*CThostFtdcSPBMInterParameterField)(unsafe.Pointer(pSPBMInterParameter)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQrySPBMPortfDefinition_
func tOnRspQrySPBMPortfDefinition_(pSPBMPortfDefinition *C.struct_CThostFtdcSPBMPortfDefinitionField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQrySPBMPortfDefinition_ != nil{
        t.OnRspQrySPBMPortfDefinition_((*CThostFtdcSPBMPortfDefinitionField)(unsafe.Pointer(pSPBMPortfDefinition)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQrySPBMInvestorPortfDef_
func tOnRspQrySPBMInvestorPortfDef_(pSPBMInvestorPortfDef *C.struct_CThostFtdcSPBMInvestorPortfDefField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQrySPBMInvestorPortfDef_ != nil{
        t.OnRspQrySPBMInvestorPortfDef_((*CThostFtdcSPBMInvestorPortfDefField)(unsafe.Pointer(pSPBMInvestorPortfDef)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryInvestorPortfMarginRatio_
func tOnRspQryInvestorPortfMarginRatio_(pInvestorPortfMarginRatio *C.struct_CThostFtdcInvestorPortfMarginRatioField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryInvestorPortfMarginRatio_ != nil{
        t.OnRspQryInvestorPortfMarginRatio_((*CThostFtdcInvestorPortfMarginRatioField)(unsafe.Pointer(pInvestorPortfMarginRatio)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}

//export tOnRspQryInvestorProdSPBMDetail_
func tOnRspQryInvestorProdSPBMDetail_(pInvestorProdSPBMDetail *C.struct_CThostFtdcInvestorProdSPBMDetailField, pRspInfo *C.struct_CThostFtdcRspInfoField, nRequestID C.int, bIsLast C._Bool) C.int {
    if t.OnRspQryInvestorProdSPBMDetail_ != nil{
        t.OnRspQryInvestorProdSPBMDetail_((*CThostFtdcInvestorProdSPBMDetailField)(unsafe.Pointer(pInvestorProdSPBMDetail)), (*CThostFtdcRspInfoField)(unsafe.Pointer(pRspInfo)), int(nRequestID), bool(bIsLast))
    }
	return 0
}
