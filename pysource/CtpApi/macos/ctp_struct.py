#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# LUX et VERITAS
# Create On: 2022/12/12 20:37:58


from ctypes import Structure
from .ctp_datatype import *


class  CThostFtdcDisseminationField(Structure):
    """信息分发"""
    _fields_ = [
        ("SequenceSeries", TThostFtdcSequenceSeriesType),
        ("SequenceNo", TThostFtdcSequenceNoType),
        
    ]
    
class  CThostFtdcReqUserLoginField(Structure):
    """用户登录请求"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("Password", TThostFtdcPasswordType),
        ("UserProductInfo", TThostFtdcProductInfoType),
        ("InterfaceProductInfo", TThostFtdcProductInfoType),
        ("ProtocolInfo", TThostFtdcProtocolInfoType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("OneTimePassword", TThostFtdcPasswordType),
        ("reserve1", TThostFtdcOldIPAddressType),
        ("LoginRemark", TThostFtdcLoginRemarkType),
        ("ClientIPPort", TThostFtdcIPPortType),
        ("ClientIPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcRspUserLoginField(Structure):
    """用户登录应答"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("LoginTime", TThostFtdcTimeType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("SystemName", TThostFtdcSystemNameType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("MaxOrderRef", TThostFtdcOrderRefType),
        ("SHFETime", TThostFtdcTimeType),
        ("DCETime", TThostFtdcTimeType),
        ("CZCETime", TThostFtdcTimeType),
        ("FFEXTime", TThostFtdcTimeType),
        ("INETime", TThostFtdcTimeType),
        ("SysVersion", TThostFtdcSysVersionType),
        ("GFEXTime", TThostFtdcTimeType),
        
    ]
    
class  CThostFtdcUserLogoutField(Structure):
    """用户登出请求"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        
    ]
    
class  CThostFtdcForceUserLogoutField(Structure):
    """强制交易员退出"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        
    ]
    
class  CThostFtdcReqAuthenticateField(Structure):
    """客户端认证请求"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("UserProductInfo", TThostFtdcProductInfoType),
        ("AuthCode", TThostFtdcAuthCodeType),
        ("AppID", TThostFtdcAppIDType),
        
    ]
    
class  CThostFtdcRspAuthenticateField(Structure):
    """客户端认证响应"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("UserProductInfo", TThostFtdcProductInfoType),
        ("AppID", TThostFtdcAppIDType),
        ("AppType", TThostFtdcAppTypeType),
        
    ]
    
class  CThostFtdcAuthenticationInfoField(Structure):
    """客户端认证信息"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("UserProductInfo", TThostFtdcProductInfoType),
        ("AuthInfo", TThostFtdcAuthInfoType),
        ("IsResult", TThostFtdcBoolType),
        ("AppID", TThostFtdcAppIDType),
        ("AppType", TThostFtdcAppTypeType),
        ("reserve1", TThostFtdcOldIPAddressType),
        ("ClientIPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcRspUserLogin2Field(Structure):
    """用户登录应答2"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("LoginTime", TThostFtdcTimeType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("SystemName", TThostFtdcSystemNameType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("MaxOrderRef", TThostFtdcOrderRefType),
        ("SHFETime", TThostFtdcTimeType),
        ("DCETime", TThostFtdcTimeType),
        ("CZCETime", TThostFtdcTimeType),
        ("FFEXTime", TThostFtdcTimeType),
        ("INETime", TThostFtdcTimeType),
        ("RandomString", TThostFtdcRandomStringType),
        
    ]
    
class  CThostFtdcTransferHeaderField(Structure):
    """银期转帐报文头"""
    _fields_ = [
        ("Version", TThostFtdcVersionType),
        ("TradeCode", TThostFtdcTradeCodeType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("TradeSerial", TThostFtdcTradeSerialType),
        ("FutureID", TThostFtdcFutureIDType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBrchID", TThostFtdcBankBrchIDType),
        ("OperNo", TThostFtdcOperNoType),
        ("DeviceID", TThostFtdcDeviceIDType),
        ("RecordNum", TThostFtdcRecordNumType),
        ("SessionID", TThostFtdcSessionIDType),
        ("RequestID", TThostFtdcRequestIDType),
        
    ]
    
class  CThostFtdcTransferBankToFutureReqField(Structure):
    """银行资金转期货请求，TradeCode=202001"""
    _fields_ = [
        ("FutureAccount", TThostFtdcAccountIDType),
        ("FuturePwdFlag", TThostFtdcFuturePwdFlagType),
        ("FutureAccPwd", TThostFtdcFutureAccPwdType),
        ("TradeAmt", TThostFtdcMoneyType),
        ("CustFee", TThostFtdcMoneyType),
        ("CurrencyCode", TThostFtdcCurrencyCodeType),
        
    ]
    
class  CThostFtdcTransferBankToFutureRspField(Structure):
    """银行资金转期货请求响应"""
    _fields_ = [
        ("RetCode", TThostFtdcRetCodeType),
        ("RetInfo", TThostFtdcRetInfoType),
        ("FutureAccount", TThostFtdcAccountIDType),
        ("TradeAmt", TThostFtdcMoneyType),
        ("CustFee", TThostFtdcMoneyType),
        ("CurrencyCode", TThostFtdcCurrencyCodeType),
        
    ]
    
class  CThostFtdcTransferFutureToBankReqField(Structure):
    """期货资金转银行请求，TradeCode=202002"""
    _fields_ = [
        ("FutureAccount", TThostFtdcAccountIDType),
        ("FuturePwdFlag", TThostFtdcFuturePwdFlagType),
        ("FutureAccPwd", TThostFtdcFutureAccPwdType),
        ("TradeAmt", TThostFtdcMoneyType),
        ("CustFee", TThostFtdcMoneyType),
        ("CurrencyCode", TThostFtdcCurrencyCodeType),
        
    ]
    
class  CThostFtdcTransferFutureToBankRspField(Structure):
    """期货资金转银行请求响应"""
    _fields_ = [
        ("RetCode", TThostFtdcRetCodeType),
        ("RetInfo", TThostFtdcRetInfoType),
        ("FutureAccount", TThostFtdcAccountIDType),
        ("TradeAmt", TThostFtdcMoneyType),
        ("CustFee", TThostFtdcMoneyType),
        ("CurrencyCode", TThostFtdcCurrencyCodeType),
        
    ]
    
class  CThostFtdcTransferQryBankReqField(Structure):
    """查询银行资金请求，TradeCode=204002"""
    _fields_ = [
        ("FutureAccount", TThostFtdcAccountIDType),
        ("FuturePwdFlag", TThostFtdcFuturePwdFlagType),
        ("FutureAccPwd", TThostFtdcFutureAccPwdType),
        ("CurrencyCode", TThostFtdcCurrencyCodeType),
        
    ]
    
class  CThostFtdcTransferQryBankRspField(Structure):
    """查询银行资金请求响应"""
    _fields_ = [
        ("RetCode", TThostFtdcRetCodeType),
        ("RetInfo", TThostFtdcRetInfoType),
        ("FutureAccount", TThostFtdcAccountIDType),
        ("TradeAmt", TThostFtdcMoneyType),
        ("UseAmt", TThostFtdcMoneyType),
        ("FetchAmt", TThostFtdcMoneyType),
        ("CurrencyCode", TThostFtdcCurrencyCodeType),
        
    ]
    
class  CThostFtdcTransferQryDetailReqField(Structure):
    """查询银行交易明细请求，TradeCode=204999"""
    _fields_ = [
        ("FutureAccount", TThostFtdcAccountIDType),
        
    ]
    
class  CThostFtdcTransferQryDetailRspField(Structure):
    """查询银行交易明细请求响应"""
    _fields_ = [
        ("TradeDate", TThostFtdcDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("TradeCode", TThostFtdcTradeCodeType),
        ("FutureSerial", TThostFtdcTradeSerialNoType),
        ("FutureID", TThostFtdcFutureIDType),
        ("FutureAccount", TThostFtdcFutureAccountType),
        ("BankSerial", TThostFtdcTradeSerialNoType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBrchID", TThostFtdcBankBrchIDType),
        ("BankAccount", TThostFtdcBankAccountType),
        ("CertCode", TThostFtdcCertCodeType),
        ("CurrencyCode", TThostFtdcCurrencyCodeType),
        ("TxAmount", TThostFtdcMoneyType),
        ("Flag", TThostFtdcTransferValidFlagType),
        
    ]
    
class  CThostFtdcRspInfoField(Structure):
    """响应信息"""
    _fields_ = [
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        
    ]
    
class  CThostFtdcExchangeField(Structure):
    """交易所"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ExchangeName", TThostFtdcExchangeNameType),
        ("ExchangeProperty", TThostFtdcExchangePropertyType),
        
    ]
    
class  CThostFtdcProductField(Structure):
    """产品"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ProductName", TThostFtdcProductNameType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ProductClass", TThostFtdcProductClassType),
        ("VolumeMultiple", TThostFtdcVolumeMultipleType),
        ("PriceTick", TThostFtdcPriceType),
        ("MaxMarketOrderVolume", TThostFtdcVolumeType),
        ("MinMarketOrderVolume", TThostFtdcVolumeType),
        ("MaxLimitOrderVolume", TThostFtdcVolumeType),
        ("MinLimitOrderVolume", TThostFtdcVolumeType),
        ("PositionType", TThostFtdcPositionTypeType),
        ("PositionDateType", TThostFtdcPositionDateTypeType),
        ("CloseDealType", TThostFtdcCloseDealTypeType),
        ("TradeCurrencyID", TThostFtdcCurrencyIDType),
        ("MortgageFundUseRange", TThostFtdcMortgageFundUseRangeType),
        ("reserve2", TThostFtdcOldInstrumentIDType),
        ("UnderlyingMultiple", TThostFtdcUnderlyingMultipleType),
        ("ProductID", TThostFtdcInstrumentIDType),
        ("ExchangeProductID", TThostFtdcInstrumentIDType),
        ("OpenLimitControlLevel", TThostFtdcOpenLimitControlLevelType),
        ("OrderFreqControlLevel", TThostFtdcOrderFreqControlLevelType),
        
    ]
    
class  CThostFtdcInstrumentField(Structure):
    """合约"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InstrumentName", TThostFtdcInstrumentNameType),
        ("reserve2", TThostFtdcOldExchangeInstIDType),
        ("reserve3", TThostFtdcOldInstrumentIDType),
        ("ProductClass", TThostFtdcProductClassType),
        ("DeliveryYear", TThostFtdcYearType),
        ("DeliveryMonth", TThostFtdcMonthType),
        ("MaxMarketOrderVolume", TThostFtdcVolumeType),
        ("MinMarketOrderVolume", TThostFtdcVolumeType),
        ("MaxLimitOrderVolume", TThostFtdcVolumeType),
        ("MinLimitOrderVolume", TThostFtdcVolumeType),
        ("VolumeMultiple", TThostFtdcVolumeMultipleType),
        ("PriceTick", TThostFtdcPriceType),
        ("CreateDate", TThostFtdcDateType),
        ("OpenDate", TThostFtdcDateType),
        ("ExpireDate", TThostFtdcDateType),
        ("StartDelivDate", TThostFtdcDateType),
        ("EndDelivDate", TThostFtdcDateType),
        ("InstLifePhase", TThostFtdcInstLifePhaseType),
        ("IsTrading", TThostFtdcBoolType),
        ("PositionType", TThostFtdcPositionTypeType),
        ("PositionDateType", TThostFtdcPositionDateTypeType),
        ("LongMarginRatio", TThostFtdcRatioType),
        ("ShortMarginRatio", TThostFtdcRatioType),
        ("MaxMarginSideAlgorithm", TThostFtdcMaxMarginSideAlgorithmType),
        ("reserve4", TThostFtdcOldInstrumentIDType),
        ("StrikePrice", TThostFtdcPriceType),
        ("OptionsType", TThostFtdcOptionsTypeType),
        ("UnderlyingMultiple", TThostFtdcUnderlyingMultipleType),
        ("CombinationType", TThostFtdcCombinationTypeType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        ("ProductID", TThostFtdcInstrumentIDType),
        ("UnderlyingInstrID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcBrokerField(Structure):
    """经纪公司"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerAbbr", TThostFtdcBrokerAbbrType),
        ("BrokerName", TThostFtdcBrokerNameType),
        ("IsActive", TThostFtdcBoolType),
        
    ]
    
class  CThostFtdcTraderField(Structure):
    """交易所交易员"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("Password", TThostFtdcPasswordType),
        ("InstallCount", TThostFtdcInstallCountType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("OrderCancelAlg", TThostFtdcOrderCancelAlgType),
        
    ]
    
class  CThostFtdcInvestorField(Structure):
    """投资者"""
    _fields_ = [
        ("InvestorID", TThostFtdcInvestorIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorGroupID", TThostFtdcInvestorIDType),
        ("InvestorName", TThostFtdcPartyNameType),
        ("IdentifiedCardType", TThostFtdcIdCardTypeType),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("IsActive", TThostFtdcBoolType),
        ("Telephone", TThostFtdcTelephoneType),
        ("Address", TThostFtdcAddressType),
        ("OpenDate", TThostFtdcDateType),
        ("Mobile", TThostFtdcMobileType),
        ("CommModelID", TThostFtdcInvestorIDType),
        ("MarginModelID", TThostFtdcInvestorIDType),
        ("IsOrderFreq", TThostFtdcEnumBoolType),
        ("IsOpenVolLimit", TThostFtdcEnumBoolType),
        
    ]
    
class  CThostFtdcTradingCodeField(Structure):
    """交易编码"""
    _fields_ = [
        ("InvestorID", TThostFtdcInvestorIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("IsActive", TThostFtdcBoolType),
        ("ClientIDType", TThostFtdcClientIDTypeType),
        ("BranchID", TThostFtdcBranchIDType),
        ("BizType", TThostFtdcBizTypeType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        
    ]
    
class  CThostFtdcPartBrokerField(Structure):
    """会员编码和经纪公司编码对照表"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("IsActive", TThostFtdcBoolType),
        
    ]
    
class  CThostFtdcSuperUserField(Structure):
    """管理用户"""
    _fields_ = [
        ("UserID", TThostFtdcUserIDType),
        ("UserName", TThostFtdcUserNameType),
        ("Password", TThostFtdcPasswordType),
        ("IsActive", TThostFtdcBoolType),
        
    ]
    
class  CThostFtdcSuperUserFunctionField(Structure):
    """管理用户功能权限"""
    _fields_ = [
        ("UserID", TThostFtdcUserIDType),
        ("FunctionCode", TThostFtdcFunctionCodeType),
        
    ]
    
class  CThostFtdcInvestorGroupField(Structure):
    """投资者组"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorGroupID", TThostFtdcInvestorIDType),
        ("InvestorGroupName", TThostFtdcInvestorGroupNameType),
        
    ]
    
class  CThostFtdcTradingAccountField(Structure):
    """资金账户"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("PreMortgage", TThostFtdcMoneyType),
        ("PreCredit", TThostFtdcMoneyType),
        ("PreDeposit", TThostFtdcMoneyType),
        ("PreBalance", TThostFtdcMoneyType),
        ("PreMargin", TThostFtdcMoneyType),
        ("InterestBase", TThostFtdcMoneyType),
        ("Interest", TThostFtdcMoneyType),
        ("Deposit", TThostFtdcMoneyType),
        ("Withdraw", TThostFtdcMoneyType),
        ("FrozenMargin", TThostFtdcMoneyType),
        ("FrozenCash", TThostFtdcMoneyType),
        ("FrozenCommission", TThostFtdcMoneyType),
        ("CurrMargin", TThostFtdcMoneyType),
        ("CashIn", TThostFtdcMoneyType),
        ("Commission", TThostFtdcMoneyType),
        ("CloseProfit", TThostFtdcMoneyType),
        ("PositionProfit", TThostFtdcMoneyType),
        ("Balance", TThostFtdcMoneyType),
        ("Available", TThostFtdcMoneyType),
        ("WithdrawQuota", TThostFtdcMoneyType),
        ("Reserve", TThostFtdcMoneyType),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("Credit", TThostFtdcMoneyType),
        ("Mortgage", TThostFtdcMoneyType),
        ("ExchangeMargin", TThostFtdcMoneyType),
        ("DeliveryMargin", TThostFtdcMoneyType),
        ("ExchangeDeliveryMargin", TThostFtdcMoneyType),
        ("ReserveBalance", TThostFtdcMoneyType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("PreFundMortgageIn", TThostFtdcMoneyType),
        ("PreFundMortgageOut", TThostFtdcMoneyType),
        ("FundMortgageIn", TThostFtdcMoneyType),
        ("FundMortgageOut", TThostFtdcMoneyType),
        ("FundMortgageAvailable", TThostFtdcMoneyType),
        ("MortgageableFund", TThostFtdcMoneyType),
        ("SpecProductMargin", TThostFtdcMoneyType),
        ("SpecProductFrozenMargin", TThostFtdcMoneyType),
        ("SpecProductCommission", TThostFtdcMoneyType),
        ("SpecProductFrozenCommission", TThostFtdcMoneyType),
        ("SpecProductPositionProfit", TThostFtdcMoneyType),
        ("SpecProductCloseProfit", TThostFtdcMoneyType),
        ("SpecProductPositionProfitByAlg", TThostFtdcMoneyType),
        ("SpecProductExchangeMargin", TThostFtdcMoneyType),
        ("BizType", TThostFtdcBizTypeType),
        ("FrozenSwap", TThostFtdcMoneyType),
        ("RemainSwap", TThostFtdcMoneyType),
        
    ]
    
class  CThostFtdcInvestorPositionField(Structure):
    """投资者持仓"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("PosiDirection", TThostFtdcPosiDirectionType),
        ("HedgeFlag", TThostFtdcHedgeFlagType),
        ("PositionDate", TThostFtdcPositionDateType),
        ("YdPosition", TThostFtdcVolumeType),
        ("Position", TThostFtdcVolumeType),
        ("LongFrozen", TThostFtdcVolumeType),
        ("ShortFrozen", TThostFtdcVolumeType),
        ("LongFrozenAmount", TThostFtdcMoneyType),
        ("ShortFrozenAmount", TThostFtdcMoneyType),
        ("OpenVolume", TThostFtdcVolumeType),
        ("CloseVolume", TThostFtdcVolumeType),
        ("OpenAmount", TThostFtdcMoneyType),
        ("CloseAmount", TThostFtdcMoneyType),
        ("PositionCost", TThostFtdcMoneyType),
        ("PreMargin", TThostFtdcMoneyType),
        ("UseMargin", TThostFtdcMoneyType),
        ("FrozenMargin", TThostFtdcMoneyType),
        ("FrozenCash", TThostFtdcMoneyType),
        ("FrozenCommission", TThostFtdcMoneyType),
        ("CashIn", TThostFtdcMoneyType),
        ("Commission", TThostFtdcMoneyType),
        ("CloseProfit", TThostFtdcMoneyType),
        ("PositionProfit", TThostFtdcMoneyType),
        ("PreSettlementPrice", TThostFtdcPriceType),
        ("SettlementPrice", TThostFtdcPriceType),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("OpenCost", TThostFtdcMoneyType),
        ("ExchangeMargin", TThostFtdcMoneyType),
        ("CombPosition", TThostFtdcVolumeType),
        ("CombLongFrozen", TThostFtdcVolumeType),
        ("CombShortFrozen", TThostFtdcVolumeType),
        ("CloseProfitByDate", TThostFtdcMoneyType),
        ("CloseProfitByTrade", TThostFtdcMoneyType),
        ("TodayPosition", TThostFtdcVolumeType),
        ("MarginRateByMoney", TThostFtdcRatioType),
        ("MarginRateByVolume", TThostFtdcRatioType),
        ("StrikeFrozen", TThostFtdcVolumeType),
        ("StrikeFrozenAmount", TThostFtdcMoneyType),
        ("AbandonFrozen", TThostFtdcVolumeType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("YdStrikeFrozen", TThostFtdcVolumeType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("PositionCostOffset", TThostFtdcMoneyType),
        ("TasPosition", TThostFtdcVolumeType),
        ("TasPositionCost", TThostFtdcMoneyType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcInstrumentMarginRateField(Structure):
    """合约保证金率"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestorRange", TThostFtdcInvestorRangeType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("HedgeFlag", TThostFtdcHedgeFlagType),
        ("LongMarginRatioByMoney", TThostFtdcRatioType),
        ("LongMarginRatioByVolume", TThostFtdcMoneyType),
        ("ShortMarginRatioByMoney", TThostFtdcRatioType),
        ("ShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("IsRelative", TThostFtdcBoolType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcInstrumentCommissionRateField(Structure):
    """合约手续费率"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestorRange", TThostFtdcInvestorRangeType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("OpenRatioByMoney", TThostFtdcRatioType),
        ("OpenRatioByVolume", TThostFtdcRatioType),
        ("CloseRatioByMoney", TThostFtdcRatioType),
        ("CloseRatioByVolume", TThostFtdcRatioType),
        ("CloseTodayRatioByMoney", TThostFtdcRatioType),
        ("CloseTodayRatioByVolume", TThostFtdcRatioType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("BizType", TThostFtdcBizTypeType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcDepthMarketDataField(Structure):
    """深度行情"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("reserve2", TThostFtdcOldExchangeInstIDType),
        ("LastPrice", TThostFtdcPriceType),
        ("PreSettlementPrice", TThostFtdcPriceType),
        ("PreClosePrice", TThostFtdcPriceType),
        ("PreOpenInterest", TThostFtdcLargeVolumeType),
        ("OpenPrice", TThostFtdcPriceType),
        ("HighestPrice", TThostFtdcPriceType),
        ("LowestPrice", TThostFtdcPriceType),
        ("Volume", TThostFtdcVolumeType),
        ("Turnover", TThostFtdcMoneyType),
        ("OpenInterest", TThostFtdcLargeVolumeType),
        ("ClosePrice", TThostFtdcPriceType),
        ("SettlementPrice", TThostFtdcPriceType),
        ("UpperLimitPrice", TThostFtdcPriceType),
        ("LowerLimitPrice", TThostFtdcPriceType),
        ("PreDelta", TThostFtdcRatioType),
        ("CurrDelta", TThostFtdcRatioType),
        ("UpdateTime", TThostFtdcTimeType),
        ("UpdateMillisec", TThostFtdcMillisecType),
        ("BidPrice1", TThostFtdcPriceType),
        ("BidVolume1", TThostFtdcVolumeType),
        ("AskPrice1", TThostFtdcPriceType),
        ("AskVolume1", TThostFtdcVolumeType),
        ("BidPrice2", TThostFtdcPriceType),
        ("BidVolume2", TThostFtdcVolumeType),
        ("AskPrice2", TThostFtdcPriceType),
        ("AskVolume2", TThostFtdcVolumeType),
        ("BidPrice3", TThostFtdcPriceType),
        ("BidVolume3", TThostFtdcVolumeType),
        ("AskPrice3", TThostFtdcPriceType),
        ("AskVolume3", TThostFtdcVolumeType),
        ("BidPrice4", TThostFtdcPriceType),
        ("BidVolume4", TThostFtdcVolumeType),
        ("AskPrice4", TThostFtdcPriceType),
        ("AskVolume4", TThostFtdcVolumeType),
        ("BidPrice5", TThostFtdcPriceType),
        ("BidVolume5", TThostFtdcVolumeType),
        ("AskPrice5", TThostFtdcPriceType),
        ("AskVolume5", TThostFtdcVolumeType),
        ("AveragePrice", TThostFtdcPriceType),
        ("ActionDay", TThostFtdcDateType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        ("BandingUpperPrice", TThostFtdcPriceType),
        ("BandingLowerPrice", TThostFtdcPriceType),
        
    ]
    
class  CThostFtdcInstrumentTradingRightField(Structure):
    """投资者合约交易权限"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestorRange", TThostFtdcInvestorRangeType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("TradingRight", TThostFtdcTradingRightType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcBrokerUserField(Structure):
    """经纪公司用户"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("UserName", TThostFtdcUserNameType),
        ("UserType", TThostFtdcUserTypeType),
        ("IsActive", TThostFtdcBoolType),
        ("IsUsingOTP", TThostFtdcBoolType),
        ("IsAuthForce", TThostFtdcBoolType),
        
    ]
    
class  CThostFtdcBrokerUserPasswordField(Structure):
    """经纪公司用户口令"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("Password", TThostFtdcPasswordType),
        ("LastUpdateTime", TThostFtdcDateTimeType),
        ("LastLoginTime", TThostFtdcDateTimeType),
        ("ExpireDate", TThostFtdcDateType),
        ("WeakExpireDate", TThostFtdcDateType),
        
    ]
    
class  CThostFtdcBrokerUserFunctionField(Structure):
    """经纪公司用户功能权限"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("BrokerFunctionCode", TThostFtdcBrokerFunctionCodeType),
        
    ]
    
class  CThostFtdcTraderOfferField(Structure):
    """交易所交易员报盘机"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("Password", TThostFtdcPasswordType),
        ("InstallID", TThostFtdcInstallIDType),
        ("OrderLocalID", TThostFtdcOrderLocalIDType),
        ("TraderConnectStatus", TThostFtdcTraderConnectStatusType),
        ("ConnectRequestDate", TThostFtdcDateType),
        ("ConnectRequestTime", TThostFtdcTimeType),
        ("LastReportDate", TThostFtdcDateType),
        ("LastReportTime", TThostFtdcTimeType),
        ("ConnectDate", TThostFtdcDateType),
        ("ConnectTime", TThostFtdcTimeType),
        ("StartDate", TThostFtdcDateType),
        ("StartTime", TThostFtdcTimeType),
        ("TradingDay", TThostFtdcDateType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("MaxTradeID", TThostFtdcTradeIDType),
        ("MaxOrderMessageReference", TThostFtdcReturnCodeType),
        ("OrderCancelAlg", TThostFtdcOrderCancelAlgType),
        
    ]
    
class  CThostFtdcSettlementInfoField(Structure):
    """投资者结算结果"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("SequenceNo", TThostFtdcSequenceNoType),
        ("Content", TThostFtdcContentType),
        ("AccountID", TThostFtdcAccountIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        
    ]
    
