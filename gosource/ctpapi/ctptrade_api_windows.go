package ctpapi

import (
	"os"
	"path"
	"path/filepath"
	"runtime"
	"syscall"
	"unsafe"
)

type Trade struct {
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

func InitTrade() *Trade {
	t := new(Trade)
	// Load DLL
	workPath, _ := os.Getwd()
	_, curFile, _, _ := runtime.Caller(1)
	dllPath := filepath.Dir(curFile)
	dllPath = path.Join(dllPath, "../../libs/ctpapi/")
	_ = os.Chdir(dllPath)
	t.h = syscall.MustLoadDLL("ctptrade_api.dll")
	os.Chdir(workPath)

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

func (t *Trade) CreateApi() uintptr {
	bs, _ := syscall.BytePtrFromString(t.logdir)
	api, _, _ := t.h.MustFindProc("tCreateApi").Call(uintptr(unsafe.Pointer(bs)))
	return api
}

func (t *Trade) CreateSpi() uintptr {
	pSpi, _, _ := t.h.MustFindProc("tCreateSpi").Call()
	return pSpi
}

func (t *Trade) GetApiVersion() string {
	ver, _, _ := t.h.MustFindProc("tGetApiVersion").Call()
	p := (*byte)(unsafe.Pointer(ver))
	data := make([]byte, 0)
	for *p != 0 {
		data = append(data, *p)
		ver += unsafe.Sizeof(byte(0))
		p = (*byte)(unsafe.Pointer(ver))
	}

	return string(data)
}

func (t *Trade) GetTradingDay() string {
	ver, _, _ := t.h.MustFindProc("tGetTradingDay").Call(uintptr(t.api))
	p := (*byte)(unsafe.Pointer(ver))
	data := make([]byte, 0)
	for *p != 0 {
		data = append(data, *p)
		ver += unsafe.Sizeof(byte(0))
		p = (*byte)(unsafe.Pointer(ver))
	}

	return string(data)
}

func (t *Trade) CTP_GetSystemInfo(pSystemInfo *TThostFtdcClientSystemInfoType, nLen TThostFtdcSystemInfoLenType) int32 {
	res, _, _ := t.h.MustFindProc("dCTP_GetSystemInfo").Call(uintptr(unsafe.Pointer(pSystemInfo)), uintptr(nLen))
	return int32(res)
}



func (t *Trade) CTP_GetDataCollectApiVersion() string {
	ver, _, _ := t.h.MustFindProc("dCTP_GetDataCollectApiVersion").Call()
	p := (*byte)(unsafe.Pointer(ver))
	data := make([]byte, 0)
	for *p != 0 {
		data = append(data, *p)
		ver += unsafe.Sizeof(byte(0))
		p = (*byte)(unsafe.Pointer(ver))
	}
	return string(data)
}


func (t *Trade) Release() { 
	t.h.MustFindProc("tRelease").Call(uintptr(t.api))
}

func (t *Trade) Init() { 
	t.h.MustFindProc("tInit").Call(uintptr(t.api))
}
func (t *Trade) Join() int32 {
	res, _, _ := t.h.MustFindProc("tJoin").Call(uintptr(t.api))
	return int32(res)
}


func (t *Trade) RegisterFront(pszFrontAddress []byte) { 
	t.h.MustFindProc("tRegisterFront").Call(uintptr(t.api), uintptr(unsafe.Pointer(&pszFrontAddress[0])))
}

func (t *Trade) RegisterNameServer(pszNsAddress []byte) { 
	t.h.MustFindProc("tRegisterNameServer").Call(uintptr(t.api), uintptr(unsafe.Pointer(&pszNsAddress[0])))
}

func (t *Trade) RegisterFensUserInfo( pFensUserInfo *CThostFtdcFensUserInfoField) { 
	t.h.MustFindProc("tRegisterFensUserInfo").Call(uintptr(t.api), uintptr(unsafe.Pointer( pFensUserInfo)))
}

func (t *Trade) RegisterSpi() { 
	t.h.MustFindProc("tRegisterSpi").Call(uintptr(t.api), uintptr(t.pSpi))
}

func (t *Trade) SubscribePrivateTopic(nResumeType THOST_TE_RESUME_TYPE) { 
	t.h.MustFindProc("tSubscribePrivateTopic").Call(uintptr(t.api), uintptr(nResumeType))
}

func (t *Trade) SubscribePublicTopic(nResumeType THOST_TE_RESUME_TYPE) { 
	t.h.MustFindProc("tSubscribePublicTopic").Call(uintptr(t.api), uintptr(nResumeType))
}
func (t *Trade) ReqAuthenticate(pReqAuthenticateField *CThostFtdcReqAuthenticateField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqAuthenticate").Call(uintptr(t.api), uintptr(unsafe.Pointer(pReqAuthenticateField)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) RegisterUserSystemInfo(pUserSystemInfo *CThostFtdcUserSystemInfoField) int32 {
	res, _, _ := t.h.MustFindProc("tRegisterUserSystemInfo").Call(uintptr(t.api), uintptr(unsafe.Pointer(pUserSystemInfo)))
	return int32(res)
}

func (t *Trade) SubmitUserSystemInfo(pUserSystemInfo *CThostFtdcUserSystemInfoField) int32 {
	res, _, _ := t.h.MustFindProc("tSubmitUserSystemInfo").Call(uintptr(t.api), uintptr(unsafe.Pointer(pUserSystemInfo)))
	return int32(res)
}

func (t *Trade) ReqUserLogin(pReqUserLoginField *CThostFtdcReqUserLoginField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqUserLogin").Call(uintptr(t.api), uintptr(unsafe.Pointer(pReqUserLoginField)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqUserLogout(pUserLogout *CThostFtdcUserLogoutField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqUserLogout").Call(uintptr(t.api), uintptr(unsafe.Pointer(pUserLogout)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqUserPasswordUpdate(pUserPasswordUpdate *CThostFtdcUserPasswordUpdateField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqUserPasswordUpdate").Call(uintptr(t.api), uintptr(unsafe.Pointer(pUserPasswordUpdate)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqTradingAccountPasswordUpdate(pTradingAccountPasswordUpdate *CThostFtdcTradingAccountPasswordUpdateField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqTradingAccountPasswordUpdate").Call(uintptr(t.api), uintptr(unsafe.Pointer(pTradingAccountPasswordUpdate)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqUserAuthMethod(pReqUserAuthMethod *CThostFtdcReqUserAuthMethodField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqUserAuthMethod").Call(uintptr(t.api), uintptr(unsafe.Pointer(pReqUserAuthMethod)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqGenUserCaptcha(pReqGenUserCaptcha *CThostFtdcReqGenUserCaptchaField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqGenUserCaptcha").Call(uintptr(t.api), uintptr(unsafe.Pointer(pReqGenUserCaptcha)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqGenUserText(pReqGenUserText *CThostFtdcReqGenUserTextField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqGenUserText").Call(uintptr(t.api), uintptr(unsafe.Pointer(pReqGenUserText)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqUserLoginWithCaptcha(pReqUserLoginWithCaptcha *CThostFtdcReqUserLoginWithCaptchaField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqUserLoginWithCaptcha").Call(uintptr(t.api), uintptr(unsafe.Pointer(pReqUserLoginWithCaptcha)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqUserLoginWithText(pReqUserLoginWithText *CThostFtdcReqUserLoginWithTextField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqUserLoginWithText").Call(uintptr(t.api), uintptr(unsafe.Pointer(pReqUserLoginWithText)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqUserLoginWithOTP(pReqUserLoginWithOTP *CThostFtdcReqUserLoginWithOTPField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqUserLoginWithOTP").Call(uintptr(t.api), uintptr(unsafe.Pointer(pReqUserLoginWithOTP)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqOrderInsert(pInputOrder *CThostFtdcInputOrderField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqOrderInsert").Call(uintptr(t.api), uintptr(unsafe.Pointer(pInputOrder)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqParkedOrderInsert(pParkedOrder *CThostFtdcParkedOrderField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqParkedOrderInsert").Call(uintptr(t.api), uintptr(unsafe.Pointer(pParkedOrder)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqParkedOrderAction(pParkedOrderAction *CThostFtdcParkedOrderActionField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqParkedOrderAction").Call(uintptr(t.api), uintptr(unsafe.Pointer(pParkedOrderAction)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqOrderAction(pInputOrderAction *CThostFtdcInputOrderActionField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqOrderAction").Call(uintptr(t.api), uintptr(unsafe.Pointer(pInputOrderAction)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryMaxOrderVolume(pQryMaxOrderVolume *CThostFtdcQryMaxOrderVolumeField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryMaxOrderVolume").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryMaxOrderVolume)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqSettlementInfoConfirm(pSettlementInfoConfirm *CThostFtdcSettlementInfoConfirmField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqSettlementInfoConfirm").Call(uintptr(t.api), uintptr(unsafe.Pointer(pSettlementInfoConfirm)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqRemoveParkedOrder(pRemoveParkedOrder *CThostFtdcRemoveParkedOrderField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqRemoveParkedOrder").Call(uintptr(t.api), uintptr(unsafe.Pointer(pRemoveParkedOrder)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqRemoveParkedOrderAction(pRemoveParkedOrderAction *CThostFtdcRemoveParkedOrderActionField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqRemoveParkedOrderAction").Call(uintptr(t.api), uintptr(unsafe.Pointer(pRemoveParkedOrderAction)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqExecOrderInsert(pInputExecOrder *CThostFtdcInputExecOrderField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqExecOrderInsert").Call(uintptr(t.api), uintptr(unsafe.Pointer(pInputExecOrder)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqExecOrderAction(pInputExecOrderAction *CThostFtdcInputExecOrderActionField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqExecOrderAction").Call(uintptr(t.api), uintptr(unsafe.Pointer(pInputExecOrderAction)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqForQuoteInsert(pInputForQuote *CThostFtdcInputForQuoteField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqForQuoteInsert").Call(uintptr(t.api), uintptr(unsafe.Pointer(pInputForQuote)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQuoteInsert(pInputQuote *CThostFtdcInputQuoteField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQuoteInsert").Call(uintptr(t.api), uintptr(unsafe.Pointer(pInputQuote)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQuoteAction(pInputQuoteAction *CThostFtdcInputQuoteActionField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQuoteAction").Call(uintptr(t.api), uintptr(unsafe.Pointer(pInputQuoteAction)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqBatchOrderAction(pInputBatchOrderAction *CThostFtdcInputBatchOrderActionField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqBatchOrderAction").Call(uintptr(t.api), uintptr(unsafe.Pointer(pInputBatchOrderAction)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqOptionSelfCloseInsert(pInputOptionSelfClose *CThostFtdcInputOptionSelfCloseField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqOptionSelfCloseInsert").Call(uintptr(t.api), uintptr(unsafe.Pointer(pInputOptionSelfClose)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqOptionSelfCloseAction(pInputOptionSelfCloseAction *CThostFtdcInputOptionSelfCloseActionField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqOptionSelfCloseAction").Call(uintptr(t.api), uintptr(unsafe.Pointer(pInputOptionSelfCloseAction)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqCombActionInsert(pInputCombAction *CThostFtdcInputCombActionField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqCombActionInsert").Call(uintptr(t.api), uintptr(unsafe.Pointer(pInputCombAction)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryOrder(pQryOrder *CThostFtdcQryOrderField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryOrder").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryOrder)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryTrade(pQryTrade *CThostFtdcQryTradeField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryTrade").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryTrade)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryInvestorPosition(pQryInvestorPosition *CThostFtdcQryInvestorPositionField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryInvestorPosition").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryInvestorPosition)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryTradingAccount(pQryTradingAccount *CThostFtdcQryTradingAccountField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryTradingAccount").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryTradingAccount)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryInvestor(pQryInvestor *CThostFtdcQryInvestorField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryInvestor").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryInvestor)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryTradingCode(pQryTradingCode *CThostFtdcQryTradingCodeField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryTradingCode").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryTradingCode)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryInstrumentMarginRate(pQryInstrumentMarginRate *CThostFtdcQryInstrumentMarginRateField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryInstrumentMarginRate").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryInstrumentMarginRate)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryInstrumentCommissionRate(pQryInstrumentCommissionRate *CThostFtdcQryInstrumentCommissionRateField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryInstrumentCommissionRate").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryInstrumentCommissionRate)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryExchange(pQryExchange *CThostFtdcQryExchangeField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryExchange").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryExchange)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryProduct(pQryProduct *CThostFtdcQryProductField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryProduct").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryProduct)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryInstrument(pQryInstrument *CThostFtdcQryInstrumentField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryInstrument").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryInstrument)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryDepthMarketData(pQryDepthMarketData *CThostFtdcQryDepthMarketDataField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryDepthMarketData").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryDepthMarketData)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryTraderOffer(pQryTraderOffer *CThostFtdcQryTraderOfferField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryTraderOffer").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryTraderOffer)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQrySettlementInfo(pQrySettlementInfo *CThostFtdcQrySettlementInfoField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQrySettlementInfo").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQrySettlementInfo)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryTransferBank(pQryTransferBank *CThostFtdcQryTransferBankField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryTransferBank").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryTransferBank)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryInvestorPositionDetail(pQryInvestorPositionDetail *CThostFtdcQryInvestorPositionDetailField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryInvestorPositionDetail").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryInvestorPositionDetail)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryNotice(pQryNotice *CThostFtdcQryNoticeField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryNotice").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryNotice)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQrySettlementInfoConfirm(pQrySettlementInfoConfirm *CThostFtdcQrySettlementInfoConfirmField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQrySettlementInfoConfirm").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQrySettlementInfoConfirm)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryInvestorPositionCombineDetail(pQryInvestorPositionCombineDetail *CThostFtdcQryInvestorPositionCombineDetailField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryInvestorPositionCombineDetail").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryInvestorPositionCombineDetail)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryCFMMCTradingAccountKey(pQryCFMMCTradingAccountKey *CThostFtdcQryCFMMCTradingAccountKeyField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryCFMMCTradingAccountKey").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryCFMMCTradingAccountKey)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryEWarrantOffset(pQryEWarrantOffset *CThostFtdcQryEWarrantOffsetField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryEWarrantOffset").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryEWarrantOffset)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryInvestorProductGroupMargin(pQryInvestorProductGroupMargin *CThostFtdcQryInvestorProductGroupMarginField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryInvestorProductGroupMargin").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryInvestorProductGroupMargin)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryExchangeMarginRate(pQryExchangeMarginRate *CThostFtdcQryExchangeMarginRateField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryExchangeMarginRate").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryExchangeMarginRate)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryExchangeMarginRateAdjust(pQryExchangeMarginRateAdjust *CThostFtdcQryExchangeMarginRateAdjustField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryExchangeMarginRateAdjust").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryExchangeMarginRateAdjust)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryExchangeRate(pQryExchangeRate *CThostFtdcQryExchangeRateField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryExchangeRate").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryExchangeRate)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQrySecAgentACIDMap(pQrySecAgentACIDMap *CThostFtdcQrySecAgentACIDMapField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQrySecAgentACIDMap").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQrySecAgentACIDMap)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryProductExchRate(pQryProductExchRate *CThostFtdcQryProductExchRateField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryProductExchRate").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryProductExchRate)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryProductGroup(pQryProductGroup *CThostFtdcQryProductGroupField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryProductGroup").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryProductGroup)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryMMInstrumentCommissionRate(pQryMMInstrumentCommissionRate *CThostFtdcQryMMInstrumentCommissionRateField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryMMInstrumentCommissionRate").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryMMInstrumentCommissionRate)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryMMOptionInstrCommRate(pQryMMOptionInstrCommRate *CThostFtdcQryMMOptionInstrCommRateField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryMMOptionInstrCommRate").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryMMOptionInstrCommRate)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryInstrumentOrderCommRate(pQryInstrumentOrderCommRate *CThostFtdcQryInstrumentOrderCommRateField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryInstrumentOrderCommRate").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryInstrumentOrderCommRate)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQrySecAgentTradingAccount(pQryTradingAccount *CThostFtdcQryTradingAccountField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQrySecAgentTradingAccount").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryTradingAccount)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQrySecAgentCheckMode(pQrySecAgentCheckMode *CThostFtdcQrySecAgentCheckModeField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQrySecAgentCheckMode").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQrySecAgentCheckMode)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQrySecAgentTradeInfo(pQrySecAgentTradeInfo *CThostFtdcQrySecAgentTradeInfoField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQrySecAgentTradeInfo").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQrySecAgentTradeInfo)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryOptionInstrTradeCost(pQryOptionInstrTradeCost *CThostFtdcQryOptionInstrTradeCostField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryOptionInstrTradeCost").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryOptionInstrTradeCost)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryOptionInstrCommRate(pQryOptionInstrCommRate *CThostFtdcQryOptionInstrCommRateField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryOptionInstrCommRate").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryOptionInstrCommRate)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryExecOrder(pQryExecOrder *CThostFtdcQryExecOrderField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryExecOrder").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryExecOrder)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryForQuote(pQryForQuote *CThostFtdcQryForQuoteField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryForQuote").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryForQuote)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryQuote(pQryQuote *CThostFtdcQryQuoteField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryQuote").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryQuote)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryOptionSelfClose(pQryOptionSelfClose *CThostFtdcQryOptionSelfCloseField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryOptionSelfClose").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryOptionSelfClose)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryInvestUnit(pQryInvestUnit *CThostFtdcQryInvestUnitField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryInvestUnit").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryInvestUnit)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryCombInstrumentGuard(pQryCombInstrumentGuard *CThostFtdcQryCombInstrumentGuardField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryCombInstrumentGuard").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryCombInstrumentGuard)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryCombAction(pQryCombAction *CThostFtdcQryCombActionField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryCombAction").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryCombAction)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryTransferSerial(pQryTransferSerial *CThostFtdcQryTransferSerialField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryTransferSerial").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryTransferSerial)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryAccountregister(pQryAccountregister *CThostFtdcQryAccountregisterField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryAccountregister").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryAccountregister)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryContractBank(pQryContractBank *CThostFtdcQryContractBankField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryContractBank").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryContractBank)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryParkedOrder(pQryParkedOrder *CThostFtdcQryParkedOrderField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryParkedOrder").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryParkedOrder)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryParkedOrderAction(pQryParkedOrderAction *CThostFtdcQryParkedOrderActionField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryParkedOrderAction").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryParkedOrderAction)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryTradingNotice(pQryTradingNotice *CThostFtdcQryTradingNoticeField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryTradingNotice").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryTradingNotice)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryBrokerTradingParams(pQryBrokerTradingParams *CThostFtdcQryBrokerTradingParamsField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryBrokerTradingParams").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryBrokerTradingParams)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryBrokerTradingAlgos(pQryBrokerTradingAlgos *CThostFtdcQryBrokerTradingAlgosField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryBrokerTradingAlgos").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryBrokerTradingAlgos)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQueryCFMMCTradingAccountToken(pQueryCFMMCTradingAccountToken *CThostFtdcQueryCFMMCTradingAccountTokenField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQueryCFMMCTradingAccountToken").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQueryCFMMCTradingAccountToken)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqFromBankToFutureByFuture(pReqTransfer *CThostFtdcReqTransferField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqFromBankToFutureByFuture").Call(uintptr(t.api), uintptr(unsafe.Pointer(pReqTransfer)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqFromFutureToBankByFuture(pReqTransfer *CThostFtdcReqTransferField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqFromFutureToBankByFuture").Call(uintptr(t.api), uintptr(unsafe.Pointer(pReqTransfer)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQueryBankAccountMoneyByFuture(pReqQueryAccount *CThostFtdcReqQueryAccountField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQueryBankAccountMoneyByFuture").Call(uintptr(t.api), uintptr(unsafe.Pointer(pReqQueryAccount)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryClassifiedInstrument(pQryClassifiedInstrument *CThostFtdcQryClassifiedInstrumentField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryClassifiedInstrument").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryClassifiedInstrument)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryCombPromotionParam(pQryCombPromotionParam *CThostFtdcQryCombPromotionParamField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryCombPromotionParam").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryCombPromotionParam)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryRiskSettleInvstPosition(pQryRiskSettleInvstPosition *CThostFtdcQryRiskSettleInvstPositionField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryRiskSettleInvstPosition").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryRiskSettleInvstPosition)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryRiskSettleProductStatus(pQryRiskSettleProductStatus *CThostFtdcQryRiskSettleProductStatusField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryRiskSettleProductStatus").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryRiskSettleProductStatus)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQrySPBMFutureParameter(pQrySPBMFutureParameter *CThostFtdcQrySPBMFutureParameterField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQrySPBMFutureParameter").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQrySPBMFutureParameter)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQrySPBMOptionParameter(pQrySPBMOptionParameter *CThostFtdcQrySPBMOptionParameterField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQrySPBMOptionParameter").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQrySPBMOptionParameter)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQrySPBMIntraParameter(pQrySPBMIntraParameter *CThostFtdcQrySPBMIntraParameterField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQrySPBMIntraParameter").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQrySPBMIntraParameter)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQrySPBMInterParameter(pQrySPBMInterParameter *CThostFtdcQrySPBMInterParameterField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQrySPBMInterParameter").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQrySPBMInterParameter)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQrySPBMPortfDefinition(pQrySPBMPortfDefinition *CThostFtdcQrySPBMPortfDefinitionField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQrySPBMPortfDefinition").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQrySPBMPortfDefinition)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQrySPBMInvestorPortfDef(pQrySPBMInvestorPortfDef *CThostFtdcQrySPBMInvestorPortfDefField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQrySPBMInvestorPortfDef").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQrySPBMInvestorPortfDef)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryInvestorPortfMarginRatio(pQryInvestorPortfMarginRatio *CThostFtdcQryInvestorPortfMarginRatioField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryInvestorPortfMarginRatio").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryInvestorPortfMarginRatio)), uintptr(nRequestID))
	return int32(res)
}

func (t *Trade) ReqQryInvestorProdSPBMDetail(pQryInvestorProdSPBMDetail *CThostFtdcQryInvestorProdSPBMDetailField, nRequestID int) int32 {
	res, _, _ := t.h.MustFindProc("tReqQryInvestorProdSPBMDetail").Call(uintptr(t.api), uintptr(unsafe.Pointer(pQryInvestorProdSPBMDetail)), uintptr(nRequestID))
	return int32(res)
}


// 当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。
func (t *Trade) OnFrontConnected(fn func()) {
    t.OnFrontConnected_ = fn
	t.h.MustFindProc("tOnFrontConnected").Call(t.pSpi, syscall.NewCallback(t.OnFrontConnected__))
}

// 当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。
func (t *Trade) OnFrontDisconnected(fn func(nReason int)) {
    t.OnFrontDisconnected_ = fn
	t.h.MustFindProc("tOnFrontDisconnected").Call(t.pSpi, syscall.NewCallback(t.OnFrontDisconnected__))
}

// 心跳超时警告。当长时间未收到报文时，该方法被调用。
func (t *Trade) OnHeartBeatWarning(fn func(nTimeLapse int)) {
    t.OnHeartBeatWarning_ = fn
	t.h.MustFindProc("tOnHeartBeatWarning").Call(t.pSpi, syscall.NewCallback(t.OnHeartBeatWarning__))
}

// 客户端认证响应
func (t *Trade) OnRspAuthenticate(fn func(pRspAuthenticateField *CThostFtdcRspAuthenticateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspAuthenticate_ = fn
	t.h.MustFindProc("tOnRspAuthenticate").Call(t.pSpi, syscall.NewCallback(t.OnRspAuthenticate__))
}

// 登录请求响应
func (t *Trade) OnRspUserLogin(fn func(pRspUserLogin *CThostFtdcRspUserLoginField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspUserLogin_ = fn
	t.h.MustFindProc("tOnRspUserLogin").Call(t.pSpi, syscall.NewCallback(t.OnRspUserLogin__))
}

// 登出请求响应
func (t *Trade) OnRspUserLogout(fn func(pUserLogout *CThostFtdcUserLogoutField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspUserLogout_ = fn
	t.h.MustFindProc("tOnRspUserLogout").Call(t.pSpi, syscall.NewCallback(t.OnRspUserLogout__))
}

// 用户口令更新请求响应
func (t *Trade) OnRspUserPasswordUpdate(fn func(pUserPasswordUpdate *CThostFtdcUserPasswordUpdateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspUserPasswordUpdate_ = fn
	t.h.MustFindProc("tOnRspUserPasswordUpdate").Call(t.pSpi, syscall.NewCallback(t.OnRspUserPasswordUpdate__))
}

// 资金账户口令更新请求响应
func (t *Trade) OnRspTradingAccountPasswordUpdate(fn func(pTradingAccountPasswordUpdate *CThostFtdcTradingAccountPasswordUpdateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspTradingAccountPasswordUpdate_ = fn
	t.h.MustFindProc("tOnRspTradingAccountPasswordUpdate").Call(t.pSpi, syscall.NewCallback(t.OnRspTradingAccountPasswordUpdate__))
}

// 查询用户当前支持的认证模式的回复
func (t *Trade) OnRspUserAuthMethod(fn func(pRspUserAuthMethod *CThostFtdcRspUserAuthMethodField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspUserAuthMethod_ = fn
	t.h.MustFindProc("tOnRspUserAuthMethod").Call(t.pSpi, syscall.NewCallback(t.OnRspUserAuthMethod__))
}

// 获取图形验证码请求的回复
func (t *Trade) OnRspGenUserCaptcha(fn func(pRspGenUserCaptcha *CThostFtdcRspGenUserCaptchaField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspGenUserCaptcha_ = fn
	t.h.MustFindProc("tOnRspGenUserCaptcha").Call(t.pSpi, syscall.NewCallback(t.OnRspGenUserCaptcha__))
}

// 获取短信验证码请求的回复
func (t *Trade) OnRspGenUserText(fn func(pRspGenUserText *CThostFtdcRspGenUserTextField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspGenUserText_ = fn
	t.h.MustFindProc("tOnRspGenUserText").Call(t.pSpi, syscall.NewCallback(t.OnRspGenUserText__))
}

// 报单录入请求响应
func (t *Trade) OnRspOrderInsert(fn func(pInputOrder *CThostFtdcInputOrderField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspOrderInsert_ = fn
	t.h.MustFindProc("tOnRspOrderInsert").Call(t.pSpi, syscall.NewCallback(t.OnRspOrderInsert__))
}

// 预埋单录入请求响应
func (t *Trade) OnRspParkedOrderInsert(fn func(pParkedOrder *CThostFtdcParkedOrderField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspParkedOrderInsert_ = fn
	t.h.MustFindProc("tOnRspParkedOrderInsert").Call(t.pSpi, syscall.NewCallback(t.OnRspParkedOrderInsert__))
}

// 预埋撤单录入请求响应
func (t *Trade) OnRspParkedOrderAction(fn func(pParkedOrderAction *CThostFtdcParkedOrderActionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspParkedOrderAction_ = fn
	t.h.MustFindProc("tOnRspParkedOrderAction").Call(t.pSpi, syscall.NewCallback(t.OnRspParkedOrderAction__))
}

// 报单操作请求响应
func (t *Trade) OnRspOrderAction(fn func(pInputOrderAction *CThostFtdcInputOrderActionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspOrderAction_ = fn
	t.h.MustFindProc("tOnRspOrderAction").Call(t.pSpi, syscall.NewCallback(t.OnRspOrderAction__))
}

// 查询最大报单数量响应
func (t *Trade) OnRspQryMaxOrderVolume(fn func(pQryMaxOrderVolume *CThostFtdcQryMaxOrderVolumeField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryMaxOrderVolume_ = fn
	t.h.MustFindProc("tOnRspQryMaxOrderVolume").Call(t.pSpi, syscall.NewCallback(t.OnRspQryMaxOrderVolume__))
}

// 投资者结算结果确认响应
func (t *Trade) OnRspSettlementInfoConfirm(fn func(pSettlementInfoConfirm *CThostFtdcSettlementInfoConfirmField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspSettlementInfoConfirm_ = fn
	t.h.MustFindProc("tOnRspSettlementInfoConfirm").Call(t.pSpi, syscall.NewCallback(t.OnRspSettlementInfoConfirm__))
}

// 删除预埋单响应
func (t *Trade) OnRspRemoveParkedOrder(fn func(pRemoveParkedOrder *CThostFtdcRemoveParkedOrderField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspRemoveParkedOrder_ = fn
	t.h.MustFindProc("tOnRspRemoveParkedOrder").Call(t.pSpi, syscall.NewCallback(t.OnRspRemoveParkedOrder__))
}

// 删除预埋撤单响应
func (t *Trade) OnRspRemoveParkedOrderAction(fn func(pRemoveParkedOrderAction *CThostFtdcRemoveParkedOrderActionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspRemoveParkedOrderAction_ = fn
	t.h.MustFindProc("tOnRspRemoveParkedOrderAction").Call(t.pSpi, syscall.NewCallback(t.OnRspRemoveParkedOrderAction__))
}

// 执行宣告录入请求响应
func (t *Trade) OnRspExecOrderInsert(fn func(pInputExecOrder *CThostFtdcInputExecOrderField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspExecOrderInsert_ = fn
	t.h.MustFindProc("tOnRspExecOrderInsert").Call(t.pSpi, syscall.NewCallback(t.OnRspExecOrderInsert__))
}

// 执行宣告操作请求响应
func (t *Trade) OnRspExecOrderAction(fn func(pInputExecOrderAction *CThostFtdcInputExecOrderActionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspExecOrderAction_ = fn
	t.h.MustFindProc("tOnRspExecOrderAction").Call(t.pSpi, syscall.NewCallback(t.OnRspExecOrderAction__))
}

// 询价录入请求响应
func (t *Trade) OnRspForQuoteInsert(fn func(pInputForQuote *CThostFtdcInputForQuoteField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspForQuoteInsert_ = fn
	t.h.MustFindProc("tOnRspForQuoteInsert").Call(t.pSpi, syscall.NewCallback(t.OnRspForQuoteInsert__))
}

// 报价录入请求响应
func (t *Trade) OnRspQuoteInsert(fn func(pInputQuote *CThostFtdcInputQuoteField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQuoteInsert_ = fn
	t.h.MustFindProc("tOnRspQuoteInsert").Call(t.pSpi, syscall.NewCallback(t.OnRspQuoteInsert__))
}

// 报价操作请求响应
func (t *Trade) OnRspQuoteAction(fn func(pInputQuoteAction *CThostFtdcInputQuoteActionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQuoteAction_ = fn
	t.h.MustFindProc("tOnRspQuoteAction").Call(t.pSpi, syscall.NewCallback(t.OnRspQuoteAction__))
}

// 批量报单操作请求响应
func (t *Trade) OnRspBatchOrderAction(fn func(pInputBatchOrderAction *CThostFtdcInputBatchOrderActionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspBatchOrderAction_ = fn
	t.h.MustFindProc("tOnRspBatchOrderAction").Call(t.pSpi, syscall.NewCallback(t.OnRspBatchOrderAction__))
}

// 期权自对冲录入请求响应
func (t *Trade) OnRspOptionSelfCloseInsert(fn func(pInputOptionSelfClose *CThostFtdcInputOptionSelfCloseField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspOptionSelfCloseInsert_ = fn
	t.h.MustFindProc("tOnRspOptionSelfCloseInsert").Call(t.pSpi, syscall.NewCallback(t.OnRspOptionSelfCloseInsert__))
}

// 期权自对冲操作请求响应
func (t *Trade) OnRspOptionSelfCloseAction(fn func(pInputOptionSelfCloseAction *CThostFtdcInputOptionSelfCloseActionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspOptionSelfCloseAction_ = fn
	t.h.MustFindProc("tOnRspOptionSelfCloseAction").Call(t.pSpi, syscall.NewCallback(t.OnRspOptionSelfCloseAction__))
}

// 申请组合录入请求响应
func (t *Trade) OnRspCombActionInsert(fn func(pInputCombAction *CThostFtdcInputCombActionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspCombActionInsert_ = fn
	t.h.MustFindProc("tOnRspCombActionInsert").Call(t.pSpi, syscall.NewCallback(t.OnRspCombActionInsert__))
}

// 请求查询报单响应
func (t *Trade) OnRspQryOrder(fn func(pOrder *CThostFtdcOrderField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryOrder_ = fn
	t.h.MustFindProc("tOnRspQryOrder").Call(t.pSpi, syscall.NewCallback(t.OnRspQryOrder__))
}

// 请求查询成交响应
func (t *Trade) OnRspQryTrade(fn func(pTrade *CThostFtdcTradeField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryTrade_ = fn
	t.h.MustFindProc("tOnRspQryTrade").Call(t.pSpi, syscall.NewCallback(t.OnRspQryTrade__))
}

// 请求查询投资者持仓响应
func (t *Trade) OnRspQryInvestorPosition(fn func(pInvestorPosition *CThostFtdcInvestorPositionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryInvestorPosition_ = fn
	t.h.MustFindProc("tOnRspQryInvestorPosition").Call(t.pSpi, syscall.NewCallback(t.OnRspQryInvestorPosition__))
}

// 请求查询资金账户响应
func (t *Trade) OnRspQryTradingAccount(fn func(pTradingAccount *CThostFtdcTradingAccountField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryTradingAccount_ = fn
	t.h.MustFindProc("tOnRspQryTradingAccount").Call(t.pSpi, syscall.NewCallback(t.OnRspQryTradingAccount__))
}

// 请求查询投资者响应
func (t *Trade) OnRspQryInvestor(fn func(pInvestor *CThostFtdcInvestorField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryInvestor_ = fn
	t.h.MustFindProc("tOnRspQryInvestor").Call(t.pSpi, syscall.NewCallback(t.OnRspQryInvestor__))
}

// 请求查询交易编码响应
func (t *Trade) OnRspQryTradingCode(fn func(pTradingCode *CThostFtdcTradingCodeField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryTradingCode_ = fn
	t.h.MustFindProc("tOnRspQryTradingCode").Call(t.pSpi, syscall.NewCallback(t.OnRspQryTradingCode__))
}

// 请求查询合约保证金率响应
func (t *Trade) OnRspQryInstrumentMarginRate(fn func(pInstrumentMarginRate *CThostFtdcInstrumentMarginRateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryInstrumentMarginRate_ = fn
	t.h.MustFindProc("tOnRspQryInstrumentMarginRate").Call(t.pSpi, syscall.NewCallback(t.OnRspQryInstrumentMarginRate__))
}

// 请求查询合约手续费率响应
func (t *Trade) OnRspQryInstrumentCommissionRate(fn func(pInstrumentCommissionRate *CThostFtdcInstrumentCommissionRateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryInstrumentCommissionRate_ = fn
	t.h.MustFindProc("tOnRspQryInstrumentCommissionRate").Call(t.pSpi, syscall.NewCallback(t.OnRspQryInstrumentCommissionRate__))
}

// 请求查询交易所响应
func (t *Trade) OnRspQryExchange(fn func(pExchange *CThostFtdcExchangeField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryExchange_ = fn
	t.h.MustFindProc("tOnRspQryExchange").Call(t.pSpi, syscall.NewCallback(t.OnRspQryExchange__))
}

// 请求查询产品响应
func (t *Trade) OnRspQryProduct(fn func(pProduct *CThostFtdcProductField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryProduct_ = fn
	t.h.MustFindProc("tOnRspQryProduct").Call(t.pSpi, syscall.NewCallback(t.OnRspQryProduct__))
}

// 请求查询合约响应
func (t *Trade) OnRspQryInstrument(fn func(pInstrument *CThostFtdcInstrumentField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryInstrument_ = fn
	t.h.MustFindProc("tOnRspQryInstrument").Call(t.pSpi, syscall.NewCallback(t.OnRspQryInstrument__))
}

// 请求查询行情响应
func (t *Trade) OnRspQryDepthMarketData(fn func(pDepthMarketData *CThostFtdcDepthMarketDataField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryDepthMarketData_ = fn
	t.h.MustFindProc("tOnRspQryDepthMarketData").Call(t.pSpi, syscall.NewCallback(t.OnRspQryDepthMarketData__))
}

// 请求查询交易员报盘机响应
func (t *Trade) OnRspQryTraderOffer(fn func(pTraderOffer *CThostFtdcTraderOfferField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryTraderOffer_ = fn
	t.h.MustFindProc("tOnRspQryTraderOffer").Call(t.pSpi, syscall.NewCallback(t.OnRspQryTraderOffer__))
}

// 请求查询投资者结算结果响应
func (t *Trade) OnRspQrySettlementInfo(fn func(pSettlementInfo *CThostFtdcSettlementInfoField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQrySettlementInfo_ = fn
	t.h.MustFindProc("tOnRspQrySettlementInfo").Call(t.pSpi, syscall.NewCallback(t.OnRspQrySettlementInfo__))
}

// 请求查询转帐银行响应
func (t *Trade) OnRspQryTransferBank(fn func(pTransferBank *CThostFtdcTransferBankField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryTransferBank_ = fn
	t.h.MustFindProc("tOnRspQryTransferBank").Call(t.pSpi, syscall.NewCallback(t.OnRspQryTransferBank__))
}

// 请求查询投资者持仓明细响应
func (t *Trade) OnRspQryInvestorPositionDetail(fn func(pInvestorPositionDetail *CThostFtdcInvestorPositionDetailField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryInvestorPositionDetail_ = fn
	t.h.MustFindProc("tOnRspQryInvestorPositionDetail").Call(t.pSpi, syscall.NewCallback(t.OnRspQryInvestorPositionDetail__))
}

// 请求查询客户通知响应
func (t *Trade) OnRspQryNotice(fn func(pNotice *CThostFtdcNoticeField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryNotice_ = fn
	t.h.MustFindProc("tOnRspQryNotice").Call(t.pSpi, syscall.NewCallback(t.OnRspQryNotice__))
}

// 请求查询结算信息确认响应
func (t *Trade) OnRspQrySettlementInfoConfirm(fn func(pSettlementInfoConfirm *CThostFtdcSettlementInfoConfirmField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQrySettlementInfoConfirm_ = fn
	t.h.MustFindProc("tOnRspQrySettlementInfoConfirm").Call(t.pSpi, syscall.NewCallback(t.OnRspQrySettlementInfoConfirm__))
}

// 请求查询投资者持仓明细响应
func (t *Trade) OnRspQryInvestorPositionCombineDetail(fn func(pInvestorPositionCombineDetail *CThostFtdcInvestorPositionCombineDetailField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryInvestorPositionCombineDetail_ = fn
	t.h.MustFindProc("tOnRspQryInvestorPositionCombineDetail").Call(t.pSpi, syscall.NewCallback(t.OnRspQryInvestorPositionCombineDetail__))
}

// 查询保证金监管系统经纪公司资金账户密钥响应
func (t *Trade) OnRspQryCFMMCTradingAccountKey(fn func(pCFMMCTradingAccountKey *CThostFtdcCFMMCTradingAccountKeyField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryCFMMCTradingAccountKey_ = fn
	t.h.MustFindProc("tOnRspQryCFMMCTradingAccountKey").Call(t.pSpi, syscall.NewCallback(t.OnRspQryCFMMCTradingAccountKey__))
}

// 请求查询仓单折抵信息响应
func (t *Trade) OnRspQryEWarrantOffset(fn func(pEWarrantOffset *CThostFtdcEWarrantOffsetField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryEWarrantOffset_ = fn
	t.h.MustFindProc("tOnRspQryEWarrantOffset").Call(t.pSpi, syscall.NewCallback(t.OnRspQryEWarrantOffset__))
}

// 请求查询投资者品种/跨品种保证金响应
func (t *Trade) OnRspQryInvestorProductGroupMargin(fn func(pInvestorProductGroupMargin *CThostFtdcInvestorProductGroupMarginField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryInvestorProductGroupMargin_ = fn
	t.h.MustFindProc("tOnRspQryInvestorProductGroupMargin").Call(t.pSpi, syscall.NewCallback(t.OnRspQryInvestorProductGroupMargin__))
}

// 请求查询交易所保证金率响应
func (t *Trade) OnRspQryExchangeMarginRate(fn func(pExchangeMarginRate *CThostFtdcExchangeMarginRateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryExchangeMarginRate_ = fn
	t.h.MustFindProc("tOnRspQryExchangeMarginRate").Call(t.pSpi, syscall.NewCallback(t.OnRspQryExchangeMarginRate__))
}

// 请求查询交易所调整保证金率响应
func (t *Trade) OnRspQryExchangeMarginRateAdjust(fn func(pExchangeMarginRateAdjust *CThostFtdcExchangeMarginRateAdjustField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryExchangeMarginRateAdjust_ = fn
	t.h.MustFindProc("tOnRspQryExchangeMarginRateAdjust").Call(t.pSpi, syscall.NewCallback(t.OnRspQryExchangeMarginRateAdjust__))
}

// 请求查询汇率响应
func (t *Trade) OnRspQryExchangeRate(fn func(pExchangeRate *CThostFtdcExchangeRateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryExchangeRate_ = fn
	t.h.MustFindProc("tOnRspQryExchangeRate").Call(t.pSpi, syscall.NewCallback(t.OnRspQryExchangeRate__))
}

// 请求查询二级代理操作员银期权限响应
func (t *Trade) OnRspQrySecAgentACIDMap(fn func(pSecAgentACIDMap *CThostFtdcSecAgentACIDMapField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQrySecAgentACIDMap_ = fn
	t.h.MustFindProc("tOnRspQrySecAgentACIDMap").Call(t.pSpi, syscall.NewCallback(t.OnRspQrySecAgentACIDMap__))
}

// 请求查询产品报价汇率
func (t *Trade) OnRspQryProductExchRate(fn func(pProductExchRate *CThostFtdcProductExchRateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryProductExchRate_ = fn
	t.h.MustFindProc("tOnRspQryProductExchRate").Call(t.pSpi, syscall.NewCallback(t.OnRspQryProductExchRate__))
}

// 请求查询产品组
func (t *Trade) OnRspQryProductGroup(fn func(pProductGroup *CThostFtdcProductGroupField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryProductGroup_ = fn
	t.h.MustFindProc("tOnRspQryProductGroup").Call(t.pSpi, syscall.NewCallback(t.OnRspQryProductGroup__))
}

// 请求查询做市商合约手续费率响应
func (t *Trade) OnRspQryMMInstrumentCommissionRate(fn func(pMMInstrumentCommissionRate *CThostFtdcMMInstrumentCommissionRateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryMMInstrumentCommissionRate_ = fn
	t.h.MustFindProc("tOnRspQryMMInstrumentCommissionRate").Call(t.pSpi, syscall.NewCallback(t.OnRspQryMMInstrumentCommissionRate__))
}

// 请求查询做市商期权合约手续费响应
func (t *Trade) OnRspQryMMOptionInstrCommRate(fn func(pMMOptionInstrCommRate *CThostFtdcMMOptionInstrCommRateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryMMOptionInstrCommRate_ = fn
	t.h.MustFindProc("tOnRspQryMMOptionInstrCommRate").Call(t.pSpi, syscall.NewCallback(t.OnRspQryMMOptionInstrCommRate__))
}

// 请求查询报单手续费响应
func (t *Trade) OnRspQryInstrumentOrderCommRate(fn func(pInstrumentOrderCommRate *CThostFtdcInstrumentOrderCommRateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryInstrumentOrderCommRate_ = fn
	t.h.MustFindProc("tOnRspQryInstrumentOrderCommRate").Call(t.pSpi, syscall.NewCallback(t.OnRspQryInstrumentOrderCommRate__))
}

// 请求查询资金账户响应
func (t *Trade) OnRspQrySecAgentTradingAccount(fn func(pTradingAccount *CThostFtdcTradingAccountField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQrySecAgentTradingAccount_ = fn
	t.h.MustFindProc("tOnRspQrySecAgentTradingAccount").Call(t.pSpi, syscall.NewCallback(t.OnRspQrySecAgentTradingAccount__))
}

// 请求查询二级代理商资金校验模式响应
func (t *Trade) OnRspQrySecAgentCheckMode(fn func(pSecAgentCheckMode *CThostFtdcSecAgentCheckModeField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQrySecAgentCheckMode_ = fn
	t.h.MustFindProc("tOnRspQrySecAgentCheckMode").Call(t.pSpi, syscall.NewCallback(t.OnRspQrySecAgentCheckMode__))
}

// 请求查询二级代理商信息响应
func (t *Trade) OnRspQrySecAgentTradeInfo(fn func(pSecAgentTradeInfo *CThostFtdcSecAgentTradeInfoField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQrySecAgentTradeInfo_ = fn
	t.h.MustFindProc("tOnRspQrySecAgentTradeInfo").Call(t.pSpi, syscall.NewCallback(t.OnRspQrySecAgentTradeInfo__))
}

// 请求查询期权交易成本响应
func (t *Trade) OnRspQryOptionInstrTradeCost(fn func(pOptionInstrTradeCost *CThostFtdcOptionInstrTradeCostField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryOptionInstrTradeCost_ = fn
	t.h.MustFindProc("tOnRspQryOptionInstrTradeCost").Call(t.pSpi, syscall.NewCallback(t.OnRspQryOptionInstrTradeCost__))
}

// 请求查询期权合约手续费响应
func (t *Trade) OnRspQryOptionInstrCommRate(fn func(pOptionInstrCommRate *CThostFtdcOptionInstrCommRateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryOptionInstrCommRate_ = fn
	t.h.MustFindProc("tOnRspQryOptionInstrCommRate").Call(t.pSpi, syscall.NewCallback(t.OnRspQryOptionInstrCommRate__))
}

// 请求查询执行宣告响应
func (t *Trade) OnRspQryExecOrder(fn func(pExecOrder *CThostFtdcExecOrderField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryExecOrder_ = fn
	t.h.MustFindProc("tOnRspQryExecOrder").Call(t.pSpi, syscall.NewCallback(t.OnRspQryExecOrder__))
}

// 请求查询询价响应
func (t *Trade) OnRspQryForQuote(fn func(pForQuote *CThostFtdcForQuoteField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryForQuote_ = fn
	t.h.MustFindProc("tOnRspQryForQuote").Call(t.pSpi, syscall.NewCallback(t.OnRspQryForQuote__))
}

// 请求查询报价响应
func (t *Trade) OnRspQryQuote(fn func(pQuote *CThostFtdcQuoteField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryQuote_ = fn
	t.h.MustFindProc("tOnRspQryQuote").Call(t.pSpi, syscall.NewCallback(t.OnRspQryQuote__))
}

// 请求查询期权自对冲响应
func (t *Trade) OnRspQryOptionSelfClose(fn func(pOptionSelfClose *CThostFtdcOptionSelfCloseField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryOptionSelfClose_ = fn
	t.h.MustFindProc("tOnRspQryOptionSelfClose").Call(t.pSpi, syscall.NewCallback(t.OnRspQryOptionSelfClose__))
}

// 请求查询投资单元响应
func (t *Trade) OnRspQryInvestUnit(fn func(pInvestUnit *CThostFtdcInvestUnitField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryInvestUnit_ = fn
	t.h.MustFindProc("tOnRspQryInvestUnit").Call(t.pSpi, syscall.NewCallback(t.OnRspQryInvestUnit__))
}

// 请求查询组合合约安全系数响应
func (t *Trade) OnRspQryCombInstrumentGuard(fn func(pCombInstrumentGuard *CThostFtdcCombInstrumentGuardField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryCombInstrumentGuard_ = fn
	t.h.MustFindProc("tOnRspQryCombInstrumentGuard").Call(t.pSpi, syscall.NewCallback(t.OnRspQryCombInstrumentGuard__))
}

// 请求查询申请组合响应
func (t *Trade) OnRspQryCombAction(fn func(pCombAction *CThostFtdcCombActionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryCombAction_ = fn
	t.h.MustFindProc("tOnRspQryCombAction").Call(t.pSpi, syscall.NewCallback(t.OnRspQryCombAction__))
}

// 请求查询转帐流水响应
func (t *Trade) OnRspQryTransferSerial(fn func(pTransferSerial *CThostFtdcTransferSerialField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryTransferSerial_ = fn
	t.h.MustFindProc("tOnRspQryTransferSerial").Call(t.pSpi, syscall.NewCallback(t.OnRspQryTransferSerial__))
}

// 请求查询银期签约关系响应
func (t *Trade) OnRspQryAccountregister(fn func(pAccountregister *CThostFtdcAccountregisterField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryAccountregister_ = fn
	t.h.MustFindProc("tOnRspQryAccountregister").Call(t.pSpi, syscall.NewCallback(t.OnRspQryAccountregister__))
}

// 错误应答
func (t *Trade) OnRspError(fn func(pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspError_ = fn
	t.h.MustFindProc("tOnRspError").Call(t.pSpi, syscall.NewCallback(t.OnRspError__))
}

// 报单通知
func (t *Trade) OnRtnOrder(fn func(pOrder *CThostFtdcOrderField)) {
    t.OnRtnOrder_ = fn
	t.h.MustFindProc("tOnRtnOrder").Call(t.pSpi, syscall.NewCallback(t.OnRtnOrder__))
}

// 成交通知
func (t *Trade) OnRtnTrade(fn func(pTrade *CThostFtdcTradeField)) {
    t.OnRtnTrade_ = fn
	t.h.MustFindProc("tOnRtnTrade").Call(t.pSpi, syscall.NewCallback(t.OnRtnTrade__))
}

// 报单录入错误回报
func (t *Trade) OnErrRtnOrderInsert(fn func(pInputOrder *CThostFtdcInputOrderField, pRspInfo *CThostFtdcRspInfoField)) {
    t.OnErrRtnOrderInsert_ = fn
	t.h.MustFindProc("tOnErrRtnOrderInsert").Call(t.pSpi, syscall.NewCallback(t.OnErrRtnOrderInsert__))
}

// 报单操作错误回报
func (t *Trade) OnErrRtnOrderAction(fn func(pOrderAction *CThostFtdcOrderActionField, pRspInfo *CThostFtdcRspInfoField)) {
    t.OnErrRtnOrderAction_ = fn
	t.h.MustFindProc("tOnErrRtnOrderAction").Call(t.pSpi, syscall.NewCallback(t.OnErrRtnOrderAction__))
}

// 合约交易状态通知
func (t *Trade) OnRtnInstrumentStatus(fn func(pInstrumentStatus *CThostFtdcInstrumentStatusField)) {
    t.OnRtnInstrumentStatus_ = fn
	t.h.MustFindProc("tOnRtnInstrumentStatus").Call(t.pSpi, syscall.NewCallback(t.OnRtnInstrumentStatus__))
}

// 交易所公告通知
func (t *Trade) OnRtnBulletin(fn func(pBulletin *CThostFtdcBulletinField)) {
    t.OnRtnBulletin_ = fn
	t.h.MustFindProc("tOnRtnBulletin").Call(t.pSpi, syscall.NewCallback(t.OnRtnBulletin__))
}

// 交易通知
func (t *Trade) OnRtnTradingNotice(fn func(pTradingNoticeInfo *CThostFtdcTradingNoticeInfoField)) {
    t.OnRtnTradingNotice_ = fn
	t.h.MustFindProc("tOnRtnTradingNotice").Call(t.pSpi, syscall.NewCallback(t.OnRtnTradingNotice__))
}

// 提示条件单校验错误
func (t *Trade) OnRtnErrorConditionalOrder(fn func(pErrorConditionalOrder *CThostFtdcErrorConditionalOrderField)) {
    t.OnRtnErrorConditionalOrder_ = fn
	t.h.MustFindProc("tOnRtnErrorConditionalOrder").Call(t.pSpi, syscall.NewCallback(t.OnRtnErrorConditionalOrder__))
}

// 执行宣告通知
func (t *Trade) OnRtnExecOrder(fn func(pExecOrder *CThostFtdcExecOrderField)) {
    t.OnRtnExecOrder_ = fn
	t.h.MustFindProc("tOnRtnExecOrder").Call(t.pSpi, syscall.NewCallback(t.OnRtnExecOrder__))
}

// 执行宣告录入错误回报
func (t *Trade) OnErrRtnExecOrderInsert(fn func(pInputExecOrder *CThostFtdcInputExecOrderField, pRspInfo *CThostFtdcRspInfoField)) {
    t.OnErrRtnExecOrderInsert_ = fn
	t.h.MustFindProc("tOnErrRtnExecOrderInsert").Call(t.pSpi, syscall.NewCallback(t.OnErrRtnExecOrderInsert__))
}

// 执行宣告操作错误回报
func (t *Trade) OnErrRtnExecOrderAction(fn func(pExecOrderAction *CThostFtdcExecOrderActionField, pRspInfo *CThostFtdcRspInfoField)) {
    t.OnErrRtnExecOrderAction_ = fn
	t.h.MustFindProc("tOnErrRtnExecOrderAction").Call(t.pSpi, syscall.NewCallback(t.OnErrRtnExecOrderAction__))
}

// 询价录入错误回报
func (t *Trade) OnErrRtnForQuoteInsert(fn func(pInputForQuote *CThostFtdcInputForQuoteField, pRspInfo *CThostFtdcRspInfoField)) {
    t.OnErrRtnForQuoteInsert_ = fn
	t.h.MustFindProc("tOnErrRtnForQuoteInsert").Call(t.pSpi, syscall.NewCallback(t.OnErrRtnForQuoteInsert__))
}

// 报价通知
func (t *Trade) OnRtnQuote(fn func(pQuote *CThostFtdcQuoteField)) {
    t.OnRtnQuote_ = fn
	t.h.MustFindProc("tOnRtnQuote").Call(t.pSpi, syscall.NewCallback(t.OnRtnQuote__))
}

// 报价录入错误回报
func (t *Trade) OnErrRtnQuoteInsert(fn func(pInputQuote *CThostFtdcInputQuoteField, pRspInfo *CThostFtdcRspInfoField)) {
    t.OnErrRtnQuoteInsert_ = fn
	t.h.MustFindProc("tOnErrRtnQuoteInsert").Call(t.pSpi, syscall.NewCallback(t.OnErrRtnQuoteInsert__))
}

// 报价操作错误回报
func (t *Trade) OnErrRtnQuoteAction(fn func(pQuoteAction *CThostFtdcQuoteActionField, pRspInfo *CThostFtdcRspInfoField)) {
    t.OnErrRtnQuoteAction_ = fn
	t.h.MustFindProc("tOnErrRtnQuoteAction").Call(t.pSpi, syscall.NewCallback(t.OnErrRtnQuoteAction__))
}

// 询价通知
func (t *Trade) OnRtnForQuoteRsp(fn func(pForQuoteRsp *CThostFtdcForQuoteRspField)) {
    t.OnRtnForQuoteRsp_ = fn
	t.h.MustFindProc("tOnRtnForQuoteRsp").Call(t.pSpi, syscall.NewCallback(t.OnRtnForQuoteRsp__))
}

// 保证金监控中心用户令牌
func (t *Trade) OnRtnCFMMCTradingAccountToken(fn func(pCFMMCTradingAccountToken *CThostFtdcCFMMCTradingAccountTokenField)) {
    t.OnRtnCFMMCTradingAccountToken_ = fn
	t.h.MustFindProc("tOnRtnCFMMCTradingAccountToken").Call(t.pSpi, syscall.NewCallback(t.OnRtnCFMMCTradingAccountToken__))
}

// 批量报单操作错误回报
func (t *Trade) OnErrRtnBatchOrderAction(fn func(pBatchOrderAction *CThostFtdcBatchOrderActionField, pRspInfo *CThostFtdcRspInfoField)) {
    t.OnErrRtnBatchOrderAction_ = fn
	t.h.MustFindProc("tOnErrRtnBatchOrderAction").Call(t.pSpi, syscall.NewCallback(t.OnErrRtnBatchOrderAction__))
}

// 期权自对冲通知
func (t *Trade) OnRtnOptionSelfClose(fn func(pOptionSelfClose *CThostFtdcOptionSelfCloseField)) {
    t.OnRtnOptionSelfClose_ = fn
	t.h.MustFindProc("tOnRtnOptionSelfClose").Call(t.pSpi, syscall.NewCallback(t.OnRtnOptionSelfClose__))
}

// 期权自对冲录入错误回报
func (t *Trade) OnErrRtnOptionSelfCloseInsert(fn func(pInputOptionSelfClose *CThostFtdcInputOptionSelfCloseField, pRspInfo *CThostFtdcRspInfoField)) {
    t.OnErrRtnOptionSelfCloseInsert_ = fn
	t.h.MustFindProc("tOnErrRtnOptionSelfCloseInsert").Call(t.pSpi, syscall.NewCallback(t.OnErrRtnOptionSelfCloseInsert__))
}

// 期权自对冲操作错误回报
func (t *Trade) OnErrRtnOptionSelfCloseAction(fn func(pOptionSelfCloseAction *CThostFtdcOptionSelfCloseActionField, pRspInfo *CThostFtdcRspInfoField)) {
    t.OnErrRtnOptionSelfCloseAction_ = fn
	t.h.MustFindProc("tOnErrRtnOptionSelfCloseAction").Call(t.pSpi, syscall.NewCallback(t.OnErrRtnOptionSelfCloseAction__))
}

// 申请组合通知
func (t *Trade) OnRtnCombAction(fn func(pCombAction *CThostFtdcCombActionField)) {
    t.OnRtnCombAction_ = fn
	t.h.MustFindProc("tOnRtnCombAction").Call(t.pSpi, syscall.NewCallback(t.OnRtnCombAction__))
}

// 申请组合录入错误回报
func (t *Trade) OnErrRtnCombActionInsert(fn func(pInputCombAction *CThostFtdcInputCombActionField, pRspInfo *CThostFtdcRspInfoField)) {
    t.OnErrRtnCombActionInsert_ = fn
	t.h.MustFindProc("tOnErrRtnCombActionInsert").Call(t.pSpi, syscall.NewCallback(t.OnErrRtnCombActionInsert__))
}

// 请求查询签约银行响应
func (t *Trade) OnRspQryContractBank(fn func(pContractBank *CThostFtdcContractBankField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryContractBank_ = fn
	t.h.MustFindProc("tOnRspQryContractBank").Call(t.pSpi, syscall.NewCallback(t.OnRspQryContractBank__))
}

// 请求查询预埋单响应
func (t *Trade) OnRspQryParkedOrder(fn func(pParkedOrder *CThostFtdcParkedOrderField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryParkedOrder_ = fn
	t.h.MustFindProc("tOnRspQryParkedOrder").Call(t.pSpi, syscall.NewCallback(t.OnRspQryParkedOrder__))
}

// 请求查询预埋撤单响应
func (t *Trade) OnRspQryParkedOrderAction(fn func(pParkedOrderAction *CThostFtdcParkedOrderActionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryParkedOrderAction_ = fn
	t.h.MustFindProc("tOnRspQryParkedOrderAction").Call(t.pSpi, syscall.NewCallback(t.OnRspQryParkedOrderAction__))
}

// 请求查询交易通知响应
func (t *Trade) OnRspQryTradingNotice(fn func(pTradingNotice *CThostFtdcTradingNoticeField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryTradingNotice_ = fn
	t.h.MustFindProc("tOnRspQryTradingNotice").Call(t.pSpi, syscall.NewCallback(t.OnRspQryTradingNotice__))
}

// 请求查询经纪公司交易参数响应
func (t *Trade) OnRspQryBrokerTradingParams(fn func(pBrokerTradingParams *CThostFtdcBrokerTradingParamsField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryBrokerTradingParams_ = fn
	t.h.MustFindProc("tOnRspQryBrokerTradingParams").Call(t.pSpi, syscall.NewCallback(t.OnRspQryBrokerTradingParams__))
}

// 请求查询经纪公司交易算法响应
func (t *Trade) OnRspQryBrokerTradingAlgos(fn func(pBrokerTradingAlgos *CThostFtdcBrokerTradingAlgosField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryBrokerTradingAlgos_ = fn
	t.h.MustFindProc("tOnRspQryBrokerTradingAlgos").Call(t.pSpi, syscall.NewCallback(t.OnRspQryBrokerTradingAlgos__))
}

// 请求查询监控中心用户令牌
func (t *Trade) OnRspQueryCFMMCTradingAccountToken(fn func(pQueryCFMMCTradingAccountToken *CThostFtdcQueryCFMMCTradingAccountTokenField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQueryCFMMCTradingAccountToken_ = fn
	t.h.MustFindProc("tOnRspQueryCFMMCTradingAccountToken").Call(t.pSpi, syscall.NewCallback(t.OnRspQueryCFMMCTradingAccountToken__))
}

// 银行发起银行资金转期货通知
func (t *Trade) OnRtnFromBankToFutureByBank(fn func(pRspTransfer *CThostFtdcRspTransferField)) {
    t.OnRtnFromBankToFutureByBank_ = fn
	t.h.MustFindProc("tOnRtnFromBankToFutureByBank").Call(t.pSpi, syscall.NewCallback(t.OnRtnFromBankToFutureByBank__))
}

// 银行发起期货资金转银行通知
func (t *Trade) OnRtnFromFutureToBankByBank(fn func(pRspTransfer *CThostFtdcRspTransferField)) {
    t.OnRtnFromFutureToBankByBank_ = fn
	t.h.MustFindProc("tOnRtnFromFutureToBankByBank").Call(t.pSpi, syscall.NewCallback(t.OnRtnFromFutureToBankByBank__))
}

// 银行发起冲正银行转期货通知
func (t *Trade) OnRtnRepealFromBankToFutureByBank(fn func(pRspRepeal *CThostFtdcRspRepealField)) {
    t.OnRtnRepealFromBankToFutureByBank_ = fn
	t.h.MustFindProc("tOnRtnRepealFromBankToFutureByBank").Call(t.pSpi, syscall.NewCallback(t.OnRtnRepealFromBankToFutureByBank__))
}

// 银行发起冲正期货转银行通知
func (t *Trade) OnRtnRepealFromFutureToBankByBank(fn func(pRspRepeal *CThostFtdcRspRepealField)) {
    t.OnRtnRepealFromFutureToBankByBank_ = fn
	t.h.MustFindProc("tOnRtnRepealFromFutureToBankByBank").Call(t.pSpi, syscall.NewCallback(t.OnRtnRepealFromFutureToBankByBank__))
}

// 期货发起银行资金转期货通知
func (t *Trade) OnRtnFromBankToFutureByFuture(fn func(pRspTransfer *CThostFtdcRspTransferField)) {
    t.OnRtnFromBankToFutureByFuture_ = fn
	t.h.MustFindProc("tOnRtnFromBankToFutureByFuture").Call(t.pSpi, syscall.NewCallback(t.OnRtnFromBankToFutureByFuture__))
}

// 期货发起期货资金转银行通知
func (t *Trade) OnRtnFromFutureToBankByFuture(fn func(pRspTransfer *CThostFtdcRspTransferField)) {
    t.OnRtnFromFutureToBankByFuture_ = fn
	t.h.MustFindProc("tOnRtnFromFutureToBankByFuture").Call(t.pSpi, syscall.NewCallback(t.OnRtnFromFutureToBankByFuture__))
}

// 系统运行时期货端手工发起冲正银行转期货请求，银行处理完毕后报盘发回的通知
func (t *Trade) OnRtnRepealFromBankToFutureByFutureManual(fn func(pRspRepeal *CThostFtdcRspRepealField)) {
    t.OnRtnRepealFromBankToFutureByFutureManual_ = fn
	t.h.MustFindProc("tOnRtnRepealFromBankToFutureByFutureManual").Call(t.pSpi, syscall.NewCallback(t.OnRtnRepealFromBankToFutureByFutureManual__))
}

// 系统运行时期货端手工发起冲正期货转银行请求，银行处理完毕后报盘发回的通知
func (t *Trade) OnRtnRepealFromFutureToBankByFutureManual(fn func(pRspRepeal *CThostFtdcRspRepealField)) {
    t.OnRtnRepealFromFutureToBankByFutureManual_ = fn
	t.h.MustFindProc("tOnRtnRepealFromFutureToBankByFutureManual").Call(t.pSpi, syscall.NewCallback(t.OnRtnRepealFromFutureToBankByFutureManual__))
}

// 期货发起查询银行余额通知
func (t *Trade) OnRtnQueryBankBalanceByFuture(fn func(pNotifyQueryAccount *CThostFtdcNotifyQueryAccountField)) {
    t.OnRtnQueryBankBalanceByFuture_ = fn
	t.h.MustFindProc("tOnRtnQueryBankBalanceByFuture").Call(t.pSpi, syscall.NewCallback(t.OnRtnQueryBankBalanceByFuture__))
}

// 期货发起银行资金转期货错误回报
func (t *Trade) OnErrRtnBankToFutureByFuture(fn func(pReqTransfer *CThostFtdcReqTransferField, pRspInfo *CThostFtdcRspInfoField)) {
    t.OnErrRtnBankToFutureByFuture_ = fn
	t.h.MustFindProc("tOnErrRtnBankToFutureByFuture").Call(t.pSpi, syscall.NewCallback(t.OnErrRtnBankToFutureByFuture__))
}

// 期货发起期货资金转银行错误回报
func (t *Trade) OnErrRtnFutureToBankByFuture(fn func(pReqTransfer *CThostFtdcReqTransferField, pRspInfo *CThostFtdcRspInfoField)) {
    t.OnErrRtnFutureToBankByFuture_ = fn
	t.h.MustFindProc("tOnErrRtnFutureToBankByFuture").Call(t.pSpi, syscall.NewCallback(t.OnErrRtnFutureToBankByFuture__))
}

// 系统运行时期货端手工发起冲正银行转期货错误回报
func (t *Trade) OnErrRtnRepealBankToFutureByFutureManual(fn func(pReqRepeal *CThostFtdcReqRepealField, pRspInfo *CThostFtdcRspInfoField)) {
    t.OnErrRtnRepealBankToFutureByFutureManual_ = fn
	t.h.MustFindProc("tOnErrRtnRepealBankToFutureByFutureManual").Call(t.pSpi, syscall.NewCallback(t.OnErrRtnRepealBankToFutureByFutureManual__))
}

// 系统运行时期货端手工发起冲正期货转银行错误回报
func (t *Trade) OnErrRtnRepealFutureToBankByFutureManual(fn func(pReqRepeal *CThostFtdcReqRepealField, pRspInfo *CThostFtdcRspInfoField)) {
    t.OnErrRtnRepealFutureToBankByFutureManual_ = fn
	t.h.MustFindProc("tOnErrRtnRepealFutureToBankByFutureManual").Call(t.pSpi, syscall.NewCallback(t.OnErrRtnRepealFutureToBankByFutureManual__))
}

// 期货发起查询银行余额错误回报
func (t *Trade) OnErrRtnQueryBankBalanceByFuture(fn func(pReqQueryAccount *CThostFtdcReqQueryAccountField, pRspInfo *CThostFtdcRspInfoField)) {
    t.OnErrRtnQueryBankBalanceByFuture_ = fn
	t.h.MustFindProc("tOnErrRtnQueryBankBalanceByFuture").Call(t.pSpi, syscall.NewCallback(t.OnErrRtnQueryBankBalanceByFuture__))
}

// 期货发起冲正银行转期货请求，银行处理完毕后报盘发回的通知
func (t *Trade) OnRtnRepealFromBankToFutureByFuture(fn func(pRspRepeal *CThostFtdcRspRepealField)) {
    t.OnRtnRepealFromBankToFutureByFuture_ = fn
	t.h.MustFindProc("tOnRtnRepealFromBankToFutureByFuture").Call(t.pSpi, syscall.NewCallback(t.OnRtnRepealFromBankToFutureByFuture__))
}

// 期货发起冲正期货转银行请求，银行处理完毕后报盘发回的通知
func (t *Trade) OnRtnRepealFromFutureToBankByFuture(fn func(pRspRepeal *CThostFtdcRspRepealField)) {
    t.OnRtnRepealFromFutureToBankByFuture_ = fn
	t.h.MustFindProc("tOnRtnRepealFromFutureToBankByFuture").Call(t.pSpi, syscall.NewCallback(t.OnRtnRepealFromFutureToBankByFuture__))
}

// 期货发起银行资金转期货应答
func (t *Trade) OnRspFromBankToFutureByFuture(fn func(pReqTransfer *CThostFtdcReqTransferField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspFromBankToFutureByFuture_ = fn
	t.h.MustFindProc("tOnRspFromBankToFutureByFuture").Call(t.pSpi, syscall.NewCallback(t.OnRspFromBankToFutureByFuture__))
}

// 期货发起期货资金转银行应答
func (t *Trade) OnRspFromFutureToBankByFuture(fn func(pReqTransfer *CThostFtdcReqTransferField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspFromFutureToBankByFuture_ = fn
	t.h.MustFindProc("tOnRspFromFutureToBankByFuture").Call(t.pSpi, syscall.NewCallback(t.OnRspFromFutureToBankByFuture__))
}

// 期货发起查询银行余额应答
func (t *Trade) OnRspQueryBankAccountMoneyByFuture(fn func(pReqQueryAccount *CThostFtdcReqQueryAccountField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQueryBankAccountMoneyByFuture_ = fn
	t.h.MustFindProc("tOnRspQueryBankAccountMoneyByFuture").Call(t.pSpi, syscall.NewCallback(t.OnRspQueryBankAccountMoneyByFuture__))
}

// 银行发起银期开户通知
func (t *Trade) OnRtnOpenAccountByBank(fn func(pOpenAccount *CThostFtdcOpenAccountField)) {
    t.OnRtnOpenAccountByBank_ = fn
	t.h.MustFindProc("tOnRtnOpenAccountByBank").Call(t.pSpi, syscall.NewCallback(t.OnRtnOpenAccountByBank__))
}

// 银行发起银期销户通知
func (t *Trade) OnRtnCancelAccountByBank(fn func(pCancelAccount *CThostFtdcCancelAccountField)) {
    t.OnRtnCancelAccountByBank_ = fn
	t.h.MustFindProc("tOnRtnCancelAccountByBank").Call(t.pSpi, syscall.NewCallback(t.OnRtnCancelAccountByBank__))
}

// 银行发起变更银行账号通知
func (t *Trade) OnRtnChangeAccountByBank(fn func(pChangeAccount *CThostFtdcChangeAccountField)) {
    t.OnRtnChangeAccountByBank_ = fn
	t.h.MustFindProc("tOnRtnChangeAccountByBank").Call(t.pSpi, syscall.NewCallback(t.OnRtnChangeAccountByBank__))
}

// 请求查询分类合约响应
func (t *Trade) OnRspQryClassifiedInstrument(fn func(pInstrument *CThostFtdcInstrumentField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryClassifiedInstrument_ = fn
	t.h.MustFindProc("tOnRspQryClassifiedInstrument").Call(t.pSpi, syscall.NewCallback(t.OnRspQryClassifiedInstrument__))
}

// 请求组合优惠比例响应
func (t *Trade) OnRspQryCombPromotionParam(fn func(pCombPromotionParam *CThostFtdcCombPromotionParamField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryCombPromotionParam_ = fn
	t.h.MustFindProc("tOnRspQryCombPromotionParam").Call(t.pSpi, syscall.NewCallback(t.OnRspQryCombPromotionParam__))
}

// 投资者风险结算持仓查询响应
func (t *Trade) OnRspQryRiskSettleInvstPosition(fn func(pRiskSettleInvstPosition *CThostFtdcRiskSettleInvstPositionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryRiskSettleInvstPosition_ = fn
	t.h.MustFindProc("tOnRspQryRiskSettleInvstPosition").Call(t.pSpi, syscall.NewCallback(t.OnRspQryRiskSettleInvstPosition__))
}

// 风险结算产品查询响应
func (t *Trade) OnRspQryRiskSettleProductStatus(fn func(pRiskSettleProductStatus *CThostFtdcRiskSettleProductStatusField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryRiskSettleProductStatus_ = fn
	t.h.MustFindProc("tOnRspQryRiskSettleProductStatus").Call(t.pSpi, syscall.NewCallback(t.OnRspQryRiskSettleProductStatus__))
}

// SPBM期货合约参数查询响应
func (t *Trade) OnRspQrySPBMFutureParameter(fn func(pSPBMFutureParameter *CThostFtdcSPBMFutureParameterField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQrySPBMFutureParameter_ = fn
	t.h.MustFindProc("tOnRspQrySPBMFutureParameter").Call(t.pSpi, syscall.NewCallback(t.OnRspQrySPBMFutureParameter__))
}

// SPBM期权合约参数查询响应
func (t *Trade) OnRspQrySPBMOptionParameter(fn func(pSPBMOptionParameter *CThostFtdcSPBMOptionParameterField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQrySPBMOptionParameter_ = fn
	t.h.MustFindProc("tOnRspQrySPBMOptionParameter").Call(t.pSpi, syscall.NewCallback(t.OnRspQrySPBMOptionParameter__))
}

// SPBM品种内对锁仓折扣参数查询响应
func (t *Trade) OnRspQrySPBMIntraParameter(fn func(pSPBMIntraParameter *CThostFtdcSPBMIntraParameterField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQrySPBMIntraParameter_ = fn
	t.h.MustFindProc("tOnRspQrySPBMIntraParameter").Call(t.pSpi, syscall.NewCallback(t.OnRspQrySPBMIntraParameter__))
}

// SPBM跨品种抵扣参数查询响应
func (t *Trade) OnRspQrySPBMInterParameter(fn func(pSPBMInterParameter *CThostFtdcSPBMInterParameterField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQrySPBMInterParameter_ = fn
	t.h.MustFindProc("tOnRspQrySPBMInterParameter").Call(t.pSpi, syscall.NewCallback(t.OnRspQrySPBMInterParameter__))
}

// SPBM组合保证金套餐查询响应
func (t *Trade) OnRspQrySPBMPortfDefinition(fn func(pSPBMPortfDefinition *CThostFtdcSPBMPortfDefinitionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQrySPBMPortfDefinition_ = fn
	t.h.MustFindProc("tOnRspQrySPBMPortfDefinition").Call(t.pSpi, syscall.NewCallback(t.OnRspQrySPBMPortfDefinition__))
}

// 投资者SPBM套餐选择查询响应
func (t *Trade) OnRspQrySPBMInvestorPortfDef(fn func(pSPBMInvestorPortfDef *CThostFtdcSPBMInvestorPortfDefField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQrySPBMInvestorPortfDef_ = fn
	t.h.MustFindProc("tOnRspQrySPBMInvestorPortfDef").Call(t.pSpi, syscall.NewCallback(t.OnRspQrySPBMInvestorPortfDef__))
}

// 投资者新型组合保证金系数查询响应
func (t *Trade) OnRspQryInvestorPortfMarginRatio(fn func(pInvestorPortfMarginRatio *CThostFtdcInvestorPortfMarginRatioField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryInvestorPortfMarginRatio_ = fn
	t.h.MustFindProc("tOnRspQryInvestorPortfMarginRatio").Call(t.pSpi, syscall.NewCallback(t.OnRspQryInvestorPortfMarginRatio__))
}

// 投资者产品SPBM明细查询响应
func (t *Trade) OnRspQryInvestorProdSPBMDetail(fn func(pInvestorProdSPBMDetail *CThostFtdcInvestorProdSPBMDetailField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool)) {
    t.OnRspQryInvestorProdSPBMDetail_ = fn
	t.h.MustFindProc("tOnRspQryInvestorProdSPBMDetail").Call(t.pSpi, syscall.NewCallback(t.OnRspQryInvestorProdSPBMDetail__))
}


// 当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。
func (t *Trade) OnFrontConnected__() uintptr {
    if t.OnFrontConnected_ != nil {    
	    t.OnFrontConnected_()
    }
	return 0
}

// 当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。
func (t *Trade) OnFrontDisconnected__(nReason int) uintptr {
    if t.OnFrontDisconnected_ != nil {    
	    t.OnFrontDisconnected_(nReason)
    }
	return 0
}

// 心跳超时警告。当长时间未收到报文时，该方法被调用。
func (t *Trade) OnHeartBeatWarning__(nTimeLapse int) uintptr {
    if t.OnHeartBeatWarning_ != nil {    
	    t.OnHeartBeatWarning_(nTimeLapse)
    }
	return 0
}

// 客户端认证响应
func (t *Trade) OnRspAuthenticate__(pRspAuthenticateField *CThostFtdcRspAuthenticateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspAuthenticate_ != nil {    
	    t.OnRspAuthenticate_(pRspAuthenticateField, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 登录请求响应
func (t *Trade) OnRspUserLogin__(pRspUserLogin *CThostFtdcRspUserLoginField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspUserLogin_ != nil {    
	    t.OnRspUserLogin_(pRspUserLogin, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 登出请求响应
func (t *Trade) OnRspUserLogout__(pUserLogout *CThostFtdcUserLogoutField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspUserLogout_ != nil {    
	    t.OnRspUserLogout_(pUserLogout, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 用户口令更新请求响应
func (t *Trade) OnRspUserPasswordUpdate__(pUserPasswordUpdate *CThostFtdcUserPasswordUpdateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspUserPasswordUpdate_ != nil {    
	    t.OnRspUserPasswordUpdate_(pUserPasswordUpdate, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 资金账户口令更新请求响应
func (t *Trade) OnRspTradingAccountPasswordUpdate__(pTradingAccountPasswordUpdate *CThostFtdcTradingAccountPasswordUpdateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspTradingAccountPasswordUpdate_ != nil {    
	    t.OnRspTradingAccountPasswordUpdate_(pTradingAccountPasswordUpdate, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 查询用户当前支持的认证模式的回复
func (t *Trade) OnRspUserAuthMethod__(pRspUserAuthMethod *CThostFtdcRspUserAuthMethodField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspUserAuthMethod_ != nil {    
	    t.OnRspUserAuthMethod_(pRspUserAuthMethod, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 获取图形验证码请求的回复
func (t *Trade) OnRspGenUserCaptcha__(pRspGenUserCaptcha *CThostFtdcRspGenUserCaptchaField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspGenUserCaptcha_ != nil {    
	    t.OnRspGenUserCaptcha_(pRspGenUserCaptcha, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 获取短信验证码请求的回复
func (t *Trade) OnRspGenUserText__(pRspGenUserText *CThostFtdcRspGenUserTextField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspGenUserText_ != nil {    
	    t.OnRspGenUserText_(pRspGenUserText, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 报单录入请求响应
func (t *Trade) OnRspOrderInsert__(pInputOrder *CThostFtdcInputOrderField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspOrderInsert_ != nil {    
	    t.OnRspOrderInsert_(pInputOrder, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 预埋单录入请求响应
func (t *Trade) OnRspParkedOrderInsert__(pParkedOrder *CThostFtdcParkedOrderField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspParkedOrderInsert_ != nil {    
	    t.OnRspParkedOrderInsert_(pParkedOrder, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 预埋撤单录入请求响应
func (t *Trade) OnRspParkedOrderAction__(pParkedOrderAction *CThostFtdcParkedOrderActionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspParkedOrderAction_ != nil {    
	    t.OnRspParkedOrderAction_(pParkedOrderAction, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 报单操作请求响应
func (t *Trade) OnRspOrderAction__(pInputOrderAction *CThostFtdcInputOrderActionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspOrderAction_ != nil {    
	    t.OnRspOrderAction_(pInputOrderAction, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 查询最大报单数量响应
func (t *Trade) OnRspQryMaxOrderVolume__(pQryMaxOrderVolume *CThostFtdcQryMaxOrderVolumeField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryMaxOrderVolume_ != nil {    
	    t.OnRspQryMaxOrderVolume_(pQryMaxOrderVolume, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 投资者结算结果确认响应
func (t *Trade) OnRspSettlementInfoConfirm__(pSettlementInfoConfirm *CThostFtdcSettlementInfoConfirmField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspSettlementInfoConfirm_ != nil {    
	    t.OnRspSettlementInfoConfirm_(pSettlementInfoConfirm, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 删除预埋单响应
func (t *Trade) OnRspRemoveParkedOrder__(pRemoveParkedOrder *CThostFtdcRemoveParkedOrderField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspRemoveParkedOrder_ != nil {    
	    t.OnRspRemoveParkedOrder_(pRemoveParkedOrder, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 删除预埋撤单响应
func (t *Trade) OnRspRemoveParkedOrderAction__(pRemoveParkedOrderAction *CThostFtdcRemoveParkedOrderActionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspRemoveParkedOrderAction_ != nil {    
	    t.OnRspRemoveParkedOrderAction_(pRemoveParkedOrderAction, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 执行宣告录入请求响应
func (t *Trade) OnRspExecOrderInsert__(pInputExecOrder *CThostFtdcInputExecOrderField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspExecOrderInsert_ != nil {    
	    t.OnRspExecOrderInsert_(pInputExecOrder, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 执行宣告操作请求响应
func (t *Trade) OnRspExecOrderAction__(pInputExecOrderAction *CThostFtdcInputExecOrderActionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspExecOrderAction_ != nil {    
	    t.OnRspExecOrderAction_(pInputExecOrderAction, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 询价录入请求响应
func (t *Trade) OnRspForQuoteInsert__(pInputForQuote *CThostFtdcInputForQuoteField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspForQuoteInsert_ != nil {    
	    t.OnRspForQuoteInsert_(pInputForQuote, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 报价录入请求响应
func (t *Trade) OnRspQuoteInsert__(pInputQuote *CThostFtdcInputQuoteField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQuoteInsert_ != nil {    
	    t.OnRspQuoteInsert_(pInputQuote, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 报价操作请求响应
func (t *Trade) OnRspQuoteAction__(pInputQuoteAction *CThostFtdcInputQuoteActionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQuoteAction_ != nil {    
	    t.OnRspQuoteAction_(pInputQuoteAction, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 批量报单操作请求响应
func (t *Trade) OnRspBatchOrderAction__(pInputBatchOrderAction *CThostFtdcInputBatchOrderActionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspBatchOrderAction_ != nil {    
	    t.OnRspBatchOrderAction_(pInputBatchOrderAction, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 期权自对冲录入请求响应
func (t *Trade) OnRspOptionSelfCloseInsert__(pInputOptionSelfClose *CThostFtdcInputOptionSelfCloseField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspOptionSelfCloseInsert_ != nil {    
	    t.OnRspOptionSelfCloseInsert_(pInputOptionSelfClose, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 期权自对冲操作请求响应
func (t *Trade) OnRspOptionSelfCloseAction__(pInputOptionSelfCloseAction *CThostFtdcInputOptionSelfCloseActionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspOptionSelfCloseAction_ != nil {    
	    t.OnRspOptionSelfCloseAction_(pInputOptionSelfCloseAction, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 申请组合录入请求响应
func (t *Trade) OnRspCombActionInsert__(pInputCombAction *CThostFtdcInputCombActionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspCombActionInsert_ != nil {    
	    t.OnRspCombActionInsert_(pInputCombAction, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询报单响应
func (t *Trade) OnRspQryOrder__(pOrder *CThostFtdcOrderField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryOrder_ != nil {    
	    t.OnRspQryOrder_(pOrder, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询成交响应
func (t *Trade) OnRspQryTrade__(pTrade *CThostFtdcTradeField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryTrade_ != nil {    
	    t.OnRspQryTrade_(pTrade, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询投资者持仓响应
func (t *Trade) OnRspQryInvestorPosition__(pInvestorPosition *CThostFtdcInvestorPositionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryInvestorPosition_ != nil {    
	    t.OnRspQryInvestorPosition_(pInvestorPosition, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询资金账户响应
func (t *Trade) OnRspQryTradingAccount__(pTradingAccount *CThostFtdcTradingAccountField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryTradingAccount_ != nil {    
	    t.OnRspQryTradingAccount_(pTradingAccount, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询投资者响应
func (t *Trade) OnRspQryInvestor__(pInvestor *CThostFtdcInvestorField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryInvestor_ != nil {    
	    t.OnRspQryInvestor_(pInvestor, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询交易编码响应
func (t *Trade) OnRspQryTradingCode__(pTradingCode *CThostFtdcTradingCodeField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryTradingCode_ != nil {    
	    t.OnRspQryTradingCode_(pTradingCode, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询合约保证金率响应
func (t *Trade) OnRspQryInstrumentMarginRate__(pInstrumentMarginRate *CThostFtdcInstrumentMarginRateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryInstrumentMarginRate_ != nil {    
	    t.OnRspQryInstrumentMarginRate_(pInstrumentMarginRate, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询合约手续费率响应
func (t *Trade) OnRspQryInstrumentCommissionRate__(pInstrumentCommissionRate *CThostFtdcInstrumentCommissionRateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryInstrumentCommissionRate_ != nil {    
	    t.OnRspQryInstrumentCommissionRate_(pInstrumentCommissionRate, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询交易所响应
func (t *Trade) OnRspQryExchange__(pExchange *CThostFtdcExchangeField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryExchange_ != nil {    
	    t.OnRspQryExchange_(pExchange, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询产品响应
func (t *Trade) OnRspQryProduct__(pProduct *CThostFtdcProductField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryProduct_ != nil {    
	    t.OnRspQryProduct_(pProduct, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询合约响应
func (t *Trade) OnRspQryInstrument__(pInstrument *CThostFtdcInstrumentField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryInstrument_ != nil {    
	    t.OnRspQryInstrument_(pInstrument, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询行情响应
func (t *Trade) OnRspQryDepthMarketData__(pDepthMarketData *CThostFtdcDepthMarketDataField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryDepthMarketData_ != nil {    
	    t.OnRspQryDepthMarketData_(pDepthMarketData, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询交易员报盘机响应
func (t *Trade) OnRspQryTraderOffer__(pTraderOffer *CThostFtdcTraderOfferField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryTraderOffer_ != nil {    
	    t.OnRspQryTraderOffer_(pTraderOffer, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询投资者结算结果响应
func (t *Trade) OnRspQrySettlementInfo__(pSettlementInfo *CThostFtdcSettlementInfoField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQrySettlementInfo_ != nil {    
	    t.OnRspQrySettlementInfo_(pSettlementInfo, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询转帐银行响应
func (t *Trade) OnRspQryTransferBank__(pTransferBank *CThostFtdcTransferBankField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryTransferBank_ != nil {    
	    t.OnRspQryTransferBank_(pTransferBank, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询投资者持仓明细响应
func (t *Trade) OnRspQryInvestorPositionDetail__(pInvestorPositionDetail *CThostFtdcInvestorPositionDetailField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryInvestorPositionDetail_ != nil {    
	    t.OnRspQryInvestorPositionDetail_(pInvestorPositionDetail, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询客户通知响应
func (t *Trade) OnRspQryNotice__(pNotice *CThostFtdcNoticeField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryNotice_ != nil {    
	    t.OnRspQryNotice_(pNotice, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询结算信息确认响应
func (t *Trade) OnRspQrySettlementInfoConfirm__(pSettlementInfoConfirm *CThostFtdcSettlementInfoConfirmField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQrySettlementInfoConfirm_ != nil {    
	    t.OnRspQrySettlementInfoConfirm_(pSettlementInfoConfirm, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询投资者持仓明细响应
func (t *Trade) OnRspQryInvestorPositionCombineDetail__(pInvestorPositionCombineDetail *CThostFtdcInvestorPositionCombineDetailField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryInvestorPositionCombineDetail_ != nil {    
	    t.OnRspQryInvestorPositionCombineDetail_(pInvestorPositionCombineDetail, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 查询保证金监管系统经纪公司资金账户密钥响应
func (t *Trade) OnRspQryCFMMCTradingAccountKey__(pCFMMCTradingAccountKey *CThostFtdcCFMMCTradingAccountKeyField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryCFMMCTradingAccountKey_ != nil {    
	    t.OnRspQryCFMMCTradingAccountKey_(pCFMMCTradingAccountKey, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询仓单折抵信息响应
func (t *Trade) OnRspQryEWarrantOffset__(pEWarrantOffset *CThostFtdcEWarrantOffsetField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryEWarrantOffset_ != nil {    
	    t.OnRspQryEWarrantOffset_(pEWarrantOffset, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询投资者品种/跨品种保证金响应
func (t *Trade) OnRspQryInvestorProductGroupMargin__(pInvestorProductGroupMargin *CThostFtdcInvestorProductGroupMarginField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryInvestorProductGroupMargin_ != nil {    
	    t.OnRspQryInvestorProductGroupMargin_(pInvestorProductGroupMargin, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询交易所保证金率响应
func (t *Trade) OnRspQryExchangeMarginRate__(pExchangeMarginRate *CThostFtdcExchangeMarginRateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryExchangeMarginRate_ != nil {    
	    t.OnRspQryExchangeMarginRate_(pExchangeMarginRate, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询交易所调整保证金率响应
func (t *Trade) OnRspQryExchangeMarginRateAdjust__(pExchangeMarginRateAdjust *CThostFtdcExchangeMarginRateAdjustField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryExchangeMarginRateAdjust_ != nil {    
	    t.OnRspQryExchangeMarginRateAdjust_(pExchangeMarginRateAdjust, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询汇率响应
func (t *Trade) OnRspQryExchangeRate__(pExchangeRate *CThostFtdcExchangeRateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryExchangeRate_ != nil {    
	    t.OnRspQryExchangeRate_(pExchangeRate, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询二级代理操作员银期权限响应
func (t *Trade) OnRspQrySecAgentACIDMap__(pSecAgentACIDMap *CThostFtdcSecAgentACIDMapField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQrySecAgentACIDMap_ != nil {    
	    t.OnRspQrySecAgentACIDMap_(pSecAgentACIDMap, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询产品报价汇率
func (t *Trade) OnRspQryProductExchRate__(pProductExchRate *CThostFtdcProductExchRateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryProductExchRate_ != nil {    
	    t.OnRspQryProductExchRate_(pProductExchRate, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询产品组
func (t *Trade) OnRspQryProductGroup__(pProductGroup *CThostFtdcProductGroupField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryProductGroup_ != nil {    
	    t.OnRspQryProductGroup_(pProductGroup, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询做市商合约手续费率响应
func (t *Trade) OnRspQryMMInstrumentCommissionRate__(pMMInstrumentCommissionRate *CThostFtdcMMInstrumentCommissionRateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryMMInstrumentCommissionRate_ != nil {    
	    t.OnRspQryMMInstrumentCommissionRate_(pMMInstrumentCommissionRate, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询做市商期权合约手续费响应
func (t *Trade) OnRspQryMMOptionInstrCommRate__(pMMOptionInstrCommRate *CThostFtdcMMOptionInstrCommRateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryMMOptionInstrCommRate_ != nil {    
	    t.OnRspQryMMOptionInstrCommRate_(pMMOptionInstrCommRate, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询报单手续费响应
func (t *Trade) OnRspQryInstrumentOrderCommRate__(pInstrumentOrderCommRate *CThostFtdcInstrumentOrderCommRateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryInstrumentOrderCommRate_ != nil {    
	    t.OnRspQryInstrumentOrderCommRate_(pInstrumentOrderCommRate, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询资金账户响应
func (t *Trade) OnRspQrySecAgentTradingAccount__(pTradingAccount *CThostFtdcTradingAccountField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQrySecAgentTradingAccount_ != nil {    
	    t.OnRspQrySecAgentTradingAccount_(pTradingAccount, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询二级代理商资金校验模式响应
func (t *Trade) OnRspQrySecAgentCheckMode__(pSecAgentCheckMode *CThostFtdcSecAgentCheckModeField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQrySecAgentCheckMode_ != nil {    
	    t.OnRspQrySecAgentCheckMode_(pSecAgentCheckMode, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询二级代理商信息响应
func (t *Trade) OnRspQrySecAgentTradeInfo__(pSecAgentTradeInfo *CThostFtdcSecAgentTradeInfoField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQrySecAgentTradeInfo_ != nil {    
	    t.OnRspQrySecAgentTradeInfo_(pSecAgentTradeInfo, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询期权交易成本响应
func (t *Trade) OnRspQryOptionInstrTradeCost__(pOptionInstrTradeCost *CThostFtdcOptionInstrTradeCostField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryOptionInstrTradeCost_ != nil {    
	    t.OnRspQryOptionInstrTradeCost_(pOptionInstrTradeCost, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询期权合约手续费响应
func (t *Trade) OnRspQryOptionInstrCommRate__(pOptionInstrCommRate *CThostFtdcOptionInstrCommRateField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryOptionInstrCommRate_ != nil {    
	    t.OnRspQryOptionInstrCommRate_(pOptionInstrCommRate, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询执行宣告响应
func (t *Trade) OnRspQryExecOrder__(pExecOrder *CThostFtdcExecOrderField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryExecOrder_ != nil {    
	    t.OnRspQryExecOrder_(pExecOrder, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询询价响应
func (t *Trade) OnRspQryForQuote__(pForQuote *CThostFtdcForQuoteField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryForQuote_ != nil {    
	    t.OnRspQryForQuote_(pForQuote, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询报价响应
func (t *Trade) OnRspQryQuote__(pQuote *CThostFtdcQuoteField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryQuote_ != nil {    
	    t.OnRspQryQuote_(pQuote, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询期权自对冲响应
func (t *Trade) OnRspQryOptionSelfClose__(pOptionSelfClose *CThostFtdcOptionSelfCloseField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryOptionSelfClose_ != nil {    
	    t.OnRspQryOptionSelfClose_(pOptionSelfClose, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询投资单元响应
func (t *Trade) OnRspQryInvestUnit__(pInvestUnit *CThostFtdcInvestUnitField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryInvestUnit_ != nil {    
	    t.OnRspQryInvestUnit_(pInvestUnit, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询组合合约安全系数响应
func (t *Trade) OnRspQryCombInstrumentGuard__(pCombInstrumentGuard *CThostFtdcCombInstrumentGuardField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryCombInstrumentGuard_ != nil {    
	    t.OnRspQryCombInstrumentGuard_(pCombInstrumentGuard, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询申请组合响应
func (t *Trade) OnRspQryCombAction__(pCombAction *CThostFtdcCombActionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryCombAction_ != nil {    
	    t.OnRspQryCombAction_(pCombAction, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询转帐流水响应
func (t *Trade) OnRspQryTransferSerial__(pTransferSerial *CThostFtdcTransferSerialField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryTransferSerial_ != nil {    
	    t.OnRspQryTransferSerial_(pTransferSerial, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询银期签约关系响应
func (t *Trade) OnRspQryAccountregister__(pAccountregister *CThostFtdcAccountregisterField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryAccountregister_ != nil {    
	    t.OnRspQryAccountregister_(pAccountregister, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 错误应答
func (t *Trade) OnRspError__(pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspError_ != nil {    
	    t.OnRspError_(pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 报单通知
func (t *Trade) OnRtnOrder__(pOrder *CThostFtdcOrderField) uintptr {
    if t.OnRtnOrder_ != nil {    
	    t.OnRtnOrder_(pOrder)
    }
	return 0
}

// 成交通知
func (t *Trade) OnRtnTrade__(pTrade *CThostFtdcTradeField) uintptr {
    if t.OnRtnTrade_ != nil {    
	    t.OnRtnTrade_(pTrade)
    }
	return 0
}

// 报单录入错误回报
func (t *Trade) OnErrRtnOrderInsert__(pInputOrder *CThostFtdcInputOrderField, pRspInfo *CThostFtdcRspInfoField) uintptr {
    if t.OnErrRtnOrderInsert_ != nil {    
	    t.OnErrRtnOrderInsert_(pInputOrder, pRspInfo)
    }
	return 0
}

// 报单操作错误回报
func (t *Trade) OnErrRtnOrderAction__(pOrderAction *CThostFtdcOrderActionField, pRspInfo *CThostFtdcRspInfoField) uintptr {
    if t.OnErrRtnOrderAction_ != nil {    
	    t.OnErrRtnOrderAction_(pOrderAction, pRspInfo)
    }
	return 0
}

// 合约交易状态通知
func (t *Trade) OnRtnInstrumentStatus__(pInstrumentStatus *CThostFtdcInstrumentStatusField) uintptr {
    if t.OnRtnInstrumentStatus_ != nil {    
	    t.OnRtnInstrumentStatus_(pInstrumentStatus)
    }
	return 0
}

// 交易所公告通知
func (t *Trade) OnRtnBulletin__(pBulletin *CThostFtdcBulletinField) uintptr {
    if t.OnRtnBulletin_ != nil {    
	    t.OnRtnBulletin_(pBulletin)
    }
	return 0
}

// 交易通知
func (t *Trade) OnRtnTradingNotice__(pTradingNoticeInfo *CThostFtdcTradingNoticeInfoField) uintptr {
    if t.OnRtnTradingNotice_ != nil {    
	    t.OnRtnTradingNotice_(pTradingNoticeInfo)
    }
	return 0
}

// 提示条件单校验错误
func (t *Trade) OnRtnErrorConditionalOrder__(pErrorConditionalOrder *CThostFtdcErrorConditionalOrderField) uintptr {
    if t.OnRtnErrorConditionalOrder_ != nil {    
	    t.OnRtnErrorConditionalOrder_(pErrorConditionalOrder)
    }
	return 0
}

// 执行宣告通知
func (t *Trade) OnRtnExecOrder__(pExecOrder *CThostFtdcExecOrderField) uintptr {
    if t.OnRtnExecOrder_ != nil {    
	    t.OnRtnExecOrder_(pExecOrder)
    }
	return 0
}

// 执行宣告录入错误回报
func (t *Trade) OnErrRtnExecOrderInsert__(pInputExecOrder *CThostFtdcInputExecOrderField, pRspInfo *CThostFtdcRspInfoField) uintptr {
    if t.OnErrRtnExecOrderInsert_ != nil {    
	    t.OnErrRtnExecOrderInsert_(pInputExecOrder, pRspInfo)
    }
	return 0
}

// 执行宣告操作错误回报
func (t *Trade) OnErrRtnExecOrderAction__(pExecOrderAction *CThostFtdcExecOrderActionField, pRspInfo *CThostFtdcRspInfoField) uintptr {
    if t.OnErrRtnExecOrderAction_ != nil {    
	    t.OnErrRtnExecOrderAction_(pExecOrderAction, pRspInfo)
    }
	return 0
}

// 询价录入错误回报
func (t *Trade) OnErrRtnForQuoteInsert__(pInputForQuote *CThostFtdcInputForQuoteField, pRspInfo *CThostFtdcRspInfoField) uintptr {
    if t.OnErrRtnForQuoteInsert_ != nil {    
	    t.OnErrRtnForQuoteInsert_(pInputForQuote, pRspInfo)
    }
	return 0
}

// 报价通知
func (t *Trade) OnRtnQuote__(pQuote *CThostFtdcQuoteField) uintptr {
    if t.OnRtnQuote_ != nil {    
	    t.OnRtnQuote_(pQuote)
    }
	return 0
}

// 报价录入错误回报
func (t *Trade) OnErrRtnQuoteInsert__(pInputQuote *CThostFtdcInputQuoteField, pRspInfo *CThostFtdcRspInfoField) uintptr {
    if t.OnErrRtnQuoteInsert_ != nil {    
	    t.OnErrRtnQuoteInsert_(pInputQuote, pRspInfo)
    }
	return 0
}

// 报价操作错误回报
func (t *Trade) OnErrRtnQuoteAction__(pQuoteAction *CThostFtdcQuoteActionField, pRspInfo *CThostFtdcRspInfoField) uintptr {
    if t.OnErrRtnQuoteAction_ != nil {    
	    t.OnErrRtnQuoteAction_(pQuoteAction, pRspInfo)
    }
	return 0
}

// 询价通知
func (t *Trade) OnRtnForQuoteRsp__(pForQuoteRsp *CThostFtdcForQuoteRspField) uintptr {
    if t.OnRtnForQuoteRsp_ != nil {    
	    t.OnRtnForQuoteRsp_(pForQuoteRsp)
    }
	return 0
}

// 保证金监控中心用户令牌
func (t *Trade) OnRtnCFMMCTradingAccountToken__(pCFMMCTradingAccountToken *CThostFtdcCFMMCTradingAccountTokenField) uintptr {
    if t.OnRtnCFMMCTradingAccountToken_ != nil {    
	    t.OnRtnCFMMCTradingAccountToken_(pCFMMCTradingAccountToken)
    }
	return 0
}

// 批量报单操作错误回报
func (t *Trade) OnErrRtnBatchOrderAction__(pBatchOrderAction *CThostFtdcBatchOrderActionField, pRspInfo *CThostFtdcRspInfoField) uintptr {
    if t.OnErrRtnBatchOrderAction_ != nil {    
	    t.OnErrRtnBatchOrderAction_(pBatchOrderAction, pRspInfo)
    }
	return 0
}

// 期权自对冲通知
func (t *Trade) OnRtnOptionSelfClose__(pOptionSelfClose *CThostFtdcOptionSelfCloseField) uintptr {
    if t.OnRtnOptionSelfClose_ != nil {    
	    t.OnRtnOptionSelfClose_(pOptionSelfClose)
    }
	return 0
}

// 期权自对冲录入错误回报
func (t *Trade) OnErrRtnOptionSelfCloseInsert__(pInputOptionSelfClose *CThostFtdcInputOptionSelfCloseField, pRspInfo *CThostFtdcRspInfoField) uintptr {
    if t.OnErrRtnOptionSelfCloseInsert_ != nil {    
	    t.OnErrRtnOptionSelfCloseInsert_(pInputOptionSelfClose, pRspInfo)
    }
	return 0
}

// 期权自对冲操作错误回报
func (t *Trade) OnErrRtnOptionSelfCloseAction__(pOptionSelfCloseAction *CThostFtdcOptionSelfCloseActionField, pRspInfo *CThostFtdcRspInfoField) uintptr {
    if t.OnErrRtnOptionSelfCloseAction_ != nil {    
	    t.OnErrRtnOptionSelfCloseAction_(pOptionSelfCloseAction, pRspInfo)
    }
	return 0
}

// 申请组合通知
func (t *Trade) OnRtnCombAction__(pCombAction *CThostFtdcCombActionField) uintptr {
    if t.OnRtnCombAction_ != nil {    
	    t.OnRtnCombAction_(pCombAction)
    }
	return 0
}

// 申请组合录入错误回报
func (t *Trade) OnErrRtnCombActionInsert__(pInputCombAction *CThostFtdcInputCombActionField, pRspInfo *CThostFtdcRspInfoField) uintptr {
    if t.OnErrRtnCombActionInsert_ != nil {    
	    t.OnErrRtnCombActionInsert_(pInputCombAction, pRspInfo)
    }
	return 0
}

// 请求查询签约银行响应
func (t *Trade) OnRspQryContractBank__(pContractBank *CThostFtdcContractBankField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryContractBank_ != nil {    
	    t.OnRspQryContractBank_(pContractBank, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询预埋单响应
func (t *Trade) OnRspQryParkedOrder__(pParkedOrder *CThostFtdcParkedOrderField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryParkedOrder_ != nil {    
	    t.OnRspQryParkedOrder_(pParkedOrder, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询预埋撤单响应
func (t *Trade) OnRspQryParkedOrderAction__(pParkedOrderAction *CThostFtdcParkedOrderActionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryParkedOrderAction_ != nil {    
	    t.OnRspQryParkedOrderAction_(pParkedOrderAction, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询交易通知响应
func (t *Trade) OnRspQryTradingNotice__(pTradingNotice *CThostFtdcTradingNoticeField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryTradingNotice_ != nil {    
	    t.OnRspQryTradingNotice_(pTradingNotice, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询经纪公司交易参数响应
func (t *Trade) OnRspQryBrokerTradingParams__(pBrokerTradingParams *CThostFtdcBrokerTradingParamsField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryBrokerTradingParams_ != nil {    
	    t.OnRspQryBrokerTradingParams_(pBrokerTradingParams, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询经纪公司交易算法响应
func (t *Trade) OnRspQryBrokerTradingAlgos__(pBrokerTradingAlgos *CThostFtdcBrokerTradingAlgosField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryBrokerTradingAlgos_ != nil {    
	    t.OnRspQryBrokerTradingAlgos_(pBrokerTradingAlgos, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求查询监控中心用户令牌
func (t *Trade) OnRspQueryCFMMCTradingAccountToken__(pQueryCFMMCTradingAccountToken *CThostFtdcQueryCFMMCTradingAccountTokenField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQueryCFMMCTradingAccountToken_ != nil {    
	    t.OnRspQueryCFMMCTradingAccountToken_(pQueryCFMMCTradingAccountToken, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 银行发起银行资金转期货通知
func (t *Trade) OnRtnFromBankToFutureByBank__(pRspTransfer *CThostFtdcRspTransferField) uintptr {
    if t.OnRtnFromBankToFutureByBank_ != nil {    
	    t.OnRtnFromBankToFutureByBank_(pRspTransfer)
    }
	return 0
}

// 银行发起期货资金转银行通知
func (t *Trade) OnRtnFromFutureToBankByBank__(pRspTransfer *CThostFtdcRspTransferField) uintptr {
    if t.OnRtnFromFutureToBankByBank_ != nil {    
	    t.OnRtnFromFutureToBankByBank_(pRspTransfer)
    }
	return 0
}

// 银行发起冲正银行转期货通知
func (t *Trade) OnRtnRepealFromBankToFutureByBank__(pRspRepeal *CThostFtdcRspRepealField) uintptr {
    if t.OnRtnRepealFromBankToFutureByBank_ != nil {    
	    t.OnRtnRepealFromBankToFutureByBank_(pRspRepeal)
    }
	return 0
}

// 银行发起冲正期货转银行通知
func (t *Trade) OnRtnRepealFromFutureToBankByBank__(pRspRepeal *CThostFtdcRspRepealField) uintptr {
    if t.OnRtnRepealFromFutureToBankByBank_ != nil {    
	    t.OnRtnRepealFromFutureToBankByBank_(pRspRepeal)
    }
	return 0
}

// 期货发起银行资金转期货通知
func (t *Trade) OnRtnFromBankToFutureByFuture__(pRspTransfer *CThostFtdcRspTransferField) uintptr {
    if t.OnRtnFromBankToFutureByFuture_ != nil {    
	    t.OnRtnFromBankToFutureByFuture_(pRspTransfer)
    }
	return 0
}

// 期货发起期货资金转银行通知
func (t *Trade) OnRtnFromFutureToBankByFuture__(pRspTransfer *CThostFtdcRspTransferField) uintptr {
    if t.OnRtnFromFutureToBankByFuture_ != nil {    
	    t.OnRtnFromFutureToBankByFuture_(pRspTransfer)
    }
	return 0
}

// 系统运行时期货端手工发起冲正银行转期货请求，银行处理完毕后报盘发回的通知
func (t *Trade) OnRtnRepealFromBankToFutureByFutureManual__(pRspRepeal *CThostFtdcRspRepealField) uintptr {
    if t.OnRtnRepealFromBankToFutureByFutureManual_ != nil {    
	    t.OnRtnRepealFromBankToFutureByFutureManual_(pRspRepeal)
    }
	return 0
}

// 系统运行时期货端手工发起冲正期货转银行请求，银行处理完毕后报盘发回的通知
func (t *Trade) OnRtnRepealFromFutureToBankByFutureManual__(pRspRepeal *CThostFtdcRspRepealField) uintptr {
    if t.OnRtnRepealFromFutureToBankByFutureManual_ != nil {    
	    t.OnRtnRepealFromFutureToBankByFutureManual_(pRspRepeal)
    }
	return 0
}

// 期货发起查询银行余额通知
func (t *Trade) OnRtnQueryBankBalanceByFuture__(pNotifyQueryAccount *CThostFtdcNotifyQueryAccountField) uintptr {
    if t.OnRtnQueryBankBalanceByFuture_ != nil {    
	    t.OnRtnQueryBankBalanceByFuture_(pNotifyQueryAccount)
    }
	return 0
}

// 期货发起银行资金转期货错误回报
func (t *Trade) OnErrRtnBankToFutureByFuture__(pReqTransfer *CThostFtdcReqTransferField, pRspInfo *CThostFtdcRspInfoField) uintptr {
    if t.OnErrRtnBankToFutureByFuture_ != nil {    
	    t.OnErrRtnBankToFutureByFuture_(pReqTransfer, pRspInfo)
    }
	return 0
}

// 期货发起期货资金转银行错误回报
func (t *Trade) OnErrRtnFutureToBankByFuture__(pReqTransfer *CThostFtdcReqTransferField, pRspInfo *CThostFtdcRspInfoField) uintptr {
    if t.OnErrRtnFutureToBankByFuture_ != nil {    
	    t.OnErrRtnFutureToBankByFuture_(pReqTransfer, pRspInfo)
    }
	return 0
}

// 系统运行时期货端手工发起冲正银行转期货错误回报
func (t *Trade) OnErrRtnRepealBankToFutureByFutureManual__(pReqRepeal *CThostFtdcReqRepealField, pRspInfo *CThostFtdcRspInfoField) uintptr {
    if t.OnErrRtnRepealBankToFutureByFutureManual_ != nil {    
	    t.OnErrRtnRepealBankToFutureByFutureManual_(pReqRepeal, pRspInfo)
    }
	return 0
}

// 系统运行时期货端手工发起冲正期货转银行错误回报
func (t *Trade) OnErrRtnRepealFutureToBankByFutureManual__(pReqRepeal *CThostFtdcReqRepealField, pRspInfo *CThostFtdcRspInfoField) uintptr {
    if t.OnErrRtnRepealFutureToBankByFutureManual_ != nil {    
	    t.OnErrRtnRepealFutureToBankByFutureManual_(pReqRepeal, pRspInfo)
    }
	return 0
}

// 期货发起查询银行余额错误回报
func (t *Trade) OnErrRtnQueryBankBalanceByFuture__(pReqQueryAccount *CThostFtdcReqQueryAccountField, pRspInfo *CThostFtdcRspInfoField) uintptr {
    if t.OnErrRtnQueryBankBalanceByFuture_ != nil {    
	    t.OnErrRtnQueryBankBalanceByFuture_(pReqQueryAccount, pRspInfo)
    }
	return 0
}

// 期货发起冲正银行转期货请求，银行处理完毕后报盘发回的通知
func (t *Trade) OnRtnRepealFromBankToFutureByFuture__(pRspRepeal *CThostFtdcRspRepealField) uintptr {
    if t.OnRtnRepealFromBankToFutureByFuture_ != nil {    
	    t.OnRtnRepealFromBankToFutureByFuture_(pRspRepeal)
    }
	return 0
}

// 期货发起冲正期货转银行请求，银行处理完毕后报盘发回的通知
func (t *Trade) OnRtnRepealFromFutureToBankByFuture__(pRspRepeal *CThostFtdcRspRepealField) uintptr {
    if t.OnRtnRepealFromFutureToBankByFuture_ != nil {    
	    t.OnRtnRepealFromFutureToBankByFuture_(pRspRepeal)
    }
	return 0
}

// 期货发起银行资金转期货应答
func (t *Trade) OnRspFromBankToFutureByFuture__(pReqTransfer *CThostFtdcReqTransferField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspFromBankToFutureByFuture_ != nil {    
	    t.OnRspFromBankToFutureByFuture_(pReqTransfer, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 期货发起期货资金转银行应答
func (t *Trade) OnRspFromFutureToBankByFuture__(pReqTransfer *CThostFtdcReqTransferField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspFromFutureToBankByFuture_ != nil {    
	    t.OnRspFromFutureToBankByFuture_(pReqTransfer, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 期货发起查询银行余额应答
func (t *Trade) OnRspQueryBankAccountMoneyByFuture__(pReqQueryAccount *CThostFtdcReqQueryAccountField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQueryBankAccountMoneyByFuture_ != nil {    
	    t.OnRspQueryBankAccountMoneyByFuture_(pReqQueryAccount, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 银行发起银期开户通知
func (t *Trade) OnRtnOpenAccountByBank__(pOpenAccount *CThostFtdcOpenAccountField) uintptr {
    if t.OnRtnOpenAccountByBank_ != nil {    
	    t.OnRtnOpenAccountByBank_(pOpenAccount)
    }
	return 0
}

// 银行发起银期销户通知
func (t *Trade) OnRtnCancelAccountByBank__(pCancelAccount *CThostFtdcCancelAccountField) uintptr {
    if t.OnRtnCancelAccountByBank_ != nil {    
	    t.OnRtnCancelAccountByBank_(pCancelAccount)
    }
	return 0
}

// 银行发起变更银行账号通知
func (t *Trade) OnRtnChangeAccountByBank__(pChangeAccount *CThostFtdcChangeAccountField) uintptr {
    if t.OnRtnChangeAccountByBank_ != nil {    
	    t.OnRtnChangeAccountByBank_(pChangeAccount)
    }
	return 0
}

// 请求查询分类合约响应
func (t *Trade) OnRspQryClassifiedInstrument__(pInstrument *CThostFtdcInstrumentField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryClassifiedInstrument_ != nil {    
	    t.OnRspQryClassifiedInstrument_(pInstrument, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 请求组合优惠比例响应
func (t *Trade) OnRspQryCombPromotionParam__(pCombPromotionParam *CThostFtdcCombPromotionParamField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryCombPromotionParam_ != nil {    
	    t.OnRspQryCombPromotionParam_(pCombPromotionParam, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 投资者风险结算持仓查询响应
func (t *Trade) OnRspQryRiskSettleInvstPosition__(pRiskSettleInvstPosition *CThostFtdcRiskSettleInvstPositionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryRiskSettleInvstPosition_ != nil {    
	    t.OnRspQryRiskSettleInvstPosition_(pRiskSettleInvstPosition, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 风险结算产品查询响应
func (t *Trade) OnRspQryRiskSettleProductStatus__(pRiskSettleProductStatus *CThostFtdcRiskSettleProductStatusField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryRiskSettleProductStatus_ != nil {    
	    t.OnRspQryRiskSettleProductStatus_(pRiskSettleProductStatus, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// SPBM期货合约参数查询响应
func (t *Trade) OnRspQrySPBMFutureParameter__(pSPBMFutureParameter *CThostFtdcSPBMFutureParameterField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQrySPBMFutureParameter_ != nil {    
	    t.OnRspQrySPBMFutureParameter_(pSPBMFutureParameter, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// SPBM期权合约参数查询响应
func (t *Trade) OnRspQrySPBMOptionParameter__(pSPBMOptionParameter *CThostFtdcSPBMOptionParameterField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQrySPBMOptionParameter_ != nil {    
	    t.OnRspQrySPBMOptionParameter_(pSPBMOptionParameter, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// SPBM品种内对锁仓折扣参数查询响应
func (t *Trade) OnRspQrySPBMIntraParameter__(pSPBMIntraParameter *CThostFtdcSPBMIntraParameterField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQrySPBMIntraParameter_ != nil {    
	    t.OnRspQrySPBMIntraParameter_(pSPBMIntraParameter, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// SPBM跨品种抵扣参数查询响应
func (t *Trade) OnRspQrySPBMInterParameter__(pSPBMInterParameter *CThostFtdcSPBMInterParameterField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQrySPBMInterParameter_ != nil {    
	    t.OnRspQrySPBMInterParameter_(pSPBMInterParameter, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// SPBM组合保证金套餐查询响应
func (t *Trade) OnRspQrySPBMPortfDefinition__(pSPBMPortfDefinition *CThostFtdcSPBMPortfDefinitionField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQrySPBMPortfDefinition_ != nil {    
	    t.OnRspQrySPBMPortfDefinition_(pSPBMPortfDefinition, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 投资者SPBM套餐选择查询响应
func (t *Trade) OnRspQrySPBMInvestorPortfDef__(pSPBMInvestorPortfDef *CThostFtdcSPBMInvestorPortfDefField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQrySPBMInvestorPortfDef_ != nil {    
	    t.OnRspQrySPBMInvestorPortfDef_(pSPBMInvestorPortfDef, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 投资者新型组合保证金系数查询响应
func (t *Trade) OnRspQryInvestorPortfMarginRatio__(pInvestorPortfMarginRatio *CThostFtdcInvestorPortfMarginRatioField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryInvestorPortfMarginRatio_ != nil {    
	    t.OnRspQryInvestorPortfMarginRatio_(pInvestorPortfMarginRatio, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}

// 投资者产品SPBM明细查询响应
func (t *Trade) OnRspQryInvestorProdSPBMDetail__(pInvestorProdSPBMDetail *CThostFtdcInvestorProdSPBMDetailField, pRspInfo *CThostFtdcRspInfoField, nRequestID int, bIsLast bool) uintptr {
    if t.OnRspQryInvestorProdSPBMDetail_ != nil {    
	    t.OnRspQryInvestorProdSPBMDetail_(pInvestorProdSPBMDetail, pRspInfo, nRequestID, bIsLast)
    }
	return 0
}