class  CThostFtdcInstrumentMarginRateAdjustField(Structure):
    """合约保证金率调整"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestorRange", TThostFtdcInvestorRangeType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("HedgeFlag", TThostFtdcHedgeFlagType),
        ("LongMarginRatioByMoney", TThostFtdcRatioType),
        ("LongMarginRatioByVolume", TThostFtdcMoneyType),
        ("ShortMarginRatioByMoney", TThostFtdcRatioType),
        ("ShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("IsRelative", TThostFtdcBoolType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcExchangeMarginRateField(Structure):
    """交易所保证金率"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("HedgeFlag", TThostFtdcHedgeFlagType),
        ("LongMarginRatioByMoney", TThostFtdcRatioType),
        ("LongMarginRatioByVolume", TThostFtdcMoneyType),
        ("ShortMarginRatioByMoney", TThostFtdcRatioType),
        ("ShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcExchangeMarginRateAdjustField(Structure):
    """交易所保证金率调整"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("HedgeFlag", TThostFtdcHedgeFlagType),
        ("LongMarginRatioByMoney", TThostFtdcRatioType),
        ("LongMarginRatioByVolume", TThostFtdcMoneyType),
        ("ShortMarginRatioByMoney", TThostFtdcRatioType),
        ("ShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("ExchLongMarginRatioByMoney", TThostFtdcRatioType),
        ("ExchLongMarginRatioByVolume", TThostFtdcMoneyType),
        ("ExchShortMarginRatioByMoney", TThostFtdcRatioType),
        ("ExchShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("NoLongMarginRatioByMoney", TThostFtdcRatioType),
        ("NoLongMarginRatioByVolume", TThostFtdcMoneyType),
        ("NoShortMarginRatioByMoney", TThostFtdcRatioType),
        ("NoShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcExchangeRateField(Structure):
    """汇率"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("FromCurrencyID", TThostFtdcCurrencyIDType),
        ("FromCurrencyUnit", TThostFtdcCurrencyUnitType),
        ("ToCurrencyID", TThostFtdcCurrencyIDType),
        ("ExchangeRate", TThostFtdcExchangeRateType),
        
    ]
    
class  CThostFtdcSettlementRefField(Structure):
    """结算引用"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        
    ]
    
class  CThostFtdcCurrentTimeField(Structure):
    """当前时间"""
    _fields_ = [
        ("CurrDate", TThostFtdcDateType),
        ("CurrTime", TThostFtdcTimeType),
        ("CurrMillisec", TThostFtdcMillisecType),
        ("ActionDay", TThostFtdcDateType),
        
    ]
    
class  CThostFtdcCommPhaseField(Structure):
    """通讯阶段"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("CommPhaseNo", TThostFtdcCommPhaseNoType),
        ("SystemID", TThostFtdcSystemIDType),
        
    ]
    
class  CThostFtdcLoginInfoField(Structure):
    """登录信息"""
    _fields_ = [
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("LoginDate", TThostFtdcDateType),
        ("LoginTime", TThostFtdcTimeType),
        ("reserve1", TThostFtdcOldIPAddressType),
        ("UserProductInfo", TThostFtdcProductInfoType),
        ("InterfaceProductInfo", TThostFtdcProductInfoType),
        ("ProtocolInfo", TThostFtdcProtocolInfoType),
        ("SystemName", TThostFtdcSystemNameType),
        ("PasswordDeprecated", TThostFtdcPasswordType),
        ("MaxOrderRef", TThostFtdcOrderRefType),
        ("SHFETime", TThostFtdcTimeType),
        ("DCETime", TThostFtdcTimeType),
        ("CZCETime", TThostFtdcTimeType),
        ("FFEXTime", TThostFtdcTimeType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("OneTimePassword", TThostFtdcPasswordType),
        ("INETime", TThostFtdcTimeType),
        ("IsQryControl", TThostFtdcBoolType),
        ("LoginRemark", TThostFtdcLoginRemarkType),
        ("Password", TThostFtdcPasswordType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcLogoutAllField(Structure):
    """登录信息"""
    _fields_ = [
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("SystemName", TThostFtdcSystemNameType),
        
    ]
    
class  CThostFtdcFrontStatusField(Structure):
    """前置状态"""
    _fields_ = [
        ("FrontID", TThostFtdcFrontIDType),
        ("LastReportDate", TThostFtdcDateType),
        ("LastReportTime", TThostFtdcTimeType),
        ("IsActive", TThostFtdcBoolType),
        
    ]
    
class  CThostFtdcUserPasswordUpdateField(Structure):
    """用户口令变更"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("OldPassword", TThostFtdcPasswordType),
        ("NewPassword", TThostFtdcPasswordType),
        
    ]
    
class  CThostFtdcInputOrderField(Structure):
    """输入报单"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("OrderRef", TThostFtdcOrderRefType),
        ("UserID", TThostFtdcUserIDType),
        ("OrderPriceType", TThostFtdcOrderPriceTypeType),
        ("Direction", TThostFtdcDirectionType),
        ("CombOffsetFlag", TThostFtdcCombOffsetFlagType),
        ("CombHedgeFlag", TThostFtdcCombHedgeFlagType),
        ("LimitPrice", TThostFtdcPriceType),
        ("VolumeTotalOriginal", TThostFtdcVolumeType),
        ("TimeCondition", TThostFtdcTimeConditionType),
        ("GTDDate", TThostFtdcDateType),
        ("VolumeCondition", TThostFtdcVolumeConditionType),
        ("MinVolume", TThostFtdcVolumeType),
        ("ContingentCondition", TThostFtdcContingentConditionType),
        ("StopPrice", TThostFtdcPriceType),
        ("ForceCloseReason", TThostFtdcForceCloseReasonType),
        ("IsAutoSuspend", TThostFtdcBoolType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("RequestID", TThostFtdcRequestIDType),
        ("UserForceClose", TThostFtdcBoolType),
        ("IsSwapOrder", TThostFtdcBoolType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcOrderField(Structure):
    """报单"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("OrderRef", TThostFtdcOrderRefType),
        ("UserID", TThostFtdcUserIDType),
        ("OrderPriceType", TThostFtdcOrderPriceTypeType),
        ("Direction", TThostFtdcDirectionType),
        ("CombOffsetFlag", TThostFtdcCombOffsetFlagType),
        ("CombHedgeFlag", TThostFtdcCombHedgeFlagType),
        ("LimitPrice", TThostFtdcPriceType),
        ("VolumeTotalOriginal", TThostFtdcVolumeType),
        ("TimeCondition", TThostFtdcTimeConditionType),
        ("GTDDate", TThostFtdcDateType),
        ("VolumeCondition", TThostFtdcVolumeConditionType),
        ("MinVolume", TThostFtdcVolumeType),
        ("ContingentCondition", TThostFtdcContingentConditionType),
        ("StopPrice", TThostFtdcPriceType),
        ("ForceCloseReason", TThostFtdcForceCloseReasonType),
        ("IsAutoSuspend", TThostFtdcBoolType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("RequestID", TThostFtdcRequestIDType),
        ("OrderLocalID", TThostFtdcOrderLocalIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve2", TThostFtdcOldExchangeInstIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("OrderSubmitStatus", TThostFtdcOrderSubmitStatusType),
        ("NotifySequence", TThostFtdcSequenceNoType),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("OrderSysID", TThostFtdcOrderSysIDType),
        ("OrderSource", TThostFtdcOrderSourceType),
        ("OrderStatus", TThostFtdcOrderStatusType),
        ("OrderType", TThostFtdcOrderTypeType),
        ("VolumeTraded", TThostFtdcVolumeType),
        ("VolumeTotal", TThostFtdcVolumeType),
        ("InsertDate", TThostFtdcDateType),
        ("InsertTime", TThostFtdcTimeType),
        ("ActiveTime", TThostFtdcTimeType),
        ("SuspendTime", TThostFtdcTimeType),
        ("UpdateTime", TThostFtdcTimeType),
        ("CancelTime", TThostFtdcTimeType),
        ("ActiveTraderID", TThostFtdcTraderIDType),
        ("ClearingPartID", TThostFtdcParticipantIDType),
        ("SequenceNo", TThostFtdcSequenceNoType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("UserProductInfo", TThostFtdcProductInfoType),
        ("StatusMsg", TThostFtdcErrorMsgType),
        ("UserForceClose", TThostFtdcBoolType),
        ("ActiveUserID", TThostFtdcUserIDType),
        ("BrokerOrderSeq", TThostFtdcSequenceNoType),
        ("RelativeOrderSysID", TThostFtdcOrderSysIDType),
        ("ZCETotalTradedVolume", TThostFtdcVolumeType),
        ("IsSwapOrder", TThostFtdcBoolType),
        ("BranchID", TThostFtdcBranchIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("reserve3", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcExchangeOrderField(Structure):
    """交易所报单"""
    _fields_ = [
        ("OrderPriceType", TThostFtdcOrderPriceTypeType),
        ("Direction", TThostFtdcDirectionType),
        ("CombOffsetFlag", TThostFtdcCombOffsetFlagType),
        ("CombHedgeFlag", TThostFtdcCombHedgeFlagType),
        ("LimitPrice", TThostFtdcPriceType),
        ("VolumeTotalOriginal", TThostFtdcVolumeType),
        ("TimeCondition", TThostFtdcTimeConditionType),
        ("GTDDate", TThostFtdcDateType),
        ("VolumeCondition", TThostFtdcVolumeConditionType),
        ("MinVolume", TThostFtdcVolumeType),
        ("ContingentCondition", TThostFtdcContingentConditionType),
        ("StopPrice", TThostFtdcPriceType),
        ("ForceCloseReason", TThostFtdcForceCloseReasonType),
        ("IsAutoSuspend", TThostFtdcBoolType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("RequestID", TThostFtdcRequestIDType),
        ("OrderLocalID", TThostFtdcOrderLocalIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve1", TThostFtdcOldExchangeInstIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("OrderSubmitStatus", TThostFtdcOrderSubmitStatusType),
        ("NotifySequence", TThostFtdcSequenceNoType),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("OrderSysID", TThostFtdcOrderSysIDType),
        ("OrderSource", TThostFtdcOrderSourceType),
        ("OrderStatus", TThostFtdcOrderStatusType),
        ("OrderType", TThostFtdcOrderTypeType),
        ("VolumeTraded", TThostFtdcVolumeType),
        ("VolumeTotal", TThostFtdcVolumeType),
        ("InsertDate", TThostFtdcDateType),
        ("InsertTime", TThostFtdcTimeType),
        ("ActiveTime", TThostFtdcTimeType),
        ("SuspendTime", TThostFtdcTimeType),
        ("UpdateTime", TThostFtdcTimeType),
        ("CancelTime", TThostFtdcTimeType),
        ("ActiveTraderID", TThostFtdcTraderIDType),
        ("ClearingPartID", TThostFtdcParticipantIDType),
        ("SequenceNo", TThostFtdcSequenceNoType),
        ("BranchID", TThostFtdcBranchIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcExchangeOrderInsertErrorField(Structure):
    """交易所报单插入失败"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("OrderLocalID", TThostFtdcOrderLocalIDType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        
    ]
    
class  CThostFtdcInputOrderActionField(Structure):
    """输入报单操作"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("OrderActionRef", TThostFtdcOrderActionRefType),
        ("OrderRef", TThostFtdcOrderRefType),
        ("RequestID", TThostFtdcRequestIDType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("OrderSysID", TThostFtdcOrderSysIDType),
        ("ActionFlag", TThostFtdcActionFlagType),
        ("LimitPrice", TThostFtdcPriceType),
        ("VolumeChange", TThostFtdcVolumeType),
        ("UserID", TThostFtdcUserIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcOrderActionField(Structure):
    """报单操作"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("OrderActionRef", TThostFtdcOrderActionRefType),
        ("OrderRef", TThostFtdcOrderRefType),
        ("RequestID", TThostFtdcRequestIDType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("OrderSysID", TThostFtdcOrderSysIDType),
        ("ActionFlag", TThostFtdcActionFlagType),
        ("LimitPrice", TThostFtdcPriceType),
        ("VolumeChange", TThostFtdcVolumeType),
        ("ActionDate", TThostFtdcDateType),
        ("ActionTime", TThostFtdcTimeType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("OrderLocalID", TThostFtdcOrderLocalIDType),
        ("ActionLocalID", TThostFtdcOrderLocalIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("OrderActionStatus", TThostFtdcOrderActionStatusType),
        ("UserID", TThostFtdcUserIDType),
        ("StatusMsg", TThostFtdcErrorMsgType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("BranchID", TThostFtdcBranchIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcExchangeOrderActionField(Structure):
    """交易所报单操作"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("OrderSysID", TThostFtdcOrderSysIDType),
        ("ActionFlag", TThostFtdcActionFlagType),
        ("LimitPrice", TThostFtdcPriceType),
        ("VolumeChange", TThostFtdcVolumeType),
        ("ActionDate", TThostFtdcDateType),
        ("ActionTime", TThostFtdcTimeType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("OrderLocalID", TThostFtdcOrderLocalIDType),
        ("ActionLocalID", TThostFtdcOrderLocalIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("OrderActionStatus", TThostFtdcOrderActionStatusType),
        ("UserID", TThostFtdcUserIDType),
        ("BranchID", TThostFtdcBranchIDType),
        ("reserve1", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcExchangeOrderActionErrorField(Structure):
    """交易所报单操作失败"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("OrderSysID", TThostFtdcOrderSysIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("OrderLocalID", TThostFtdcOrderLocalIDType),
        ("ActionLocalID", TThostFtdcOrderLocalIDType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        
    ]
    
class  CThostFtdcExchangeTradeField(Structure):
    """交易所成交"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("TradeID", TThostFtdcTradeIDType),
        ("Direction", TThostFtdcDirectionType),
        ("OrderSysID", TThostFtdcOrderSysIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("TradingRole", TThostFtdcTradingRoleType),
        ("reserve1", TThostFtdcOldExchangeInstIDType),
        ("OffsetFlag", TThostFtdcOffsetFlagType),
        ("HedgeFlag", TThostFtdcHedgeFlagType),
        ("Price", TThostFtdcPriceType),
        ("Volume", TThostFtdcVolumeType),
        ("TradeDate", TThostFtdcDateType),
        ("TradeTime", TThostFtdcTimeType),
        ("TradeType", TThostFtdcTradeTypeType),
        ("PriceSource", TThostFtdcPriceSourceType),
        ("TraderID", TThostFtdcTraderIDType),
        ("OrderLocalID", TThostFtdcOrderLocalIDType),
        ("ClearingPartID", TThostFtdcParticipantIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("SequenceNo", TThostFtdcSequenceNoType),
        ("TradeSource", TThostFtdcTradeSourceType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        
    ]
    
class  CThostFtdcTradeField(Structure):
    """成交"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("OrderRef", TThostFtdcOrderRefType),
        ("UserID", TThostFtdcUserIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("TradeID", TThostFtdcTradeIDType),
        ("Direction", TThostFtdcDirectionType),
        ("OrderSysID", TThostFtdcOrderSysIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("TradingRole", TThostFtdcTradingRoleType),
        ("reserve2", TThostFtdcOldExchangeInstIDType),
        ("OffsetFlag", TThostFtdcOffsetFlagType),
        ("HedgeFlag", TThostFtdcHedgeFlagType),
        ("Price", TThostFtdcPriceType),
        ("Volume", TThostFtdcVolumeType),
        ("TradeDate", TThostFtdcDateType),
        ("TradeTime", TThostFtdcTimeType),
        ("TradeType", TThostFtdcTradeTypeType),
        ("PriceSource", TThostFtdcPriceSourceType),
        ("TraderID", TThostFtdcTraderIDType),
        ("OrderLocalID", TThostFtdcOrderLocalIDType),
        ("ClearingPartID", TThostFtdcParticipantIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("SequenceNo", TThostFtdcSequenceNoType),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("BrokerOrderSeq", TThostFtdcSequenceNoType),
        ("TradeSource", TThostFtdcTradeSourceType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        
    ]
    
class  CThostFtdcUserSessionField(Structure):
    """用户会话"""
    _fields_ = [
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("LoginDate", TThostFtdcDateType),
        ("LoginTime", TThostFtdcTimeType),
        ("reserve1", TThostFtdcOldIPAddressType),
        ("UserProductInfo", TThostFtdcProductInfoType),
        ("InterfaceProductInfo", TThostFtdcProductInfoType),
        ("ProtocolInfo", TThostFtdcProtocolInfoType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("LoginRemark", TThostFtdcLoginRemarkType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcQryMaxOrderVolumeField(Structure):
    """查询最大报单数量"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("Direction", TThostFtdcDirectionType),
        ("OffsetFlag", TThostFtdcOffsetFlagType),
        ("HedgeFlag", TThostFtdcHedgeFlagType),
        ("MaxVolume", TThostFtdcVolumeType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcSettlementInfoConfirmField(Structure):
    """投资者结算结果确认信息"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("ConfirmDate", TThostFtdcDateType),
        ("ConfirmTime", TThostFtdcTimeType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        
    ]
    
class  CThostFtdcSyncDepositField(Structure):
    """出入金同步"""
    _fields_ = [
        ("DepositSeqNo", TThostFtdcDepositSeqNoType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("Deposit", TThostFtdcMoneyType),
        ("IsForce", TThostFtdcBoolType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("IsFromSopt", TThostFtdcBoolType),
        ("TradingPassword", TThostFtdcPasswordType),
        
    ]
    
class  CThostFtdcSyncFundMortgageField(Structure):
    """货币质押同步"""
    _fields_ = [
        ("MortgageSeqNo", TThostFtdcDepositSeqNoType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("FromCurrencyID", TThostFtdcCurrencyIDType),
        ("MortgageAmount", TThostFtdcMoneyType),
        ("ToCurrencyID", TThostFtdcCurrencyIDType),
        
    ]
    
class  CThostFtdcBrokerSyncField(Structure):
    """经纪公司同步"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        
    ]
    
class  CThostFtdcSyncingInvestorField(Structure):
    """正在同步中的投资者"""
    _fields_ = [
        ("InvestorID", TThostFtdcInvestorIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorGroupID", TThostFtdcInvestorIDType),
        ("InvestorName", TThostFtdcPartyNameType),
        ("IdentifiedCardType", TThostFtdcIdCardTypeType),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("IsActive", TThostFtdcBoolType),
        ("Telephone", TThostFtdcTelephoneType),
        ("Address", TThostFtdcAddressType),
        ("OpenDate", TThostFtdcDateType),
        ("Mobile", TThostFtdcMobileType),
        ("CommModelID", TThostFtdcInvestorIDType),
        ("MarginModelID", TThostFtdcInvestorIDType),
        ("IsOrderFreq", TThostFtdcEnumBoolType),
        ("IsOpenVolLimit", TThostFtdcEnumBoolType),
        
    ]
    
class  CThostFtdcSyncingTradingCodeField(Structure):
    """正在同步中的交易代码"""
    _fields_ = [
        ("InvestorID", TThostFtdcInvestorIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("IsActive", TThostFtdcBoolType),
        ("ClientIDType", TThostFtdcClientIDTypeType),
        
    ]
    
class  CThostFtdcSyncingInvestorGroupField(Structure):
    """正在同步中的投资者分组"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorGroupID", TThostFtdcInvestorIDType),
        ("InvestorGroupName", TThostFtdcInvestorGroupNameType),
        
    ]
    
class  CThostFtdcSyncingTradingAccountField(Structure):
    """正在同步中的交易账号"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("PreMortgage", TThostFtdcMoneyType),
        ("PreCredit", TThostFtdcMoneyType),
        ("PreDeposit", TThostFtdcMoneyType),
        ("PreBalance", TThostFtdcMoneyType),
        ("PreMargin", TThostFtdcMoneyType),
        ("InterestBase", TThostFtdcMoneyType),
        ("Interest", TThostFtdcMoneyType),
        ("Deposit", TThostFtdcMoneyType),
        ("Withdraw", TThostFtdcMoneyType),
        ("FrozenMargin", TThostFtdcMoneyType),
        ("FrozenCash", TThostFtdcMoneyType),
        ("FrozenCommission", TThostFtdcMoneyType),
        ("CurrMargin", TThostFtdcMoneyType),
        ("CashIn", TThostFtdcMoneyType),
        ("Commission", TThostFtdcMoneyType),
        ("CloseProfit", TThostFtdcMoneyType),
        ("PositionProfit", TThostFtdcMoneyType),
        ("Balance", TThostFtdcMoneyType),
        ("Available", TThostFtdcMoneyType),
        ("WithdrawQuota", TThostFtdcMoneyType),
        ("Reserve", TThostFtdcMoneyType),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("Credit", TThostFtdcMoneyType),
        ("Mortgage", TThostFtdcMoneyType),
        ("ExchangeMargin", TThostFtdcMoneyType),
        ("DeliveryMargin", TThostFtdcMoneyType),
        ("ExchangeDeliveryMargin", TThostFtdcMoneyType),
        ("ReserveBalance", TThostFtdcMoneyType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("PreFundMortgageIn", TThostFtdcMoneyType),
        ("PreFundMortgageOut", TThostFtdcMoneyType),
        ("FundMortgageIn", TThostFtdcMoneyType),
        ("FundMortgageOut", TThostFtdcMoneyType),
        ("FundMortgageAvailable", TThostFtdcMoneyType),
        ("MortgageableFund", TThostFtdcMoneyType),
        ("SpecProductMargin", TThostFtdcMoneyType),
        ("SpecProductFrozenMargin", TThostFtdcMoneyType),
        ("SpecProductCommission", TThostFtdcMoneyType),
        ("SpecProductFrozenCommission", TThostFtdcMoneyType),
        ("SpecProductPositionProfit", TThostFtdcMoneyType),
        ("SpecProductCloseProfit", TThostFtdcMoneyType),
        ("SpecProductPositionProfitByAlg", TThostFtdcMoneyType),
        ("SpecProductExchangeMargin", TThostFtdcMoneyType),
        ("FrozenSwap", TThostFtdcMoneyType),
        ("RemainSwap", TThostFtdcMoneyType),
        
    ]
    
class  CThostFtdcSyncingInvestorPositionField(Structure):
    """正在同步中的投资者持仓"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("PosiDirection", TThostFtdcPosiDirectionType),
        ("HedgeFlag", TThostFtdcHedgeFlagType),
        ("PositionDate", TThostFtdcPositionDateType),
        ("YdPosition", TThostFtdcVolumeType),
        ("Position", TThostFtdcVolumeType),
        ("LongFrozen", TThostFtdcVolumeType),
        ("ShortFrozen", TThostFtdcVolumeType),
        ("LongFrozenAmount", TThostFtdcMoneyType),
        ("ShortFrozenAmount", TThostFtdcMoneyType),
        ("OpenVolume", TThostFtdcVolumeType),
        ("CloseVolume", TThostFtdcVolumeType),
        ("OpenAmount", TThostFtdcMoneyType),
        ("CloseAmount", TThostFtdcMoneyType),
        ("PositionCost", TThostFtdcMoneyType),
        ("PreMargin", TThostFtdcMoneyType),
        ("UseMargin", TThostFtdcMoneyType),
        ("FrozenMargin", TThostFtdcMoneyType),
        ("FrozenCash", TThostFtdcMoneyType),
        ("FrozenCommission", TThostFtdcMoneyType),
        ("CashIn", TThostFtdcMoneyType),
        ("Commission", TThostFtdcMoneyType),
        ("CloseProfit", TThostFtdcMoneyType),
        ("PositionProfit", TThostFtdcMoneyType),
        ("PreSettlementPrice", TThostFtdcPriceType),
        ("SettlementPrice", TThostFtdcPriceType),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("OpenCost", TThostFtdcMoneyType),
        ("ExchangeMargin", TThostFtdcMoneyType),
        ("CombPosition", TThostFtdcVolumeType),
        ("CombLongFrozen", TThostFtdcVolumeType),
        ("CombShortFrozen", TThostFtdcVolumeType),
        ("CloseProfitByDate", TThostFtdcMoneyType),
        ("CloseProfitByTrade", TThostFtdcMoneyType),
        ("TodayPosition", TThostFtdcVolumeType),
        ("MarginRateByMoney", TThostFtdcRatioType),
        ("MarginRateByVolume", TThostFtdcRatioType),
        ("StrikeFrozen", TThostFtdcVolumeType),
        ("StrikeFrozenAmount", TThostFtdcMoneyType),
        ("AbandonFrozen", TThostFtdcVolumeType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("YdStrikeFrozen", TThostFtdcVolumeType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("PositionCostOffset", TThostFtdcMoneyType),
        ("TasPosition", TThostFtdcVolumeType),
        ("TasPositionCost", TThostFtdcMoneyType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcSyncingInstrumentMarginRateField(Structure):
    """正在同步中的合约保证金率"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestorRange", TThostFtdcInvestorRangeType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("HedgeFlag", TThostFtdcHedgeFlagType),
        ("LongMarginRatioByMoney", TThostFtdcRatioType),
        ("LongMarginRatioByVolume", TThostFtdcMoneyType),
        ("ShortMarginRatioByMoney", TThostFtdcRatioType),
        ("ShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("IsRelative", TThostFtdcBoolType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcSyncingInstrumentCommissionRateField(Structure):
    """正在同步中的合约手续费率"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestorRange", TThostFtdcInvestorRangeType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("OpenRatioByMoney", TThostFtdcRatioType),
        ("OpenRatioByVolume", TThostFtdcRatioType),
        ("CloseRatioByMoney", TThostFtdcRatioType),
        ("CloseRatioByVolume", TThostFtdcRatioType),
        ("CloseTodayRatioByMoney", TThostFtdcRatioType),
        ("CloseTodayRatioByVolume", TThostFtdcRatioType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcSyncingInstrumentTradingRightField(Structure):
    """正在同步中的合约交易权限"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestorRange", TThostFtdcInvestorRangeType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("TradingRight", TThostFtdcTradingRightType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcQryOrderField(Structure):
    """查询报单"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("OrderSysID", TThostFtdcOrderSysIDType),
        ("InsertTimeStart", TThostFtdcTimeType),
        ("InsertTimeEnd", TThostFtdcTimeType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcQryTradeField(Structure):
    """查询成交"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("TradeID", TThostFtdcTradeIDType),
        ("TradeTimeStart", TThostFtdcTimeType),
        ("TradeTimeEnd", TThostFtdcTimeType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcQryInvestorPositionField(Structure):
    """查询投资者持仓"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcQryTradingAccountField(Structure):
    """查询资金账户"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("BizType", TThostFtdcBizTypeType),
        ("AccountID", TThostFtdcAccountIDType),
        
    ]
    
class  CThostFtdcQryInvestorField(Structure):
    """查询投资者"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        
    ]
    
class  CThostFtdcQryTradingCodeField(Structure):
    """查询交易编码"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("ClientIDType", TThostFtdcClientIDTypeType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        
    ]
    
class  CThostFtdcQryInvestorGroupField(Structure):
    """查询投资者组"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        
    ]
    
class  CThostFtdcQryInstrumentMarginRateField(Structure):
    """查询合约保证金率"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("HedgeFlag", TThostFtdcHedgeFlagType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcQryInstrumentCommissionRateField(Structure):
    """查询手续费率"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcQryInstrumentTradingRightField(Structure):
    """查询合约交易权限"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcQryBrokerField(Structure):
    """查询经纪公司"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        
    ]
    
class  CThostFtdcQryTraderField(Structure):
    """查询交易员"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("TraderID", TThostFtdcTraderIDType),
        
    ]
    
class  CThostFtdcQrySuperUserFunctionField(Structure):
    """查询管理用户功能权限"""
    _fields_ = [
        ("UserID", TThostFtdcUserIDType),
        
    ]
    
class  CThostFtdcQryUserSessionField(Structure):
    """查询用户会话"""
    _fields_ = [
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        
    ]
    
class  CThostFtdcQryPartBrokerField(Structure):
    """查询经纪公司会员代码"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        
    ]
    
class  CThostFtdcQryFrontStatusField(Structure):
    """查询前置状态"""
    _fields_ = [
        ("FrontID", TThostFtdcFrontIDType),
        
    ]
    
class  CThostFtdcQryExchangeOrderField(Structure):
    """查询交易所报单"""
    _fields_ = [
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve1", TThostFtdcOldExchangeInstIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        
    ]
    
class  CThostFtdcQryOrderActionField(Structure):
    """查询报单操作"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        
    ]
    
class  CThostFtdcQryExchangeOrderActionField(Structure):
    """查询交易所报单操作"""
    _fields_ = [
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("TraderID", TThostFtdcTraderIDType),
        
    ]
    
class  CThostFtdcQrySuperUserField(Structure):
    """查询管理用户"""
    _fields_ = [
        ("UserID", TThostFtdcUserIDType),
        
    ]
    
class  CThostFtdcQryExchangeField(Structure):
    """查询交易所"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        
    ]
    
class  CThostFtdcQryProductField(Structure):
    """查询产品"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ProductClass", TThostFtdcProductClassType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ProductID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcQryInstrumentField(Structure):
    """查询合约"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("reserve2", TThostFtdcOldExchangeInstIDType),
        ("reserve3", TThostFtdcOldInstrumentIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        ("ProductID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcQryDepthMarketDataField(Structure):
    """查询行情"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcQryBrokerUserField(Structure):
    """查询经纪公司用户"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        
    ]
    
class  CThostFtdcQryBrokerUserFunctionField(Structure):
    """查询经纪公司用户权限"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        
    ]
    
class  CThostFtdcQryTraderOfferField(Structure):
    """查询交易员报盘机"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("TraderID", TThostFtdcTraderIDType),
        
    ]
    
class  CThostFtdcQrySyncDepositField(Structure):
    """查询出入金流水"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("DepositSeqNo", TThostFtdcDepositSeqNoType),
        
    ]
    
class  CThostFtdcQrySettlementInfoField(Structure):
    """查询投资者结算结果"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("TradingDay", TThostFtdcDateType),
        ("AccountID", TThostFtdcAccountIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        
    ]
    
class  CThostFtdcQryExchangeMarginRateField(Structure):
    """查询交易所保证金率"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("HedgeFlag", TThostFtdcHedgeFlagType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcQryExchangeMarginRateAdjustField(Structure):
    """查询交易所调整保证金率"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("HedgeFlag", TThostFtdcHedgeFlagType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcQryExchangeRateField(Structure):
    """查询汇率"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("FromCurrencyID", TThostFtdcCurrencyIDType),
        ("ToCurrencyID", TThostFtdcCurrencyIDType),
        
    ]
    
class  CThostFtdcQrySyncFundMortgageField(Structure):
    """查询货币质押流水"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("MortgageSeqNo", TThostFtdcDepositSeqNoType),
        
    ]
    
class  CThostFtdcQryHisOrderField(Structure):
    """查询报单"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("OrderSysID", TThostFtdcOrderSysIDType),
        ("InsertTimeStart", TThostFtdcTimeType),
        ("InsertTimeEnd", TThostFtdcTimeType),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcOptionInstrMiniMarginField(Structure):
    """当前期权合约最小保证金"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestorRange", TThostFtdcInvestorRangeType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("MinMargin", TThostFtdcMoneyType),
        ("ValueMethod", TThostFtdcValueMethodType),
        ("IsRelative", TThostFtdcBoolType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcOptionInstrMarginAdjustField(Structure):
    """当前期权合约保证金调整系数"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestorRange", TThostFtdcInvestorRangeType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("SShortMarginRatioByMoney", TThostFtdcRatioType),
        ("SShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("HShortMarginRatioByMoney", TThostFtdcRatioType),
        ("HShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("AShortMarginRatioByMoney", TThostFtdcRatioType),
        ("AShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("IsRelative", TThostFtdcBoolType),
        ("MShortMarginRatioByMoney", TThostFtdcRatioType),
        ("MShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcOptionInstrCommRateField(Structure):
    """当前期权合约手续费的详细内容"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestorRange", TThostFtdcInvestorRangeType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("OpenRatioByMoney", TThostFtdcRatioType),
        ("OpenRatioByVolume", TThostFtdcRatioType),
        ("CloseRatioByMoney", TThostFtdcRatioType),
        ("CloseRatioByVolume", TThostFtdcRatioType),
        ("CloseTodayRatioByMoney", TThostFtdcRatioType),
        ("CloseTodayRatioByVolume", TThostFtdcRatioType),
        ("StrikeRatioByMoney", TThostFtdcRatioType),
        ("StrikeRatioByVolume", TThostFtdcRatioType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcOptionInstrTradeCostField(Structure):
    """期权交易成本"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("HedgeFlag", TThostFtdcHedgeFlagType),
        ("FixedMargin", TThostFtdcMoneyType),
        ("MiniMargin", TThostFtdcMoneyType),
        ("Royalty", TThostFtdcMoneyType),
        ("ExchFixedMargin", TThostFtdcMoneyType),
        ("ExchMiniMargin", TThostFtdcMoneyType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcQryOptionInstrTradeCostField(Structure):
    """期权交易成本查询"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("HedgeFlag", TThostFtdcHedgeFlagType),
        ("InputPrice", TThostFtdcPriceType),
        ("UnderlyingPrice", TThostFtdcPriceType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcQryOptionInstrCommRateField(Structure):
    """期权手续费率查询"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcIndexPriceField(Structure):
    """股指现货指数"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ClosePrice", TThostFtdcPriceType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcInputExecOrderField(Structure):
    """输入的执行宣告"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExecOrderRef", TThostFtdcOrderRefType),
        ("UserID", TThostFtdcUserIDType),
        ("Volume", TThostFtdcVolumeType),
        ("RequestID", TThostFtdcRequestIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("OffsetFlag", TThostFtdcOffsetFlagType),
        ("HedgeFlag", TThostFtdcHedgeFlagType),
        ("ActionType", TThostFtdcActionTypeType),
        ("PosiDirection", TThostFtdcPosiDirectionType),
        ("ReservePositionFlag", TThostFtdcExecOrderPositionFlagType),
        ("CloseFlag", TThostFtdcExecOrderCloseFlagType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcInputExecOrderActionField(Structure):
    """输入执行宣告操作"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("ExecOrderActionRef", TThostFtdcOrderActionRefType),
        ("ExecOrderRef", TThostFtdcOrderRefType),
        ("RequestID", TThostFtdcRequestIDType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ExecOrderSysID", TThostFtdcExecOrderSysIDType),
        ("ActionFlag", TThostFtdcActionFlagType),
        ("UserID", TThostFtdcUserIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcExecOrderField(Structure):
    """执行宣告"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExecOrderRef", TThostFtdcOrderRefType),
        ("UserID", TThostFtdcUserIDType),
        ("Volume", TThostFtdcVolumeType),
        ("RequestID", TThostFtdcRequestIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("OffsetFlag", TThostFtdcOffsetFlagType),
        ("HedgeFlag", TThostFtdcHedgeFlagType),
        ("ActionType", TThostFtdcActionTypeType),
        ("PosiDirection", TThostFtdcPosiDirectionType),
        ("ReservePositionFlag", TThostFtdcExecOrderPositionFlagType),
        ("CloseFlag", TThostFtdcExecOrderCloseFlagType),
        ("ExecOrderLocalID", TThostFtdcOrderLocalIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve2", TThostFtdcOldExchangeInstIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("OrderSubmitStatus", TThostFtdcOrderSubmitStatusType),
        ("NotifySequence", TThostFtdcSequenceNoType),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("ExecOrderSysID", TThostFtdcExecOrderSysIDType),
        ("InsertDate", TThostFtdcDateType),
        ("InsertTime", TThostFtdcTimeType),
        ("CancelTime", TThostFtdcTimeType),
        ("ExecResult", TThostFtdcExecResultType),
        ("ClearingPartID", TThostFtdcParticipantIDType),
        ("SequenceNo", TThostFtdcSequenceNoType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("UserProductInfo", TThostFtdcProductInfoType),
        ("StatusMsg", TThostFtdcErrorMsgType),
        ("ActiveUserID", TThostFtdcUserIDType),
        ("BrokerExecOrderSeq", TThostFtdcSequenceNoType),
        ("BranchID", TThostFtdcBranchIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("reserve3", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcExecOrderActionField(Structure):
    """执行宣告操作"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("ExecOrderActionRef", TThostFtdcOrderActionRefType),
        ("ExecOrderRef", TThostFtdcOrderRefType),
        ("RequestID", TThostFtdcRequestIDType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ExecOrderSysID", TThostFtdcExecOrderSysIDType),
        ("ActionFlag", TThostFtdcActionFlagType),
        ("ActionDate", TThostFtdcDateType),
        ("ActionTime", TThostFtdcTimeType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("ExecOrderLocalID", TThostFtdcOrderLocalIDType),
        ("ActionLocalID", TThostFtdcOrderLocalIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("OrderActionStatus", TThostFtdcOrderActionStatusType),
        ("UserID", TThostFtdcUserIDType),
        ("ActionType", TThostFtdcActionTypeType),
        ("StatusMsg", TThostFtdcErrorMsgType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("BranchID", TThostFtdcBranchIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcQryExecOrderField(Structure):
    """执行宣告查询"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ExecOrderSysID", TThostFtdcExecOrderSysIDType),
        ("InsertTimeStart", TThostFtdcTimeType),
        ("InsertTimeEnd", TThostFtdcTimeType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcExchangeExecOrderField(Structure):
    """交易所执行宣告信息"""
    _fields_ = [
        ("Volume", TThostFtdcVolumeType),
        ("RequestID", TThostFtdcRequestIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("OffsetFlag", TThostFtdcOffsetFlagType),
        ("HedgeFlag", TThostFtdcHedgeFlagType),
        ("ActionType", TThostFtdcActionTypeType),
        ("PosiDirection", TThostFtdcPosiDirectionType),
        ("ReservePositionFlag", TThostFtdcExecOrderPositionFlagType),
        ("CloseFlag", TThostFtdcExecOrderCloseFlagType),
        ("ExecOrderLocalID", TThostFtdcOrderLocalIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve1", TThostFtdcOldExchangeInstIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("OrderSubmitStatus", TThostFtdcOrderSubmitStatusType),
        ("NotifySequence", TThostFtdcSequenceNoType),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("ExecOrderSysID", TThostFtdcExecOrderSysIDType),
        ("InsertDate", TThostFtdcDateType),
        ("InsertTime", TThostFtdcTimeType),
        ("CancelTime", TThostFtdcTimeType),
        ("ExecResult", TThostFtdcExecResultType),
        ("ClearingPartID", TThostFtdcParticipantIDType),
        ("SequenceNo", TThostFtdcSequenceNoType),
        ("BranchID", TThostFtdcBranchIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcQryExchangeExecOrderField(Structure):
    """交易所执行宣告查询"""
    _fields_ = [
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve1", TThostFtdcOldExchangeInstIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        
    ]
    
class  CThostFtdcQryExecOrderActionField(Structure):
    """执行宣告操作查询"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        
    ]
    
class  CThostFtdcExchangeExecOrderActionField(Structure):
    """交易所执行宣告操作"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ExecOrderSysID", TThostFtdcExecOrderSysIDType),
        ("ActionFlag", TThostFtdcActionFlagType),
        ("ActionDate", TThostFtdcDateType),
        ("ActionTime", TThostFtdcTimeType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("ExecOrderLocalID", TThostFtdcOrderLocalIDType),
        ("ActionLocalID", TThostFtdcOrderLocalIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("OrderActionStatus", TThostFtdcOrderActionStatusType),
        ("UserID", TThostFtdcUserIDType),
        ("ActionType", TThostFtdcActionTypeType),
        ("BranchID", TThostFtdcBranchIDType),
        ("reserve1", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("reserve2", TThostFtdcOldExchangeInstIDType),
        ("Volume", TThostFtdcVolumeType),
        ("IPAddress", TThostFtdcIPAddressType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        
    ]
    
class  CThostFtdcQryExchangeExecOrderActionField(Structure):
    """交易所执行宣告操作查询"""
    _fields_ = [
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("TraderID", TThostFtdcTraderIDType),
        
    ]
    
class  CThostFtdcErrExecOrderField(Structure):
    """错误执行宣告"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExecOrderRef", TThostFtdcOrderRefType),
        ("UserID", TThostFtdcUserIDType),
        ("Volume", TThostFtdcVolumeType),
        ("RequestID", TThostFtdcRequestIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("OffsetFlag", TThostFtdcOffsetFlagType),
        ("HedgeFlag", TThostFtdcHedgeFlagType),
        ("ActionType", TThostFtdcActionTypeType),
        ("PosiDirection", TThostFtdcPosiDirectionType),
        ("ReservePositionFlag", TThostFtdcExecOrderPositionFlagType),
        ("CloseFlag", TThostFtdcExecOrderCloseFlagType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcQryErrExecOrderField(Structure):
    """查询错误执行宣告"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        
    ]
    
class  CThostFtdcErrExecOrderActionField(Structure):
    """错误执行宣告操作"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("ExecOrderActionRef", TThostFtdcOrderActionRefType),
        ("ExecOrderRef", TThostFtdcOrderRefType),
        ("RequestID", TThostFtdcRequestIDType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ExecOrderSysID", TThostFtdcExecOrderSysIDType),
        ("ActionFlag", TThostFtdcActionFlagType),
        ("UserID", TThostFtdcUserIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcQryErrExecOrderActionField(Structure):
    """查询错误执行宣告操作"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        
    ]
    
class  CThostFtdcOptionInstrTradingRightField(Structure):
    """投资者期权合约交易权限"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestorRange", TThostFtdcInvestorRangeType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("Direction", TThostFtdcDirectionType),
        ("TradingRight", TThostFtdcTradingRightType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcQryOptionInstrTradingRightField(Structure):
    """查询期权合约交易权限"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("Direction", TThostFtdcDirectionType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcInputForQuoteField(Structure):
    """输入的询价"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ForQuoteRef", TThostFtdcOrderRefType),
        ("UserID", TThostFtdcUserIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcForQuoteField(Structure):
    """询价"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ForQuoteRef", TThostFtdcOrderRefType),
        ("UserID", TThostFtdcUserIDType),
        ("ForQuoteLocalID", TThostFtdcOrderLocalIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve2", TThostFtdcOldExchangeInstIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("InsertDate", TThostFtdcDateType),
        ("InsertTime", TThostFtdcTimeType),
        ("ForQuoteStatus", TThostFtdcForQuoteStatusType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("StatusMsg", TThostFtdcErrorMsgType),
        ("ActiveUserID", TThostFtdcUserIDType),
        ("BrokerForQutoSeq", TThostFtdcSequenceNoType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("reserve3", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcQryForQuoteField(Structure):
    """询价查询"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InsertTimeStart", TThostFtdcTimeType),
        ("InsertTimeEnd", TThostFtdcTimeType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcExchangeForQuoteField(Structure):
    """交易所询价信息"""
    _fields_ = [
        ("ForQuoteLocalID", TThostFtdcOrderLocalIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve1", TThostFtdcOldExchangeInstIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("InsertDate", TThostFtdcDateType),
        ("InsertTime", TThostFtdcTimeType),
        ("ForQuoteStatus", TThostFtdcForQuoteStatusType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcQryExchangeForQuoteField(Structure):
    """交易所询价查询"""
    _fields_ = [
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve1", TThostFtdcOldExchangeInstIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        
    ]
    
class  CThostFtdcInputQuoteField(Structure):
    """输入的报价"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("QuoteRef", TThostFtdcOrderRefType),
        ("UserID", TThostFtdcUserIDType),
        ("AskPrice", TThostFtdcPriceType),
        ("BidPrice", TThostFtdcPriceType),
        ("AskVolume", TThostFtdcVolumeType),
        ("BidVolume", TThostFtdcVolumeType),
        ("RequestID", TThostFtdcRequestIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("AskOffsetFlag", TThostFtdcOffsetFlagType),
        ("BidOffsetFlag", TThostFtdcOffsetFlagType),
        ("AskHedgeFlag", TThostFtdcHedgeFlagType),
        ("BidHedgeFlag", TThostFtdcHedgeFlagType),
        ("AskOrderRef", TThostFtdcOrderRefType),
        ("BidOrderRef", TThostFtdcOrderRefType),
        ("ForQuoteSysID", TThostFtdcOrderSysIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        ("ReplaceSysID", TThostFtdcOrderSysIDType),
        
    ]
    
class  CThostFtdcInputQuoteActionField(Structure):
    """输入报价操作"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("QuoteActionRef", TThostFtdcOrderActionRefType),
        ("QuoteRef", TThostFtdcOrderRefType),
        ("RequestID", TThostFtdcRequestIDType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("QuoteSysID", TThostFtdcOrderSysIDType),
        ("ActionFlag", TThostFtdcActionFlagType),
        ("UserID", TThostFtdcUserIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcQuoteField(Structure):
    """报价"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("QuoteRef", TThostFtdcOrderRefType),
        ("UserID", TThostFtdcUserIDType),
        ("AskPrice", TThostFtdcPriceType),
        ("BidPrice", TThostFtdcPriceType),
        ("AskVolume", TThostFtdcVolumeType),
        ("BidVolume", TThostFtdcVolumeType),
        ("RequestID", TThostFtdcRequestIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("AskOffsetFlag", TThostFtdcOffsetFlagType),
        ("BidOffsetFlag", TThostFtdcOffsetFlagType),
        ("AskHedgeFlag", TThostFtdcHedgeFlagType),
        ("BidHedgeFlag", TThostFtdcHedgeFlagType),
        ("QuoteLocalID", TThostFtdcOrderLocalIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve2", TThostFtdcOldExchangeInstIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("NotifySequence", TThostFtdcSequenceNoType),
        ("OrderSubmitStatus", TThostFtdcOrderSubmitStatusType),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("QuoteSysID", TThostFtdcOrderSysIDType),
        ("InsertDate", TThostFtdcDateType),
        ("InsertTime", TThostFtdcTimeType),
        ("CancelTime", TThostFtdcTimeType),
        ("QuoteStatus", TThostFtdcOrderStatusType),
        ("ClearingPartID", TThostFtdcParticipantIDType),
        ("SequenceNo", TThostFtdcSequenceNoType),
        ("AskOrderSysID", TThostFtdcOrderSysIDType),
        ("BidOrderSysID", TThostFtdcOrderSysIDType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("UserProductInfo", TThostFtdcProductInfoType),
        ("StatusMsg", TThostFtdcErrorMsgType),
        ("ActiveUserID", TThostFtdcUserIDType),
        ("BrokerQuoteSeq", TThostFtdcSequenceNoType),
        ("AskOrderRef", TThostFtdcOrderRefType),
        ("BidOrderRef", TThostFtdcOrderRefType),
        ("ForQuoteSysID", TThostFtdcOrderSysIDType),
        ("BranchID", TThostFtdcBranchIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("reserve3", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        ("ReplaceSysID", TThostFtdcOrderSysIDType),
        
    ]
    
class  CThostFtdcQuoteActionField(Structure):
    """报价操作"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("QuoteActionRef", TThostFtdcOrderActionRefType),
        ("QuoteRef", TThostFtdcOrderRefType),
        ("RequestID", TThostFtdcRequestIDType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("QuoteSysID", TThostFtdcOrderSysIDType),
        ("ActionFlag", TThostFtdcActionFlagType),
        ("ActionDate", TThostFtdcDateType),
        ("ActionTime", TThostFtdcTimeType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("QuoteLocalID", TThostFtdcOrderLocalIDType),
        ("ActionLocalID", TThostFtdcOrderLocalIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("OrderActionStatus", TThostFtdcOrderActionStatusType),
        ("UserID", TThostFtdcUserIDType),
        ("StatusMsg", TThostFtdcErrorMsgType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("BranchID", TThostFtdcBranchIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcQryQuoteField(Structure):
    """报价查询"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("QuoteSysID", TThostFtdcOrderSysIDType),
        ("InsertTimeStart", TThostFtdcTimeType),
        ("InsertTimeEnd", TThostFtdcTimeType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcExchangeQuoteField(Structure):
    """交易所报价信息"""
    _fields_ = [
        ("AskPrice", TThostFtdcPriceType),
        ("BidPrice", TThostFtdcPriceType),
        ("AskVolume", TThostFtdcVolumeType),
        ("BidVolume", TThostFtdcVolumeType),
        ("RequestID", TThostFtdcRequestIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("AskOffsetFlag", TThostFtdcOffsetFlagType),
        ("BidOffsetFlag", TThostFtdcOffsetFlagType),
        ("AskHedgeFlag", TThostFtdcHedgeFlagType),
        ("BidHedgeFlag", TThostFtdcHedgeFlagType),
        ("QuoteLocalID", TThostFtdcOrderLocalIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve1", TThostFtdcOldExchangeInstIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("NotifySequence", TThostFtdcSequenceNoType),
        ("OrderSubmitStatus", TThostFtdcOrderSubmitStatusType),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("QuoteSysID", TThostFtdcOrderSysIDType),
        ("InsertDate", TThostFtdcDateType),
        ("InsertTime", TThostFtdcTimeType),
        ("CancelTime", TThostFtdcTimeType),
        ("QuoteStatus", TThostFtdcOrderStatusType),
        ("ClearingPartID", TThostFtdcParticipantIDType),
        ("SequenceNo", TThostFtdcSequenceNoType),
        ("AskOrderSysID", TThostFtdcOrderSysIDType),
        ("BidOrderSysID", TThostFtdcOrderSysIDType),
        ("ForQuoteSysID", TThostFtdcOrderSysIDType),
        ("BranchID", TThostFtdcBranchIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcQryExchangeQuoteField(Structure):
    """交易所报价查询"""
    _fields_ = [
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve1", TThostFtdcOldExchangeInstIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        
    ]
    
class  CThostFtdcQryQuoteActionField(Structure):
    """报价操作查询"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        
    ]
    
class  CThostFtdcExchangeQuoteActionField(Structure):
    """交易所报价操作"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("QuoteSysID", TThostFtdcOrderSysIDType),
        ("ActionFlag", TThostFtdcActionFlagType),
        ("ActionDate", TThostFtdcDateType),
        ("ActionTime", TThostFtdcTimeType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("QuoteLocalID", TThostFtdcOrderLocalIDType),
        ("ActionLocalID", TThostFtdcOrderLocalIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("OrderActionStatus", TThostFtdcOrderActionStatusType),
        ("UserID", TThostFtdcUserIDType),
        ("reserve1", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcQryExchangeQuoteActionField(Structure):
    """交易所报价操作查询"""
    _fields_ = [
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("TraderID", TThostFtdcTraderIDType),
        
    ]
    
class  CThostFtdcOptionInstrDeltaField(Structure):
    """期权合约delta值"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestorRange", TThostFtdcInvestorRangeType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("Delta", TThostFtdcRatioType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcForQuoteRspField(Structure):
    """发给做市商的询价请求"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ForQuoteSysID", TThostFtdcOrderSysIDType),
        ("ForQuoteTime", TThostFtdcTimeType),
        ("ActionDay", TThostFtdcDateType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcStrikeOffsetField(Structure):
    """当前期权合约执行偏移值的详细内容"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestorRange", TThostFtdcInvestorRangeType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("Offset", TThostFtdcMoneyType),
        ("OffsetType", TThostFtdcStrikeOffsetTypeType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcQryStrikeOffsetField(Structure):
    """期权执行偏移值查询"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcInputBatchOrderActionField(Structure):
    """输入批量报单操作"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("OrderActionRef", TThostFtdcOrderActionRefType),
        ("RequestID", TThostFtdcRequestIDType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("UserID", TThostFtdcUserIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("reserve1", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcBatchOrderActionField(Structure):
    """批量报单操作"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("OrderActionRef", TThostFtdcOrderActionRefType),
        ("RequestID", TThostFtdcRequestIDType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ActionDate", TThostFtdcDateType),
        ("ActionTime", TThostFtdcTimeType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("ActionLocalID", TThostFtdcOrderLocalIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("OrderActionStatus", TThostFtdcOrderActionStatusType),
        ("UserID", TThostFtdcUserIDType),
        ("StatusMsg", TThostFtdcErrorMsgType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("reserve1", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcExchangeBatchOrderActionField(Structure):
    """交易所批量报单操作"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ActionDate", TThostFtdcDateType),
        ("ActionTime", TThostFtdcTimeType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("ActionLocalID", TThostFtdcOrderLocalIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("OrderActionStatus", TThostFtdcOrderActionStatusType),
        ("UserID", TThostFtdcUserIDType),
        ("reserve1", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcQryBatchOrderActionField(Structure):
    """查询批量报单操作"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        
    ]
    
class  CThostFtdcCombInstrumentGuardField(Structure):
    """组合合约安全系数"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("GuarantRatio", TThostFtdcRatioType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcQryCombInstrumentGuardField(Structure):
    """组合合约安全系数查询"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcInputCombActionField(Structure):
    """输入的申请组合"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("CombActionRef", TThostFtdcOrderRefType),
        ("UserID", TThostFtdcUserIDType),
        ("Direction", TThostFtdcDirectionType),
        ("Volume", TThostFtdcVolumeType),
        ("CombDirection", TThostFtdcCombDirectionType),
        ("HedgeFlag", TThostFtdcHedgeFlagType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcCombActionField(Structure):
    """申请组合"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("CombActionRef", TThostFtdcOrderRefType),
        ("UserID", TThostFtdcUserIDType),
        ("Direction", TThostFtdcDirectionType),
        ("Volume", TThostFtdcVolumeType),
        ("CombDirection", TThostFtdcCombDirectionType),
        ("HedgeFlag", TThostFtdcHedgeFlagType),
        ("ActionLocalID", TThostFtdcOrderLocalIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve2", TThostFtdcOldExchangeInstIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("ActionStatus", TThostFtdcOrderActionStatusType),
        ("NotifySequence", TThostFtdcSequenceNoType),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("SequenceNo", TThostFtdcSequenceNoType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("UserProductInfo", TThostFtdcProductInfoType),
        ("StatusMsg", TThostFtdcErrorMsgType),
        ("reserve3", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("ComTradeID", TThostFtdcTradeIDType),
        ("BranchID", TThostFtdcBranchIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcQryCombActionField(Structure):
    """申请组合查询"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcExchangeCombActionField(Structure):
    """交易所申请组合信息"""
    _fields_ = [
        ("Direction", TThostFtdcDirectionType),
        ("Volume", TThostFtdcVolumeType),
        ("CombDirection", TThostFtdcCombDirectionType),
        ("HedgeFlag", TThostFtdcHedgeFlagType),
        ("ActionLocalID", TThostFtdcOrderLocalIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve1", TThostFtdcOldExchangeInstIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("ActionStatus", TThostFtdcOrderActionStatusType),
        ("NotifySequence", TThostFtdcSequenceNoType),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("SequenceNo", TThostFtdcSequenceNoType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("ComTradeID", TThostFtdcTradeIDType),
        ("BranchID", TThostFtdcBranchIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcQryExchangeCombActionField(Structure):
    """交易所申请组合查询"""
    _fields_ = [
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve1", TThostFtdcOldExchangeInstIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        
    ]
    
class  CThostFtdcProductExchRateField(Structure):
    """产品报价汇率"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("QuoteCurrencyID", TThostFtdcCurrencyIDType),
        ("ExchangeRate", TThostFtdcExchangeRateType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ProductID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcQryProductExchRateField(Structure):
    """产品报价汇率查询"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ProductID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcQryForQuoteParamField(Structure):
    """查询询价价差参数"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcForQuoteParamField(Structure):
    """询价价差参数"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("LastPrice", TThostFtdcPriceType),
        ("PriceInterval", TThostFtdcPriceType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcMMOptionInstrCommRateField(Structure):
    """当前做市商期权合约手续费的详细内容"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestorRange", TThostFtdcInvestorRangeType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("OpenRatioByMoney", TThostFtdcRatioType),
        ("OpenRatioByVolume", TThostFtdcRatioType),
        ("CloseRatioByMoney", TThostFtdcRatioType),
        ("CloseRatioByVolume", TThostFtdcRatioType),
        ("CloseTodayRatioByMoney", TThostFtdcRatioType),
        ("CloseTodayRatioByVolume", TThostFtdcRatioType),
        ("StrikeRatioByMoney", TThostFtdcRatioType),
        ("StrikeRatioByVolume", TThostFtdcRatioType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcQryMMOptionInstrCommRateField(Structure):
    """做市商期权手续费率查询"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcMMInstrumentCommissionRateField(Structure):
    """做市商合约手续费率"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestorRange", TThostFtdcInvestorRangeType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("OpenRatioByMoney", TThostFtdcRatioType),
        ("OpenRatioByVolume", TThostFtdcRatioType),
        ("CloseRatioByMoney", TThostFtdcRatioType),
        ("CloseRatioByVolume", TThostFtdcRatioType),
        ("CloseTodayRatioByMoney", TThostFtdcRatioType),
        ("CloseTodayRatioByVolume", TThostFtdcRatioType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcQryMMInstrumentCommissionRateField(Structure):
    """查询做市商合约手续费率"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcInstrumentOrderCommRateField(Structure):
    """当前报单手续费的详细内容"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestorRange", TThostFtdcInvestorRangeType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("HedgeFlag", TThostFtdcHedgeFlagType),
        ("OrderCommByVolume", TThostFtdcRatioType),
        ("OrderActionCommByVolume", TThostFtdcRatioType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("OrderCommByTrade", TThostFtdcRatioType),
        ("OrderActionCommByTrade", TThostFtdcRatioType),
        
    ]
    
class  CThostFtdcQryInstrumentOrderCommRateField(Structure):
    """报单手续费率查询"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcTradeParamField(Structure):
    """交易参数"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("TradeParamID", TThostFtdcTradeParamIDType),
        ("TradeParamValue", TThostFtdcSettlementParamValueType),
        ("Memo", TThostFtdcMemoType),
        
    ]
    
class  CThostFtdcInstrumentMarginRateULField(Structure):
    """合约保证金率调整"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestorRange", TThostFtdcInvestorRangeType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("HedgeFlag", TThostFtdcHedgeFlagType),
        ("LongMarginRatioByMoney", TThostFtdcRatioType),
        ("LongMarginRatioByVolume", TThostFtdcMoneyType),
        ("ShortMarginRatioByMoney", TThostFtdcRatioType),
        ("ShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcFutureLimitPosiParamField(Structure):
    """期货持仓限制参数"""
    _fields_ = [
        ("InvestorRange", TThostFtdcInvestorRangeType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("SpecOpenVolume", TThostFtdcVolumeType),
        ("ArbiOpenVolume", TThostFtdcVolumeType),
        ("OpenVolume", TThostFtdcVolumeType),
        ("ProductID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcLoginForbiddenIPField(Structure):
    """禁止登录IP"""
    _fields_ = [
        ("reserve1", TThostFtdcOldIPAddressType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcIPListField(Structure):
    """IP列表"""
    _fields_ = [
        ("reserve1", TThostFtdcOldIPAddressType),
        ("IsWhite", TThostFtdcBoolType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcInputOptionSelfCloseField(Structure):
    """输入的期权自对冲"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("OptionSelfCloseRef", TThostFtdcOrderRefType),
        ("UserID", TThostFtdcUserIDType),
        ("Volume", TThostFtdcVolumeType),
        ("RequestID", TThostFtdcRequestIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("HedgeFlag", TThostFtdcHedgeFlagType),
        ("OptSelfCloseFlag", TThostFtdcOptSelfCloseFlagType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcInputOptionSelfCloseActionField(Structure):
    """输入期权自对冲操作"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("OptionSelfCloseActionRef", TThostFtdcOrderActionRefType),
        ("OptionSelfCloseRef", TThostFtdcOrderRefType),
        ("RequestID", TThostFtdcRequestIDType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("OptionSelfCloseSysID", TThostFtdcOrderSysIDType),
        ("ActionFlag", TThostFtdcActionFlagType),
        ("UserID", TThostFtdcUserIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcOptionSelfCloseField(Structure):
    """期权自对冲"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("OptionSelfCloseRef", TThostFtdcOrderRefType),
        ("UserID", TThostFtdcUserIDType),
        ("Volume", TThostFtdcVolumeType),
        ("RequestID", TThostFtdcRequestIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("HedgeFlag", TThostFtdcHedgeFlagType),
        ("OptSelfCloseFlag", TThostFtdcOptSelfCloseFlagType),
        ("OptionSelfCloseLocalID", TThostFtdcOrderLocalIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve2", TThostFtdcOldExchangeInstIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("OrderSubmitStatus", TThostFtdcOrderSubmitStatusType),
        ("NotifySequence", TThostFtdcSequenceNoType),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("OptionSelfCloseSysID", TThostFtdcOrderSysIDType),
        ("InsertDate", TThostFtdcDateType),
        ("InsertTime", TThostFtdcTimeType),
        ("CancelTime", TThostFtdcTimeType),
        ("ExecResult", TThostFtdcExecResultType),
        ("ClearingPartID", TThostFtdcParticipantIDType),
        ("SequenceNo", TThostFtdcSequenceNoType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("UserProductInfo", TThostFtdcProductInfoType),
        ("StatusMsg", TThostFtdcErrorMsgType),
        ("ActiveUserID", TThostFtdcUserIDType),
        ("BrokerOptionSelfCloseSeq", TThostFtdcSequenceNoType),
        ("BranchID", TThostFtdcBranchIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("reserve3", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcOptionSelfCloseActionField(Structure):
    """期权自对冲操作"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("OptionSelfCloseActionRef", TThostFtdcOrderActionRefType),
        ("OptionSelfCloseRef", TThostFtdcOrderRefType),
        ("RequestID", TThostFtdcRequestIDType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("OptionSelfCloseSysID", TThostFtdcOrderSysIDType),
        ("ActionFlag", TThostFtdcActionFlagType),
        ("ActionDate", TThostFtdcDateType),
        ("ActionTime", TThostFtdcTimeType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("OptionSelfCloseLocalID", TThostFtdcOrderLocalIDType),
        ("ActionLocalID", TThostFtdcOrderLocalIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("OrderActionStatus", TThostFtdcOrderActionStatusType),
        ("UserID", TThostFtdcUserIDType),
        ("StatusMsg", TThostFtdcErrorMsgType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("BranchID", TThostFtdcBranchIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcQryOptionSelfCloseField(Structure):
    """期权自对冲查询"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("OptionSelfCloseSysID", TThostFtdcOrderSysIDType),
        ("InsertTimeStart", TThostFtdcTimeType),
        ("InsertTimeEnd", TThostFtdcTimeType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcExchangeOptionSelfCloseField(Structure):
    """交易所期权自对冲信息"""
    _fields_ = [
        ("Volume", TThostFtdcVolumeType),
        ("RequestID", TThostFtdcRequestIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("HedgeFlag", TThostFtdcHedgeFlagType),
        ("OptSelfCloseFlag", TThostFtdcOptSelfCloseFlagType),
        ("OptionSelfCloseLocalID", TThostFtdcOrderLocalIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve1", TThostFtdcOldExchangeInstIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("OrderSubmitStatus", TThostFtdcOrderSubmitStatusType),
        ("NotifySequence", TThostFtdcSequenceNoType),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("OptionSelfCloseSysID", TThostFtdcOrderSysIDType),
        ("InsertDate", TThostFtdcDateType),
        ("InsertTime", TThostFtdcTimeType),
        ("CancelTime", TThostFtdcTimeType),
        ("ExecResult", TThostFtdcExecResultType),
        ("ClearingPartID", TThostFtdcParticipantIDType),
        ("SequenceNo", TThostFtdcSequenceNoType),
        ("BranchID", TThostFtdcBranchIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcQryOptionSelfCloseActionField(Structure):
    """期权自对冲操作查询"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        
    ]
    
class  CThostFtdcExchangeOptionSelfCloseActionField(Structure):
    """交易所期权自对冲操作"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("OptionSelfCloseSysID", TThostFtdcOrderSysIDType),
        ("ActionFlag", TThostFtdcActionFlagType),
        ("ActionDate", TThostFtdcDateType),
        ("ActionTime", TThostFtdcTimeType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("OptionSelfCloseLocalID", TThostFtdcOrderLocalIDType),
        ("ActionLocalID", TThostFtdcOrderLocalIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("OrderActionStatus", TThostFtdcOrderActionStatusType),
        ("UserID", TThostFtdcUserIDType),
        ("BranchID", TThostFtdcBranchIDType),
        ("reserve1", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("reserve2", TThostFtdcOldExchangeInstIDType),
        ("OptSelfCloseFlag", TThostFtdcOptSelfCloseFlagType),
        ("IPAddress", TThostFtdcIPAddressType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        
    ]
    
class  CThostFtdcSyncDelaySwapField(Structure):
    """延时换汇同步"""
    _fields_ = [
        ("DelaySwapSeqNo", TThostFtdcDepositSeqNoType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("FromCurrencyID", TThostFtdcCurrencyIDType),
        ("FromAmount", TThostFtdcMoneyType),
        ("FromFrozenSwap", TThostFtdcMoneyType),
        ("FromRemainSwap", TThostFtdcMoneyType),
        ("ToCurrencyID", TThostFtdcCurrencyIDType),
        ("ToAmount", TThostFtdcMoneyType),
        ("IsManualSwap", TThostFtdcBoolType),
        ("IsAllRemainSetZero", TThostFtdcBoolType),
        
    ]
    
class  CThostFtdcQrySyncDelaySwapField(Structure):
    """查询延时换汇同步"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("DelaySwapSeqNo", TThostFtdcDepositSeqNoType),
        
    ]
    
class  CThostFtdcInvestUnitField(Structure):
    """投资单元"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InvestorUnitName", TThostFtdcPartyNameType),
        ("InvestorGroupID", TThostFtdcInvestorIDType),
        ("CommModelID", TThostFtdcInvestorIDType),
        ("MarginModelID", TThostFtdcInvestorIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        
    ]
    
class  CThostFtdcQryInvestUnitField(Structure):
    """查询投资单元"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        
    ]
    
class  CThostFtdcSecAgentCheckModeField(Structure):
    """二级代理商资金校验模式"""
    _fields_ = [
        ("InvestorID", TThostFtdcInvestorIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("BrokerSecAgentID", TThostFtdcAccountIDType),
        ("CheckSelfAccount", TThostFtdcBoolType),
        
    ]
    
class  CThostFtdcSecAgentTradeInfoField(Structure):
    """二级代理商信息"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerSecAgentID", TThostFtdcAccountIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("LongCustomerName", TThostFtdcLongIndividualNameType),
        
    ]
    
class  CThostFtdcMarketDataField(Structure):
    """市场行情"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("reserve2", TThostFtdcOldExchangeInstIDType),
        ("LastPrice", TThostFtdcPriceType),
        ("PreSettlementPrice", TThostFtdcPriceType),
        ("PreClosePrice", TThostFtdcPriceType),
        ("PreOpenInterest", TThostFtdcLargeVolumeType),
        ("OpenPrice", TThostFtdcPriceType),
        ("HighestPrice", TThostFtdcPriceType),
        ("LowestPrice", TThostFtdcPriceType),
        ("Volume", TThostFtdcVolumeType),
        ("Turnover", TThostFtdcMoneyType),
        ("OpenInterest", TThostFtdcLargeVolumeType),
        ("ClosePrice", TThostFtdcPriceType),
        ("SettlementPrice", TThostFtdcPriceType),
        ("UpperLimitPrice", TThostFtdcPriceType),
        ("LowerLimitPrice", TThostFtdcPriceType),
        ("PreDelta", TThostFtdcRatioType),
        ("CurrDelta", TThostFtdcRatioType),
        ("UpdateTime", TThostFtdcTimeType),
        ("UpdateMillisec", TThostFtdcMillisecType),
        ("ActionDay", TThostFtdcDateType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        
    ]
    
class  CThostFtdcMarketDataBaseField(Structure):
    """行情基础属性"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("PreSettlementPrice", TThostFtdcPriceType),
        ("PreClosePrice", TThostFtdcPriceType),
        ("PreOpenInterest", TThostFtdcLargeVolumeType),
        ("PreDelta", TThostFtdcRatioType),
        
    ]
    
class  CThostFtdcMarketDataStaticField(Structure):
    """行情静态属性"""
    _fields_ = [
        ("OpenPrice", TThostFtdcPriceType),
        ("HighestPrice", TThostFtdcPriceType),
        ("LowestPrice", TThostFtdcPriceType),
        ("ClosePrice", TThostFtdcPriceType),
        ("UpperLimitPrice", TThostFtdcPriceType),
        ("LowerLimitPrice", TThostFtdcPriceType),
        ("SettlementPrice", TThostFtdcPriceType),
        ("CurrDelta", TThostFtdcRatioType),
        
    ]
    
class  CThostFtdcMarketDataLastMatchField(Structure):
    """行情最新成交属性"""
    _fields_ = [
        ("LastPrice", TThostFtdcPriceType),
        ("Volume", TThostFtdcVolumeType),
        ("Turnover", TThostFtdcMoneyType),
        ("OpenInterest", TThostFtdcLargeVolumeType),
        
    ]
    
class  CThostFtdcMarketDataBestPriceField(Structure):
    """行情最优价属性"""
    _fields_ = [
        ("BidPrice1", TThostFtdcPriceType),
        ("BidVolume1", TThostFtdcVolumeType),
        ("AskPrice1", TThostFtdcPriceType),
        ("AskVolume1", TThostFtdcVolumeType),
        
    ]
    
class  CThostFtdcMarketDataBid23Field(Structure):
    """行情申买二、三属性"""
    _fields_ = [
        ("BidPrice2", TThostFtdcPriceType),
        ("BidVolume2", TThostFtdcVolumeType),
        ("BidPrice3", TThostFtdcPriceType),
        ("BidVolume3", TThostFtdcVolumeType),
        
    ]
    
class  CThostFtdcMarketDataAsk23Field(Structure):
    """行情申卖二、三属性"""
    _fields_ = [
        ("AskPrice2", TThostFtdcPriceType),
        ("AskVolume2", TThostFtdcVolumeType),
        ("AskPrice3", TThostFtdcPriceType),
        ("AskVolume3", TThostFtdcVolumeType),
        
    ]
    
class  CThostFtdcMarketDataBid45Field(Structure):
    """行情申买四、五属性"""
    _fields_ = [
        ("BidPrice4", TThostFtdcPriceType),
        ("BidVolume4", TThostFtdcVolumeType),
        ("BidPrice5", TThostFtdcPriceType),
        ("BidVolume5", TThostFtdcVolumeType),
        
    ]
    
class  CThostFtdcMarketDataAsk45Field(Structure):
    """行情申卖四、五属性"""
    _fields_ = [
        ("AskPrice4", TThostFtdcPriceType),
        ("AskVolume4", TThostFtdcVolumeType),
        ("AskPrice5", TThostFtdcPriceType),
        ("AskVolume5", TThostFtdcVolumeType),
        
    ]
    
class  CThostFtdcMarketDataUpdateTimeField(Structure):
    """行情更新时间属性"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("UpdateTime", TThostFtdcTimeType),
        ("UpdateMillisec", TThostFtdcMillisecType),
        ("ActionDay", TThostFtdcDateType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcMarketDataBandingPriceField(Structure):
    """行情上下带价"""
    _fields_ = [
        ("BandingUpperPrice", TThostFtdcPriceType),
        ("BandingLowerPrice", TThostFtdcPriceType),
        
    ]
    
class  CThostFtdcMarketDataExchangeField(Structure):
    """行情交易所代码属性"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        
    ]
    
class  CThostFtdcSpecificInstrumentField(Structure):
    """指定的合约"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcInstrumentStatusField(Structure):
    """合约状态"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("reserve1", TThostFtdcOldExchangeInstIDType),
        ("SettlementGroupID", TThostFtdcSettlementGroupIDType),
        ("reserve2", TThostFtdcOldInstrumentIDType),
        ("InstrumentStatus", TThostFtdcInstrumentStatusType),
        ("TradingSegmentSN", TThostFtdcTradingSegmentSNType),
        ("EnterTime", TThostFtdcTimeType),
        ("EnterReason", TThostFtdcInstStatusEnterReasonType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcQryInstrumentStatusField(Structure):
    """查询合约状态"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("reserve1", TThostFtdcOldExchangeInstIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        
    ]
    
class  CThostFtdcInvestorAccountField(Structure):
    """投资者账户"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        
    ]
    
class  CThostFtdcPositionProfitAlgorithmField(Structure):
    """浮动盈亏算法"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("Algorithm", TThostFtdcAlgorithmType),
        ("Memo", TThostFtdcMemoType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        
    ]
    
class  CThostFtdcDiscountField(Structure):
    """会员资金折扣"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorRange", TThostFtdcInvestorRangeType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("Discount", TThostFtdcRatioType),
        
    ]
    
class  CThostFtdcQryTransferBankField(Structure):
    """查询转帐银行"""
    _fields_ = [
        ("BankID", TThostFtdcBankIDType),
        ("BankBrchID", TThostFtdcBankBrchIDType),
        
    ]
    
class  CThostFtdcTransferBankField(Structure):
    """转帐银行"""
    _fields_ = [
        ("BankID", TThostFtdcBankIDType),
        ("BankBrchID", TThostFtdcBankBrchIDType),
        ("BankName", TThostFtdcBankNameType),
        ("IsActive", TThostFtdcBoolType),
        
    ]
    
class  CThostFtdcQryInvestorPositionDetailField(Structure):
    """查询投资者持仓明细"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcInvestorPositionDetailField(Structure):
    """投资者持仓明细"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("HedgeFlag", TThostFtdcHedgeFlagType),
        ("Direction", TThostFtdcDirectionType),
        ("OpenDate", TThostFtdcDateType),
        ("TradeID", TThostFtdcTradeIDType),
        ("Volume", TThostFtdcVolumeType),
        ("OpenPrice", TThostFtdcPriceType),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("TradeType", TThostFtdcTradeTypeType),
        ("reserve2", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("CloseProfitByDate", TThostFtdcMoneyType),
        ("CloseProfitByTrade", TThostFtdcMoneyType),
        ("PositionProfitByDate", TThostFtdcMoneyType),
        ("PositionProfitByTrade", TThostFtdcMoneyType),
        ("Margin", TThostFtdcMoneyType),
        ("ExchMargin", TThostFtdcMoneyType),
        ("MarginRateByMoney", TThostFtdcRatioType),
        ("MarginRateByVolume", TThostFtdcRatioType),
        ("LastSettlementPrice", TThostFtdcPriceType),
        ("SettlementPrice", TThostFtdcPriceType),
        ("CloseVolume", TThostFtdcVolumeType),
        ("CloseAmount", TThostFtdcMoneyType),
        ("TimeFirstVolume", TThostFtdcVolumeType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("SpecPosiType", TThostFtdcSpecPosiTypeType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("CombInstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcTradingAccountPasswordField(Structure):
    """资金账户口令域"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("Password", TThostFtdcPasswordType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        
    ]
    
class  CThostFtdcMDTraderOfferField(Structure):
    """交易所行情报盘机"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("Password", TThostFtdcPasswordType),
        ("InstallID", TThostFtdcInstallIDType),
        ("OrderLocalID", TThostFtdcOrderLocalIDType),
        ("TraderConnectStatus", TThostFtdcTraderConnectStatusType),
        ("ConnectRequestDate", TThostFtdcDateType),
        ("ConnectRequestTime", TThostFtdcTimeType),
        ("LastReportDate", TThostFtdcDateType),
        ("LastReportTime", TThostFtdcTimeType),
        ("ConnectDate", TThostFtdcDateType),
        ("ConnectTime", TThostFtdcTimeType),
        ("StartDate", TThostFtdcDateType),
        ("StartTime", TThostFtdcTimeType),
        ("TradingDay", TThostFtdcDateType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("MaxTradeID", TThostFtdcTradeIDType),
        ("MaxOrderMessageReference", TThostFtdcReturnCodeType),
        ("OrderCancelAlg", TThostFtdcOrderCancelAlgType),
        
    ]
    
class  CThostFtdcQryMDTraderOfferField(Structure):
    """查询行情报盘机"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("TraderID", TThostFtdcTraderIDType),
        
    ]
    
class  CThostFtdcQryNoticeField(Structure):
    """查询客户通知"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        
    ]
    
class  CThostFtdcNoticeField(Structure):
    """客户通知"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("Content", TThostFtdcContentType),
        ("SequenceLabel", TThostFtdcSequenceLabelType),
        
    ]
    
class  CThostFtdcUserRightField(Structure):
    """用户权限"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("UserRightType", TThostFtdcUserRightTypeType),
        ("IsForbidden", TThostFtdcBoolType),
        
    ]
    
class  CThostFtdcQrySettlementInfoConfirmField(Structure):
    """查询结算信息确认域"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        
    ]
    
class  CThostFtdcLoadSettlementInfoField(Structure):
    """装载结算信息"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        
    ]
    
class  CThostFtdcBrokerWithdrawAlgorithmField(Structure):
    """经纪公司可提资金算法表"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("WithdrawAlgorithm", TThostFtdcAlgorithmType),
        ("UsingRatio", TThostFtdcRatioType),
        ("IncludeCloseProfit", TThostFtdcIncludeCloseProfitType),
        ("AllWithoutTrade", TThostFtdcAllWithoutTradeType),
        ("AvailIncludeCloseProfit", TThostFtdcIncludeCloseProfitType),
        ("IsBrokerUserEvent", TThostFtdcBoolType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("FundMortgageRatio", TThostFtdcRatioType),
        ("BalanceAlgorithm", TThostFtdcBalanceAlgorithmType),
        
    ]
    
class  CThostFtdcTradingAccountPasswordUpdateV1Field(Structure):
    """资金账户口令变更域"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("OldPassword", TThostFtdcPasswordType),
        ("NewPassword", TThostFtdcPasswordType),
        
    ]
    
class  CThostFtdcTradingAccountPasswordUpdateField(Structure):
    """资金账户口令变更域"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("OldPassword", TThostFtdcPasswordType),
        ("NewPassword", TThostFtdcPasswordType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        
    ]
    
class  CThostFtdcQryCombinationLegField(Structure):
    """查询组合合约分腿"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("LegID", TThostFtdcLegIDType),
        ("reserve2", TThostFtdcOldInstrumentIDType),
        ("CombInstrumentID", TThostFtdcInstrumentIDType),
        ("LegInstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcQrySyncStatusField(Structure):
    """查询组合合约分腿"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        
    ]
    
class  CThostFtdcCombinationLegField(Structure):
    """组合交易合约的单腿"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("LegID", TThostFtdcLegIDType),
        ("reserve2", TThostFtdcOldInstrumentIDType),
        ("Direction", TThostFtdcDirectionType),
        ("LegMultiple", TThostFtdcLegMultipleType),
        ("ImplyLevel", TThostFtdcImplyLevelType),
        ("CombInstrumentID", TThostFtdcInstrumentIDType),
        ("LegInstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcSyncStatusField(Structure):
    """数据同步状态"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("DataSyncStatus", TThostFtdcDataSyncStatusType),
        
    ]
    
class  CThostFtdcQryLinkManField(Structure):
    """查询联系人"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        
    ]
    
class  CThostFtdcLinkManField(Structure):
    """联系人"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("PersonType", TThostFtdcPersonTypeType),
        ("IdentifiedCardType", TThostFtdcIdCardTypeType),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("PersonName", TThostFtdcPartyNameType),
        ("Telephone", TThostFtdcTelephoneType),
        ("Address", TThostFtdcAddressType),
        ("ZipCode", TThostFtdcZipCodeType),
        ("Priority", TThostFtdcPriorityType),
        ("UOAZipCode", TThostFtdcUOAZipCodeType),
        ("PersonFullName", TThostFtdcInvestorFullNameType),
        
    ]
    
class  CThostFtdcQryBrokerUserEventField(Structure):
    """查询经纪公司用户事件"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("UserEventType", TThostFtdcUserEventTypeType),
        
    ]
    
class  CThostFtdcBrokerUserEventField(Structure):
    """查询经纪公司用户事件"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("UserEventType", TThostFtdcUserEventTypeType),
        ("EventSequenceNo", TThostFtdcSequenceNoType),
        ("EventDate", TThostFtdcDateType),
        ("EventTime", TThostFtdcTimeType),
        ("UserEventInfo", TThostFtdcUserEventInfoType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcQryContractBankField(Structure):
    """查询签约银行请求"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBrchID", TThostFtdcBankBrchIDType),
        
    ]
    
class  CThostFtdcContractBankField(Structure):
    """查询签约银行响应"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBrchID", TThostFtdcBankBrchIDType),
        ("BankName", TThostFtdcBankNameType),
        
    ]
    
class  CThostFtdcInvestorPositionCombineDetailField(Structure):
    """投资者组合持仓明细"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("OpenDate", TThostFtdcDateType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("ComTradeID", TThostFtdcTradeIDType),
        ("TradeID", TThostFtdcTradeIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("HedgeFlag", TThostFtdcHedgeFlagType),
        ("Direction", TThostFtdcDirectionType),
        ("TotalAmt", TThostFtdcVolumeType),
        ("Margin", TThostFtdcMoneyType),
        ("ExchMargin", TThostFtdcMoneyType),
        ("MarginRateByMoney", TThostFtdcRatioType),
        ("MarginRateByVolume", TThostFtdcRatioType),
        ("LegID", TThostFtdcLegIDType),
        ("LegMultiple", TThostFtdcLegMultipleType),
        ("reserve2", TThostFtdcOldInstrumentIDType),
        ("TradeGroupID", TThostFtdcTradeGroupIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("CombInstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcParkedOrderField(Structure):
    """预埋单"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("OrderRef", TThostFtdcOrderRefType),
        ("UserID", TThostFtdcUserIDType),
        ("OrderPriceType", TThostFtdcOrderPriceTypeType),
        ("Direction", TThostFtdcDirectionType),
        ("CombOffsetFlag", TThostFtdcCombOffsetFlagType),
        ("CombHedgeFlag", TThostFtdcCombHedgeFlagType),
        ("LimitPrice", TThostFtdcPriceType),
        ("VolumeTotalOriginal", TThostFtdcVolumeType),
        ("TimeCondition", TThostFtdcTimeConditionType),
        ("GTDDate", TThostFtdcDateType),
        ("VolumeCondition", TThostFtdcVolumeConditionType),
        ("MinVolume", TThostFtdcVolumeType),
        ("ContingentCondition", TThostFtdcContingentConditionType),
        ("StopPrice", TThostFtdcPriceType),
        ("ForceCloseReason", TThostFtdcForceCloseReasonType),
        ("IsAutoSuspend", TThostFtdcBoolType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("RequestID", TThostFtdcRequestIDType),
        ("UserForceClose", TThostFtdcBoolType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ParkedOrderID", TThostFtdcParkedOrderIDType),
        ("UserType", TThostFtdcUserTypeType),
        ("Status", TThostFtdcParkedOrderStatusType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        ("IsSwapOrder", TThostFtdcBoolType),
        ("AccountID", TThostFtdcAccountIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcParkedOrderActionField(Structure):
    """输入预埋单操作"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("OrderActionRef", TThostFtdcOrderActionRefType),
        ("OrderRef", TThostFtdcOrderRefType),
        ("RequestID", TThostFtdcRequestIDType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("OrderSysID", TThostFtdcOrderSysIDType),
        ("ActionFlag", TThostFtdcActionFlagType),
        ("LimitPrice", TThostFtdcPriceType),
        ("VolumeChange", TThostFtdcVolumeType),
        ("UserID", TThostFtdcUserIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ParkedOrderActionID", TThostFtdcParkedOrderActionIDType),
        ("UserType", TThostFtdcUserTypeType),
        ("Status", TThostFtdcParkedOrderStatusType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcQryParkedOrderField(Structure):
    """查询预埋单"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcQryParkedOrderActionField(Structure):
    """查询预埋撤单"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcRemoveParkedOrderField(Structure):
    """删除预埋单"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("ParkedOrderID", TThostFtdcParkedOrderIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        
    ]
    
class  CThostFtdcRemoveParkedOrderActionField(Structure):
    """删除预埋撤单"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("ParkedOrderActionID", TThostFtdcParkedOrderActionIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        
    ]
    
class  CThostFtdcInvestorWithdrawAlgorithmField(Structure):
    """经纪公司可提资金算法表"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorRange", TThostFtdcInvestorRangeType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("UsingRatio", TThostFtdcRatioType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("FundMortgageRatio", TThostFtdcRatioType),
        
    ]
    
class  CThostFtdcQryInvestorPositionCombineDetailField(Structure):
    """查询组合持仓明细"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("CombInstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcMarketDataAveragePriceField(Structure):
    """成交均价"""
    _fields_ = [
        ("AveragePrice", TThostFtdcPriceType),
        
    ]
    
class  CThostFtdcVerifyInvestorPasswordField(Structure):
    """校验投资者密码"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("Password", TThostFtdcPasswordType),
        
    ]
    
class  CThostFtdcUserIPField(Structure):
    """用户IP"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("reserve1", TThostFtdcOldIPAddressType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("IPAddress", TThostFtdcIPAddressType),
        ("IPMask", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcTradingNoticeInfoField(Structure):
    """用户事件通知信息"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("SendTime", TThostFtdcTimeType),
        ("FieldContent", TThostFtdcContentType),
        ("SequenceSeries", TThostFtdcSequenceSeriesType),
        ("SequenceNo", TThostFtdcSequenceNoType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        
    ]
    
class  CThostFtdcTradingNoticeField(Structure):
    """用户事件通知"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorRange", TThostFtdcInvestorRangeType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("SequenceSeries", TThostFtdcSequenceSeriesType),
        ("UserID", TThostFtdcUserIDType),
        ("SendTime", TThostFtdcTimeType),
        ("SequenceNo", TThostFtdcSequenceNoType),
        ("FieldContent", TThostFtdcContentType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        
    ]
    
class  CThostFtdcQryTradingNoticeField(Structure):
    """查询交易事件通知"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        
    ]
    
class  CThostFtdcQryErrOrderField(Structure):
    """查询错误报单"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        
    ]
    
class  CThostFtdcErrOrderField(Structure):
    """错误报单"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("OrderRef", TThostFtdcOrderRefType),
        ("UserID", TThostFtdcUserIDType),
        ("OrderPriceType", TThostFtdcOrderPriceTypeType),
        ("Direction", TThostFtdcDirectionType),
        ("CombOffsetFlag", TThostFtdcCombOffsetFlagType),
        ("CombHedgeFlag", TThostFtdcCombHedgeFlagType),
        ("LimitPrice", TThostFtdcPriceType),
        ("VolumeTotalOriginal", TThostFtdcVolumeType),
        ("TimeCondition", TThostFtdcTimeConditionType),
        ("GTDDate", TThostFtdcDateType),
        ("VolumeCondition", TThostFtdcVolumeConditionType),
        ("MinVolume", TThostFtdcVolumeType),
        ("ContingentCondition", TThostFtdcContingentConditionType),
        ("StopPrice", TThostFtdcPriceType),
        ("ForceCloseReason", TThostFtdcForceCloseReasonType),
        ("IsAutoSuspend", TThostFtdcBoolType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("RequestID", TThostFtdcRequestIDType),
        ("UserForceClose", TThostFtdcBoolType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        ("IsSwapOrder", TThostFtdcBoolType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcErrorConditionalOrderField(Structure):
    """查询错误报单操作"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("OrderRef", TThostFtdcOrderRefType),
        ("UserID", TThostFtdcUserIDType),
        ("OrderPriceType", TThostFtdcOrderPriceTypeType),
        ("Direction", TThostFtdcDirectionType),
        ("CombOffsetFlag", TThostFtdcCombOffsetFlagType),
        ("CombHedgeFlag", TThostFtdcCombHedgeFlagType),
        ("LimitPrice", TThostFtdcPriceType),
        ("VolumeTotalOriginal", TThostFtdcVolumeType),
        ("TimeCondition", TThostFtdcTimeConditionType),
        ("GTDDate", TThostFtdcDateType),
        ("VolumeCondition", TThostFtdcVolumeConditionType),
        ("MinVolume", TThostFtdcVolumeType),
        ("ContingentCondition", TThostFtdcContingentConditionType),
        ("StopPrice", TThostFtdcPriceType),
        ("ForceCloseReason", TThostFtdcForceCloseReasonType),
        ("IsAutoSuspend", TThostFtdcBoolType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("RequestID", TThostFtdcRequestIDType),
        ("OrderLocalID", TThostFtdcOrderLocalIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("reserve2", TThostFtdcOldExchangeInstIDType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("OrderSubmitStatus", TThostFtdcOrderSubmitStatusType),
        ("NotifySequence", TThostFtdcSequenceNoType),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("OrderSysID", TThostFtdcOrderSysIDType),
        ("OrderSource", TThostFtdcOrderSourceType),
        ("OrderStatus", TThostFtdcOrderStatusType),
        ("OrderType", TThostFtdcOrderTypeType),
        ("VolumeTraded", TThostFtdcVolumeType),
        ("VolumeTotal", TThostFtdcVolumeType),
        ("InsertDate", TThostFtdcDateType),
        ("InsertTime", TThostFtdcTimeType),
        ("ActiveTime", TThostFtdcTimeType),
        ("SuspendTime", TThostFtdcTimeType),
        ("UpdateTime", TThostFtdcTimeType),
        ("CancelTime", TThostFtdcTimeType),
        ("ActiveTraderID", TThostFtdcTraderIDType),
        ("ClearingPartID", TThostFtdcParticipantIDType),
        ("SequenceNo", TThostFtdcSequenceNoType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("UserProductInfo", TThostFtdcProductInfoType),
        ("StatusMsg", TThostFtdcErrorMsgType),
        ("UserForceClose", TThostFtdcBoolType),
        ("ActiveUserID", TThostFtdcUserIDType),
        ("BrokerOrderSeq", TThostFtdcSequenceNoType),
        ("RelativeOrderSysID", TThostFtdcOrderSysIDType),
        ("ZCETotalTradedVolume", TThostFtdcVolumeType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        ("IsSwapOrder", TThostFtdcBoolType),
        ("BranchID", TThostFtdcBranchIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("reserve3", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcQryErrOrderActionField(Structure):
    """查询错误报单操作"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        
    ]
    
class  CThostFtdcErrOrderActionField(Structure):
    """错误报单操作"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("OrderActionRef", TThostFtdcOrderActionRefType),
        ("OrderRef", TThostFtdcOrderRefType),
        ("RequestID", TThostFtdcRequestIDType),
        ("FrontID", TThostFtdcFrontIDType),
        ("SessionID", TThostFtdcSessionIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("OrderSysID", TThostFtdcOrderSysIDType),
        ("ActionFlag", TThostFtdcActionFlagType),
        ("LimitPrice", TThostFtdcPriceType),
        ("VolumeChange", TThostFtdcVolumeType),
        ("ActionDate", TThostFtdcDateType),
        ("ActionTime", TThostFtdcTimeType),
        ("TraderID", TThostFtdcTraderIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("OrderLocalID", TThostFtdcOrderLocalIDType),
        ("ActionLocalID", TThostFtdcOrderLocalIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ClientID", TThostFtdcClientIDType),
        ("BusinessUnit", TThostFtdcBusinessUnitType),
        ("OrderActionStatus", TThostFtdcOrderActionStatusType),
        ("UserID", TThostFtdcUserIDType),
        ("StatusMsg", TThostFtdcErrorMsgType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("BranchID", TThostFtdcBranchIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("reserve2", TThostFtdcOldIPAddressType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcQryExchangeSequenceField(Structure):
    """查询交易所状态"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        
    ]
    
class  CThostFtdcExchangeSequenceField(Structure):
    """交易所状态"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("SequenceNo", TThostFtdcSequenceNoType),
        ("MarketStatus", TThostFtdcInstrumentStatusType),
        
    ]
    
class  CThostFtdcQryMaxOrderVolumeWithPriceField(Structure):
    """根据价格查询最大报单数量"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("Direction", TThostFtdcDirectionType),
        ("OffsetFlag", TThostFtdcOffsetFlagType),
        ("HedgeFlag", TThostFtdcHedgeFlagType),
        ("MaxVolume", TThostFtdcVolumeType),
        ("Price", TThostFtdcPriceType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcQryBrokerTradingParamsField(Structure):
    """查询经纪公司交易参数"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("AccountID", TThostFtdcAccountIDType),
        
    ]
    
class  CThostFtdcBrokerTradingParamsField(Structure):
    """经纪公司交易参数"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("MarginPriceType", TThostFtdcMarginPriceTypeType),
        ("Algorithm", TThostFtdcAlgorithmType),
        ("AvailIncludeCloseProfit", TThostFtdcIncludeCloseProfitType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("OptionRoyaltyPriceType", TThostFtdcOptionRoyaltyPriceTypeType),
        ("AccountID", TThostFtdcAccountIDType),
        
    ]
    
class  CThostFtdcQryBrokerTradingAlgosField(Structure):
    """查询经纪公司交易算法"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcBrokerTradingAlgosField(Structure):
    """经纪公司交易算法"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("HandlePositionAlgoID", TThostFtdcHandlePositionAlgoIDType),
        ("FindMarginRateAlgoID", TThostFtdcFindMarginRateAlgoIDType),
        ("HandleTradingAccountAlgoID", TThostFtdcHandleTradingAccountAlgoIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcQueryBrokerDepositField(Structure):
    """查询经纪公司资金"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        
    ]
    
class  CThostFtdcBrokerDepositField(Structure):
    """经纪公司资金"""
    _fields_ = [
        ("TradingDay", TThostFtdcTradeDateType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("PreBalance", TThostFtdcMoneyType),
        ("CurrMargin", TThostFtdcMoneyType),
        ("CloseProfit", TThostFtdcMoneyType),
        ("Balance", TThostFtdcMoneyType),
        ("Deposit", TThostFtdcMoneyType),
        ("Withdraw", TThostFtdcMoneyType),
        ("Available", TThostFtdcMoneyType),
        ("Reserve", TThostFtdcMoneyType),
        ("FrozenMargin", TThostFtdcMoneyType),
        
    ]
    
class  CThostFtdcQryCFMMCBrokerKeyField(Structure):
    """查询保证金监管系统经纪公司密钥"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        
    ]
    
class  CThostFtdcCFMMCBrokerKeyField(Structure):
    """保证金监管系统经纪公司密钥"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("CreateDate", TThostFtdcDateType),
        ("CreateTime", TThostFtdcTimeType),
        ("KeyID", TThostFtdcSequenceNoType),
        ("CurrentKey", TThostFtdcCFMMCKeyType),
        ("KeyKind", TThostFtdcCFMMCKeyKindType),
        
    ]
    
class  CThostFtdcCFMMCTradingAccountKeyField(Structure):
    """保证金监管系统经纪公司资金账户密钥"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("KeyID", TThostFtdcSequenceNoType),
        ("CurrentKey", TThostFtdcCFMMCKeyType),
        
    ]
    
class  CThostFtdcQryCFMMCTradingAccountKeyField(Structure):
    """请求查询保证金监管系统经纪公司资金账户密钥"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        
    ]
    
class  CThostFtdcBrokerUserOTPParamField(Structure):
    """用户动态令牌参数"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("OTPVendorsID", TThostFtdcOTPVendorsIDType),
        ("SerialNumber", TThostFtdcSerialNumberType),
        ("AuthKey", TThostFtdcAuthKeyType),
        ("LastDrift", TThostFtdcLastDriftType),
        ("LastSuccess", TThostFtdcLastSuccessType),
        ("OTPType", TThostFtdcOTPTypeType),
        
    ]
    
class  CThostFtdcManualSyncBrokerUserOTPField(Structure):
    """手工同步用户动态令牌"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("OTPType", TThostFtdcOTPTypeType),
        ("FirstOTP", TThostFtdcPasswordType),
        ("SecondOTP", TThostFtdcPasswordType),
        
    ]
    
class  CThostFtdcCommRateModelField(Structure):
    """投资者手续费率模板"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("CommModelID", TThostFtdcInvestorIDType),
        ("CommModelName", TThostFtdcCommModelNameType),
        
    ]
    
class  CThostFtdcQryCommRateModelField(Structure):
    """请求查询投资者手续费率模板"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("CommModelID", TThostFtdcInvestorIDType),
        
    ]
    
class  CThostFtdcMarginModelField(Structure):
    """投资者保证金率模板"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("MarginModelID", TThostFtdcInvestorIDType),
        ("MarginModelName", TThostFtdcCommModelNameType),
        
    ]
    
class  CThostFtdcQryMarginModelField(Structure):
    """请求查询投资者保证金率模板"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("MarginModelID", TThostFtdcInvestorIDType),
        
    ]
    
class  CThostFtdcEWarrantOffsetField(Structure):
    """仓单折抵信息"""
    _fields_ = [
        ("TradingDay", TThostFtdcTradeDateType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("Direction", TThostFtdcDirectionType),
        ("HedgeFlag", TThostFtdcHedgeFlagType),
        ("Volume", TThostFtdcVolumeType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcQryEWarrantOffsetField(Structure):
    """查询仓单折抵信息"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcQryInvestorProductGroupMarginField(Structure):
    """查询投资者品种/跨品种保证金"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("HedgeFlag", TThostFtdcHedgeFlagType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("ProductGroupID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcInvestorProductGroupMarginField(Structure):
    """投资者品种/跨品种保证金"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("FrozenMargin", TThostFtdcMoneyType),
        ("LongFrozenMargin", TThostFtdcMoneyType),
        ("ShortFrozenMargin", TThostFtdcMoneyType),
        ("UseMargin", TThostFtdcMoneyType),
        ("LongUseMargin", TThostFtdcMoneyType),
        ("ShortUseMargin", TThostFtdcMoneyType),
        ("ExchMargin", TThostFtdcMoneyType),
        ("LongExchMargin", TThostFtdcMoneyType),
        ("ShortExchMargin", TThostFtdcMoneyType),
        ("CloseProfit", TThostFtdcMoneyType),
        ("FrozenCommission", TThostFtdcMoneyType),
        ("Commission", TThostFtdcMoneyType),
        ("FrozenCash", TThostFtdcMoneyType),
        ("CashIn", TThostFtdcMoneyType),
        ("PositionProfit", TThostFtdcMoneyType),
        ("OffsetAmount", TThostFtdcMoneyType),
        ("LongOffsetAmount", TThostFtdcMoneyType),
        ("ShortOffsetAmount", TThostFtdcMoneyType),
        ("ExchOffsetAmount", TThostFtdcMoneyType),
        ("LongExchOffsetAmount", TThostFtdcMoneyType),
        ("ShortExchOffsetAmount", TThostFtdcMoneyType),
        ("HedgeFlag", TThostFtdcHedgeFlagType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("ProductGroupID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcQueryCFMMCTradingAccountTokenField(Structure):
    """查询监控中心用户令牌"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        
    ]
    
class  CThostFtdcCFMMCTradingAccountTokenField(Structure):
    """监控中心用户令牌"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("ParticipantID", TThostFtdcParticipantIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("KeyID", TThostFtdcSequenceNoType),
        ("Token", TThostFtdcCFMMCTokenType),
        
    ]
    
class  CThostFtdcQryProductGroupField(Structure):
    """查询产品组"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ProductID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcProductGroupField(Structure):
    """投资者品种/跨品种保证金产品组"""
    _fields_ = [
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("reserve2", TThostFtdcOldInstrumentIDType),
        ("ProductID", TThostFtdcInstrumentIDType),
        ("ProductGroupID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcBulletinField(Structure):
    """交易所公告"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("TradingDay", TThostFtdcDateType),
        ("BulletinID", TThostFtdcBulletinIDType),
        ("SequenceNo", TThostFtdcSequenceNoType),
        ("NewsType", TThostFtdcNewsTypeType),
        ("NewsUrgency", TThostFtdcNewsUrgencyType),
        ("SendTime", TThostFtdcTimeType),
        ("Abstract", TThostFtdcAbstractType),
        ("ComeFrom", TThostFtdcComeFromType),
        ("Content", TThostFtdcContentType),
        ("URLLink", TThostFtdcURLLinkType),
        ("MarketID", TThostFtdcMarketIDType),
        
    ]
    
class  CThostFtdcQryBulletinField(Structure):
    """查询交易所公告"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("BulletinID", TThostFtdcBulletinIDType),
        ("SequenceNo", TThostFtdcSequenceNoType),
        ("NewsType", TThostFtdcNewsTypeType),
        ("NewsUrgency", TThostFtdcNewsUrgencyType),
        
    ]
    
class  CThostFtdcMulticastInstrumentField(Structure):
    """MulticastInstrument"""
    _fields_ = [
        ("TopicID", TThostFtdcInstallIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InstrumentNo", TThostFtdcInstallIDType),
        ("CodePrice", TThostFtdcPriceType),
        ("VolumeMultiple", TThostFtdcVolumeMultipleType),
        ("PriceTick", TThostFtdcPriceType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcQryMulticastInstrumentField(Structure):
    """QryMulticastInstrument"""
    _fields_ = [
        ("TopicID", TThostFtdcInstallIDType),
        ("reserve1", TThostFtdcOldInstrumentIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcAppIDAuthAssignField(Structure):
    """App客户端权限分配"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("AppID", TThostFtdcAppIDType),
        ("DRIdentityID", TThostFtdcDRIdentityIDType),
        
    ]
    
class  CThostFtdcReqOpenAccountField(Structure):
    """转帐开户请求"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", TThostFtdcLastFragmentType),
        ("SessionID", TThostFtdcSessionIDType),
        ("CustomerName", TThostFtdcIndividualNameType),
        ("IdCardType", TThostFtdcIdCardTypeType),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("Gender", TThostFtdcGenderType),
        ("CountryCode", TThostFtdcCountryCodeType),
        ("CustType", TThostFtdcCustTypeType),
        ("Address", TThostFtdcAddressType),
        ("ZipCode", TThostFtdcZipCodeType),
        ("Telephone", TThostFtdcTelephoneType),
        ("MobilePhone", TThostFtdcMobilePhoneType),
        ("Fax", TThostFtdcFaxType),
        ("EMail", TThostFtdcEMailType),
        ("MoneyAccountStatus", TThostFtdcMoneyAccountStatusType),
        ("BankAccount", TThostFtdcBankAccountType),
        ("BankPassWord", TThostFtdcPasswordType),
        ("AccountID", TThostFtdcAccountIDType),
        ("Password", TThostFtdcPasswordType),
        ("InstallID", TThostFtdcInstallIDType),
        ("VerifyCertNoFlag", TThostFtdcYesNoIndicatorType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("CashExchangeCode", TThostFtdcCashExchangeCodeType),
        ("Digest", TThostFtdcDigestType),
        ("BankAccType", TThostFtdcBankAccTypeType),
        ("DeviceID", TThostFtdcDeviceIDType),
        ("BankSecuAccType", TThostFtdcBankAccTypeType),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("BankSecuAcc", TThostFtdcBankAccountType),
        ("BankPwdFlag", TThostFtdcPwdFlagType),
        ("SecuPwdFlag", TThostFtdcPwdFlagType),
        ("OperNo", TThostFtdcOperNoType),
        ("TID", TThostFtdcTIDType),
        ("UserID", TThostFtdcUserIDType),
        ("LongCustomerName", TThostFtdcLongIndividualNameType),
        
    ]
    
class  CThostFtdcReqCancelAccountField(Structure):
    """转帐销户请求"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", TThostFtdcLastFragmentType),
        ("SessionID", TThostFtdcSessionIDType),
        ("CustomerName", TThostFtdcIndividualNameType),
        ("IdCardType", TThostFtdcIdCardTypeType),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("Gender", TThostFtdcGenderType),
        ("CountryCode", TThostFtdcCountryCodeType),
        ("CustType", TThostFtdcCustTypeType),
        ("Address", TThostFtdcAddressType),
        ("ZipCode", TThostFtdcZipCodeType),
        ("Telephone", TThostFtdcTelephoneType),
        ("MobilePhone", TThostFtdcMobilePhoneType),
        ("Fax", TThostFtdcFaxType),
        ("EMail", TThostFtdcEMailType),
        ("MoneyAccountStatus", TThostFtdcMoneyAccountStatusType),
        ("BankAccount", TThostFtdcBankAccountType),
        ("BankPassWord", TThostFtdcPasswordType),
        ("AccountID", TThostFtdcAccountIDType),
        ("Password", TThostFtdcPasswordType),
        ("InstallID", TThostFtdcInstallIDType),
        ("VerifyCertNoFlag", TThostFtdcYesNoIndicatorType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("CashExchangeCode", TThostFtdcCashExchangeCodeType),
        ("Digest", TThostFtdcDigestType),
        ("BankAccType", TThostFtdcBankAccTypeType),
        ("DeviceID", TThostFtdcDeviceIDType),
        ("BankSecuAccType", TThostFtdcBankAccTypeType),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("BankSecuAcc", TThostFtdcBankAccountType),
        ("BankPwdFlag", TThostFtdcPwdFlagType),
        ("SecuPwdFlag", TThostFtdcPwdFlagType),
        ("OperNo", TThostFtdcOperNoType),
        ("TID", TThostFtdcTIDType),
        ("UserID", TThostFtdcUserIDType),
        ("LongCustomerName", TThostFtdcLongIndividualNameType),
        
    ]
    
class  CThostFtdcReqChangeAccountField(Structure):
    """变更银行账户请求"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", TThostFtdcLastFragmentType),
        ("SessionID", TThostFtdcSessionIDType),
        ("CustomerName", TThostFtdcIndividualNameType),
        ("IdCardType", TThostFtdcIdCardTypeType),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("Gender", TThostFtdcGenderType),
        ("CountryCode", TThostFtdcCountryCodeType),
        ("CustType", TThostFtdcCustTypeType),
        ("Address", TThostFtdcAddressType),
        ("ZipCode", TThostFtdcZipCodeType),
        ("Telephone", TThostFtdcTelephoneType),
        ("MobilePhone", TThostFtdcMobilePhoneType),
        ("Fax", TThostFtdcFaxType),
        ("EMail", TThostFtdcEMailType),
        ("MoneyAccountStatus", TThostFtdcMoneyAccountStatusType),
        ("BankAccount", TThostFtdcBankAccountType),
        ("BankPassWord", TThostFtdcPasswordType),
        ("NewBankAccount", TThostFtdcBankAccountType),
        ("NewBankPassWord", TThostFtdcPasswordType),
        ("AccountID", TThostFtdcAccountIDType),
        ("Password", TThostFtdcPasswordType),
        ("BankAccType", TThostFtdcBankAccTypeType),
        ("InstallID", TThostFtdcInstallIDType),
        ("VerifyCertNoFlag", TThostFtdcYesNoIndicatorType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("BankPwdFlag", TThostFtdcPwdFlagType),
        ("SecuPwdFlag", TThostFtdcPwdFlagType),
        ("TID", TThostFtdcTIDType),
        ("Digest", TThostFtdcDigestType),
        ("LongCustomerName", TThostFtdcLongIndividualNameType),
        
    ]
    
class  CThostFtdcReqTransferField(Structure):
    """转账请求"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", TThostFtdcLastFragmentType),
        ("SessionID", TThostFtdcSessionIDType),
        ("CustomerName", TThostFtdcIndividualNameType),
        ("IdCardType", TThostFtdcIdCardTypeType),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("CustType", TThostFtdcCustTypeType),
        ("BankAccount", TThostFtdcBankAccountType),
        ("BankPassWord", TThostFtdcPasswordType),
        ("AccountID", TThostFtdcAccountIDType),
        ("Password", TThostFtdcPasswordType),
        ("InstallID", TThostFtdcInstallIDType),
        ("FutureSerial", TThostFtdcFutureSerialType),
        ("UserID", TThostFtdcUserIDType),
        ("VerifyCertNoFlag", TThostFtdcYesNoIndicatorType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("TradeAmount", TThostFtdcTradeAmountType),
        ("FutureFetchAmount", TThostFtdcTradeAmountType),
        ("FeePayFlag", TThostFtdcFeePayFlagType),
        ("CustFee", TThostFtdcCustFeeType),
        ("BrokerFee", TThostFtdcFutureFeeType),
        ("Message", TThostFtdcAddInfoType),
        ("Digest", TThostFtdcDigestType),
        ("BankAccType", TThostFtdcBankAccTypeType),
        ("DeviceID", TThostFtdcDeviceIDType),
        ("BankSecuAccType", TThostFtdcBankAccTypeType),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("BankSecuAcc", TThostFtdcBankAccountType),
        ("BankPwdFlag", TThostFtdcPwdFlagType),
        ("SecuPwdFlag", TThostFtdcPwdFlagType),
        ("OperNo", TThostFtdcOperNoType),
        ("RequestID", TThostFtdcRequestIDType),
        ("TID", TThostFtdcTIDType),
        ("TransferStatus", TThostFtdcTransferStatusType),
        ("LongCustomerName", TThostFtdcLongIndividualNameType),
        
    ]
    
class  CThostFtdcRspTransferField(Structure):
    """银行发起银行资金转期货响应"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", TThostFtdcLastFragmentType),
        ("SessionID", TThostFtdcSessionIDType),
        ("CustomerName", TThostFtdcIndividualNameType),
        ("IdCardType", TThostFtdcIdCardTypeType),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("CustType", TThostFtdcCustTypeType),
        ("BankAccount", TThostFtdcBankAccountType),
        ("BankPassWord", TThostFtdcPasswordType),
        ("AccountID", TThostFtdcAccountIDType),
        ("Password", TThostFtdcPasswordType),
        ("InstallID", TThostFtdcInstallIDType),
        ("FutureSerial", TThostFtdcFutureSerialType),
        ("UserID", TThostFtdcUserIDType),
        ("VerifyCertNoFlag", TThostFtdcYesNoIndicatorType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("TradeAmount", TThostFtdcTradeAmountType),
        ("FutureFetchAmount", TThostFtdcTradeAmountType),
        ("FeePayFlag", TThostFtdcFeePayFlagType),
        ("CustFee", TThostFtdcCustFeeType),
        ("BrokerFee", TThostFtdcFutureFeeType),
        ("Message", TThostFtdcAddInfoType),
        ("Digest", TThostFtdcDigestType),
        ("BankAccType", TThostFtdcBankAccTypeType),
        ("DeviceID", TThostFtdcDeviceIDType),
        ("BankSecuAccType", TThostFtdcBankAccTypeType),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("BankSecuAcc", TThostFtdcBankAccountType),
        ("BankPwdFlag", TThostFtdcPwdFlagType),
        ("SecuPwdFlag", TThostFtdcPwdFlagType),
        ("OperNo", TThostFtdcOperNoType),
        ("RequestID", TThostFtdcRequestIDType),
        ("TID", TThostFtdcTIDType),
        ("TransferStatus", TThostFtdcTransferStatusType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        ("LongCustomerName", TThostFtdcLongIndividualNameType),
        
    ]
    
class  CThostFtdcReqRepealField(Structure):
    """冲正请求"""
    _fields_ = [
        ("RepealTimeInterval", TThostFtdcRepealTimeIntervalType),
        ("RepealedTimes", TThostFtdcRepealedTimesType),
        ("BankRepealFlag", TThostFtdcBankRepealFlagType),
        ("BrokerRepealFlag", TThostFtdcBrokerRepealFlagType),
        ("PlateRepealSerial", TThostFtdcPlateSerialType),
        ("BankRepealSerial", TThostFtdcBankSerialType),
        ("FutureRepealSerial", TThostFtdcFutureSerialType),
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", TThostFtdcLastFragmentType),
        ("SessionID", TThostFtdcSessionIDType),
        ("CustomerName", TThostFtdcIndividualNameType),
        ("IdCardType", TThostFtdcIdCardTypeType),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("CustType", TThostFtdcCustTypeType),
        ("BankAccount", TThostFtdcBankAccountType),
        ("BankPassWord", TThostFtdcPasswordType),
        ("AccountID", TThostFtdcAccountIDType),
        ("Password", TThostFtdcPasswordType),
        ("InstallID", TThostFtdcInstallIDType),
        ("FutureSerial", TThostFtdcFutureSerialType),
        ("UserID", TThostFtdcUserIDType),
        ("VerifyCertNoFlag", TThostFtdcYesNoIndicatorType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("TradeAmount", TThostFtdcTradeAmountType),
        ("FutureFetchAmount", TThostFtdcTradeAmountType),
        ("FeePayFlag", TThostFtdcFeePayFlagType),
        ("CustFee", TThostFtdcCustFeeType),
        ("BrokerFee", TThostFtdcFutureFeeType),
        ("Message", TThostFtdcAddInfoType),
        ("Digest", TThostFtdcDigestType),
        ("BankAccType", TThostFtdcBankAccTypeType),
        ("DeviceID", TThostFtdcDeviceIDType),
        ("BankSecuAccType", TThostFtdcBankAccTypeType),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("BankSecuAcc", TThostFtdcBankAccountType),
        ("BankPwdFlag", TThostFtdcPwdFlagType),
        ("SecuPwdFlag", TThostFtdcPwdFlagType),
        ("OperNo", TThostFtdcOperNoType),
        ("RequestID", TThostFtdcRequestIDType),
        ("TID", TThostFtdcTIDType),
        ("TransferStatus", TThostFtdcTransferStatusType),
        ("LongCustomerName", TThostFtdcLongIndividualNameType),
        
    ]
    
class  CThostFtdcRspRepealField(Structure):
    """冲正响应"""
    _fields_ = [
        ("RepealTimeInterval", TThostFtdcRepealTimeIntervalType),
        ("RepealedTimes", TThostFtdcRepealedTimesType),
        ("BankRepealFlag", TThostFtdcBankRepealFlagType),
        ("BrokerRepealFlag", TThostFtdcBrokerRepealFlagType),
        ("PlateRepealSerial", TThostFtdcPlateSerialType),
        ("BankRepealSerial", TThostFtdcBankSerialType),
        ("FutureRepealSerial", TThostFtdcFutureSerialType),
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", TThostFtdcLastFragmentType),
        ("SessionID", TThostFtdcSessionIDType),
        ("CustomerName", TThostFtdcIndividualNameType),
        ("IdCardType", TThostFtdcIdCardTypeType),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("CustType", TThostFtdcCustTypeType),
        ("BankAccount", TThostFtdcBankAccountType),
        ("BankPassWord", TThostFtdcPasswordType),
        ("AccountID", TThostFtdcAccountIDType),
        ("Password", TThostFtdcPasswordType),
        ("InstallID", TThostFtdcInstallIDType),
        ("FutureSerial", TThostFtdcFutureSerialType),
        ("UserID", TThostFtdcUserIDType),
        ("VerifyCertNoFlag", TThostFtdcYesNoIndicatorType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("TradeAmount", TThostFtdcTradeAmountType),
        ("FutureFetchAmount", TThostFtdcTradeAmountType),
        ("FeePayFlag", TThostFtdcFeePayFlagType),
        ("CustFee", TThostFtdcCustFeeType),
        ("BrokerFee", TThostFtdcFutureFeeType),
        ("Message", TThostFtdcAddInfoType),
        ("Digest", TThostFtdcDigestType),
        ("BankAccType", TThostFtdcBankAccTypeType),
        ("DeviceID", TThostFtdcDeviceIDType),
        ("BankSecuAccType", TThostFtdcBankAccTypeType),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("BankSecuAcc", TThostFtdcBankAccountType),
        ("BankPwdFlag", TThostFtdcPwdFlagType),
        ("SecuPwdFlag", TThostFtdcPwdFlagType),
        ("OperNo", TThostFtdcOperNoType),
        ("RequestID", TThostFtdcRequestIDType),
        ("TID", TThostFtdcTIDType),
        ("TransferStatus", TThostFtdcTransferStatusType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        ("LongCustomerName", TThostFtdcLongIndividualNameType),
        
    ]
    
class  CThostFtdcReqQueryAccountField(Structure):
    """查询账户信息请求"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", TThostFtdcLastFragmentType),
        ("SessionID", TThostFtdcSessionIDType),
        ("CustomerName", TThostFtdcIndividualNameType),
        ("IdCardType", TThostFtdcIdCardTypeType),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("CustType", TThostFtdcCustTypeType),
        ("BankAccount", TThostFtdcBankAccountType),
        ("BankPassWord", TThostFtdcPasswordType),
        ("AccountID", TThostFtdcAccountIDType),
        ("Password", TThostFtdcPasswordType),
        ("FutureSerial", TThostFtdcFutureSerialType),
        ("InstallID", TThostFtdcInstallIDType),
        ("UserID", TThostFtdcUserIDType),
        ("VerifyCertNoFlag", TThostFtdcYesNoIndicatorType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("Digest", TThostFtdcDigestType),
        ("BankAccType", TThostFtdcBankAccTypeType),
        ("DeviceID", TThostFtdcDeviceIDType),
        ("BankSecuAccType", TThostFtdcBankAccTypeType),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("BankSecuAcc", TThostFtdcBankAccountType),
        ("BankPwdFlag", TThostFtdcPwdFlagType),
        ("SecuPwdFlag", TThostFtdcPwdFlagType),
        ("OperNo", TThostFtdcOperNoType),
        ("RequestID", TThostFtdcRequestIDType),
        ("TID", TThostFtdcTIDType),
        ("LongCustomerName", TThostFtdcLongIndividualNameType),
        
    ]
    
class  CThostFtdcRspQueryAccountField(Structure):
    """查询账户信息响应"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", TThostFtdcLastFragmentType),
        ("SessionID", TThostFtdcSessionIDType),
        ("CustomerName", TThostFtdcIndividualNameType),
        ("IdCardType", TThostFtdcIdCardTypeType),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("CustType", TThostFtdcCustTypeType),
        ("BankAccount", TThostFtdcBankAccountType),
        ("BankPassWord", TThostFtdcPasswordType),
        ("AccountID", TThostFtdcAccountIDType),
        ("Password", TThostFtdcPasswordType),
        ("FutureSerial", TThostFtdcFutureSerialType),
        ("InstallID", TThostFtdcInstallIDType),
        ("UserID", TThostFtdcUserIDType),
        ("VerifyCertNoFlag", TThostFtdcYesNoIndicatorType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("Digest", TThostFtdcDigestType),
        ("BankAccType", TThostFtdcBankAccTypeType),
        ("DeviceID", TThostFtdcDeviceIDType),
        ("BankSecuAccType", TThostFtdcBankAccTypeType),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("BankSecuAcc", TThostFtdcBankAccountType),
        ("BankPwdFlag", TThostFtdcPwdFlagType),
        ("SecuPwdFlag", TThostFtdcPwdFlagType),
        ("OperNo", TThostFtdcOperNoType),
        ("RequestID", TThostFtdcRequestIDType),
        ("TID", TThostFtdcTIDType),
        ("BankUseAmount", TThostFtdcTradeAmountType),
        ("BankFetchAmount", TThostFtdcTradeAmountType),
        ("LongCustomerName", TThostFtdcLongIndividualNameType),
        
    ]
    
class  CThostFtdcFutureSignIOField(Structure):
    """期商签到签退"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", TThostFtdcLastFragmentType),
        ("SessionID", TThostFtdcSessionIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("UserID", TThostFtdcUserIDType),
        ("Digest", TThostFtdcDigestType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("DeviceID", TThostFtdcDeviceIDType),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("OperNo", TThostFtdcOperNoType),
        ("RequestID", TThostFtdcRequestIDType),
        ("TID", TThostFtdcTIDType),
        
    ]
    
class  CThostFtdcRspFutureSignInField(Structure):
    """期商签到响应"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", TThostFtdcLastFragmentType),
        ("SessionID", TThostFtdcSessionIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("UserID", TThostFtdcUserIDType),
        ("Digest", TThostFtdcDigestType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("DeviceID", TThostFtdcDeviceIDType),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("OperNo", TThostFtdcOperNoType),
        ("RequestID", TThostFtdcRequestIDType),
        ("TID", TThostFtdcTIDType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        ("PinKey", TThostFtdcPasswordKeyType),
        ("MacKey", TThostFtdcPasswordKeyType),
        
    ]
    
class  CThostFtdcReqFutureSignOutField(Structure):
    """期商签退请求"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", TThostFtdcLastFragmentType),
        ("SessionID", TThostFtdcSessionIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("UserID", TThostFtdcUserIDType),
        ("Digest", TThostFtdcDigestType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("DeviceID", TThostFtdcDeviceIDType),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("OperNo", TThostFtdcOperNoType),
        ("RequestID", TThostFtdcRequestIDType),
        ("TID", TThostFtdcTIDType),
        
    ]
    
class  CThostFtdcRspFutureSignOutField(Structure):
    """期商签退响应"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", TThostFtdcLastFragmentType),
        ("SessionID", TThostFtdcSessionIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("UserID", TThostFtdcUserIDType),
        ("Digest", TThostFtdcDigestType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("DeviceID", TThostFtdcDeviceIDType),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("OperNo", TThostFtdcOperNoType),
        ("RequestID", TThostFtdcRequestIDType),
        ("TID", TThostFtdcTIDType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        
    ]
    
class  CThostFtdcReqQueryTradeResultBySerialField(Structure):
    """查询指定流水号的交易结果请求"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", TThostFtdcLastFragmentType),
        ("SessionID", TThostFtdcSessionIDType),
        ("Reference", TThostFtdcSerialType),
        ("RefrenceIssureType", TThostFtdcInstitutionTypeType),
        ("RefrenceIssure", TThostFtdcOrganCodeType),
        ("CustomerName", TThostFtdcIndividualNameType),
        ("IdCardType", TThostFtdcIdCardTypeType),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("CustType", TThostFtdcCustTypeType),
        ("BankAccount", TThostFtdcBankAccountType),
        ("BankPassWord", TThostFtdcPasswordType),
        ("AccountID", TThostFtdcAccountIDType),
        ("Password", TThostFtdcPasswordType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("TradeAmount", TThostFtdcTradeAmountType),
        ("Digest", TThostFtdcDigestType),
        ("LongCustomerName", TThostFtdcLongIndividualNameType),
        
    ]
    
class  CThostFtdcRspQueryTradeResultBySerialField(Structure):
    """查询指定流水号的交易结果响应"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", TThostFtdcLastFragmentType),
        ("SessionID", TThostFtdcSessionIDType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        ("Reference", TThostFtdcSerialType),
        ("RefrenceIssureType", TThostFtdcInstitutionTypeType),
        ("RefrenceIssure", TThostFtdcOrganCodeType),
        ("OriginReturnCode", TThostFtdcReturnCodeType),
        ("OriginDescrInfoForReturnCode", TThostFtdcDescrInfoForReturnCodeType),
        ("BankAccount", TThostFtdcBankAccountType),
        ("BankPassWord", TThostFtdcPasswordType),
        ("AccountID", TThostFtdcAccountIDType),
        ("Password", TThostFtdcPasswordType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("TradeAmount", TThostFtdcTradeAmountType),
        ("Digest", TThostFtdcDigestType),
        
    ]
    
class  CThostFtdcReqDayEndFileReadyField(Structure):
    """日终文件就绪请求"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", TThostFtdcLastFragmentType),
        ("SessionID", TThostFtdcSessionIDType),
        ("FileBusinessCode", TThostFtdcFileBusinessCodeType),
        ("Digest", TThostFtdcDigestType),
        
    ]
    
class  CThostFtdcReturnResultField(Structure):
    """返回结果"""
    _fields_ = [
        ("ReturnCode", TThostFtdcReturnCodeType),
        ("DescrInfoForReturnCode", TThostFtdcDescrInfoForReturnCodeType),
        
    ]
    
class  CThostFtdcVerifyFuturePasswordField(Structure):
    """验证期货资金密码"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", TThostFtdcLastFragmentType),
        ("SessionID", TThostFtdcSessionIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("Password", TThostFtdcPasswordType),
        ("BankAccount", TThostFtdcBankAccountType),
        ("BankPassWord", TThostFtdcPasswordType),
        ("InstallID", TThostFtdcInstallIDType),
        ("TID", TThostFtdcTIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        
    ]
    
class  CThostFtdcVerifyCustInfoField(Structure):
    """验证客户信息"""
    _fields_ = [
        ("CustomerName", TThostFtdcIndividualNameType),
        ("IdCardType", TThostFtdcIdCardTypeType),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("CustType", TThostFtdcCustTypeType),
        ("LongCustomerName", TThostFtdcLongIndividualNameType),
        
    ]
    
class  CThostFtdcVerifyFuturePasswordAndCustInfoField(Structure):
    """验证期货资金密码和客户信息"""
    _fields_ = [
        ("CustomerName", TThostFtdcIndividualNameType),
        ("IdCardType", TThostFtdcIdCardTypeType),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("CustType", TThostFtdcCustTypeType),
        ("AccountID", TThostFtdcAccountIDType),
        ("Password", TThostFtdcPasswordType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("LongCustomerName", TThostFtdcLongIndividualNameType),
        
    ]
    
class  CThostFtdcDepositResultInformField(Structure):
    """验证期货资金密码和客户信息"""
    _fields_ = [
        ("DepositSeqNo", TThostFtdcDepositSeqNoType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("Deposit", TThostFtdcMoneyType),
        ("RequestID", TThostFtdcRequestIDType),
        ("ReturnCode", TThostFtdcReturnCodeType),
        ("DescrInfoForReturnCode", TThostFtdcDescrInfoForReturnCodeType),
        
    ]
    
class  CThostFtdcReqSyncKeyField(Structure):
    """交易核心向银期报盘发出密钥同步请求"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", TThostFtdcLastFragmentType),
        ("SessionID", TThostFtdcSessionIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("UserID", TThostFtdcUserIDType),
        ("Message", TThostFtdcAddInfoType),
        ("DeviceID", TThostFtdcDeviceIDType),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("OperNo", TThostFtdcOperNoType),
        ("RequestID", TThostFtdcRequestIDType),
        ("TID", TThostFtdcTIDType),
        
    ]
    
class  CThostFtdcRspSyncKeyField(Structure):
    """交易核心向银期报盘发出密钥同步响应"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", TThostFtdcLastFragmentType),
        ("SessionID", TThostFtdcSessionIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("UserID", TThostFtdcUserIDType),
        ("Message", TThostFtdcAddInfoType),
        ("DeviceID", TThostFtdcDeviceIDType),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("OperNo", TThostFtdcOperNoType),
        ("RequestID", TThostFtdcRequestIDType),
        ("TID", TThostFtdcTIDType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        
    ]
    
class  CThostFtdcNotifyQueryAccountField(Structure):
    """查询账户信息通知"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", TThostFtdcLastFragmentType),
        ("SessionID", TThostFtdcSessionIDType),
        ("CustomerName", TThostFtdcIndividualNameType),
        ("IdCardType", TThostFtdcIdCardTypeType),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("CustType", TThostFtdcCustTypeType),
        ("BankAccount", TThostFtdcBankAccountType),
        ("BankPassWord", TThostFtdcPasswordType),
        ("AccountID", TThostFtdcAccountIDType),
        ("Password", TThostFtdcPasswordType),
        ("FutureSerial", TThostFtdcFutureSerialType),
        ("InstallID", TThostFtdcInstallIDType),
        ("UserID", TThostFtdcUserIDType),
        ("VerifyCertNoFlag", TThostFtdcYesNoIndicatorType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("Digest", TThostFtdcDigestType),
        ("BankAccType", TThostFtdcBankAccTypeType),
        ("DeviceID", TThostFtdcDeviceIDType),
        ("BankSecuAccType", TThostFtdcBankAccTypeType),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("BankSecuAcc", TThostFtdcBankAccountType),
        ("BankPwdFlag", TThostFtdcPwdFlagType),
        ("SecuPwdFlag", TThostFtdcPwdFlagType),
        ("OperNo", TThostFtdcOperNoType),
        ("RequestID", TThostFtdcRequestIDType),
        ("TID", TThostFtdcTIDType),
        ("BankUseAmount", TThostFtdcTradeAmountType),
        ("BankFetchAmount", TThostFtdcTradeAmountType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        ("LongCustomerName", TThostFtdcLongIndividualNameType),
        
    ]
    
class  CThostFtdcTransferSerialField(Structure):
    """银期转账交易流水表"""
    _fields_ = [
        ("PlateSerial", TThostFtdcPlateSerialType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradingDay", TThostFtdcDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("TradeCode", TThostFtdcTradeCodeType),
        ("SessionID", TThostFtdcSessionIDType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BankAccType", TThostFtdcBankAccTypeType),
        ("BankAccount", TThostFtdcBankAccountType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("FutureAccType", TThostFtdcFutureAccTypeType),
        ("AccountID", TThostFtdcAccountIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("FutureSerial", TThostFtdcFutureSerialType),
        ("IdCardType", TThostFtdcIdCardTypeType),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("TradeAmount", TThostFtdcTradeAmountType),
        ("CustFee", TThostFtdcCustFeeType),
        ("BrokerFee", TThostFtdcFutureFeeType),
        ("AvailabilityFlag", TThostFtdcAvailabilityFlagType),
        ("OperatorCode", TThostFtdcOperatorCodeType),
        ("BankNewAccount", TThostFtdcBankAccountType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        
    ]
    
class  CThostFtdcQryTransferSerialField(Structure):
    """请求查询转帐流水"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("BankID", TThostFtdcBankIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        
    ]
    
class  CThostFtdcNotifyFutureSignInField(Structure):
    """期商签到通知"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", TThostFtdcLastFragmentType),
        ("SessionID", TThostFtdcSessionIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("UserID", TThostFtdcUserIDType),
        ("Digest", TThostFtdcDigestType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("DeviceID", TThostFtdcDeviceIDType),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("OperNo", TThostFtdcOperNoType),
        ("RequestID", TThostFtdcRequestIDType),
        ("TID", TThostFtdcTIDType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        ("PinKey", TThostFtdcPasswordKeyType),
        ("MacKey", TThostFtdcPasswordKeyType),
        
    ]
    
class  CThostFtdcNotifyFutureSignOutField(Structure):
    """期商签退通知"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", TThostFtdcLastFragmentType),
        ("SessionID", TThostFtdcSessionIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("UserID", TThostFtdcUserIDType),
        ("Digest", TThostFtdcDigestType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("DeviceID", TThostFtdcDeviceIDType),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("OperNo", TThostFtdcOperNoType),
        ("RequestID", TThostFtdcRequestIDType),
        ("TID", TThostFtdcTIDType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        
    ]
    
class  CThostFtdcNotifySyncKeyField(Structure):
    """交易核心向银期报盘发出密钥同步处理结果的通知"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", TThostFtdcLastFragmentType),
        ("SessionID", TThostFtdcSessionIDType),
        ("InstallID", TThostFtdcInstallIDType),
        ("UserID", TThostFtdcUserIDType),
        ("Message", TThostFtdcAddInfoType),
        ("DeviceID", TThostFtdcDeviceIDType),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("OperNo", TThostFtdcOperNoType),
        ("RequestID", TThostFtdcRequestIDType),
        ("TID", TThostFtdcTIDType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        
    ]
    
class  CThostFtdcQryAccountregisterField(Structure):
    """请求查询银期签约关系"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        
    ]
    
class  CThostFtdcAccountregisterField(Structure):
    """客户开销户信息表"""
    _fields_ = [
        ("TradeDay", TThostFtdcTradeDateType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BankAccount", TThostFtdcBankAccountType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("IdCardType", TThostFtdcIdCardTypeType),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("CustomerName", TThostFtdcIndividualNameType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("OpenOrDestroy", TThostFtdcOpenOrDestroyType),
        ("RegDate", TThostFtdcTradeDateType),
        ("OutDate", TThostFtdcTradeDateType),
        ("TID", TThostFtdcTIDType),
        ("CustType", TThostFtdcCustTypeType),
        ("BankAccType", TThostFtdcBankAccTypeType),
        ("LongCustomerName", TThostFtdcLongIndividualNameType),
        
    ]
    
class  CThostFtdcOpenAccountField(Structure):
    """银期开户信息"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", TThostFtdcLastFragmentType),
        ("SessionID", TThostFtdcSessionIDType),
        ("CustomerName", TThostFtdcIndividualNameType),
        ("IdCardType", TThostFtdcIdCardTypeType),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("Gender", TThostFtdcGenderType),
        ("CountryCode", TThostFtdcCountryCodeType),
        ("CustType", TThostFtdcCustTypeType),
        ("Address", TThostFtdcAddressType),
        ("ZipCode", TThostFtdcZipCodeType),
        ("Telephone", TThostFtdcTelephoneType),
        ("MobilePhone", TThostFtdcMobilePhoneType),
        ("Fax", TThostFtdcFaxType),
        ("EMail", TThostFtdcEMailType),
        ("MoneyAccountStatus", TThostFtdcMoneyAccountStatusType),
        ("BankAccount", TThostFtdcBankAccountType),
        ("BankPassWord", TThostFtdcPasswordType),
        ("AccountID", TThostFtdcAccountIDType),
        ("Password", TThostFtdcPasswordType),
        ("InstallID", TThostFtdcInstallIDType),
        ("VerifyCertNoFlag", TThostFtdcYesNoIndicatorType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("CashExchangeCode", TThostFtdcCashExchangeCodeType),
        ("Digest", TThostFtdcDigestType),
        ("BankAccType", TThostFtdcBankAccTypeType),
        ("DeviceID", TThostFtdcDeviceIDType),
        ("BankSecuAccType", TThostFtdcBankAccTypeType),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("BankSecuAcc", TThostFtdcBankAccountType),
        ("BankPwdFlag", TThostFtdcPwdFlagType),
        ("SecuPwdFlag", TThostFtdcPwdFlagType),
        ("OperNo", TThostFtdcOperNoType),
        ("TID", TThostFtdcTIDType),
        ("UserID", TThostFtdcUserIDType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        ("LongCustomerName", TThostFtdcLongIndividualNameType),
        
    ]
    
class  CThostFtdcCancelAccountField(Structure):
    """银期销户信息"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", TThostFtdcLastFragmentType),
        ("SessionID", TThostFtdcSessionIDType),
        ("CustomerName", TThostFtdcIndividualNameType),
        ("IdCardType", TThostFtdcIdCardTypeType),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("Gender", TThostFtdcGenderType),
        ("CountryCode", TThostFtdcCountryCodeType),
        ("CustType", TThostFtdcCustTypeType),
        ("Address", TThostFtdcAddressType),
        ("ZipCode", TThostFtdcZipCodeType),
        ("Telephone", TThostFtdcTelephoneType),
        ("MobilePhone", TThostFtdcMobilePhoneType),
        ("Fax", TThostFtdcFaxType),
        ("EMail", TThostFtdcEMailType),
        ("MoneyAccountStatus", TThostFtdcMoneyAccountStatusType),
        ("BankAccount", TThostFtdcBankAccountType),
        ("BankPassWord", TThostFtdcPasswordType),
        ("AccountID", TThostFtdcAccountIDType),
        ("Password", TThostFtdcPasswordType),
        ("InstallID", TThostFtdcInstallIDType),
        ("VerifyCertNoFlag", TThostFtdcYesNoIndicatorType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("CashExchangeCode", TThostFtdcCashExchangeCodeType),
        ("Digest", TThostFtdcDigestType),
        ("BankAccType", TThostFtdcBankAccTypeType),
        ("DeviceID", TThostFtdcDeviceIDType),
        ("BankSecuAccType", TThostFtdcBankAccTypeType),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("BankSecuAcc", TThostFtdcBankAccountType),
        ("BankPwdFlag", TThostFtdcPwdFlagType),
        ("SecuPwdFlag", TThostFtdcPwdFlagType),
        ("OperNo", TThostFtdcOperNoType),
        ("TID", TThostFtdcTIDType),
        ("UserID", TThostFtdcUserIDType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        ("LongCustomerName", TThostFtdcLongIndividualNameType),
        
    ]
    
class  CThostFtdcChangeAccountField(Structure):
    """银期变更银行账号信息"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", TThostFtdcLastFragmentType),
        ("SessionID", TThostFtdcSessionIDType),
        ("CustomerName", TThostFtdcIndividualNameType),
        ("IdCardType", TThostFtdcIdCardTypeType),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("Gender", TThostFtdcGenderType),
        ("CountryCode", TThostFtdcCountryCodeType),
        ("CustType", TThostFtdcCustTypeType),
        ("Address", TThostFtdcAddressType),
        ("ZipCode", TThostFtdcZipCodeType),
        ("Telephone", TThostFtdcTelephoneType),
        ("MobilePhone", TThostFtdcMobilePhoneType),
        ("Fax", TThostFtdcFaxType),
        ("EMail", TThostFtdcEMailType),
        ("MoneyAccountStatus", TThostFtdcMoneyAccountStatusType),
        ("BankAccount", TThostFtdcBankAccountType),
        ("BankPassWord", TThostFtdcPasswordType),
        ("NewBankAccount", TThostFtdcBankAccountType),
        ("NewBankPassWord", TThostFtdcPasswordType),
        ("AccountID", TThostFtdcAccountIDType),
        ("Password", TThostFtdcPasswordType),
        ("BankAccType", TThostFtdcBankAccTypeType),
        ("InstallID", TThostFtdcInstallIDType),
        ("VerifyCertNoFlag", TThostFtdcYesNoIndicatorType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("BankPwdFlag", TThostFtdcPwdFlagType),
        ("SecuPwdFlag", TThostFtdcPwdFlagType),
        ("TID", TThostFtdcTIDType),
        ("Digest", TThostFtdcDigestType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        ("LongCustomerName", TThostFtdcLongIndividualNameType),
        
    ]
    
class  CThostFtdcSecAgentACIDMapField(Structure):
    """二级代理操作员银期权限"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("BrokerSecAgentID", TThostFtdcAccountIDType),
        
    ]
    
class  CThostFtdcQrySecAgentACIDMapField(Structure):
    """二级代理操作员银期权限查询"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        
    ]
    
class  CThostFtdcUserRightsAssignField(Structure):
    """灾备中心交易权限"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("DRIdentityID", TThostFtdcDRIdentityIDType),
        
    ]
    
class  CThostFtdcBrokerUserRightAssignField(Structure):
    """经济公司是否有在本标示的交易权限"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("DRIdentityID", TThostFtdcDRIdentityIDType),
        ("Tradeable", TThostFtdcBoolType),
        
    ]
    
class  CThostFtdcDRTransferField(Structure):
    """灾备交易转换报文"""
    _fields_ = [
        ("OrigDRIdentityID", TThostFtdcDRIdentityIDType),
        ("DestDRIdentityID", TThostFtdcDRIdentityIDType),
        ("OrigBrokerID", TThostFtdcBrokerIDType),
        ("DestBrokerID", TThostFtdcBrokerIDType),
        
    ]
    
class  CThostFtdcFensUserInfoField(Structure):
    """Fens用户信息"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("LoginMode", TThostFtdcLoginModeType),
        
    ]
    
class  CThostFtdcCurrTransferIdentityField(Structure):
    """当前银期所属交易中心"""
    _fields_ = [
        ("IdentityID", TThostFtdcDRIdentityIDType),
        
    ]
    
class  CThostFtdcLoginForbiddenUserField(Structure):
    """禁止登录用户"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("reserve1", TThostFtdcOldIPAddressType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcQryLoginForbiddenUserField(Structure):
    """查询禁止登录用户"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        
    ]
    
class  CThostFtdcTradingAccountReserveField(Structure):
    """资金账户基本准备金"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("Reserve", TThostFtdcMoneyType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        
    ]
    
class  CThostFtdcQryLoginForbiddenIPField(Structure):
    """查询禁止登录IP"""
    _fields_ = [
        ("reserve1", TThostFtdcOldIPAddressType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcQryIPListField(Structure):
    """查询IP列表"""
    _fields_ = [
        ("reserve1", TThostFtdcOldIPAddressType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcQryUserRightsAssignField(Structure):
    """查询用户下单权限分配表"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        
    ]
    
class  CThostFtdcReserveOpenAccountConfirmField(Structure):
    """银期预约开户确认请求"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", TThostFtdcLastFragmentType),
        ("SessionID", TThostFtdcSessionIDType),
        ("CustomerName", TThostFtdcLongIndividualNameType),
        ("IdCardType", TThostFtdcIdCardTypeType),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("Gender", TThostFtdcGenderType),
        ("CountryCode", TThostFtdcCountryCodeType),
        ("CustType", TThostFtdcCustTypeType),
        ("Address", TThostFtdcAddressType),
        ("ZipCode", TThostFtdcZipCodeType),
        ("Telephone", TThostFtdcTelephoneType),
        ("MobilePhone", TThostFtdcMobilePhoneType),
        ("Fax", TThostFtdcFaxType),
        ("EMail", TThostFtdcEMailType),
        ("MoneyAccountStatus", TThostFtdcMoneyAccountStatusType),
        ("BankAccount", TThostFtdcBankAccountType),
        ("BankPassWord", TThostFtdcPasswordType),
        ("InstallID", TThostFtdcInstallIDType),
        ("VerifyCertNoFlag", TThostFtdcYesNoIndicatorType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("Digest", TThostFtdcDigestType),
        ("BankAccType", TThostFtdcBankAccTypeType),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("TID", TThostFtdcTIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("Password", TThostFtdcPasswordType),
        ("BankReserveOpenSeq", TThostFtdcBankSerialType),
        ("BookDate", TThostFtdcTradeDateType),
        ("BookPsw", TThostFtdcPasswordType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        
    ]
    
class  CThostFtdcReserveOpenAccountField(Structure):
    """银期预约开户"""
    _fields_ = [
        ("TradeCode", TThostFtdcTradeCodeType),
        ("BankID", TThostFtdcBankIDType),
        ("BankBranchID", TThostFtdcBankBrchIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerBranchID", TThostFtdcFutureBranchIDType),
        ("TradeDate", TThostFtdcTradeDateType),
        ("TradeTime", TThostFtdcTradeTimeType),
        ("BankSerial", TThostFtdcBankSerialType),
        ("TradingDay", TThostFtdcTradeDateType),
        ("PlateSerial", TThostFtdcSerialType),
        ("LastFragment", TThostFtdcLastFragmentType),
        ("SessionID", TThostFtdcSessionIDType),
        ("CustomerName", TThostFtdcLongIndividualNameType),
        ("IdCardType", TThostFtdcIdCardTypeType),
        ("IdentifiedCardNo", TThostFtdcIdentifiedCardNoType),
        ("Gender", TThostFtdcGenderType),
        ("CountryCode", TThostFtdcCountryCodeType),
        ("CustType", TThostFtdcCustTypeType),
        ("Address", TThostFtdcAddressType),
        ("ZipCode", TThostFtdcZipCodeType),
        ("Telephone", TThostFtdcTelephoneType),
        ("MobilePhone", TThostFtdcMobilePhoneType),
        ("Fax", TThostFtdcFaxType),
        ("EMail", TThostFtdcEMailType),
        ("MoneyAccountStatus", TThostFtdcMoneyAccountStatusType),
        ("BankAccount", TThostFtdcBankAccountType),
        ("BankPassWord", TThostFtdcPasswordType),
        ("InstallID", TThostFtdcInstallIDType),
        ("VerifyCertNoFlag", TThostFtdcYesNoIndicatorType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("Digest", TThostFtdcDigestType),
        ("BankAccType", TThostFtdcBankAccTypeType),
        ("BrokerIDByBank", TThostFtdcBankCodingForFutureType),
        ("TID", TThostFtdcTIDType),
        ("ReserveOpenAccStas", TThostFtdcReserveOpenAccStasType),
        ("ErrorID", TThostFtdcErrorIDType),
        ("ErrorMsg", TThostFtdcErrorMsgType),
        
    ]
    
class  CThostFtdcAccountPropertyField(Structure):
    """银行账户属性"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("BankID", TThostFtdcBankIDType),
        ("BankAccount", TThostFtdcBankAccountType),
        ("OpenName", TThostFtdcInvestorFullNameType),
        ("OpenBank", TThostFtdcOpenBankType),
        ("IsActive", TThostFtdcBoolType),
        ("AccountSourceType", TThostFtdcAccountSourceTypeType),
        ("OpenDate", TThostFtdcDateType),
        ("CancelDate", TThostFtdcDateType),
        ("OperatorID", TThostFtdcOperatorIDType),
        ("OperateDate", TThostFtdcDateType),
        ("OperateTime", TThostFtdcTimeType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        
    ]
    
class  CThostFtdcQryCurrDRIdentityField(Structure):
    """查询当前交易中心"""
    _fields_ = [
        ("DRIdentityID", TThostFtdcDRIdentityIDType),
        
    ]
    
class  CThostFtdcCurrDRIdentityField(Structure):
    """当前交易中心"""
    _fields_ = [
        ("DRIdentityID", TThostFtdcDRIdentityIDType),
        
    ]
    
class  CThostFtdcQrySecAgentCheckModeField(Structure):
    """查询二级代理商资金校验模式"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        
    ]
    
class  CThostFtdcQrySecAgentTradeInfoField(Structure):
    """查询二级代理商信息"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("BrokerSecAgentID", TThostFtdcAccountIDType),
        
    ]
    
class  CThostFtdcReqUserAuthMethodField(Structure):
    """用户发出获取安全安全登陆方法请求"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        
    ]
    
class  CThostFtdcRspUserAuthMethodField(Structure):
    """用户发出获取安全安全登陆方法回复"""
    _fields_ = [
        ("UsableAuthMethod", TThostFtdcCurrentAuthMethodType),
        
    ]
    
class  CThostFtdcReqGenUserCaptchaField(Structure):
    """用户发出获取安全安全登陆方法请求"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        
    ]
    
class  CThostFtdcRspGenUserCaptchaField(Structure):
    """生成的图片验证码信息"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("CaptchaInfoLen", TThostFtdcCaptchaInfoLenType),
        ("CaptchaInfo", TThostFtdcCaptchaInfoType),
        
    ]
    
class  CThostFtdcReqGenUserTextField(Structure):
    """用户发出获取安全安全登陆方法请求"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        
    ]
    
class  CThostFtdcRspGenUserTextField(Structure):
    """短信验证码生成的回复"""
    _fields_ = [
        ("UserTextSeq", TThostFtdcUserTextSeqType),
        
    ]
    
class  CThostFtdcReqUserLoginWithCaptchaField(Structure):
    """用户发出带图形验证码的登录请求请求"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("Password", TThostFtdcPasswordType),
        ("UserProductInfo", TThostFtdcProductInfoType),
        ("InterfaceProductInfo", TThostFtdcProductInfoType),
        ("ProtocolInfo", TThostFtdcProtocolInfoType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("reserve1", TThostFtdcOldIPAddressType),
        ("LoginRemark", TThostFtdcLoginRemarkType),
        ("Captcha", TThostFtdcPasswordType),
        ("ClientIPPort", TThostFtdcIPPortType),
        ("ClientIPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcReqUserLoginWithTextField(Structure):
    """用户发出带短信验证码的登录请求请求"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("Password", TThostFtdcPasswordType),
        ("UserProductInfo", TThostFtdcProductInfoType),
        ("InterfaceProductInfo", TThostFtdcProductInfoType),
        ("ProtocolInfo", TThostFtdcProtocolInfoType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("reserve1", TThostFtdcOldIPAddressType),
        ("LoginRemark", TThostFtdcLoginRemarkType),
        ("Text", TThostFtdcPasswordType),
        ("ClientIPPort", TThostFtdcIPPortType),
        ("ClientIPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcReqUserLoginWithOTPField(Structure):
    """用户发出带动态验证码的登录请求请求"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("Password", TThostFtdcPasswordType),
        ("UserProductInfo", TThostFtdcProductInfoType),
        ("InterfaceProductInfo", TThostFtdcProductInfoType),
        ("ProtocolInfo", TThostFtdcProtocolInfoType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("reserve1", TThostFtdcOldIPAddressType),
        ("LoginRemark", TThostFtdcLoginRemarkType),
        ("OTPPassword", TThostFtdcPasswordType),
        ("ClientIPPort", TThostFtdcIPPortType),
        ("ClientIPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcReqApiHandshakeField(Structure):
    """api握手请求"""
    _fields_ = [
        ("CryptoKeyVersion", TThostFtdcCryptoKeyVersionType),
        
    ]
    
class  CThostFtdcRspApiHandshakeField(Structure):
    """front发给api的握手回复"""
    _fields_ = [
        ("FrontHandshakeDataLen", TThostFtdcHandshakeDataLenType),
        ("FrontHandshakeData", TThostFtdcHandshakeDataType),
        ("IsApiAuthEnabled", TThostFtdcBoolType),
        
    ]
    
class  CThostFtdcReqVerifyApiKeyField(Structure):
    """api给front的验证key的请求"""
    _fields_ = [
        ("ApiHandshakeDataLen", TThostFtdcHandshakeDataLenType),
        ("ApiHandshakeData", TThostFtdcHandshakeDataType),
        
    ]
    
class  CThostFtdcDepartmentUserField(Structure):
    """操作员组织架构关系"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("InvestorRange", TThostFtdcDepartmentRangeType),
        ("InvestorID", TThostFtdcInvestorIDType),
        
    ]
    
class  CThostFtdcQueryFreqField(Structure):
    """查询频率，每秒查询比数"""
    _fields_ = [
        ("QueryFreq", TThostFtdcQueryFreqType),
        
    ]
    
class  CThostFtdcAuthForbiddenIPField(Structure):
    """禁止认证IP"""
    _fields_ = [
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcQryAuthForbiddenIPField(Structure):
    """查询禁止认证IP"""
    _fields_ = [
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcSyncDelaySwapFrozenField(Structure):
    """换汇可提冻结"""
    _fields_ = [
        ("DelaySwapSeqNo", TThostFtdcDepositSeqNoType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("FromCurrencyID", TThostFtdcCurrencyIDType),
        ("FromRemainSwap", TThostFtdcMoneyType),
        ("IsManualSwap", TThostFtdcBoolType),
        
    ]
    
class  CThostFtdcUserSystemInfoField(Structure):
    """用户系统信息"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("ClientSystemInfoLen", TThostFtdcSystemInfoLenType),
        ("ClientSystemInfo", TThostFtdcClientSystemInfoType),
        ("reserve1", TThostFtdcOldIPAddressType),
        ("ClientIPPort", TThostFtdcIPPortType),
        ("ClientLoginTime", TThostFtdcTimeType),
        ("ClientAppID", TThostFtdcAppIDType),
        ("ClientPublicIP", TThostFtdcIPAddressType),
        ("ClientLoginRemark", TThostFtdcClientLoginRemarkType),
        
    ]
    
class  CThostFtdcAuthUserIDField(Structure):
    """终端用户绑定信息"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("AppID", TThostFtdcAppIDType),
        ("UserID", TThostFtdcUserIDType),
        ("AuthType", TThostFtdcAuthTypeType),
        
    ]
    
class  CThostFtdcAuthIPField(Structure):
    """用户IP绑定信息"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("AppID", TThostFtdcAppIDType),
        ("IPAddress", TThostFtdcIPAddressType),
        
    ]
    
class  CThostFtdcQryClassifiedInstrumentField(Structure):
    """查询分类合约"""
    _fields_ = [
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        ("ProductID", TThostFtdcInstrumentIDType),
        ("TradingType", TThostFtdcTradingTypeType),
        ("ClassType", TThostFtdcClassTypeType),
        
    ]
    
class  CThostFtdcQryCombPromotionParamField(Structure):
    """查询组合优惠比例"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcCombPromotionParamField(Structure):
    """组合优惠比例"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("CombHedgeFlag", TThostFtdcCombHedgeFlagType),
        ("Xparameter", TThostFtdcDiscountRatioType),
        
    ]
    
class  CThostFtdcReqUserLoginSCField(Structure):
    """国密用户登录请求"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("UserID", TThostFtdcUserIDType),
        ("Password", TThostFtdcPasswordType),
        ("UserProductInfo", TThostFtdcProductInfoType),
        ("InterfaceProductInfo", TThostFtdcProductInfoType),
        ("ProtocolInfo", TThostFtdcProtocolInfoType),
        ("MacAddress", TThostFtdcMacAddressType),
        ("OneTimePassword", TThostFtdcPasswordType),
        ("ClientIPAddress", TThostFtdcIPAddressType),
        ("LoginRemark", TThostFtdcLoginRemarkType),
        ("ClientIPPort", TThostFtdcIPPortType),
        ("AuthCode", TThostFtdcAuthCodeType),
        ("AppID", TThostFtdcAppIDType),
        
    ]
    
class  CThostFtdcQryRiskSettleInvstPositionField(Structure):
    """投资者风险结算持仓查询"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcQryRiskSettleProductStatusField(Structure):
    """风险结算产品查询"""
    _fields_ = [
        ("ProductID", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcRiskSettleInvstPositionField(Structure):
    """投资者风险结算持仓"""
    _fields_ = [
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("PosiDirection", TThostFtdcPosiDirectionType),
        ("HedgeFlag", TThostFtdcHedgeFlagType),
        ("PositionDate", TThostFtdcPositionDateType),
        ("YdPosition", TThostFtdcVolumeType),
        ("Position", TThostFtdcVolumeType),
        ("LongFrozen", TThostFtdcVolumeType),
        ("ShortFrozen", TThostFtdcVolumeType),
        ("LongFrozenAmount", TThostFtdcMoneyType),
        ("ShortFrozenAmount", TThostFtdcMoneyType),
        ("OpenVolume", TThostFtdcVolumeType),
        ("CloseVolume", TThostFtdcVolumeType),
        ("OpenAmount", TThostFtdcMoneyType),
        ("CloseAmount", TThostFtdcMoneyType),
        ("PositionCost", TThostFtdcMoneyType),
        ("PreMargin", TThostFtdcMoneyType),
        ("UseMargin", TThostFtdcMoneyType),
        ("FrozenMargin", TThostFtdcMoneyType),
        ("FrozenCash", TThostFtdcMoneyType),
        ("FrozenCommission", TThostFtdcMoneyType),
        ("CashIn", TThostFtdcMoneyType),
        ("Commission", TThostFtdcMoneyType),
        ("CloseProfit", TThostFtdcMoneyType),
        ("PositionProfit", TThostFtdcMoneyType),
        ("PreSettlementPrice", TThostFtdcPriceType),
        ("SettlementPrice", TThostFtdcPriceType),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("OpenCost", TThostFtdcMoneyType),
        ("ExchangeMargin", TThostFtdcMoneyType),
        ("CombPosition", TThostFtdcVolumeType),
        ("CombLongFrozen", TThostFtdcVolumeType),
        ("CombShortFrozen", TThostFtdcVolumeType),
        ("CloseProfitByDate", TThostFtdcMoneyType),
        ("CloseProfitByTrade", TThostFtdcMoneyType),
        ("TodayPosition", TThostFtdcVolumeType),
        ("MarginRateByMoney", TThostFtdcRatioType),
        ("MarginRateByVolume", TThostFtdcRatioType),
        ("StrikeFrozen", TThostFtdcVolumeType),
        ("StrikeFrozenAmount", TThostFtdcMoneyType),
        ("AbandonFrozen", TThostFtdcVolumeType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("YdStrikeFrozen", TThostFtdcVolumeType),
        ("InvestUnitID", TThostFtdcInvestUnitIDType),
        ("PositionCostOffset", TThostFtdcMoneyType),
        ("TasPosition", TThostFtdcVolumeType),
        ("TasPositionCost", TThostFtdcMoneyType),
        
    ]
    
class  CThostFtdcRiskSettleProductStatusField(Structure):
    """风险品种"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ProductID", TThostFtdcInstrumentIDType),
        ("ProductStatus", TThostFtdcProductStatusType),
        
    ]
    
class  CThostFtdcSyncDeltaInfoField(Structure):
    """风险结算追平信息"""
    _fields_ = [
        ("SyncDeltaSequenceNo", TThostFtdcSequenceNoType),
        ("SyncDeltaStatus", TThostFtdcSyncDeltaStatusType),
        ("SyncDescription", TThostFtdcSyncDescriptionType),
        ("IsOnlyTrdDelta", TThostFtdcBoolType),
        
    ]
    
class  CThostFtdcSyncDeltaProductStatusField(Structure):
    """风险结算追平产品信息"""
    _fields_ = [
        ("SyncDeltaSequenceNo", TThostFtdcSequenceNoType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ProductID", TThostFtdcInstrumentIDType),
        ("ProductStatus", TThostFtdcProductStatusType),
        
    ]
    
class  CThostFtdcSyncDeltaInvstPosDtlField(Structure):
    """风险结算追平持仓明细"""
    _fields_ = [
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("HedgeFlag", TThostFtdcHedgeFlagType),
        ("Direction", TThostFtdcDirectionType),
        ("OpenDate", TThostFtdcDateType),
        ("TradeID", TThostFtdcTradeIDType),
        ("Volume", TThostFtdcVolumeType),
        ("OpenPrice", TThostFtdcPriceType),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("TradeType", TThostFtdcTradeTypeType),
        ("CombInstrumentID", TThostFtdcInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("CloseProfitByDate", TThostFtdcMoneyType),
        ("CloseProfitByTrade", TThostFtdcMoneyType),
        ("PositionProfitByDate", TThostFtdcMoneyType),
        ("PositionProfitByTrade", TThostFtdcMoneyType),
        ("Margin", TThostFtdcMoneyType),
        ("ExchMargin", TThostFtdcMoneyType),
        ("MarginRateByMoney", TThostFtdcRatioType),
        ("MarginRateByVolume", TThostFtdcRatioType),
        ("LastSettlementPrice", TThostFtdcPriceType),
        ("SettlementPrice", TThostFtdcPriceType),
        ("CloseVolume", TThostFtdcVolumeType),
        ("CloseAmount", TThostFtdcMoneyType),
        ("TimeFirstVolume", TThostFtdcVolumeType),
        ("SpecPosiType", TThostFtdcSpecPosiTypeType),
        ("ActionDirection", TThostFtdcActionDirectionType),
        ("SyncDeltaSequenceNo", TThostFtdcSequenceNoType),
        
    ]
    
class  CThostFtdcSyncDeltaInvstPosCombDtlField(Structure):
    """风险结算追平组合持仓明细"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("OpenDate", TThostFtdcDateType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("ComTradeID", TThostFtdcTradeIDType),
        ("TradeID", TThostFtdcTradeIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("HedgeFlag", TThostFtdcHedgeFlagType),
        ("Direction", TThostFtdcDirectionType),
        ("TotalAmt", TThostFtdcVolumeType),
        ("Margin", TThostFtdcMoneyType),
        ("ExchMargin", TThostFtdcMoneyType),
        ("MarginRateByMoney", TThostFtdcRatioType),
        ("MarginRateByVolume", TThostFtdcRatioType),
        ("LegID", TThostFtdcLegIDType),
        ("LegMultiple", TThostFtdcLegMultipleType),
        ("TradeGroupID", TThostFtdcTradeGroupIDType),
        ("ActionDirection", TThostFtdcActionDirectionType),
        ("SyncDeltaSequenceNo", TThostFtdcSequenceNoType),
        
    ]
    
class  CThostFtdcSyncDeltaTradingAccountField(Structure):
    """风险结算追平资金"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("AccountID", TThostFtdcAccountIDType),
        ("PreMortgage", TThostFtdcMoneyType),
        ("PreCredit", TThostFtdcMoneyType),
        ("PreDeposit", TThostFtdcMoneyType),
        ("PreBalance", TThostFtdcMoneyType),
        ("PreMargin", TThostFtdcMoneyType),
        ("InterestBase", TThostFtdcMoneyType),
        ("Interest", TThostFtdcMoneyType),
        ("Deposit", TThostFtdcMoneyType),
        ("Withdraw", TThostFtdcMoneyType),
        ("FrozenMargin", TThostFtdcMoneyType),
        ("FrozenCash", TThostFtdcMoneyType),
        ("FrozenCommission", TThostFtdcMoneyType),
        ("CurrMargin", TThostFtdcMoneyType),
        ("CashIn", TThostFtdcMoneyType),
        ("Commission", TThostFtdcMoneyType),
        ("CloseProfit", TThostFtdcMoneyType),
        ("PositionProfit", TThostFtdcMoneyType),
        ("Balance", TThostFtdcMoneyType),
        ("Available", TThostFtdcMoneyType),
        ("WithdrawQuota", TThostFtdcMoneyType),
        ("Reserve", TThostFtdcMoneyType),
        ("TradingDay", TThostFtdcDateType),
        ("SettlementID", TThostFtdcSettlementIDType),
        ("Credit", TThostFtdcMoneyType),
        ("Mortgage", TThostFtdcMoneyType),
        ("ExchangeMargin", TThostFtdcMoneyType),
        ("DeliveryMargin", TThostFtdcMoneyType),
        ("ExchangeDeliveryMargin", TThostFtdcMoneyType),
        ("ReserveBalance", TThostFtdcMoneyType),
        ("CurrencyID", TThostFtdcCurrencyIDType),
        ("PreFundMortgageIn", TThostFtdcMoneyType),
        ("PreFundMortgageOut", TThostFtdcMoneyType),
        ("FundMortgageIn", TThostFtdcMoneyType),
        ("FundMortgageOut", TThostFtdcMoneyType),
        ("FundMortgageAvailable", TThostFtdcMoneyType),
        ("MortgageableFund", TThostFtdcMoneyType),
        ("SpecProductMargin", TThostFtdcMoneyType),
        ("SpecProductFrozenMargin", TThostFtdcMoneyType),
        ("SpecProductCommission", TThostFtdcMoneyType),
        ("SpecProductFrozenCommission", TThostFtdcMoneyType),
        ("SpecProductPositionProfit", TThostFtdcMoneyType),
        ("SpecProductCloseProfit", TThostFtdcMoneyType),
        ("SpecProductPositionProfitByAlg", TThostFtdcMoneyType),
        ("SpecProductExchangeMargin", TThostFtdcMoneyType),
        ("FrozenSwap", TThostFtdcMoneyType),
        ("RemainSwap", TThostFtdcMoneyType),
        ("SyncDeltaSequenceNo", TThostFtdcSequenceNoType),
        
    ]
    
class  CThostFtdcSyncDeltaInitInvstMarginField(Structure):
    """投资者风险结算总保证金"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("LastRiskTotalInvstMargin", TThostFtdcMoneyType),
        ("LastRiskTotalExchMargin", TThostFtdcMoneyType),
        ("ThisSyncInvstMargin", TThostFtdcMoneyType),
        ("ThisSyncExchMargin", TThostFtdcMoneyType),
        ("RemainRiskInvstMargin", TThostFtdcMoneyType),
        ("RemainRiskExchMargin", TThostFtdcMoneyType),
        ("LastRiskSpecTotalInvstMargin", TThostFtdcMoneyType),
        ("LastRiskSpecTotalExchMargin", TThostFtdcMoneyType),
        ("ThisSyncSpecInvstMargin", TThostFtdcMoneyType),
        ("ThisSyncSpecExchMargin", TThostFtdcMoneyType),
        ("RemainRiskSpecInvstMargin", TThostFtdcMoneyType),
        ("RemainRiskSpecExchMargin", TThostFtdcMoneyType),
        ("SyncDeltaSequenceNo", TThostFtdcSequenceNoType),
        
    ]
    
class  CThostFtdcSyncDeltaDceCombInstrumentField(Structure):
    """风险结算追平组合优先级"""
    _fields_ = [
        ("CombInstrumentID", TThostFtdcInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        ("TradeGroupID", TThostFtdcTradeGroupIDType),
        ("CombHedgeFlag", TThostFtdcHedgeFlagType),
        ("CombinationType", TThostFtdcDceCombinationTypeType),
        ("Direction", TThostFtdcDirectionType),
        ("ProductID", TThostFtdcInstrumentIDType),
        ("Xparameter", TThostFtdcDiscountRatioType),
        ("ActionDirection", TThostFtdcActionDirectionType),
        ("SyncDeltaSequenceNo", TThostFtdcSequenceNoType),
        
    ]
    
class  CThostFtdcSyncDeltaInvstMarginRateField(Structure):
    """风险结算追平投资者期货保证金率"""
    _fields_ = [
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("InvestorRange", TThostFtdcInvestorRangeType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("HedgeFlag", TThostFtdcHedgeFlagType),
        ("LongMarginRatioByMoney", TThostFtdcRatioType),
        ("LongMarginRatioByVolume", TThostFtdcMoneyType),
        ("ShortMarginRatioByMoney", TThostFtdcRatioType),
        ("ShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("IsRelative", TThostFtdcBoolType),
        ("ActionDirection", TThostFtdcActionDirectionType),
        ("SyncDeltaSequenceNo", TThostFtdcSequenceNoType),
        
    ]
    
class  CThostFtdcSyncDeltaExchMarginRateField(Structure):
    """风险结算追平交易所期货保证金率"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("HedgeFlag", TThostFtdcHedgeFlagType),
        ("LongMarginRatioByMoney", TThostFtdcRatioType),
        ("LongMarginRatioByVolume", TThostFtdcMoneyType),
        ("ShortMarginRatioByMoney", TThostFtdcRatioType),
        ("ShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("ActionDirection", TThostFtdcActionDirectionType),
        ("SyncDeltaSequenceNo", TThostFtdcSequenceNoType),
        
    ]
    
class  CThostFtdcSyncDeltaOptExchMarginField(Structure):
    """风险结算追平中金现货期权交易所保证金率"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("SShortMarginRatioByMoney", TThostFtdcRatioType),
        ("SShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("HShortMarginRatioByMoney", TThostFtdcRatioType),
        ("HShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("AShortMarginRatioByMoney", TThostFtdcRatioType),
        ("AShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("MShortMarginRatioByMoney", TThostFtdcRatioType),
        ("MShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("ActionDirection", TThostFtdcActionDirectionType),
        ("SyncDeltaSequenceNo", TThostFtdcSequenceNoType),
        
    ]
    
class  CThostFtdcSyncDeltaOptInvstMarginField(Structure):
    """风险结算追平中金现货期权投资者保证金率"""
    _fields_ = [
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("InvestorRange", TThostFtdcInvestorRangeType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("SShortMarginRatioByMoney", TThostFtdcRatioType),
        ("SShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("HShortMarginRatioByMoney", TThostFtdcRatioType),
        ("HShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("AShortMarginRatioByMoney", TThostFtdcRatioType),
        ("AShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("IsRelative", TThostFtdcBoolType),
        ("MShortMarginRatioByMoney", TThostFtdcRatioType),
        ("MShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("ActionDirection", TThostFtdcActionDirectionType),
        ("SyncDeltaSequenceNo", TThostFtdcSequenceNoType),
        
    ]
    
class  CThostFtdcSyncDeltaInvstMarginRateULField(Structure):
    """风险结算追平期权标的调整保证金率"""
    _fields_ = [
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("InvestorRange", TThostFtdcInvestorRangeType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("HedgeFlag", TThostFtdcHedgeFlagType),
        ("LongMarginRatioByMoney", TThostFtdcRatioType),
        ("LongMarginRatioByVolume", TThostFtdcMoneyType),
        ("ShortMarginRatioByMoney", TThostFtdcRatioType),
        ("ShortMarginRatioByVolume", TThostFtdcMoneyType),
        ("ActionDirection", TThostFtdcActionDirectionType),
        ("SyncDeltaSequenceNo", TThostFtdcSequenceNoType),
        
    ]
    
class  CThostFtdcSyncDeltaOptInvstCommRateField(Structure):
    """风险结算追平期权手续费率"""
    _fields_ = [
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("InvestorRange", TThostFtdcInvestorRangeType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("OpenRatioByMoney", TThostFtdcRatioType),
        ("OpenRatioByVolume", TThostFtdcRatioType),
        ("CloseRatioByMoney", TThostFtdcRatioType),
        ("CloseRatioByVolume", TThostFtdcRatioType),
        ("CloseTodayRatioByMoney", TThostFtdcRatioType),
        ("CloseTodayRatioByVolume", TThostFtdcRatioType),
        ("StrikeRatioByMoney", TThostFtdcRatioType),
        ("StrikeRatioByVolume", TThostFtdcRatioType),
        ("ActionDirection", TThostFtdcActionDirectionType),
        ("SyncDeltaSequenceNo", TThostFtdcSequenceNoType),
        
    ]
    
class  CThostFtdcSyncDeltaInvstCommRateField(Structure):
    """风险结算追平期货手续费率"""
    _fields_ = [
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("InvestorRange", TThostFtdcInvestorRangeType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("OpenRatioByMoney", TThostFtdcRatioType),
        ("OpenRatioByVolume", TThostFtdcRatioType),
        ("CloseRatioByMoney", TThostFtdcRatioType),
        ("CloseRatioByVolume", TThostFtdcRatioType),
        ("CloseTodayRatioByMoney", TThostFtdcRatioType),
        ("CloseTodayRatioByVolume", TThostFtdcRatioType),
        ("ActionDirection", TThostFtdcActionDirectionType),
        ("SyncDeltaSequenceNo", TThostFtdcSequenceNoType),
        
    ]
    
class  CThostFtdcSyncDeltaProductExchRateField(Structure):
    """风险结算追平交叉汇率"""
    _fields_ = [
        ("ProductID", TThostFtdcInstrumentIDType),
        ("QuoteCurrencyID", TThostFtdcCurrencyIDType),
        ("ExchangeRate", TThostFtdcExchangeRateType),
        ("ActionDirection", TThostFtdcActionDirectionType),
        ("SyncDeltaSequenceNo", TThostFtdcSequenceNoType),
        
    ]
    
class  CThostFtdcSyncDeltaDepthMarketDataField(Structure):
    """风险结算追平行情"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ExchangeInstID", TThostFtdcExchangeInstIDType),
        ("LastPrice", TThostFtdcPriceType),
        ("PreSettlementPrice", TThostFtdcPriceType),
        ("PreClosePrice", TThostFtdcPriceType),
        ("PreOpenInterest", TThostFtdcLargeVolumeType),
        ("OpenPrice", TThostFtdcPriceType),
        ("HighestPrice", TThostFtdcPriceType),
        ("LowestPrice", TThostFtdcPriceType),
        ("Volume", TThostFtdcVolumeType),
        ("Turnover", TThostFtdcMoneyType),
        ("OpenInterest", TThostFtdcLargeVolumeType),
        ("ClosePrice", TThostFtdcPriceType),
        ("SettlementPrice", TThostFtdcPriceType),
        ("UpperLimitPrice", TThostFtdcPriceType),
        ("LowerLimitPrice", TThostFtdcPriceType),
        ("PreDelta", TThostFtdcRatioType),
        ("CurrDelta", TThostFtdcRatioType),
        ("UpdateTime", TThostFtdcTimeType),
        ("UpdateMillisec", TThostFtdcMillisecType),
        ("BidPrice1", TThostFtdcPriceType),
        ("BidVolume1", TThostFtdcVolumeType),
        ("AskPrice1", TThostFtdcPriceType),
        ("AskVolume1", TThostFtdcVolumeType),
        ("BidPrice2", TThostFtdcPriceType),
        ("BidVolume2", TThostFtdcVolumeType),
        ("AskPrice2", TThostFtdcPriceType),
        ("AskVolume2", TThostFtdcVolumeType),
        ("BidPrice3", TThostFtdcPriceType),
        ("BidVolume3", TThostFtdcVolumeType),
        ("AskPrice3", TThostFtdcPriceType),
        ("AskVolume3", TThostFtdcVolumeType),
        ("BidPrice4", TThostFtdcPriceType),
        ("BidVolume4", TThostFtdcVolumeType),
        ("AskPrice4", TThostFtdcPriceType),
        ("AskVolume4", TThostFtdcVolumeType),
        ("BidPrice5", TThostFtdcPriceType),
        ("BidVolume5", TThostFtdcVolumeType),
        ("AskPrice5", TThostFtdcPriceType),
        ("AskVolume5", TThostFtdcVolumeType),
        ("AveragePrice", TThostFtdcPriceType),
        ("ActionDay", TThostFtdcDateType),
        ("BandingUpperPrice", TThostFtdcPriceType),
        ("BandingLowerPrice", TThostFtdcPriceType),
        ("ActionDirection", TThostFtdcActionDirectionType),
        ("SyncDeltaSequenceNo", TThostFtdcSequenceNoType),
        
    ]
    
class  CThostFtdcSyncDeltaIndexPriceField(Structure):
    """风险结算追平现货指数"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("ClosePrice", TThostFtdcPriceType),
        ("ActionDirection", TThostFtdcActionDirectionType),
        ("SyncDeltaSequenceNo", TThostFtdcSequenceNoType),
        
    ]
    
class  CThostFtdcSyncDeltaEWarrantOffsetField(Structure):
    """风险结算追平仓单折抵"""
    _fields_ = [
        ("TradingDay", TThostFtdcTradeDateType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("Direction", TThostFtdcDirectionType),
        ("HedgeFlag", TThostFtdcHedgeFlagType),
        ("Volume", TThostFtdcVolumeType),
        ("ActionDirection", TThostFtdcActionDirectionType),
        ("SyncDeltaSequenceNo", TThostFtdcSequenceNoType),
        
    ]
    
class  CThostFtdcSPBMFutureParameterField(Structure):
    """SPBM期货合约保证金参数"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("ProdFamilyCode", TThostFtdcInstrumentIDType),
        ("Cvf", TThostFtdcVolumeMultipleType),
        ("TimeRange", TThostFtdcTimeRangeType),
        ("MarginRate", TThostFtdcRatioType),
        ("LockRateX", TThostFtdcRatioType),
        ("AddOnRate", TThostFtdcRatioType),
        ("PreSettlementPrice", TThostFtdcPriceType),
        
    ]
    
class  CThostFtdcSPBMOptionParameterField(Structure):
    """SPBM期权合约保证金参数"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("ProdFamilyCode", TThostFtdcInstrumentIDType),
        ("Cvf", TThostFtdcVolumeMultipleType),
        ("DownPrice", TThostFtdcPriceType),
        ("Delta", TThostFtdcDeltaType),
        ("SlimiDelta", TThostFtdcDeltaType),
        ("PreSettlementPrice", TThostFtdcPriceType),
        
    ]
    
class  CThostFtdcSPBMIntraParameterField(Structure):
    """SPBM品种内对锁仓折扣参数"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ProdFamilyCode", TThostFtdcInstrumentIDType),
        ("IntraRateY", TThostFtdcRatioType),
        
    ]
    
class  CThostFtdcSPBMInterParameterField(Structure):
    """SPBM跨品种抵扣参数"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("SpreadId", TThostFtdcSpreadIdType),
        ("InterRateZ", TThostFtdcRatioType),
        ("Leg1ProdFamilyCode", TThostFtdcInstrumentIDType),
        ("Leg2ProdFamilyCode", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcSyncSPBMParameterEndField(Structure):
    """同步SPBM参数结束"""
    _fields_ = [
        ("TradingDay", TThostFtdcDateType),
        
    ]
    
class  CThostFtdcQrySPBMFutureParameterField(Structure):
    """SPBM期货合约保证金参数查询"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("ProdFamilyCode", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcQrySPBMOptionParameterField(Structure):
    """SPBM期权合约保证金参数查询"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("InstrumentID", TThostFtdcInstrumentIDType),
        ("ProdFamilyCode", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcQrySPBMIntraParameterField(Structure):
    """SPBM品种内对锁仓折扣参数查询"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("ProdFamilyCode", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcQrySPBMInterParameterField(Structure):
    """SPBM跨品种抵扣参数查询"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("Leg1ProdFamilyCode", TThostFtdcInstrumentIDType),
        ("Leg2ProdFamilyCode", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcSPBMPortfDefinitionField(Structure):
    """组合保证金套餐"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("PortfolioDefID", TThostFtdcPortfolioDefIDType),
        ("ProdFamilyCode", TThostFtdcInstrumentIDType),
        ("IsSPBM", TThostFtdcBoolType),
        
    ]
    
class  CThostFtdcSPBMInvestorPortfDefField(Structure):
    """投资者套餐选择"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("PortfolioDefID", TThostFtdcPortfolioDefIDType),
        
    ]
    
class  CThostFtdcInvestorPortfMarginRatioField(Structure):
    """投资者新型组合保证金系数"""
    _fields_ = [
        ("InvestorRange", TThostFtdcInvestorRangeType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("MarginRatio", TThostFtdcRatioType),
        
    ]
    
class  CThostFtdcQrySPBMPortfDefinitionField(Structure):
    """组合保证金套餐查询"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("PortfolioDefID", TThostFtdcPortfolioDefIDType),
        ("ProdFamilyCode", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcQrySPBMInvestorPortfDefField(Structure):
    """投资者套餐选择查询"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        
    ]
    
class  CThostFtdcQryInvestorPortfMarginRatioField(Structure):
    """投资者新型组合保证金系数查询"""
    _fields_ = [
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("ExchangeID", TThostFtdcExchangeIDType),
        
    ]
    
class  CThostFtdcInvestorProdSPBMDetailField(Structure):
    """投资者产品SPBM明细"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("ProdFamilyCode", TThostFtdcInstrumentIDType),
        ("IntraInstrMargin", TThostFtdcMoneyType),
        ("BCollectingMargin", TThostFtdcMoneyType),
        ("SCollectingMargin", TThostFtdcMoneyType),
        ("IntraProdMargin", TThostFtdcMoneyType),
        ("NetMargin", TThostFtdcMoneyType),
        ("InterProdMargin", TThostFtdcMoneyType),
        ("SingleMargin", TThostFtdcMoneyType),
        ("AddOnMargin", TThostFtdcMoneyType),
        ("DeliveryMargin", TThostFtdcMoneyType),
        ("CallOptionMinRisk", TThostFtdcMoneyType),
        ("PutOptionMinRisk", TThostFtdcMoneyType),
        ("OptionMinRisk", TThostFtdcMoneyType),
        ("OptionValueOffset", TThostFtdcMoneyType),
        ("OptionRoyalty", TThostFtdcMoneyType),
        ("RealOptionValueOffset", TThostFtdcMoneyType),
        ("Margin", TThostFtdcMoneyType),
        ("ExchMargin", TThostFtdcMoneyType),
        
    ]
    
class  CThostFtdcQryInvestorProdSPBMDetailField(Structure):
    """投资者产品SPBM明细查询"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("ProdFamilyCode", TThostFtdcInstrumentIDType),
        
    ]
    
class  CThostFtdcPortfTradeParamSettingField(Structure):
    """组保交易参数设置"""
    _fields_ = [
        ("ExchangeID", TThostFtdcExchangeIDType),
        ("BrokerID", TThostFtdcBrokerIDType),
        ("InvestorID", TThostFtdcInvestorIDType),
        ("Portfolio", TThostFtdcPortfolioType),
        ("IsActionVerify", TThostFtdcBoolType),
        ("IsCloseVerify", TThostFtdcBoolType),
        
    ]
    