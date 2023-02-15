#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# LUX et VERITAS
# Create On: 2022/12/13 13:21:04

import os
import copy
import platform
from ctypes import *
from .ctp_struct import *


class Trade(object):

    def __init__(self, logdir="./log/") -> None:
        dllpath = os.path.join(os.path.abspath(os.path.dirname(__file__)), "../../../libs/ctpapi")
        if "Windows" in platform.system():
            dln = "ctptrade_api.dll"
        elif "Linux" in platform.system():
            dln = "libctptrade_api.so"
        elif "Darwin" in platform.system():
            dln = "libctptrade_api.dylib"
        absolute_dllfile_path = os.path.join(dllpath,dln)
        if not os.path.exists(absolute_dllfile_path):
            raise Exception("缺少DLL接口文件")

        # make log dir for api log
        self.logdir = os.path.join(os.getcwd(), logdir)
        if not os.path.exists(self.logdir):
            os.mkdir(self.logdir)
 
        dlldir = os.path.split(absolute_dllfile_path)[0]
        # change work directory
        cur_path = os.getcwd()
        os.chdir(dlldir)

        self.h = CDLL(absolute_dllfile_path)

        self.h.tCreateApi.argtypes = [c_char_p]
        self.h.tCreateApi.restype = c_void_p

        self.h.tCreateSpi.argtypes = []
        self.h.tCreateSpi.restype = c_void_p

        self.h.tGetApiVersion.argtypes = []
        self.h.tGetApiVersion.restype = c_char_p

        self.h.tGetTradingDay.argtypes = [c_void_p]
        self.h.tGetTradingDay.restype = c_char_p

        self.h.dCTP_GetSystemInfo.argtypes = [c_char_p, c_int]
        self.h.dCTP_GetSystemInfo.restype = c_int

        self.h.dCTP_GetSystemInfoUnAesEncode.argtypes = [c_char_p, c_int]
        self.h.dCTP_GetSystemInfoUnAesEncode.restype = c_int

        self.h.dCTP_GetDataCollectApiVersion.argtypes = []
        self.h.dCTP_GetDataCollectApiVersion.restype = c_char_p

        self.api = None
        self.pSpi = None

        #################### 请求函数 #######################
        # 创建TraderApi
        self.h.tRelease.argtypes = [c_void_p]
        self.h.tRelease.restype = c_void_p
        # 初始化
        self.h.tInit.argtypes = [c_void_p]
        self.h.tInit.restype = c_void_p
        # 等待接口线程结束运行
        self.h.tJoin.argtypes = [c_void_p]
        self.h.tJoin.restype = c_void_p
        # 注册前置机网络地址
        self.h.tRegisterFront.argtypes = [c_void_p, c_void_p]
        self.h.tRegisterFront.restype = c_void_p
        # @remark RegisterNameServer优先于RegisterFront
        self.h.tRegisterNameServer.argtypes = [c_void_p, c_void_p]
        self.h.tRegisterNameServer.restype = c_void_p
        # 注册名字服务器用户信息
        self.h.tRegisterFensUserInfo.argtypes = [c_void_p, c_void_p]
        self.h.tRegisterFensUserInfo.restype = c_void_p
        # 注册回调接口
        self.h.tRegisterSpi.argtypes = [c_void_p, c_void_p]
        self.h.tRegisterSpi.restype = c_void_p
        # 订阅私有流。
        self.h.tSubscribePrivateTopic.argtypes = [c_void_p, c_void_p]
        self.h.tSubscribePrivateTopic.restype = c_void_p
        # 订阅公共流。
        self.h.tSubscribePublicTopic.argtypes = [c_void_p, c_void_p]
        self.h.tSubscribePublicTopic.restype = c_void_p
        # 客户端认证请求
        self.h.tReqAuthenticate.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqAuthenticate.restype = c_void_p
        # 注册用户终端信息，用于中继服务器多连接模式
        self.h.tRegisterUserSystemInfo.argtypes = [c_void_p, c_void_p]
        self.h.tRegisterUserSystemInfo.restype = c_void_p
        # 上报用户终端信息，用于中继服务器操作员登录模式
        self.h.tSubmitUserSystemInfo.argtypes = [c_void_p, c_void_p]
        self.h.tSubmitUserSystemInfo.restype = c_void_p
        # 用户登录请求
        self.h.tReqUserLogin.argtypes = [c_void_p, c_void_p, c_int32, c_void_p, c_void_p]
        self.h.tReqUserLogin.restype = c_void_p
        # 登出请求
        self.h.tReqUserLogout.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqUserLogout.restype = c_void_p
        # 用户口令更新请求
        self.h.tReqUserPasswordUpdate.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqUserPasswordUpdate.restype = c_void_p
        # 资金账户口令更新请求
        self.h.tReqTradingAccountPasswordUpdate.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqTradingAccountPasswordUpdate.restype = c_void_p
        # 查询用户当前支持的认证模式
        self.h.tReqUserAuthMethod.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqUserAuthMethod.restype = c_void_p
        # 用户发出获取图形验证码请求
        self.h.tReqGenUserCaptcha.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqGenUserCaptcha.restype = c_void_p
        # 用户发出获取短信验证码请求
        self.h.tReqGenUserText.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqGenUserText.restype = c_void_p
        # 用户发出带有图片验证码的登陆请求
        self.h.tReqUserLoginWithCaptcha.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqUserLoginWithCaptcha.restype = c_void_p
        # 用户发出带有短信验证码的登陆请求
        self.h.tReqUserLoginWithText.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqUserLoginWithText.restype = c_void_p
        # 用户发出带有动态口令的登陆请求
        self.h.tReqUserLoginWithOTP.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqUserLoginWithOTP.restype = c_void_p
        # 报单录入请求
        self.h.tReqOrderInsert.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqOrderInsert.restype = c_void_p
        # 预埋单录入请求
        self.h.tReqParkedOrderInsert.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqParkedOrderInsert.restype = c_void_p
        # 预埋撤单录入请求
        self.h.tReqParkedOrderAction.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqParkedOrderAction.restype = c_void_p
        # 报单操作请求
        self.h.tReqOrderAction.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqOrderAction.restype = c_void_p
        # 查询最大报单数量请求
        self.h.tReqQryMaxOrderVolume.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryMaxOrderVolume.restype = c_void_p
        # 投资者结算结果确认
        self.h.tReqSettlementInfoConfirm.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqSettlementInfoConfirm.restype = c_void_p
        # 请求删除预埋单
        self.h.tReqRemoveParkedOrder.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqRemoveParkedOrder.restype = c_void_p
        # 请求删除预埋撤单
        self.h.tReqRemoveParkedOrderAction.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqRemoveParkedOrderAction.restype = c_void_p
        # 执行宣告录入请求
        self.h.tReqExecOrderInsert.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqExecOrderInsert.restype = c_void_p
        # 执行宣告操作请求
        self.h.tReqExecOrderAction.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqExecOrderAction.restype = c_void_p
        # 询价录入请求
        self.h.tReqForQuoteInsert.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqForQuoteInsert.restype = c_void_p
        # 报价录入请求
        self.h.tReqQuoteInsert.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQuoteInsert.restype = c_void_p
        # 报价操作请求
        self.h.tReqQuoteAction.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQuoteAction.restype = c_void_p
        # 批量报单操作请求
        self.h.tReqBatchOrderAction.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqBatchOrderAction.restype = c_void_p
        # 期权自对冲录入请求
        self.h.tReqOptionSelfCloseInsert.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqOptionSelfCloseInsert.restype = c_void_p
        # 期权自对冲操作请求
        self.h.tReqOptionSelfCloseAction.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqOptionSelfCloseAction.restype = c_void_p
        # 申请组合录入请求
        self.h.tReqCombActionInsert.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqCombActionInsert.restype = c_void_p
        # 请求查询报单
        self.h.tReqQryOrder.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryOrder.restype = c_void_p
        # 请求查询成交
        self.h.tReqQryTrade.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryTrade.restype = c_void_p
        # 请求查询投资者持仓
        self.h.tReqQryInvestorPosition.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryInvestorPosition.restype = c_void_p
        # 请求查询资金账户
        self.h.tReqQryTradingAccount.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryTradingAccount.restype = c_void_p
        # 请求查询投资者
        self.h.tReqQryInvestor.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryInvestor.restype = c_void_p
        # 请求查询交易编码
        self.h.tReqQryTradingCode.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryTradingCode.restype = c_void_p
        # 请求查询合约保证金率
        self.h.tReqQryInstrumentMarginRate.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryInstrumentMarginRate.restype = c_void_p
        # 请求查询合约手续费率
        self.h.tReqQryInstrumentCommissionRate.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryInstrumentCommissionRate.restype = c_void_p
        # 请求查询交易所
        self.h.tReqQryExchange.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryExchange.restype = c_void_p
        # 请求查询产品
        self.h.tReqQryProduct.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryProduct.restype = c_void_p
        # 请求查询合约
        self.h.tReqQryInstrument.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryInstrument.restype = c_void_p
        # 请求查询行情
        self.h.tReqQryDepthMarketData.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryDepthMarketData.restype = c_void_p
        # 请求查询交易员报盘机
        self.h.tReqQryTraderOffer.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryTraderOffer.restype = c_void_p
        # 请求查询投资者结算结果
        self.h.tReqQrySettlementInfo.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQrySettlementInfo.restype = c_void_p
        # 请求查询转帐银行
        self.h.tReqQryTransferBank.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryTransferBank.restype = c_void_p
        # 请求查询投资者持仓明细
        self.h.tReqQryInvestorPositionDetail.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryInvestorPositionDetail.restype = c_void_p
        # 请求查询客户通知
        self.h.tReqQryNotice.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryNotice.restype = c_void_p
        # 请求查询结算信息确认
        self.h.tReqQrySettlementInfoConfirm.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQrySettlementInfoConfirm.restype = c_void_p
        # 请求查询投资者持仓明细
        self.h.tReqQryInvestorPositionCombineDetail.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryInvestorPositionCombineDetail.restype = c_void_p
        # 请求查询保证金监管系统经纪公司资金账户密钥
        self.h.tReqQryCFMMCTradingAccountKey.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryCFMMCTradingAccountKey.restype = c_void_p
        # 请求查询仓单折抵信息
        self.h.tReqQryEWarrantOffset.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryEWarrantOffset.restype = c_void_p
        # 请求查询投资者品种/跨品种保证金
        self.h.tReqQryInvestorProductGroupMargin.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryInvestorProductGroupMargin.restype = c_void_p
        # 请求查询交易所保证金率
        self.h.tReqQryExchangeMarginRate.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryExchangeMarginRate.restype = c_void_p
        # 请求查询交易所调整保证金率
        self.h.tReqQryExchangeMarginRateAdjust.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryExchangeMarginRateAdjust.restype = c_void_p
        # 请求查询汇率
        self.h.tReqQryExchangeRate.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryExchangeRate.restype = c_void_p
        # 请求查询二级代理操作员银期权限
        self.h.tReqQrySecAgentACIDMap.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQrySecAgentACIDMap.restype = c_void_p
        # 请求查询产品报价汇率
        self.h.tReqQryProductExchRate.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryProductExchRate.restype = c_void_p
        # 请求查询产品组
        self.h.tReqQryProductGroup.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryProductGroup.restype = c_void_p
        # 请求查询做市商合约手续费率
        self.h.tReqQryMMInstrumentCommissionRate.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryMMInstrumentCommissionRate.restype = c_void_p
        # 请求查询做市商期权合约手续费
        self.h.tReqQryMMOptionInstrCommRate.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryMMOptionInstrCommRate.restype = c_void_p
        # 请求查询报单手续费
        self.h.tReqQryInstrumentOrderCommRate.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryInstrumentOrderCommRate.restype = c_void_p
        # 请求查询资金账户
        self.h.tReqQrySecAgentTradingAccount.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQrySecAgentTradingAccount.restype = c_void_p
        # 请求查询二级代理商资金校验模式
        self.h.tReqQrySecAgentCheckMode.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQrySecAgentCheckMode.restype = c_void_p
        # 请求查询二级代理商信息
        self.h.tReqQrySecAgentTradeInfo.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQrySecAgentTradeInfo.restype = c_void_p
        # 请求查询期权交易成本
        self.h.tReqQryOptionInstrTradeCost.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryOptionInstrTradeCost.restype = c_void_p
        # 请求查询期权合约手续费
        self.h.tReqQryOptionInstrCommRate.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryOptionInstrCommRate.restype = c_void_p
        # 请求查询执行宣告
        self.h.tReqQryExecOrder.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryExecOrder.restype = c_void_p
        # 请求查询询价
        self.h.tReqQryForQuote.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryForQuote.restype = c_void_p
        # 请求查询报价
        self.h.tReqQryQuote.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryQuote.restype = c_void_p
        # 请求查询期权自对冲
        self.h.tReqQryOptionSelfClose.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryOptionSelfClose.restype = c_void_p
        # 请求查询投资单元
        self.h.tReqQryInvestUnit.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryInvestUnit.restype = c_void_p
        # 请求查询组合合约安全系数
        self.h.tReqQryCombInstrumentGuard.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryCombInstrumentGuard.restype = c_void_p
        # 请求查询申请组合
        self.h.tReqQryCombAction.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryCombAction.restype = c_void_p
        # 请求查询转帐流水
        self.h.tReqQryTransferSerial.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryTransferSerial.restype = c_void_p
        # 请求查询银期签约关系
        self.h.tReqQryAccountregister.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryAccountregister.restype = c_void_p
        # 请求查询签约银行
        self.h.tReqQryContractBank.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryContractBank.restype = c_void_p
        # 请求查询预埋单
        self.h.tReqQryParkedOrder.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryParkedOrder.restype = c_void_p
        # 请求查询预埋撤单
        self.h.tReqQryParkedOrderAction.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryParkedOrderAction.restype = c_void_p
        # 请求查询交易通知
        self.h.tReqQryTradingNotice.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryTradingNotice.restype = c_void_p
        # 请求查询经纪公司交易参数
        self.h.tReqQryBrokerTradingParams.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryBrokerTradingParams.restype = c_void_p
        # 请求查询经纪公司交易算法
        self.h.tReqQryBrokerTradingAlgos.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryBrokerTradingAlgos.restype = c_void_p
        # 请求查询监控中心用户令牌
        self.h.tReqQueryCFMMCTradingAccountToken.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQueryCFMMCTradingAccountToken.restype = c_void_p
        # 期货发起银行资金转期货请求
        self.h.tReqFromBankToFutureByFuture.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqFromBankToFutureByFuture.restype = c_void_p
        # 期货发起期货资金转银行请求
        self.h.tReqFromFutureToBankByFuture.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqFromFutureToBankByFuture.restype = c_void_p
        # 期货发起查询银行余额请求
        self.h.tReqQueryBankAccountMoneyByFuture.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQueryBankAccountMoneyByFuture.restype = c_void_p
        # 请求查询分类合约
        self.h.tReqQryClassifiedInstrument.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryClassifiedInstrument.restype = c_void_p
        # 请求组合优惠比例
        self.h.tReqQryCombPromotionParam.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryCombPromotionParam.restype = c_void_p
        # 投资者风险结算持仓查询
        self.h.tReqQryRiskSettleInvstPosition.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryRiskSettleInvstPosition.restype = c_void_p
        # 风险结算产品查询
        self.h.tReqQryRiskSettleProductStatus.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryRiskSettleProductStatus.restype = c_void_p
        # SPBM期货合约参数查询
        self.h.tReqQrySPBMFutureParameter.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQrySPBMFutureParameter.restype = c_void_p
        # SPBM期权合约参数查询
        self.h.tReqQrySPBMOptionParameter.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQrySPBMOptionParameter.restype = c_void_p
        # SPBM品种内对锁仓折扣参数查询
        self.h.tReqQrySPBMIntraParameter.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQrySPBMIntraParameter.restype = c_void_p
        # SPBM跨品种抵扣参数查询
        self.h.tReqQrySPBMInterParameter.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQrySPBMInterParameter.restype = c_void_p
        # SPBM组合保证金套餐查询
        self.h.tReqQrySPBMPortfDefinition.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQrySPBMPortfDefinition.restype = c_void_p
        # 投资者SPBM套餐选择查询
        self.h.tReqQrySPBMInvestorPortfDef.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQrySPBMInvestorPortfDef.restype = c_void_p
        # 投资者新型组合保证金系数查询
        self.h.tReqQryInvestorPortfMarginRatio.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryInvestorPortfMarginRatio.restype = c_void_p
        # 投资者产品SPBM明细查询
        self.h.tReqQryInvestorProdSPBMDetail.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.tReqQryInvestorProdSPBMDetail.restype = c_void_p
        
        os.chdir(cur_path)

    def CreateApi(self):
        self.api = self.h.tCreateApi(c_char_p(self.logdir.encode("utf-8")))

    def CreateSpi(self):
        self.pSpi = self.h.tCreateSpi()
        #################### 响应函数 #########################
        # 当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。
        self.h.tOnFrontConnected.argtypes = [c_void_p, c_void_p]
        self.h.tOnFrontConnected.restype = None
        self.FP_OnFrontConnected = CFUNCTYPE(None)(self.__OnFrontConnected)
        self.h.tOnFrontConnected(self.pSpi, self.FP_OnFrontConnected)
        # 当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。
        self.h.tOnFrontDisconnected.argtypes = [c_void_p, c_void_p]
        self.h.tOnFrontDisconnected.restype = None
        self.FP_OnFrontDisconnected = CFUNCTYPE(None, c_int32)(self.__OnFrontDisconnected)
        self.h.tOnFrontDisconnected(self.pSpi, self.FP_OnFrontDisconnected)
        # 心跳超时警告。当长时间未收到报文时，该方法被调用。
        self.h.tOnHeartBeatWarning.argtypes = [c_void_p, c_void_p]
        self.h.tOnHeartBeatWarning.restype = None
        self.FP_OnHeartBeatWarning = CFUNCTYPE(None, c_int32)(self.__OnHeartBeatWarning)
        self.h.tOnHeartBeatWarning(self.pSpi, self.FP_OnHeartBeatWarning)
        # 客户端认证响应
        self.h.tOnRspAuthenticate.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspAuthenticate.restype = None
        self.FP_OnRspAuthenticate = CFUNCTYPE(None, POINTER(CThostFtdcRspAuthenticateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspAuthenticate)
        self.h.tOnRspAuthenticate(self.pSpi, self.FP_OnRspAuthenticate)
        # 登录请求响应
        self.h.tOnRspUserLogin.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspUserLogin.restype = None
        self.FP_OnRspUserLogin = CFUNCTYPE(None, POINTER(CThostFtdcRspUserLoginField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspUserLogin)
        self.h.tOnRspUserLogin(self.pSpi, self.FP_OnRspUserLogin)
        # 登出请求响应
        self.h.tOnRspUserLogout.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspUserLogout.restype = None
        self.FP_OnRspUserLogout = CFUNCTYPE(None, POINTER(CThostFtdcUserLogoutField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspUserLogout)
        self.h.tOnRspUserLogout(self.pSpi, self.FP_OnRspUserLogout)
        # 用户口令更新请求响应
        self.h.tOnRspUserPasswordUpdate.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspUserPasswordUpdate.restype = None
        self.FP_OnRspUserPasswordUpdate = CFUNCTYPE(None, POINTER(CThostFtdcUserPasswordUpdateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspUserPasswordUpdate)
        self.h.tOnRspUserPasswordUpdate(self.pSpi, self.FP_OnRspUserPasswordUpdate)
        # 资金账户口令更新请求响应
        self.h.tOnRspTradingAccountPasswordUpdate.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspTradingAccountPasswordUpdate.restype = None
        self.FP_OnRspTradingAccountPasswordUpdate = CFUNCTYPE(None, POINTER(CThostFtdcTradingAccountPasswordUpdateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspTradingAccountPasswordUpdate)
        self.h.tOnRspTradingAccountPasswordUpdate(self.pSpi, self.FP_OnRspTradingAccountPasswordUpdate)
        # 查询用户当前支持的认证模式的回复
        self.h.tOnRspUserAuthMethod.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspUserAuthMethod.restype = None
        self.FP_OnRspUserAuthMethod = CFUNCTYPE(None, POINTER(CThostFtdcRspUserAuthMethodField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspUserAuthMethod)
        self.h.tOnRspUserAuthMethod(self.pSpi, self.FP_OnRspUserAuthMethod)
        # 获取图形验证码请求的回复
        self.h.tOnRspGenUserCaptcha.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspGenUserCaptcha.restype = None
        self.FP_OnRspGenUserCaptcha = CFUNCTYPE(None, POINTER(CThostFtdcRspGenUserCaptchaField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspGenUserCaptcha)
        self.h.tOnRspGenUserCaptcha(self.pSpi, self.FP_OnRspGenUserCaptcha)
        # 获取短信验证码请求的回复
        self.h.tOnRspGenUserText.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspGenUserText.restype = None
        self.FP_OnRspGenUserText = CFUNCTYPE(None, POINTER(CThostFtdcRspGenUserTextField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspGenUserText)
        self.h.tOnRspGenUserText(self.pSpi, self.FP_OnRspGenUserText)
        # 报单录入请求响应
        self.h.tOnRspOrderInsert.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspOrderInsert.restype = None
        self.FP_OnRspOrderInsert = CFUNCTYPE(None, POINTER(CThostFtdcInputOrderField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspOrderInsert)
        self.h.tOnRspOrderInsert(self.pSpi, self.FP_OnRspOrderInsert)
        # 预埋单录入请求响应
        self.h.tOnRspParkedOrderInsert.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspParkedOrderInsert.restype = None
        self.FP_OnRspParkedOrderInsert = CFUNCTYPE(None, POINTER(CThostFtdcParkedOrderField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspParkedOrderInsert)
        self.h.tOnRspParkedOrderInsert(self.pSpi, self.FP_OnRspParkedOrderInsert)
        # 预埋撤单录入请求响应
        self.h.tOnRspParkedOrderAction.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspParkedOrderAction.restype = None
        self.FP_OnRspParkedOrderAction = CFUNCTYPE(None, POINTER(CThostFtdcParkedOrderActionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspParkedOrderAction)
        self.h.tOnRspParkedOrderAction(self.pSpi, self.FP_OnRspParkedOrderAction)
        # 报单操作请求响应
        self.h.tOnRspOrderAction.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspOrderAction.restype = None
        self.FP_OnRspOrderAction = CFUNCTYPE(None, POINTER(CThostFtdcInputOrderActionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspOrderAction)
        self.h.tOnRspOrderAction(self.pSpi, self.FP_OnRspOrderAction)
        # 查询最大报单数量响应
        self.h.tOnRspQryMaxOrderVolume.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryMaxOrderVolume.restype = None
        self.FP_OnRspQryMaxOrderVolume = CFUNCTYPE(None, POINTER(CThostFtdcQryMaxOrderVolumeField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryMaxOrderVolume)
        self.h.tOnRspQryMaxOrderVolume(self.pSpi, self.FP_OnRspQryMaxOrderVolume)
        # 投资者结算结果确认响应
        self.h.tOnRspSettlementInfoConfirm.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspSettlementInfoConfirm.restype = None
        self.FP_OnRspSettlementInfoConfirm = CFUNCTYPE(None, POINTER(CThostFtdcSettlementInfoConfirmField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspSettlementInfoConfirm)
        self.h.tOnRspSettlementInfoConfirm(self.pSpi, self.FP_OnRspSettlementInfoConfirm)
        # 删除预埋单响应
        self.h.tOnRspRemoveParkedOrder.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspRemoveParkedOrder.restype = None
        self.FP_OnRspRemoveParkedOrder = CFUNCTYPE(None, POINTER(CThostFtdcRemoveParkedOrderField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspRemoveParkedOrder)
        self.h.tOnRspRemoveParkedOrder(self.pSpi, self.FP_OnRspRemoveParkedOrder)
        # 删除预埋撤单响应
        self.h.tOnRspRemoveParkedOrderAction.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspRemoveParkedOrderAction.restype = None
        self.FP_OnRspRemoveParkedOrderAction = CFUNCTYPE(None, POINTER(CThostFtdcRemoveParkedOrderActionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspRemoveParkedOrderAction)
        self.h.tOnRspRemoveParkedOrderAction(self.pSpi, self.FP_OnRspRemoveParkedOrderAction)
        # 执行宣告录入请求响应
        self.h.tOnRspExecOrderInsert.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspExecOrderInsert.restype = None
        self.FP_OnRspExecOrderInsert = CFUNCTYPE(None, POINTER(CThostFtdcInputExecOrderField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspExecOrderInsert)
        self.h.tOnRspExecOrderInsert(self.pSpi, self.FP_OnRspExecOrderInsert)
        # 执行宣告操作请求响应
        self.h.tOnRspExecOrderAction.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspExecOrderAction.restype = None
        self.FP_OnRspExecOrderAction = CFUNCTYPE(None, POINTER(CThostFtdcInputExecOrderActionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspExecOrderAction)
        self.h.tOnRspExecOrderAction(self.pSpi, self.FP_OnRspExecOrderAction)
        # 询价录入请求响应
        self.h.tOnRspForQuoteInsert.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspForQuoteInsert.restype = None
        self.FP_OnRspForQuoteInsert = CFUNCTYPE(None, POINTER(CThostFtdcInputForQuoteField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspForQuoteInsert)
        self.h.tOnRspForQuoteInsert(self.pSpi, self.FP_OnRspForQuoteInsert)
        # 报价录入请求响应
        self.h.tOnRspQuoteInsert.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQuoteInsert.restype = None
        self.FP_OnRspQuoteInsert = CFUNCTYPE(None, POINTER(CThostFtdcInputQuoteField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQuoteInsert)
        self.h.tOnRspQuoteInsert(self.pSpi, self.FP_OnRspQuoteInsert)
        # 报价操作请求响应
        self.h.tOnRspQuoteAction.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQuoteAction.restype = None
        self.FP_OnRspQuoteAction = CFUNCTYPE(None, POINTER(CThostFtdcInputQuoteActionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQuoteAction)
        self.h.tOnRspQuoteAction(self.pSpi, self.FP_OnRspQuoteAction)
        # 批量报单操作请求响应
        self.h.tOnRspBatchOrderAction.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspBatchOrderAction.restype = None
        self.FP_OnRspBatchOrderAction = CFUNCTYPE(None, POINTER(CThostFtdcInputBatchOrderActionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspBatchOrderAction)
        self.h.tOnRspBatchOrderAction(self.pSpi, self.FP_OnRspBatchOrderAction)
        # 期权自对冲录入请求响应
        self.h.tOnRspOptionSelfCloseInsert.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspOptionSelfCloseInsert.restype = None
        self.FP_OnRspOptionSelfCloseInsert = CFUNCTYPE(None, POINTER(CThostFtdcInputOptionSelfCloseField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspOptionSelfCloseInsert)
        self.h.tOnRspOptionSelfCloseInsert(self.pSpi, self.FP_OnRspOptionSelfCloseInsert)
        # 期权自对冲操作请求响应
        self.h.tOnRspOptionSelfCloseAction.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspOptionSelfCloseAction.restype = None
        self.FP_OnRspOptionSelfCloseAction = CFUNCTYPE(None, POINTER(CThostFtdcInputOptionSelfCloseActionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspOptionSelfCloseAction)
        self.h.tOnRspOptionSelfCloseAction(self.pSpi, self.FP_OnRspOptionSelfCloseAction)
        # 申请组合录入请求响应
        self.h.tOnRspCombActionInsert.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspCombActionInsert.restype = None
        self.FP_OnRspCombActionInsert = CFUNCTYPE(None, POINTER(CThostFtdcInputCombActionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspCombActionInsert)
        self.h.tOnRspCombActionInsert(self.pSpi, self.FP_OnRspCombActionInsert)
        # 请求查询报单响应
        self.h.tOnRspQryOrder.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryOrder.restype = None
        self.FP_OnRspQryOrder = CFUNCTYPE(None, POINTER(CThostFtdcOrderField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryOrder)
        self.h.tOnRspQryOrder(self.pSpi, self.FP_OnRspQryOrder)
        # 请求查询成交响应
        self.h.tOnRspQryTrade.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryTrade.restype = None
        self.FP_OnRspQryTrade = CFUNCTYPE(None, POINTER(CThostFtdcTradeField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryTrade)
        self.h.tOnRspQryTrade(self.pSpi, self.FP_OnRspQryTrade)
        # 请求查询投资者持仓响应
        self.h.tOnRspQryInvestorPosition.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryInvestorPosition.restype = None
        self.FP_OnRspQryInvestorPosition = CFUNCTYPE(None, POINTER(CThostFtdcInvestorPositionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInvestorPosition)
        self.h.tOnRspQryInvestorPosition(self.pSpi, self.FP_OnRspQryInvestorPosition)
        # 请求查询资金账户响应
        self.h.tOnRspQryTradingAccount.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryTradingAccount.restype = None
        self.FP_OnRspQryTradingAccount = CFUNCTYPE(None, POINTER(CThostFtdcTradingAccountField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryTradingAccount)
        self.h.tOnRspQryTradingAccount(self.pSpi, self.FP_OnRspQryTradingAccount)
        # 请求查询投资者响应
        self.h.tOnRspQryInvestor.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryInvestor.restype = None
        self.FP_OnRspQryInvestor = CFUNCTYPE(None, POINTER(CThostFtdcInvestorField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInvestor)
        self.h.tOnRspQryInvestor(self.pSpi, self.FP_OnRspQryInvestor)
        # 请求查询交易编码响应
        self.h.tOnRspQryTradingCode.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryTradingCode.restype = None
        self.FP_OnRspQryTradingCode = CFUNCTYPE(None, POINTER(CThostFtdcTradingCodeField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryTradingCode)
        self.h.tOnRspQryTradingCode(self.pSpi, self.FP_OnRspQryTradingCode)
        # 请求查询合约保证金率响应
        self.h.tOnRspQryInstrumentMarginRate.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryInstrumentMarginRate.restype = None
        self.FP_OnRspQryInstrumentMarginRate = CFUNCTYPE(None, POINTER(CThostFtdcInstrumentMarginRateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInstrumentMarginRate)
        self.h.tOnRspQryInstrumentMarginRate(self.pSpi, self.FP_OnRspQryInstrumentMarginRate)
        # 请求查询合约手续费率响应
        self.h.tOnRspQryInstrumentCommissionRate.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryInstrumentCommissionRate.restype = None
        self.FP_OnRspQryInstrumentCommissionRate = CFUNCTYPE(None, POINTER(CThostFtdcInstrumentCommissionRateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInstrumentCommissionRate)
        self.h.tOnRspQryInstrumentCommissionRate(self.pSpi, self.FP_OnRspQryInstrumentCommissionRate)
        # 请求查询交易所响应
        self.h.tOnRspQryExchange.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryExchange.restype = None
        self.FP_OnRspQryExchange = CFUNCTYPE(None, POINTER(CThostFtdcExchangeField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryExchange)
        self.h.tOnRspQryExchange(self.pSpi, self.FP_OnRspQryExchange)
        # 请求查询产品响应
        self.h.tOnRspQryProduct.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryProduct.restype = None
        self.FP_OnRspQryProduct = CFUNCTYPE(None, POINTER(CThostFtdcProductField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryProduct)
        self.h.tOnRspQryProduct(self.pSpi, self.FP_OnRspQryProduct)
        # 请求查询合约响应
        self.h.tOnRspQryInstrument.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryInstrument.restype = None
        self.FP_OnRspQryInstrument = CFUNCTYPE(None, POINTER(CThostFtdcInstrumentField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInstrument)
        self.h.tOnRspQryInstrument(self.pSpi, self.FP_OnRspQryInstrument)
        # 请求查询行情响应
        self.h.tOnRspQryDepthMarketData.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryDepthMarketData.restype = None
        self.FP_OnRspQryDepthMarketData = CFUNCTYPE(None, POINTER(CThostFtdcDepthMarketDataField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryDepthMarketData)
        self.h.tOnRspQryDepthMarketData(self.pSpi, self.FP_OnRspQryDepthMarketData)
        # 请求查询交易员报盘机响应
        self.h.tOnRspQryTraderOffer.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryTraderOffer.restype = None
        self.FP_OnRspQryTraderOffer = CFUNCTYPE(None, POINTER(CThostFtdcTraderOfferField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryTraderOffer)
        self.h.tOnRspQryTraderOffer(self.pSpi, self.FP_OnRspQryTraderOffer)
        # 请求查询投资者结算结果响应
        self.h.tOnRspQrySettlementInfo.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQrySettlementInfo.restype = None
        self.FP_OnRspQrySettlementInfo = CFUNCTYPE(None, POINTER(CThostFtdcSettlementInfoField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQrySettlementInfo)
        self.h.tOnRspQrySettlementInfo(self.pSpi, self.FP_OnRspQrySettlementInfo)
        # 请求查询转帐银行响应
        self.h.tOnRspQryTransferBank.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryTransferBank.restype = None
        self.FP_OnRspQryTransferBank = CFUNCTYPE(None, POINTER(CThostFtdcTransferBankField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryTransferBank)
        self.h.tOnRspQryTransferBank(self.pSpi, self.FP_OnRspQryTransferBank)
        # 请求查询投资者持仓明细响应
        self.h.tOnRspQryInvestorPositionDetail.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryInvestorPositionDetail.restype = None
        self.FP_OnRspQryInvestorPositionDetail = CFUNCTYPE(None, POINTER(CThostFtdcInvestorPositionDetailField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInvestorPositionDetail)
        self.h.tOnRspQryInvestorPositionDetail(self.pSpi, self.FP_OnRspQryInvestorPositionDetail)
        # 请求查询客户通知响应
        self.h.tOnRspQryNotice.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryNotice.restype = None
        self.FP_OnRspQryNotice = CFUNCTYPE(None, POINTER(CThostFtdcNoticeField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryNotice)
        self.h.tOnRspQryNotice(self.pSpi, self.FP_OnRspQryNotice)
        # 请求查询结算信息确认响应
        self.h.tOnRspQrySettlementInfoConfirm.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQrySettlementInfoConfirm.restype = None
        self.FP_OnRspQrySettlementInfoConfirm = CFUNCTYPE(None, POINTER(CThostFtdcSettlementInfoConfirmField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQrySettlementInfoConfirm)
        self.h.tOnRspQrySettlementInfoConfirm(self.pSpi, self.FP_OnRspQrySettlementInfoConfirm)
        # 请求查询投资者持仓明细响应
        self.h.tOnRspQryInvestorPositionCombineDetail.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryInvestorPositionCombineDetail.restype = None
        self.FP_OnRspQryInvestorPositionCombineDetail = CFUNCTYPE(None, POINTER(CThostFtdcInvestorPositionCombineDetailField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInvestorPositionCombineDetail)
        self.h.tOnRspQryInvestorPositionCombineDetail(self.pSpi, self.FP_OnRspQryInvestorPositionCombineDetail)
        # 查询保证金监管系统经纪公司资金账户密钥响应
        self.h.tOnRspQryCFMMCTradingAccountKey.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryCFMMCTradingAccountKey.restype = None
        self.FP_OnRspQryCFMMCTradingAccountKey = CFUNCTYPE(None, POINTER(CThostFtdcCFMMCTradingAccountKeyField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryCFMMCTradingAccountKey)
        self.h.tOnRspQryCFMMCTradingAccountKey(self.pSpi, self.FP_OnRspQryCFMMCTradingAccountKey)
        # 请求查询仓单折抵信息响应
        self.h.tOnRspQryEWarrantOffset.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryEWarrantOffset.restype = None
        self.FP_OnRspQryEWarrantOffset = CFUNCTYPE(None, POINTER(CThostFtdcEWarrantOffsetField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryEWarrantOffset)
        self.h.tOnRspQryEWarrantOffset(self.pSpi, self.FP_OnRspQryEWarrantOffset)
        # 请求查询投资者品种/跨品种保证金响应
        self.h.tOnRspQryInvestorProductGroupMargin.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryInvestorProductGroupMargin.restype = None
        self.FP_OnRspQryInvestorProductGroupMargin = CFUNCTYPE(None, POINTER(CThostFtdcInvestorProductGroupMarginField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInvestorProductGroupMargin)
        self.h.tOnRspQryInvestorProductGroupMargin(self.pSpi, self.FP_OnRspQryInvestorProductGroupMargin)
        # 请求查询交易所保证金率响应
        self.h.tOnRspQryExchangeMarginRate.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryExchangeMarginRate.restype = None
        self.FP_OnRspQryExchangeMarginRate = CFUNCTYPE(None, POINTER(CThostFtdcExchangeMarginRateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryExchangeMarginRate)
        self.h.tOnRspQryExchangeMarginRate(self.pSpi, self.FP_OnRspQryExchangeMarginRate)
        # 请求查询交易所调整保证金率响应
        self.h.tOnRspQryExchangeMarginRateAdjust.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryExchangeMarginRateAdjust.restype = None
        self.FP_OnRspQryExchangeMarginRateAdjust = CFUNCTYPE(None, POINTER(CThostFtdcExchangeMarginRateAdjustField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryExchangeMarginRateAdjust)
        self.h.tOnRspQryExchangeMarginRateAdjust(self.pSpi, self.FP_OnRspQryExchangeMarginRateAdjust)
        # 请求查询汇率响应
        self.h.tOnRspQryExchangeRate.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryExchangeRate.restype = None
        self.FP_OnRspQryExchangeRate = CFUNCTYPE(None, POINTER(CThostFtdcExchangeRateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryExchangeRate)
        self.h.tOnRspQryExchangeRate(self.pSpi, self.FP_OnRspQryExchangeRate)
        # 请求查询二级代理操作员银期权限响应
        self.h.tOnRspQrySecAgentACIDMap.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQrySecAgentACIDMap.restype = None
        self.FP_OnRspQrySecAgentACIDMap = CFUNCTYPE(None, POINTER(CThostFtdcSecAgentACIDMapField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQrySecAgentACIDMap)
        self.h.tOnRspQrySecAgentACIDMap(self.pSpi, self.FP_OnRspQrySecAgentACIDMap)
        # 请求查询产品报价汇率
        self.h.tOnRspQryProductExchRate.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryProductExchRate.restype = None
        self.FP_OnRspQryProductExchRate = CFUNCTYPE(None, POINTER(CThostFtdcProductExchRateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryProductExchRate)
        self.h.tOnRspQryProductExchRate(self.pSpi, self.FP_OnRspQryProductExchRate)
        # 请求查询产品组
        self.h.tOnRspQryProductGroup.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryProductGroup.restype = None
        self.FP_OnRspQryProductGroup = CFUNCTYPE(None, POINTER(CThostFtdcProductGroupField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryProductGroup)
        self.h.tOnRspQryProductGroup(self.pSpi, self.FP_OnRspQryProductGroup)
        # 请求查询做市商合约手续费率响应
        self.h.tOnRspQryMMInstrumentCommissionRate.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryMMInstrumentCommissionRate.restype = None
        self.FP_OnRspQryMMInstrumentCommissionRate = CFUNCTYPE(None, POINTER(CThostFtdcMMInstrumentCommissionRateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryMMInstrumentCommissionRate)
        self.h.tOnRspQryMMInstrumentCommissionRate(self.pSpi, self.FP_OnRspQryMMInstrumentCommissionRate)
        # 请求查询做市商期权合约手续费响应
        self.h.tOnRspQryMMOptionInstrCommRate.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryMMOptionInstrCommRate.restype = None
        self.FP_OnRspQryMMOptionInstrCommRate = CFUNCTYPE(None, POINTER(CThostFtdcMMOptionInstrCommRateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryMMOptionInstrCommRate)
        self.h.tOnRspQryMMOptionInstrCommRate(self.pSpi, self.FP_OnRspQryMMOptionInstrCommRate)
        # 请求查询报单手续费响应
        self.h.tOnRspQryInstrumentOrderCommRate.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryInstrumentOrderCommRate.restype = None
        self.FP_OnRspQryInstrumentOrderCommRate = CFUNCTYPE(None, POINTER(CThostFtdcInstrumentOrderCommRateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInstrumentOrderCommRate)
        self.h.tOnRspQryInstrumentOrderCommRate(self.pSpi, self.FP_OnRspQryInstrumentOrderCommRate)
        # 请求查询资金账户响应
        self.h.tOnRspQrySecAgentTradingAccount.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQrySecAgentTradingAccount.restype = None
        self.FP_OnRspQrySecAgentTradingAccount = CFUNCTYPE(None, POINTER(CThostFtdcTradingAccountField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQrySecAgentTradingAccount)
        self.h.tOnRspQrySecAgentTradingAccount(self.pSpi, self.FP_OnRspQrySecAgentTradingAccount)
        # 请求查询二级代理商资金校验模式响应
        self.h.tOnRspQrySecAgentCheckMode.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQrySecAgentCheckMode.restype = None
        self.FP_OnRspQrySecAgentCheckMode = CFUNCTYPE(None, POINTER(CThostFtdcSecAgentCheckModeField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQrySecAgentCheckMode)
        self.h.tOnRspQrySecAgentCheckMode(self.pSpi, self.FP_OnRspQrySecAgentCheckMode)
        # 请求查询二级代理商信息响应
        self.h.tOnRspQrySecAgentTradeInfo.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQrySecAgentTradeInfo.restype = None
        self.FP_OnRspQrySecAgentTradeInfo = CFUNCTYPE(None, POINTER(CThostFtdcSecAgentTradeInfoField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQrySecAgentTradeInfo)
        self.h.tOnRspQrySecAgentTradeInfo(self.pSpi, self.FP_OnRspQrySecAgentTradeInfo)
        # 请求查询期权交易成本响应
        self.h.tOnRspQryOptionInstrTradeCost.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryOptionInstrTradeCost.restype = None
        self.FP_OnRspQryOptionInstrTradeCost = CFUNCTYPE(None, POINTER(CThostFtdcOptionInstrTradeCostField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryOptionInstrTradeCost)
        self.h.tOnRspQryOptionInstrTradeCost(self.pSpi, self.FP_OnRspQryOptionInstrTradeCost)
        # 请求查询期权合约手续费响应
        self.h.tOnRspQryOptionInstrCommRate.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryOptionInstrCommRate.restype = None
        self.FP_OnRspQryOptionInstrCommRate = CFUNCTYPE(None, POINTER(CThostFtdcOptionInstrCommRateField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryOptionInstrCommRate)
        self.h.tOnRspQryOptionInstrCommRate(self.pSpi, self.FP_OnRspQryOptionInstrCommRate)
        # 请求查询执行宣告响应
        self.h.tOnRspQryExecOrder.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryExecOrder.restype = None
        self.FP_OnRspQryExecOrder = CFUNCTYPE(None, POINTER(CThostFtdcExecOrderField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryExecOrder)
        self.h.tOnRspQryExecOrder(self.pSpi, self.FP_OnRspQryExecOrder)
        # 请求查询询价响应
        self.h.tOnRspQryForQuote.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryForQuote.restype = None
        self.FP_OnRspQryForQuote = CFUNCTYPE(None, POINTER(CThostFtdcForQuoteField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryForQuote)
        self.h.tOnRspQryForQuote(self.pSpi, self.FP_OnRspQryForQuote)
        # 请求查询报价响应
        self.h.tOnRspQryQuote.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryQuote.restype = None
        self.FP_OnRspQryQuote = CFUNCTYPE(None, POINTER(CThostFtdcQuoteField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryQuote)
        self.h.tOnRspQryQuote(self.pSpi, self.FP_OnRspQryQuote)
        # 请求查询期权自对冲响应
        self.h.tOnRspQryOptionSelfClose.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryOptionSelfClose.restype = None
        self.FP_OnRspQryOptionSelfClose = CFUNCTYPE(None, POINTER(CThostFtdcOptionSelfCloseField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryOptionSelfClose)
        self.h.tOnRspQryOptionSelfClose(self.pSpi, self.FP_OnRspQryOptionSelfClose)
        # 请求查询投资单元响应
        self.h.tOnRspQryInvestUnit.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryInvestUnit.restype = None
        self.FP_OnRspQryInvestUnit = CFUNCTYPE(None, POINTER(CThostFtdcInvestUnitField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInvestUnit)
        self.h.tOnRspQryInvestUnit(self.pSpi, self.FP_OnRspQryInvestUnit)
        # 请求查询组合合约安全系数响应
        self.h.tOnRspQryCombInstrumentGuard.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryCombInstrumentGuard.restype = None
        self.FP_OnRspQryCombInstrumentGuard = CFUNCTYPE(None, POINTER(CThostFtdcCombInstrumentGuardField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryCombInstrumentGuard)
        self.h.tOnRspQryCombInstrumentGuard(self.pSpi, self.FP_OnRspQryCombInstrumentGuard)
        # 请求查询申请组合响应
        self.h.tOnRspQryCombAction.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryCombAction.restype = None
        self.FP_OnRspQryCombAction = CFUNCTYPE(None, POINTER(CThostFtdcCombActionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryCombAction)
        self.h.tOnRspQryCombAction(self.pSpi, self.FP_OnRspQryCombAction)
        # 请求查询转帐流水响应
        self.h.tOnRspQryTransferSerial.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryTransferSerial.restype = None
        self.FP_OnRspQryTransferSerial = CFUNCTYPE(None, POINTER(CThostFtdcTransferSerialField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryTransferSerial)
        self.h.tOnRspQryTransferSerial(self.pSpi, self.FP_OnRspQryTransferSerial)
        # 请求查询银期签约关系响应
        self.h.tOnRspQryAccountregister.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryAccountregister.restype = None
        self.FP_OnRspQryAccountregister = CFUNCTYPE(None, POINTER(CThostFtdcAccountregisterField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryAccountregister)
        self.h.tOnRspQryAccountregister(self.pSpi, self.FP_OnRspQryAccountregister)
        # 错误应答
        self.h.tOnRspError.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspError.restype = None
        self.FP_OnRspError = CFUNCTYPE(None, POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspError)
        self.h.tOnRspError(self.pSpi, self.FP_OnRspError)
        # 报单通知
        self.h.tOnRtnOrder.argtypes = [c_void_p, c_void_p]
        self.h.tOnRtnOrder.restype = None
        self.FP_OnRtnOrder = CFUNCTYPE(None, POINTER(CThostFtdcOrderField))(self.__OnRtnOrder)
        self.h.tOnRtnOrder(self.pSpi, self.FP_OnRtnOrder)
        # 成交通知
        self.h.tOnRtnTrade.argtypes = [c_void_p, c_void_p]
        self.h.tOnRtnTrade.restype = None
        self.FP_OnRtnTrade = CFUNCTYPE(None, POINTER(CThostFtdcTradeField))(self.__OnRtnTrade)
        self.h.tOnRtnTrade(self.pSpi, self.FP_OnRtnTrade)
        # 报单录入错误回报
        self.h.tOnErrRtnOrderInsert.argtypes = [c_void_p, c_void_p]
        self.h.tOnErrRtnOrderInsert.restype = None
        self.FP_OnErrRtnOrderInsert = CFUNCTYPE(None, POINTER(CThostFtdcInputOrderField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnOrderInsert)
        self.h.tOnErrRtnOrderInsert(self.pSpi, self.FP_OnErrRtnOrderInsert)
        # 报单操作错误回报
        self.h.tOnErrRtnOrderAction.argtypes = [c_void_p, c_void_p]
        self.h.tOnErrRtnOrderAction.restype = None
        self.FP_OnErrRtnOrderAction = CFUNCTYPE(None, POINTER(CThostFtdcOrderActionField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnOrderAction)
        self.h.tOnErrRtnOrderAction(self.pSpi, self.FP_OnErrRtnOrderAction)
        # 合约交易状态通知
        self.h.tOnRtnInstrumentStatus.argtypes = [c_void_p, c_void_p]
        self.h.tOnRtnInstrumentStatus.restype = None
        self.FP_OnRtnInstrumentStatus = CFUNCTYPE(None, POINTER(CThostFtdcInstrumentStatusField))(self.__OnRtnInstrumentStatus)
        self.h.tOnRtnInstrumentStatus(self.pSpi, self.FP_OnRtnInstrumentStatus)
        # 交易所公告通知
        self.h.tOnRtnBulletin.argtypes = [c_void_p, c_void_p]
        self.h.tOnRtnBulletin.restype = None
        self.FP_OnRtnBulletin = CFUNCTYPE(None, POINTER(CThostFtdcBulletinField))(self.__OnRtnBulletin)
        self.h.tOnRtnBulletin(self.pSpi, self.FP_OnRtnBulletin)
        # 交易通知
        self.h.tOnRtnTradingNotice.argtypes = [c_void_p, c_void_p]
        self.h.tOnRtnTradingNotice.restype = None
        self.FP_OnRtnTradingNotice = CFUNCTYPE(None, POINTER(CThostFtdcTradingNoticeInfoField))(self.__OnRtnTradingNotice)
        self.h.tOnRtnTradingNotice(self.pSpi, self.FP_OnRtnTradingNotice)
        # 提示条件单校验错误
        self.h.tOnRtnErrorConditionalOrder.argtypes = [c_void_p, c_void_p]
        self.h.tOnRtnErrorConditionalOrder.restype = None
        self.FP_OnRtnErrorConditionalOrder = CFUNCTYPE(None, POINTER(CThostFtdcErrorConditionalOrderField))(self.__OnRtnErrorConditionalOrder)
        self.h.tOnRtnErrorConditionalOrder(self.pSpi, self.FP_OnRtnErrorConditionalOrder)
        # 执行宣告通知
        self.h.tOnRtnExecOrder.argtypes = [c_void_p, c_void_p]
        self.h.tOnRtnExecOrder.restype = None
        self.FP_OnRtnExecOrder = CFUNCTYPE(None, POINTER(CThostFtdcExecOrderField))(self.__OnRtnExecOrder)
        self.h.tOnRtnExecOrder(self.pSpi, self.FP_OnRtnExecOrder)
        # 执行宣告录入错误回报
        self.h.tOnErrRtnExecOrderInsert.argtypes = [c_void_p, c_void_p]
        self.h.tOnErrRtnExecOrderInsert.restype = None
        self.FP_OnErrRtnExecOrderInsert = CFUNCTYPE(None, POINTER(CThostFtdcInputExecOrderField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnExecOrderInsert)
        self.h.tOnErrRtnExecOrderInsert(self.pSpi, self.FP_OnErrRtnExecOrderInsert)
        # 执行宣告操作错误回报
        self.h.tOnErrRtnExecOrderAction.argtypes = [c_void_p, c_void_p]
        self.h.tOnErrRtnExecOrderAction.restype = None
        self.FP_OnErrRtnExecOrderAction = CFUNCTYPE(None, POINTER(CThostFtdcExecOrderActionField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnExecOrderAction)
        self.h.tOnErrRtnExecOrderAction(self.pSpi, self.FP_OnErrRtnExecOrderAction)
        # 询价录入错误回报
        self.h.tOnErrRtnForQuoteInsert.argtypes = [c_void_p, c_void_p]
        self.h.tOnErrRtnForQuoteInsert.restype = None
        self.FP_OnErrRtnForQuoteInsert = CFUNCTYPE(None, POINTER(CThostFtdcInputForQuoteField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnForQuoteInsert)
        self.h.tOnErrRtnForQuoteInsert(self.pSpi, self.FP_OnErrRtnForQuoteInsert)
        # 报价通知
        self.h.tOnRtnQuote.argtypes = [c_void_p, c_void_p]
        self.h.tOnRtnQuote.restype = None
        self.FP_OnRtnQuote = CFUNCTYPE(None, POINTER(CThostFtdcQuoteField))(self.__OnRtnQuote)
        self.h.tOnRtnQuote(self.pSpi, self.FP_OnRtnQuote)
        # 报价录入错误回报
        self.h.tOnErrRtnQuoteInsert.argtypes = [c_void_p, c_void_p]
        self.h.tOnErrRtnQuoteInsert.restype = None
        self.FP_OnErrRtnQuoteInsert = CFUNCTYPE(None, POINTER(CThostFtdcInputQuoteField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnQuoteInsert)
        self.h.tOnErrRtnQuoteInsert(self.pSpi, self.FP_OnErrRtnQuoteInsert)
        # 报价操作错误回报
        self.h.tOnErrRtnQuoteAction.argtypes = [c_void_p, c_void_p]
        self.h.tOnErrRtnQuoteAction.restype = None
        self.FP_OnErrRtnQuoteAction = CFUNCTYPE(None, POINTER(CThostFtdcQuoteActionField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnQuoteAction)
        self.h.tOnErrRtnQuoteAction(self.pSpi, self.FP_OnErrRtnQuoteAction)
        # 询价通知
        self.h.tOnRtnForQuoteRsp.argtypes = [c_void_p, c_void_p]
        self.h.tOnRtnForQuoteRsp.restype = None
        self.FP_OnRtnForQuoteRsp = CFUNCTYPE(None, POINTER(CThostFtdcForQuoteRspField))(self.__OnRtnForQuoteRsp)
        self.h.tOnRtnForQuoteRsp(self.pSpi, self.FP_OnRtnForQuoteRsp)
        # 保证金监控中心用户令牌
        self.h.tOnRtnCFMMCTradingAccountToken.argtypes = [c_void_p, c_void_p]
        self.h.tOnRtnCFMMCTradingAccountToken.restype = None
        self.FP_OnRtnCFMMCTradingAccountToken = CFUNCTYPE(None, POINTER(CThostFtdcCFMMCTradingAccountTokenField))(self.__OnRtnCFMMCTradingAccountToken)
        self.h.tOnRtnCFMMCTradingAccountToken(self.pSpi, self.FP_OnRtnCFMMCTradingAccountToken)
        # 批量报单操作错误回报
        self.h.tOnErrRtnBatchOrderAction.argtypes = [c_void_p, c_void_p]
        self.h.tOnErrRtnBatchOrderAction.restype = None
        self.FP_OnErrRtnBatchOrderAction = CFUNCTYPE(None, POINTER(CThostFtdcBatchOrderActionField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnBatchOrderAction)
        self.h.tOnErrRtnBatchOrderAction(self.pSpi, self.FP_OnErrRtnBatchOrderAction)
        # 期权自对冲通知
        self.h.tOnRtnOptionSelfClose.argtypes = [c_void_p, c_void_p]
        self.h.tOnRtnOptionSelfClose.restype = None
        self.FP_OnRtnOptionSelfClose = CFUNCTYPE(None, POINTER(CThostFtdcOptionSelfCloseField))(self.__OnRtnOptionSelfClose)
        self.h.tOnRtnOptionSelfClose(self.pSpi, self.FP_OnRtnOptionSelfClose)
        # 期权自对冲录入错误回报
        self.h.tOnErrRtnOptionSelfCloseInsert.argtypes = [c_void_p, c_void_p]
        self.h.tOnErrRtnOptionSelfCloseInsert.restype = None
        self.FP_OnErrRtnOptionSelfCloseInsert = CFUNCTYPE(None, POINTER(CThostFtdcInputOptionSelfCloseField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnOptionSelfCloseInsert)
        self.h.tOnErrRtnOptionSelfCloseInsert(self.pSpi, self.FP_OnErrRtnOptionSelfCloseInsert)
        # 期权自对冲操作错误回报
        self.h.tOnErrRtnOptionSelfCloseAction.argtypes = [c_void_p, c_void_p]
        self.h.tOnErrRtnOptionSelfCloseAction.restype = None
        self.FP_OnErrRtnOptionSelfCloseAction = CFUNCTYPE(None, POINTER(CThostFtdcOptionSelfCloseActionField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnOptionSelfCloseAction)
        self.h.tOnErrRtnOptionSelfCloseAction(self.pSpi, self.FP_OnErrRtnOptionSelfCloseAction)
        # 申请组合通知
        self.h.tOnRtnCombAction.argtypes = [c_void_p, c_void_p]
        self.h.tOnRtnCombAction.restype = None
        self.FP_OnRtnCombAction = CFUNCTYPE(None, POINTER(CThostFtdcCombActionField))(self.__OnRtnCombAction)
        self.h.tOnRtnCombAction(self.pSpi, self.FP_OnRtnCombAction)
        # 申请组合录入错误回报
        self.h.tOnErrRtnCombActionInsert.argtypes = [c_void_p, c_void_p]
        self.h.tOnErrRtnCombActionInsert.restype = None
        self.FP_OnErrRtnCombActionInsert = CFUNCTYPE(None, POINTER(CThostFtdcInputCombActionField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnCombActionInsert)
        self.h.tOnErrRtnCombActionInsert(self.pSpi, self.FP_OnErrRtnCombActionInsert)
        # 请求查询签约银行响应
        self.h.tOnRspQryContractBank.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryContractBank.restype = None
        self.FP_OnRspQryContractBank = CFUNCTYPE(None, POINTER(CThostFtdcContractBankField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryContractBank)
        self.h.tOnRspQryContractBank(self.pSpi, self.FP_OnRspQryContractBank)
        # 请求查询预埋单响应
        self.h.tOnRspQryParkedOrder.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryParkedOrder.restype = None
        self.FP_OnRspQryParkedOrder = CFUNCTYPE(None, POINTER(CThostFtdcParkedOrderField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryParkedOrder)
        self.h.tOnRspQryParkedOrder(self.pSpi, self.FP_OnRspQryParkedOrder)
        # 请求查询预埋撤单响应
        self.h.tOnRspQryParkedOrderAction.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryParkedOrderAction.restype = None
        self.FP_OnRspQryParkedOrderAction = CFUNCTYPE(None, POINTER(CThostFtdcParkedOrderActionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryParkedOrderAction)
        self.h.tOnRspQryParkedOrderAction(self.pSpi, self.FP_OnRspQryParkedOrderAction)
        # 请求查询交易通知响应
        self.h.tOnRspQryTradingNotice.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryTradingNotice.restype = None
        self.FP_OnRspQryTradingNotice = CFUNCTYPE(None, POINTER(CThostFtdcTradingNoticeField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryTradingNotice)
        self.h.tOnRspQryTradingNotice(self.pSpi, self.FP_OnRspQryTradingNotice)
        # 请求查询经纪公司交易参数响应
        self.h.tOnRspQryBrokerTradingParams.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryBrokerTradingParams.restype = None
        self.FP_OnRspQryBrokerTradingParams = CFUNCTYPE(None, POINTER(CThostFtdcBrokerTradingParamsField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryBrokerTradingParams)
        self.h.tOnRspQryBrokerTradingParams(self.pSpi, self.FP_OnRspQryBrokerTradingParams)
        # 请求查询经纪公司交易算法响应
        self.h.tOnRspQryBrokerTradingAlgos.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryBrokerTradingAlgos.restype = None
        self.FP_OnRspQryBrokerTradingAlgos = CFUNCTYPE(None, POINTER(CThostFtdcBrokerTradingAlgosField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryBrokerTradingAlgos)
        self.h.tOnRspQryBrokerTradingAlgos(self.pSpi, self.FP_OnRspQryBrokerTradingAlgos)
        # 请求查询监控中心用户令牌
        self.h.tOnRspQueryCFMMCTradingAccountToken.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQueryCFMMCTradingAccountToken.restype = None
        self.FP_OnRspQueryCFMMCTradingAccountToken = CFUNCTYPE(None, POINTER(CThostFtdcQueryCFMMCTradingAccountTokenField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQueryCFMMCTradingAccountToken)
        self.h.tOnRspQueryCFMMCTradingAccountToken(self.pSpi, self.FP_OnRspQueryCFMMCTradingAccountToken)
        # 银行发起银行资金转期货通知
        self.h.tOnRtnFromBankToFutureByBank.argtypes = [c_void_p, c_void_p]
        self.h.tOnRtnFromBankToFutureByBank.restype = None
        self.FP_OnRtnFromBankToFutureByBank = CFUNCTYPE(None, POINTER(CThostFtdcRspTransferField))(self.__OnRtnFromBankToFutureByBank)
        self.h.tOnRtnFromBankToFutureByBank(self.pSpi, self.FP_OnRtnFromBankToFutureByBank)
        # 银行发起期货资金转银行通知
        self.h.tOnRtnFromFutureToBankByBank.argtypes = [c_void_p, c_void_p]
        self.h.tOnRtnFromFutureToBankByBank.restype = None
        self.FP_OnRtnFromFutureToBankByBank = CFUNCTYPE(None, POINTER(CThostFtdcRspTransferField))(self.__OnRtnFromFutureToBankByBank)
        self.h.tOnRtnFromFutureToBankByBank(self.pSpi, self.FP_OnRtnFromFutureToBankByBank)
        # 银行发起冲正银行转期货通知
        self.h.tOnRtnRepealFromBankToFutureByBank.argtypes = [c_void_p, c_void_p]
        self.h.tOnRtnRepealFromBankToFutureByBank.restype = None
        self.FP_OnRtnRepealFromBankToFutureByBank = CFUNCTYPE(None, POINTER(CThostFtdcRspRepealField))(self.__OnRtnRepealFromBankToFutureByBank)
        self.h.tOnRtnRepealFromBankToFutureByBank(self.pSpi, self.FP_OnRtnRepealFromBankToFutureByBank)
        # 银行发起冲正期货转银行通知
        self.h.tOnRtnRepealFromFutureToBankByBank.argtypes = [c_void_p, c_void_p]
        self.h.tOnRtnRepealFromFutureToBankByBank.restype = None
        self.FP_OnRtnRepealFromFutureToBankByBank = CFUNCTYPE(None, POINTER(CThostFtdcRspRepealField))(self.__OnRtnRepealFromFutureToBankByBank)
        self.h.tOnRtnRepealFromFutureToBankByBank(self.pSpi, self.FP_OnRtnRepealFromFutureToBankByBank)
        # 期货发起银行资金转期货通知
        self.h.tOnRtnFromBankToFutureByFuture.argtypes = [c_void_p, c_void_p]
        self.h.tOnRtnFromBankToFutureByFuture.restype = None
        self.FP_OnRtnFromBankToFutureByFuture = CFUNCTYPE(None, POINTER(CThostFtdcRspTransferField))(self.__OnRtnFromBankToFutureByFuture)
        self.h.tOnRtnFromBankToFutureByFuture(self.pSpi, self.FP_OnRtnFromBankToFutureByFuture)
        # 期货发起期货资金转银行通知
        self.h.tOnRtnFromFutureToBankByFuture.argtypes = [c_void_p, c_void_p]
        self.h.tOnRtnFromFutureToBankByFuture.restype = None
        self.FP_OnRtnFromFutureToBankByFuture = CFUNCTYPE(None, POINTER(CThostFtdcRspTransferField))(self.__OnRtnFromFutureToBankByFuture)
        self.h.tOnRtnFromFutureToBankByFuture(self.pSpi, self.FP_OnRtnFromFutureToBankByFuture)
        # 系统运行时期货端手工发起冲正银行转期货请求，银行处理完毕后报盘发回的通知
        self.h.tOnRtnRepealFromBankToFutureByFutureManual.argtypes = [c_void_p, c_void_p]
        self.h.tOnRtnRepealFromBankToFutureByFutureManual.restype = None
        self.FP_OnRtnRepealFromBankToFutureByFutureManual = CFUNCTYPE(None, POINTER(CThostFtdcRspRepealField))(self.__OnRtnRepealFromBankToFutureByFutureManual)
        self.h.tOnRtnRepealFromBankToFutureByFutureManual(self.pSpi, self.FP_OnRtnRepealFromBankToFutureByFutureManual)
        # 系统运行时期货端手工发起冲正期货转银行请求，银行处理完毕后报盘发回的通知
        self.h.tOnRtnRepealFromFutureToBankByFutureManual.argtypes = [c_void_p, c_void_p]
        self.h.tOnRtnRepealFromFutureToBankByFutureManual.restype = None
        self.FP_OnRtnRepealFromFutureToBankByFutureManual = CFUNCTYPE(None, POINTER(CThostFtdcRspRepealField))(self.__OnRtnRepealFromFutureToBankByFutureManual)
        self.h.tOnRtnRepealFromFutureToBankByFutureManual(self.pSpi, self.FP_OnRtnRepealFromFutureToBankByFutureManual)
        # 期货发起查询银行余额通知
        self.h.tOnRtnQueryBankBalanceByFuture.argtypes = [c_void_p, c_void_p]
        self.h.tOnRtnQueryBankBalanceByFuture.restype = None
        self.FP_OnRtnQueryBankBalanceByFuture = CFUNCTYPE(None, POINTER(CThostFtdcNotifyQueryAccountField))(self.__OnRtnQueryBankBalanceByFuture)
        self.h.tOnRtnQueryBankBalanceByFuture(self.pSpi, self.FP_OnRtnQueryBankBalanceByFuture)
        # 期货发起银行资金转期货错误回报
        self.h.tOnErrRtnBankToFutureByFuture.argtypes = [c_void_p, c_void_p]
        self.h.tOnErrRtnBankToFutureByFuture.restype = None
        self.FP_OnErrRtnBankToFutureByFuture = CFUNCTYPE(None, POINTER(CThostFtdcReqTransferField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnBankToFutureByFuture)
        self.h.tOnErrRtnBankToFutureByFuture(self.pSpi, self.FP_OnErrRtnBankToFutureByFuture)
        # 期货发起期货资金转银行错误回报
        self.h.tOnErrRtnFutureToBankByFuture.argtypes = [c_void_p, c_void_p]
        self.h.tOnErrRtnFutureToBankByFuture.restype = None
        self.FP_OnErrRtnFutureToBankByFuture = CFUNCTYPE(None, POINTER(CThostFtdcReqTransferField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnFutureToBankByFuture)
        self.h.tOnErrRtnFutureToBankByFuture(self.pSpi, self.FP_OnErrRtnFutureToBankByFuture)
        # 系统运行时期货端手工发起冲正银行转期货错误回报
        self.h.tOnErrRtnRepealBankToFutureByFutureManual.argtypes = [c_void_p, c_void_p]
        self.h.tOnErrRtnRepealBankToFutureByFutureManual.restype = None
        self.FP_OnErrRtnRepealBankToFutureByFutureManual = CFUNCTYPE(None, POINTER(CThostFtdcReqRepealField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnRepealBankToFutureByFutureManual)
        self.h.tOnErrRtnRepealBankToFutureByFutureManual(self.pSpi, self.FP_OnErrRtnRepealBankToFutureByFutureManual)
        # 系统运行时期货端手工发起冲正期货转银行错误回报
        self.h.tOnErrRtnRepealFutureToBankByFutureManual.argtypes = [c_void_p, c_void_p]
        self.h.tOnErrRtnRepealFutureToBankByFutureManual.restype = None
        self.FP_OnErrRtnRepealFutureToBankByFutureManual = CFUNCTYPE(None, POINTER(CThostFtdcReqRepealField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnRepealFutureToBankByFutureManual)
        self.h.tOnErrRtnRepealFutureToBankByFutureManual(self.pSpi, self.FP_OnErrRtnRepealFutureToBankByFutureManual)
        # 期货发起查询银行余额错误回报
        self.h.tOnErrRtnQueryBankBalanceByFuture.argtypes = [c_void_p, c_void_p]
        self.h.tOnErrRtnQueryBankBalanceByFuture.restype = None
        self.FP_OnErrRtnQueryBankBalanceByFuture = CFUNCTYPE(None, POINTER(CThostFtdcReqQueryAccountField), POINTER(CThostFtdcRspInfoField))(self.__OnErrRtnQueryBankBalanceByFuture)
        self.h.tOnErrRtnQueryBankBalanceByFuture(self.pSpi, self.FP_OnErrRtnQueryBankBalanceByFuture)
        # 期货发起冲正银行转期货请求，银行处理完毕后报盘发回的通知
        self.h.tOnRtnRepealFromBankToFutureByFuture.argtypes = [c_void_p, c_void_p]
        self.h.tOnRtnRepealFromBankToFutureByFuture.restype = None
        self.FP_OnRtnRepealFromBankToFutureByFuture = CFUNCTYPE(None, POINTER(CThostFtdcRspRepealField))(self.__OnRtnRepealFromBankToFutureByFuture)
        self.h.tOnRtnRepealFromBankToFutureByFuture(self.pSpi, self.FP_OnRtnRepealFromBankToFutureByFuture)
        # 期货发起冲正期货转银行请求，银行处理完毕后报盘发回的通知
        self.h.tOnRtnRepealFromFutureToBankByFuture.argtypes = [c_void_p, c_void_p]
        self.h.tOnRtnRepealFromFutureToBankByFuture.restype = None
        self.FP_OnRtnRepealFromFutureToBankByFuture = CFUNCTYPE(None, POINTER(CThostFtdcRspRepealField))(self.__OnRtnRepealFromFutureToBankByFuture)
        self.h.tOnRtnRepealFromFutureToBankByFuture(self.pSpi, self.FP_OnRtnRepealFromFutureToBankByFuture)
        # 期货发起银行资金转期货应答
        self.h.tOnRspFromBankToFutureByFuture.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspFromBankToFutureByFuture.restype = None
        self.FP_OnRspFromBankToFutureByFuture = CFUNCTYPE(None, POINTER(CThostFtdcReqTransferField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspFromBankToFutureByFuture)
        self.h.tOnRspFromBankToFutureByFuture(self.pSpi, self.FP_OnRspFromBankToFutureByFuture)
        # 期货发起期货资金转银行应答
        self.h.tOnRspFromFutureToBankByFuture.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspFromFutureToBankByFuture.restype = None
        self.FP_OnRspFromFutureToBankByFuture = CFUNCTYPE(None, POINTER(CThostFtdcReqTransferField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspFromFutureToBankByFuture)
        self.h.tOnRspFromFutureToBankByFuture(self.pSpi, self.FP_OnRspFromFutureToBankByFuture)
        # 期货发起查询银行余额应答
        self.h.tOnRspQueryBankAccountMoneyByFuture.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQueryBankAccountMoneyByFuture.restype = None
        self.FP_OnRspQueryBankAccountMoneyByFuture = CFUNCTYPE(None, POINTER(CThostFtdcReqQueryAccountField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQueryBankAccountMoneyByFuture)
        self.h.tOnRspQueryBankAccountMoneyByFuture(self.pSpi, self.FP_OnRspQueryBankAccountMoneyByFuture)
        # 银行发起银期开户通知
        self.h.tOnRtnOpenAccountByBank.argtypes = [c_void_p, c_void_p]
        self.h.tOnRtnOpenAccountByBank.restype = None
        self.FP_OnRtnOpenAccountByBank = CFUNCTYPE(None, POINTER(CThostFtdcOpenAccountField))(self.__OnRtnOpenAccountByBank)
        self.h.tOnRtnOpenAccountByBank(self.pSpi, self.FP_OnRtnOpenAccountByBank)
        # 银行发起银期销户通知
        self.h.tOnRtnCancelAccountByBank.argtypes = [c_void_p, c_void_p]
        self.h.tOnRtnCancelAccountByBank.restype = None
        self.FP_OnRtnCancelAccountByBank = CFUNCTYPE(None, POINTER(CThostFtdcCancelAccountField))(self.__OnRtnCancelAccountByBank)
        self.h.tOnRtnCancelAccountByBank(self.pSpi, self.FP_OnRtnCancelAccountByBank)
        # 银行发起变更银行账号通知
        self.h.tOnRtnChangeAccountByBank.argtypes = [c_void_p, c_void_p]
        self.h.tOnRtnChangeAccountByBank.restype = None
        self.FP_OnRtnChangeAccountByBank = CFUNCTYPE(None, POINTER(CThostFtdcChangeAccountField))(self.__OnRtnChangeAccountByBank)
        self.h.tOnRtnChangeAccountByBank(self.pSpi, self.FP_OnRtnChangeAccountByBank)
        # 请求查询分类合约响应
        self.h.tOnRspQryClassifiedInstrument.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryClassifiedInstrument.restype = None
        self.FP_OnRspQryClassifiedInstrument = CFUNCTYPE(None, POINTER(CThostFtdcInstrumentField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryClassifiedInstrument)
        self.h.tOnRspQryClassifiedInstrument(self.pSpi, self.FP_OnRspQryClassifiedInstrument)
        # 请求组合优惠比例响应
        self.h.tOnRspQryCombPromotionParam.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryCombPromotionParam.restype = None
        self.FP_OnRspQryCombPromotionParam = CFUNCTYPE(None, POINTER(CThostFtdcCombPromotionParamField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryCombPromotionParam)
        self.h.tOnRspQryCombPromotionParam(self.pSpi, self.FP_OnRspQryCombPromotionParam)
        # 投资者风险结算持仓查询响应
        self.h.tOnRspQryRiskSettleInvstPosition.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryRiskSettleInvstPosition.restype = None
        self.FP_OnRspQryRiskSettleInvstPosition = CFUNCTYPE(None, POINTER(CThostFtdcRiskSettleInvstPositionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryRiskSettleInvstPosition)
        self.h.tOnRspQryRiskSettleInvstPosition(self.pSpi, self.FP_OnRspQryRiskSettleInvstPosition)
        # 风险结算产品查询响应
        self.h.tOnRspQryRiskSettleProductStatus.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryRiskSettleProductStatus.restype = None
        self.FP_OnRspQryRiskSettleProductStatus = CFUNCTYPE(None, POINTER(CThostFtdcRiskSettleProductStatusField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryRiskSettleProductStatus)
        self.h.tOnRspQryRiskSettleProductStatus(self.pSpi, self.FP_OnRspQryRiskSettleProductStatus)
        # SPBM期货合约参数查询响应
        self.h.tOnRspQrySPBMFutureParameter.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQrySPBMFutureParameter.restype = None
        self.FP_OnRspQrySPBMFutureParameter = CFUNCTYPE(None, POINTER(CThostFtdcSPBMFutureParameterField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQrySPBMFutureParameter)
        self.h.tOnRspQrySPBMFutureParameter(self.pSpi, self.FP_OnRspQrySPBMFutureParameter)
        # SPBM期权合约参数查询响应
        self.h.tOnRspQrySPBMOptionParameter.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQrySPBMOptionParameter.restype = None
        self.FP_OnRspQrySPBMOptionParameter = CFUNCTYPE(None, POINTER(CThostFtdcSPBMOptionParameterField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQrySPBMOptionParameter)
        self.h.tOnRspQrySPBMOptionParameter(self.pSpi, self.FP_OnRspQrySPBMOptionParameter)
        # SPBM品种内对锁仓折扣参数查询响应
        self.h.tOnRspQrySPBMIntraParameter.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQrySPBMIntraParameter.restype = None
        self.FP_OnRspQrySPBMIntraParameter = CFUNCTYPE(None, POINTER(CThostFtdcSPBMIntraParameterField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQrySPBMIntraParameter)
        self.h.tOnRspQrySPBMIntraParameter(self.pSpi, self.FP_OnRspQrySPBMIntraParameter)
        # SPBM跨品种抵扣参数查询响应
        self.h.tOnRspQrySPBMInterParameter.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQrySPBMInterParameter.restype = None
        self.FP_OnRspQrySPBMInterParameter = CFUNCTYPE(None, POINTER(CThostFtdcSPBMInterParameterField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQrySPBMInterParameter)
        self.h.tOnRspQrySPBMInterParameter(self.pSpi, self.FP_OnRspQrySPBMInterParameter)
        # SPBM组合保证金套餐查询响应
        self.h.tOnRspQrySPBMPortfDefinition.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQrySPBMPortfDefinition.restype = None
        self.FP_OnRspQrySPBMPortfDefinition = CFUNCTYPE(None, POINTER(CThostFtdcSPBMPortfDefinitionField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQrySPBMPortfDefinition)
        self.h.tOnRspQrySPBMPortfDefinition(self.pSpi, self.FP_OnRspQrySPBMPortfDefinition)
        # 投资者SPBM套餐选择查询响应
        self.h.tOnRspQrySPBMInvestorPortfDef.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQrySPBMInvestorPortfDef.restype = None
        self.FP_OnRspQrySPBMInvestorPortfDef = CFUNCTYPE(None, POINTER(CThostFtdcSPBMInvestorPortfDefField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQrySPBMInvestorPortfDef)
        self.h.tOnRspQrySPBMInvestorPortfDef(self.pSpi, self.FP_OnRspQrySPBMInvestorPortfDef)
        # 投资者新型组合保证金系数查询响应
        self.h.tOnRspQryInvestorPortfMarginRatio.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryInvestorPortfMarginRatio.restype = None
        self.FP_OnRspQryInvestorPortfMarginRatio = CFUNCTYPE(None, POINTER(CThostFtdcInvestorPortfMarginRatioField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInvestorPortfMarginRatio)
        self.h.tOnRspQryInvestorPortfMarginRatio(self.pSpi, self.FP_OnRspQryInvestorPortfMarginRatio)
        # 投资者产品SPBM明细查询响应
        self.h.tOnRspQryInvestorProdSPBMDetail.argtypes = [c_void_p, c_void_p]
        self.h.tOnRspQryInvestorProdSPBMDetail.restype = None
        self.FP_OnRspQryInvestorProdSPBMDetail = CFUNCTYPE(None, POINTER(CThostFtdcInvestorProdSPBMDetailField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInvestorProdSPBMDetail)
        self.h.tOnRspQryInvestorProdSPBMDetail(self.pSpi, self.FP_OnRspQryInvestorProdSPBMDetail)
        

    def GetApiVersion(self):
        v = str(self.h.tGetApiVersion(), encoding="utf-8")
        return str(v)

    def GetTradingDay(self):
        v = str(self.h.tGetTradingDay(self.api), encoding="utf-8")
        return str(v)

    def CTP_GetSystemInfo(self, pSystemInfo:TThostFtdcClientSystemInfoType, nLen:TThostFtdcSystemInfoLenType):
        res = self.h.dCTP_GetSystemInfo(pSystemInfo, nLen)
        return res

    def CTP_GetSystemInfoUnAesEncode(self, pSystemInfo:TThostFtdcClientSystemInfoType, nLen:TThostFtdcSystemInfoLenType):
        res = self.h.dCTP_GetSystemInfoUnAesEncode(pSystemInfo, nLen)
        return res

    def CTP_GetDataCollectApiVersion(self):
        v = str(self.h.dCTP_GetDataCollectApiVersion(), encoding="utf-8")
        return v
    #################### 请求函数 #######################
    
    def Release(self): 
        """ 创建TraderApi """
        self.h.tRelease(self.api)
    
    def Init(self): 
        """ 初始化 """
        self.h.tInit(self.api)
    
    def Join(self): 
        """ 等待接口线程结束运行 """ 
        return self.h.tJoin(self.api) 
    
    def RegisterFront(self, pszFrontAddress:str): 
        """ 注册前置机网络地址 """
        self.h.tRegisterFront(self.api, bytes(pszFrontAddress, encoding='ascii'))
    
    def RegisterNameServer(self, pszNsAddress:str): 
        """ @remark RegisterNameServer优先于RegisterFront """
        self.h.tRegisterNameServer(self.api, bytes(pszNsAddress, encoding='ascii'))
    
    def RegisterFensUserInfo(self,  pFensUserInfo:CThostFtdcFensUserInfoField): 
        """ 注册名字服务器用户信息 """
        self.h.tRegisterFensUserInfo(self.api, byref( pFensUserInfo))
    
    def RegisterSpi(self): 
        """ 注册回调接口 """
        self.h.tRegisterSpi(self.api, self.pSpi)
    
    def SubscribePrivateTopic(self, nResumeType:THOST_TE_RESUME_TYPE): 
        """ 订阅私有流。 """
        self.h.tSubscribePrivateTopic(self.api, nResumeType)
    
    def SubscribePublicTopic(self, nResumeType:THOST_TE_RESUME_TYPE): 
        """ 订阅公共流。 """
        self.h.tSubscribePublicTopic(self.api, nResumeType)
    
    def ReqAuthenticate(self, pReqAuthenticateField:CThostFtdcReqAuthenticateField, nRequestID:int): 
        """ 客户端认证请求 """ 
        return self.h.tReqAuthenticate(self.api, byref(pReqAuthenticateField), nRequestID) 
    
    def RegisterUserSystemInfo(self, pUserSystemInfo:CThostFtdcUserSystemInfoField): 
        """ 注册用户终端信息，用于中继服务器多连接模式 """ 
        return self.h.tRegisterUserSystemInfo(self.api, byref(pUserSystemInfo)) 
    
    def SubmitUserSystemInfo(self, pUserSystemInfo:CThostFtdcUserSystemInfoField): 
        """ 上报用户终端信息，用于中继服务器操作员登录模式 """ 
        return self.h.tSubmitUserSystemInfo(self.api, byref(pUserSystemInfo)) 
    
    def ReqUserLogin(self, pReqUserLoginField:CThostFtdcReqUserLoginField, nRequestID:int): 
        """ 用户登录请求 """ 
        systemInfo = TThostFtdcClientSystemInfoType()
        length = TThostFtdcSystemInfoLenType(273)
        self.CTP_GetSystemInfoUnAesEncode(systemInfo, length)
        systemInfo = systemInfo.value
        length = length.value
        return self.h.tReqUserLogin(self.api, byref(pReqUserLoginField), nRequestID, length, systemInfo) 
    
    def ReqUserLogout(self, pUserLogout:CThostFtdcUserLogoutField, nRequestID:int): 
        """ 登出请求 """ 
        return self.h.tReqUserLogout(self.api, byref(pUserLogout), nRequestID) 
    
    def ReqUserPasswordUpdate(self, pUserPasswordUpdate:CThostFtdcUserPasswordUpdateField, nRequestID:int): 
        """ 用户口令更新请求 """ 
        return self.h.tReqUserPasswordUpdate(self.api, byref(pUserPasswordUpdate), nRequestID) 
    
    def ReqTradingAccountPasswordUpdate(self, pTradingAccountPasswordUpdate:CThostFtdcTradingAccountPasswordUpdateField, nRequestID:int): 
        """ 资金账户口令更新请求 """ 
        return self.h.tReqTradingAccountPasswordUpdate(self.api, byref(pTradingAccountPasswordUpdate), nRequestID) 
    
    def ReqUserAuthMethod(self, pReqUserAuthMethod:CThostFtdcReqUserAuthMethodField, nRequestID:int): 
        """ 查询用户当前支持的认证模式 """ 
        return self.h.tReqUserAuthMethod(self.api, byref(pReqUserAuthMethod), nRequestID) 
    
    def ReqGenUserCaptcha(self, pReqGenUserCaptcha:CThostFtdcReqGenUserCaptchaField, nRequestID:int): 
        """ 用户发出获取图形验证码请求 """ 
        return self.h.tReqGenUserCaptcha(self.api, byref(pReqGenUserCaptcha), nRequestID) 
    
    def ReqGenUserText(self, pReqGenUserText:CThostFtdcReqGenUserTextField, nRequestID:int): 
        """ 用户发出获取短信验证码请求 """ 
        return self.h.tReqGenUserText(self.api, byref(pReqGenUserText), nRequestID) 
    
    def ReqUserLoginWithCaptcha(self, pReqUserLoginWithCaptcha:CThostFtdcReqUserLoginWithCaptchaField, nRequestID:int): 
        """ 用户发出带有图片验证码的登陆请求 """ 
        return self.h.tReqUserLoginWithCaptcha(self.api, byref(pReqUserLoginWithCaptcha), nRequestID) 
    
    def ReqUserLoginWithText(self, pReqUserLoginWithText:CThostFtdcReqUserLoginWithTextField, nRequestID:int): 
        """ 用户发出带有短信验证码的登陆请求 """ 
        return self.h.tReqUserLoginWithText(self.api, byref(pReqUserLoginWithText), nRequestID) 
    
    def ReqUserLoginWithOTP(self, pReqUserLoginWithOTP:CThostFtdcReqUserLoginWithOTPField, nRequestID:int): 
        """ 用户发出带有动态口令的登陆请求 """ 
        return self.h.tReqUserLoginWithOTP(self.api, byref(pReqUserLoginWithOTP), nRequestID) 
    
    def ReqOrderInsert(self, pInputOrder:CThostFtdcInputOrderField, nRequestID:int): 
        """ 报单录入请求 """ 
        return self.h.tReqOrderInsert(self.api, byref(pInputOrder), nRequestID) 
    
    def ReqParkedOrderInsert(self, pParkedOrder:CThostFtdcParkedOrderField, nRequestID:int): 
        """ 预埋单录入请求 """ 
        return self.h.tReqParkedOrderInsert(self.api, byref(pParkedOrder), nRequestID) 
    
    def ReqParkedOrderAction(self, pParkedOrderAction:CThostFtdcParkedOrderActionField, nRequestID:int): 
        """ 预埋撤单录入请求 """ 
        return self.h.tReqParkedOrderAction(self.api, byref(pParkedOrderAction), nRequestID) 
    
    def ReqOrderAction(self, pInputOrderAction:CThostFtdcInputOrderActionField, nRequestID:int): 
        """ 报单操作请求 """ 
        return self.h.tReqOrderAction(self.api, byref(pInputOrderAction), nRequestID) 
    
    def ReqQryMaxOrderVolume(self, pQryMaxOrderVolume:CThostFtdcQryMaxOrderVolumeField, nRequestID:int): 
        """ 查询最大报单数量请求 """ 
        return self.h.tReqQryMaxOrderVolume(self.api, byref(pQryMaxOrderVolume), nRequestID) 
    
    def ReqSettlementInfoConfirm(self, pSettlementInfoConfirm:CThostFtdcSettlementInfoConfirmField, nRequestID:int): 
        """ 投资者结算结果确认 """ 
        return self.h.tReqSettlementInfoConfirm(self.api, byref(pSettlementInfoConfirm), nRequestID) 
    
    def ReqRemoveParkedOrder(self, pRemoveParkedOrder:CThostFtdcRemoveParkedOrderField, nRequestID:int): 
        """ 请求删除预埋单 """ 
        return self.h.tReqRemoveParkedOrder(self.api, byref(pRemoveParkedOrder), nRequestID) 
    
    def ReqRemoveParkedOrderAction(self, pRemoveParkedOrderAction:CThostFtdcRemoveParkedOrderActionField, nRequestID:int): 
        """ 请求删除预埋撤单 """ 
        return self.h.tReqRemoveParkedOrderAction(self.api, byref(pRemoveParkedOrderAction), nRequestID) 
    
    def ReqExecOrderInsert(self, pInputExecOrder:CThostFtdcInputExecOrderField, nRequestID:int): 
        """ 执行宣告录入请求 """ 
        return self.h.tReqExecOrderInsert(self.api, byref(pInputExecOrder), nRequestID) 
    
    def ReqExecOrderAction(self, pInputExecOrderAction:CThostFtdcInputExecOrderActionField, nRequestID:int): 
        """ 执行宣告操作请求 """ 
        return self.h.tReqExecOrderAction(self.api, byref(pInputExecOrderAction), nRequestID) 
    
    def ReqForQuoteInsert(self, pInputForQuote:CThostFtdcInputForQuoteField, nRequestID:int): 
        """ 询价录入请求 """ 
        return self.h.tReqForQuoteInsert(self.api, byref(pInputForQuote), nRequestID) 
    
    def ReqQuoteInsert(self, pInputQuote:CThostFtdcInputQuoteField, nRequestID:int): 
        """ 报价录入请求 """ 
        return self.h.tReqQuoteInsert(self.api, byref(pInputQuote), nRequestID) 
    
    def ReqQuoteAction(self, pInputQuoteAction:CThostFtdcInputQuoteActionField, nRequestID:int): 
        """ 报价操作请求 """ 
        return self.h.tReqQuoteAction(self.api, byref(pInputQuoteAction), nRequestID) 
    
    def ReqBatchOrderAction(self, pInputBatchOrderAction:CThostFtdcInputBatchOrderActionField, nRequestID:int): 
        """ 批量报单操作请求 """ 
        return self.h.tReqBatchOrderAction(self.api, byref(pInputBatchOrderAction), nRequestID) 
    
    def ReqOptionSelfCloseInsert(self, pInputOptionSelfClose:CThostFtdcInputOptionSelfCloseField, nRequestID:int): 
        """ 期权自对冲录入请求 """ 
        return self.h.tReqOptionSelfCloseInsert(self.api, byref(pInputOptionSelfClose), nRequestID) 
    
    def ReqOptionSelfCloseAction(self, pInputOptionSelfCloseAction:CThostFtdcInputOptionSelfCloseActionField, nRequestID:int): 
        """ 期权自对冲操作请求 """ 
        return self.h.tReqOptionSelfCloseAction(self.api, byref(pInputOptionSelfCloseAction), nRequestID) 
    
    def ReqCombActionInsert(self, pInputCombAction:CThostFtdcInputCombActionField, nRequestID:int): 
        """ 申请组合录入请求 """ 
        return self.h.tReqCombActionInsert(self.api, byref(pInputCombAction), nRequestID) 
    
    def ReqQryOrder(self, pQryOrder:CThostFtdcQryOrderField, nRequestID:int): 
        """ 请求查询报单 """ 
        return self.h.tReqQryOrder(self.api, byref(pQryOrder), nRequestID) 
    
    def ReqQryTrade(self, pQryTrade:CThostFtdcQryTradeField, nRequestID:int): 
        """ 请求查询成交 """ 
        return self.h.tReqQryTrade(self.api, byref(pQryTrade), nRequestID) 
    
    def ReqQryInvestorPosition(self, pQryInvestorPosition:CThostFtdcQryInvestorPositionField, nRequestID:int): 
        """ 请求查询投资者持仓 """ 
        return self.h.tReqQryInvestorPosition(self.api, byref(pQryInvestorPosition), nRequestID) 
    
    def ReqQryTradingAccount(self, pQryTradingAccount:CThostFtdcQryTradingAccountField, nRequestID:int): 
        """ 请求查询资金账户 """ 
        return self.h.tReqQryTradingAccount(self.api, byref(pQryTradingAccount), nRequestID) 
    
    def ReqQryInvestor(self, pQryInvestor:CThostFtdcQryInvestorField, nRequestID:int): 
        """ 请求查询投资者 """ 
        return self.h.tReqQryInvestor(self.api, byref(pQryInvestor), nRequestID) 
    
    def ReqQryTradingCode(self, pQryTradingCode:CThostFtdcQryTradingCodeField, nRequestID:int): 
        """ 请求查询交易编码 """ 
        return self.h.tReqQryTradingCode(self.api, byref(pQryTradingCode), nRequestID) 
    
    def ReqQryInstrumentMarginRate(self, pQryInstrumentMarginRate:CThostFtdcQryInstrumentMarginRateField, nRequestID:int): 
        """ 请求查询合约保证金率 """ 
        return self.h.tReqQryInstrumentMarginRate(self.api, byref(pQryInstrumentMarginRate), nRequestID) 
    
    def ReqQryInstrumentCommissionRate(self, pQryInstrumentCommissionRate:CThostFtdcQryInstrumentCommissionRateField, nRequestID:int): 
        """ 请求查询合约手续费率 """ 
        return self.h.tReqQryInstrumentCommissionRate(self.api, byref(pQryInstrumentCommissionRate), nRequestID) 
    
    def ReqQryExchange(self, pQryExchange:CThostFtdcQryExchangeField, nRequestID:int): 
        """ 请求查询交易所 """ 
        return self.h.tReqQryExchange(self.api, byref(pQryExchange), nRequestID) 
    
    def ReqQryProduct(self, pQryProduct:CThostFtdcQryProductField, nRequestID:int): 
        """ 请求查询产品 """ 
        return self.h.tReqQryProduct(self.api, byref(pQryProduct), nRequestID) 
    
    def ReqQryInstrument(self, pQryInstrument:CThostFtdcQryInstrumentField, nRequestID:int): 
        """ 请求查询合约 """ 
        return self.h.tReqQryInstrument(self.api, byref(pQryInstrument), nRequestID) 
    
    def ReqQryDepthMarketData(self, pQryDepthMarketData:CThostFtdcQryDepthMarketDataField, nRequestID:int): 
        """ 请求查询行情 """ 
        return self.h.tReqQryDepthMarketData(self.api, byref(pQryDepthMarketData), nRequestID) 
    
    def ReqQryTraderOffer(self, pQryTraderOffer:CThostFtdcQryTraderOfferField, nRequestID:int): 
        """ 请求查询交易员报盘机 """ 
        return self.h.tReqQryTraderOffer(self.api, byref(pQryTraderOffer), nRequestID) 
    
    def ReqQrySettlementInfo(self, pQrySettlementInfo:CThostFtdcQrySettlementInfoField, nRequestID:int): 
        """ 请求查询投资者结算结果 """ 
        return self.h.tReqQrySettlementInfo(self.api, byref(pQrySettlementInfo), nRequestID) 
    
    def ReqQryTransferBank(self, pQryTransferBank:CThostFtdcQryTransferBankField, nRequestID:int): 
        """ 请求查询转帐银行 """ 
        return self.h.tReqQryTransferBank(self.api, byref(pQryTransferBank), nRequestID) 
    
    def ReqQryInvestorPositionDetail(self, pQryInvestorPositionDetail:CThostFtdcQryInvestorPositionDetailField, nRequestID:int): 
        """ 请求查询投资者持仓明细 """ 
        return self.h.tReqQryInvestorPositionDetail(self.api, byref(pQryInvestorPositionDetail), nRequestID) 
    
    def ReqQryNotice(self, pQryNotice:CThostFtdcQryNoticeField, nRequestID:int): 
        """ 请求查询客户通知 """ 
        return self.h.tReqQryNotice(self.api, byref(pQryNotice), nRequestID) 
    
    def ReqQrySettlementInfoConfirm(self, pQrySettlementInfoConfirm:CThostFtdcQrySettlementInfoConfirmField, nRequestID:int): 
        """ 请求查询结算信息确认 """ 
        return self.h.tReqQrySettlementInfoConfirm(self.api, byref(pQrySettlementInfoConfirm), nRequestID) 
    
    def ReqQryInvestorPositionCombineDetail(self, pQryInvestorPositionCombineDetail:CThostFtdcQryInvestorPositionCombineDetailField, nRequestID:int): 
        """ 请求查询投资者持仓明细 """ 
        return self.h.tReqQryInvestorPositionCombineDetail(self.api, byref(pQryInvestorPositionCombineDetail), nRequestID) 
    
    def ReqQryCFMMCTradingAccountKey(self, pQryCFMMCTradingAccountKey:CThostFtdcQryCFMMCTradingAccountKeyField, nRequestID:int): 
        """ 请求查询保证金监管系统经纪公司资金账户密钥 """ 
        return self.h.tReqQryCFMMCTradingAccountKey(self.api, byref(pQryCFMMCTradingAccountKey), nRequestID) 
    
    def ReqQryEWarrantOffset(self, pQryEWarrantOffset:CThostFtdcQryEWarrantOffsetField, nRequestID:int): 
        """ 请求查询仓单折抵信息 """ 
        return self.h.tReqQryEWarrantOffset(self.api, byref(pQryEWarrantOffset), nRequestID) 
    
    def ReqQryInvestorProductGroupMargin(self, pQryInvestorProductGroupMargin:CThostFtdcQryInvestorProductGroupMarginField, nRequestID:int): 
        """ 请求查询投资者品种/跨品种保证金 """ 
        return self.h.tReqQryInvestorProductGroupMargin(self.api, byref(pQryInvestorProductGroupMargin), nRequestID) 
    
    def ReqQryExchangeMarginRate(self, pQryExchangeMarginRate:CThostFtdcQryExchangeMarginRateField, nRequestID:int): 
        """ 请求查询交易所保证金率 """ 
        return self.h.tReqQryExchangeMarginRate(self.api, byref(pQryExchangeMarginRate), nRequestID) 
    
    def ReqQryExchangeMarginRateAdjust(self, pQryExchangeMarginRateAdjust:CThostFtdcQryExchangeMarginRateAdjustField, nRequestID:int): 
        """ 请求查询交易所调整保证金率 """ 
        return self.h.tReqQryExchangeMarginRateAdjust(self.api, byref(pQryExchangeMarginRateAdjust), nRequestID) 
    
    def ReqQryExchangeRate(self, pQryExchangeRate:CThostFtdcQryExchangeRateField, nRequestID:int): 
        """ 请求查询汇率 """ 
        return self.h.tReqQryExchangeRate(self.api, byref(pQryExchangeRate), nRequestID) 
    
    def ReqQrySecAgentACIDMap(self, pQrySecAgentACIDMap:CThostFtdcQrySecAgentACIDMapField, nRequestID:int): 
        """ 请求查询二级代理操作员银期权限 """ 
        return self.h.tReqQrySecAgentACIDMap(self.api, byref(pQrySecAgentACIDMap), nRequestID) 
    
    def ReqQryProductExchRate(self, pQryProductExchRate:CThostFtdcQryProductExchRateField, nRequestID:int): 
        """ 请求查询产品报价汇率 """ 
        return self.h.tReqQryProductExchRate(self.api, byref(pQryProductExchRate), nRequestID) 
    
    def ReqQryProductGroup(self, pQryProductGroup:CThostFtdcQryProductGroupField, nRequestID:int): 
        """ 请求查询产品组 """ 
        return self.h.tReqQryProductGroup(self.api, byref(pQryProductGroup), nRequestID) 
    
    def ReqQryMMInstrumentCommissionRate(self, pQryMMInstrumentCommissionRate:CThostFtdcQryMMInstrumentCommissionRateField, nRequestID:int): 
        """ 请求查询做市商合约手续费率 """ 
        return self.h.tReqQryMMInstrumentCommissionRate(self.api, byref(pQryMMInstrumentCommissionRate), nRequestID) 
    
    def ReqQryMMOptionInstrCommRate(self, pQryMMOptionInstrCommRate:CThostFtdcQryMMOptionInstrCommRateField, nRequestID:int): 
        """ 请求查询做市商期权合约手续费 """ 
        return self.h.tReqQryMMOptionInstrCommRate(self.api, byref(pQryMMOptionInstrCommRate), nRequestID) 
    
    def ReqQryInstrumentOrderCommRate(self, pQryInstrumentOrderCommRate:CThostFtdcQryInstrumentOrderCommRateField, nRequestID:int): 
        """ 请求查询报单手续费 """ 
        return self.h.tReqQryInstrumentOrderCommRate(self.api, byref(pQryInstrumentOrderCommRate), nRequestID) 
    
    def ReqQrySecAgentTradingAccount(self, pQryTradingAccount:CThostFtdcQryTradingAccountField, nRequestID:int): 
        """ 请求查询资金账户 """ 
        return self.h.tReqQrySecAgentTradingAccount(self.api, byref(pQryTradingAccount), nRequestID) 
    
    def ReqQrySecAgentCheckMode(self, pQrySecAgentCheckMode:CThostFtdcQrySecAgentCheckModeField, nRequestID:int): 
        """ 请求查询二级代理商资金校验模式 """ 
        return self.h.tReqQrySecAgentCheckMode(self.api, byref(pQrySecAgentCheckMode), nRequestID) 
    
    def ReqQrySecAgentTradeInfo(self, pQrySecAgentTradeInfo:CThostFtdcQrySecAgentTradeInfoField, nRequestID:int): 
        """ 请求查询二级代理商信息 """ 
        return self.h.tReqQrySecAgentTradeInfo(self.api, byref(pQrySecAgentTradeInfo), nRequestID) 
    
    def ReqQryOptionInstrTradeCost(self, pQryOptionInstrTradeCost:CThostFtdcQryOptionInstrTradeCostField, nRequestID:int): 
        """ 请求查询期权交易成本 """ 
        return self.h.tReqQryOptionInstrTradeCost(self.api, byref(pQryOptionInstrTradeCost), nRequestID) 
    
    def ReqQryOptionInstrCommRate(self, pQryOptionInstrCommRate:CThostFtdcQryOptionInstrCommRateField, nRequestID:int): 
        """ 请求查询期权合约手续费 """ 
        return self.h.tReqQryOptionInstrCommRate(self.api, byref(pQryOptionInstrCommRate), nRequestID) 
    
    def ReqQryExecOrder(self, pQryExecOrder:CThostFtdcQryExecOrderField, nRequestID:int): 
        """ 请求查询执行宣告 """ 
        return self.h.tReqQryExecOrder(self.api, byref(pQryExecOrder), nRequestID) 
    
    def ReqQryForQuote(self, pQryForQuote:CThostFtdcQryForQuoteField, nRequestID:int): 
        """ 请求查询询价 """ 
        return self.h.tReqQryForQuote(self.api, byref(pQryForQuote), nRequestID) 
    
    def ReqQryQuote(self, pQryQuote:CThostFtdcQryQuoteField, nRequestID:int): 
        """ 请求查询报价 """ 
        return self.h.tReqQryQuote(self.api, byref(pQryQuote), nRequestID) 
    
    def ReqQryOptionSelfClose(self, pQryOptionSelfClose:CThostFtdcQryOptionSelfCloseField, nRequestID:int): 
        """ 请求查询期权自对冲 """ 
        return self.h.tReqQryOptionSelfClose(self.api, byref(pQryOptionSelfClose), nRequestID) 
    
    def ReqQryInvestUnit(self, pQryInvestUnit:CThostFtdcQryInvestUnitField, nRequestID:int): 
        """ 请求查询投资单元 """ 
        return self.h.tReqQryInvestUnit(self.api, byref(pQryInvestUnit), nRequestID) 
    
    def ReqQryCombInstrumentGuard(self, pQryCombInstrumentGuard:CThostFtdcQryCombInstrumentGuardField, nRequestID:int): 
        """ 请求查询组合合约安全系数 """ 
        return self.h.tReqQryCombInstrumentGuard(self.api, byref(pQryCombInstrumentGuard), nRequestID) 
    
    def ReqQryCombAction(self, pQryCombAction:CThostFtdcQryCombActionField, nRequestID:int): 
        """ 请求查询申请组合 """ 
        return self.h.tReqQryCombAction(self.api, byref(pQryCombAction), nRequestID) 
    
    def ReqQryTransferSerial(self, pQryTransferSerial:CThostFtdcQryTransferSerialField, nRequestID:int): 
        """ 请求查询转帐流水 """ 
        return self.h.tReqQryTransferSerial(self.api, byref(pQryTransferSerial), nRequestID) 
    
    def ReqQryAccountregister(self, pQryAccountregister:CThostFtdcQryAccountregisterField, nRequestID:int): 
        """ 请求查询银期签约关系 """ 
        return self.h.tReqQryAccountregister(self.api, byref(pQryAccountregister), nRequestID) 
    
    def ReqQryContractBank(self, pQryContractBank:CThostFtdcQryContractBankField, nRequestID:int): 
        """ 请求查询签约银行 """ 
        return self.h.tReqQryContractBank(self.api, byref(pQryContractBank), nRequestID) 
    
    def ReqQryParkedOrder(self, pQryParkedOrder:CThostFtdcQryParkedOrderField, nRequestID:int): 
        """ 请求查询预埋单 """ 
        return self.h.tReqQryParkedOrder(self.api, byref(pQryParkedOrder), nRequestID) 
    
    def ReqQryParkedOrderAction(self, pQryParkedOrderAction:CThostFtdcQryParkedOrderActionField, nRequestID:int): 
        """ 请求查询预埋撤单 """ 
        return self.h.tReqQryParkedOrderAction(self.api, byref(pQryParkedOrderAction), nRequestID) 
    
    def ReqQryTradingNotice(self, pQryTradingNotice:CThostFtdcQryTradingNoticeField, nRequestID:int): 
        """ 请求查询交易通知 """ 
        return self.h.tReqQryTradingNotice(self.api, byref(pQryTradingNotice), nRequestID) 
    
    def ReqQryBrokerTradingParams(self, pQryBrokerTradingParams:CThostFtdcQryBrokerTradingParamsField, nRequestID:int): 
        """ 请求查询经纪公司交易参数 """ 
        return self.h.tReqQryBrokerTradingParams(self.api, byref(pQryBrokerTradingParams), nRequestID) 
    
    def ReqQryBrokerTradingAlgos(self, pQryBrokerTradingAlgos:CThostFtdcQryBrokerTradingAlgosField, nRequestID:int): 
        """ 请求查询经纪公司交易算法 """ 
        return self.h.tReqQryBrokerTradingAlgos(self.api, byref(pQryBrokerTradingAlgos), nRequestID) 
    
    def ReqQueryCFMMCTradingAccountToken(self, pQueryCFMMCTradingAccountToken:CThostFtdcQueryCFMMCTradingAccountTokenField, nRequestID:int): 
        """ 请求查询监控中心用户令牌 """ 
        return self.h.tReqQueryCFMMCTradingAccountToken(self.api, byref(pQueryCFMMCTradingAccountToken), nRequestID) 
    
    def ReqFromBankToFutureByFuture(self, pReqTransfer:CThostFtdcReqTransferField, nRequestID:int): 
        """ 期货发起银行资金转期货请求 """ 
        return self.h.tReqFromBankToFutureByFuture(self.api, byref(pReqTransfer), nRequestID) 
    
    def ReqFromFutureToBankByFuture(self, pReqTransfer:CThostFtdcReqTransferField, nRequestID:int): 
        """ 期货发起期货资金转银行请求 """ 
        return self.h.tReqFromFutureToBankByFuture(self.api, byref(pReqTransfer), nRequestID) 
    
    def ReqQueryBankAccountMoneyByFuture(self, pReqQueryAccount:CThostFtdcReqQueryAccountField, nRequestID:int): 
        """ 期货发起查询银行余额请求 """ 
        return self.h.tReqQueryBankAccountMoneyByFuture(self.api, byref(pReqQueryAccount), nRequestID) 
    
    def ReqQryClassifiedInstrument(self, pQryClassifiedInstrument:CThostFtdcQryClassifiedInstrumentField, nRequestID:int): 
        """ 请求查询分类合约 """ 
        return self.h.tReqQryClassifiedInstrument(self.api, byref(pQryClassifiedInstrument), nRequestID) 
    
    def ReqQryCombPromotionParam(self, pQryCombPromotionParam:CThostFtdcQryCombPromotionParamField, nRequestID:int): 
        """ 请求组合优惠比例 """ 
        return self.h.tReqQryCombPromotionParam(self.api, byref(pQryCombPromotionParam), nRequestID) 
    
    def ReqQryRiskSettleInvstPosition(self, pQryRiskSettleInvstPosition:CThostFtdcQryRiskSettleInvstPositionField, nRequestID:int): 
        """ 投资者风险结算持仓查询 """ 
        return self.h.tReqQryRiskSettleInvstPosition(self.api, byref(pQryRiskSettleInvstPosition), nRequestID) 
    
    def ReqQryRiskSettleProductStatus(self, pQryRiskSettleProductStatus:CThostFtdcQryRiskSettleProductStatusField, nRequestID:int): 
        """ 风险结算产品查询 """ 
        return self.h.tReqQryRiskSettleProductStatus(self.api, byref(pQryRiskSettleProductStatus), nRequestID) 
    
    def ReqQrySPBMFutureParameter(self, pQrySPBMFutureParameter:CThostFtdcQrySPBMFutureParameterField, nRequestID:int): 
        """ SPBM期货合约参数查询 """ 
        return self.h.tReqQrySPBMFutureParameter(self.api, byref(pQrySPBMFutureParameter), nRequestID) 
    
    def ReqQrySPBMOptionParameter(self, pQrySPBMOptionParameter:CThostFtdcQrySPBMOptionParameterField, nRequestID:int): 
        """ SPBM期权合约参数查询 """ 
        return self.h.tReqQrySPBMOptionParameter(self.api, byref(pQrySPBMOptionParameter), nRequestID) 
    
    def ReqQrySPBMIntraParameter(self, pQrySPBMIntraParameter:CThostFtdcQrySPBMIntraParameterField, nRequestID:int): 
        """ SPBM品种内对锁仓折扣参数查询 """ 
        return self.h.tReqQrySPBMIntraParameter(self.api, byref(pQrySPBMIntraParameter), nRequestID) 
    
    def ReqQrySPBMInterParameter(self, pQrySPBMInterParameter:CThostFtdcQrySPBMInterParameterField, nRequestID:int): 
        """ SPBM跨品种抵扣参数查询 """ 
        return self.h.tReqQrySPBMInterParameter(self.api, byref(pQrySPBMInterParameter), nRequestID) 
    
    def ReqQrySPBMPortfDefinition(self, pQrySPBMPortfDefinition:CThostFtdcQrySPBMPortfDefinitionField, nRequestID:int): 
        """ SPBM组合保证金套餐查询 """ 
        return self.h.tReqQrySPBMPortfDefinition(self.api, byref(pQrySPBMPortfDefinition), nRequestID) 
    
    def ReqQrySPBMInvestorPortfDef(self, pQrySPBMInvestorPortfDef:CThostFtdcQrySPBMInvestorPortfDefField, nRequestID:int): 
        """ 投资者SPBM套餐选择查询 """ 
        return self.h.tReqQrySPBMInvestorPortfDef(self.api, byref(pQrySPBMInvestorPortfDef), nRequestID) 
    
    def ReqQryInvestorPortfMarginRatio(self, pQryInvestorPortfMarginRatio:CThostFtdcQryInvestorPortfMarginRatioField, nRequestID:int): 
        """ 投资者新型组合保证金系数查询 """ 
        return self.h.tReqQryInvestorPortfMarginRatio(self.api, byref(pQryInvestorPortfMarginRatio), nRequestID) 
    
    def ReqQryInvestorProdSPBMDetail(self, pQryInvestorProdSPBMDetail:CThostFtdcQryInvestorProdSPBMDetailField, nRequestID:int): 
        """ 投资者产品SPBM明细查询 """ 
        return self.h.tReqQryInvestorProdSPBMDetail(self.api, byref(pQryInvestorProdSPBMDetail), nRequestID) 
    
    #################### 响应函数 #########################
    
    def __OnFrontConnected(self):
        self.OnFrontConnected()
    def OnFrontConnected(self):
        """ 当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。 """
        print('===OnFrontConnected===:')
    
    def __OnFrontDisconnected(self, nReason:int):
        self.OnFrontDisconnected(nReason)
    def OnFrontDisconnected(self, nReason:int):
        """ 当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。 """
        print('===OnFrontDisconnected===:nReason:int')
    
    def __OnHeartBeatWarning(self, nTimeLapse:int):
        self.OnHeartBeatWarning(nTimeLapse)
    def OnHeartBeatWarning(self, nTimeLapse:int):
        """ 心跳超时警告。当长时间未收到报文时，该方法被调用。 """
        print('===OnHeartBeatWarning===:nTimeLapse:int')
    
    def __OnRspAuthenticate(self, pRspAuthenticateField:CThostFtdcRspAuthenticateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspAuthenticate(copy.deepcopy(POINTER(CThostFtdcRspAuthenticateField).from_param(pRspAuthenticateField).contents) if pRspAuthenticateField else CThostFtdcRspAuthenticateField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspAuthenticate(self, pRspAuthenticateField:CThostFtdcRspAuthenticateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 客户端认证响应 """
        print('===OnRspAuthenticate===:pRspAuthenticateField:CThostFtdcRspAuthenticateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspUserLogin(self, pRspUserLogin:CThostFtdcRspUserLoginField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspUserLogin(copy.deepcopy(POINTER(CThostFtdcRspUserLoginField).from_param(pRspUserLogin).contents) if pRspUserLogin else CThostFtdcRspUserLoginField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspUserLogin(self, pRspUserLogin:CThostFtdcRspUserLoginField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 登录请求响应 """
        print('===OnRspUserLogin===:pRspUserLogin:CThostFtdcRspUserLoginField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspUserLogout(self, pUserLogout:CThostFtdcUserLogoutField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspUserLogout(copy.deepcopy(POINTER(CThostFtdcUserLogoutField).from_param(pUserLogout).contents) if pUserLogout else CThostFtdcUserLogoutField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspUserLogout(self, pUserLogout:CThostFtdcUserLogoutField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 登出请求响应 """
        print('===OnRspUserLogout===:pUserLogout:CThostFtdcUserLogoutField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspUserPasswordUpdate(self, pUserPasswordUpdate:CThostFtdcUserPasswordUpdateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspUserPasswordUpdate(copy.deepcopy(POINTER(CThostFtdcUserPasswordUpdateField).from_param(pUserPasswordUpdate).contents) if pUserPasswordUpdate else CThostFtdcUserPasswordUpdateField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspUserPasswordUpdate(self, pUserPasswordUpdate:CThostFtdcUserPasswordUpdateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 用户口令更新请求响应 """
        print('===OnRspUserPasswordUpdate===:pUserPasswordUpdate:CThostFtdcUserPasswordUpdateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspTradingAccountPasswordUpdate(self, pTradingAccountPasswordUpdate:CThostFtdcTradingAccountPasswordUpdateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspTradingAccountPasswordUpdate(copy.deepcopy(POINTER(CThostFtdcTradingAccountPasswordUpdateField).from_param(pTradingAccountPasswordUpdate).contents) if pTradingAccountPasswordUpdate else CThostFtdcTradingAccountPasswordUpdateField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspTradingAccountPasswordUpdate(self, pTradingAccountPasswordUpdate:CThostFtdcTradingAccountPasswordUpdateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 资金账户口令更新请求响应 """
        print('===OnRspTradingAccountPasswordUpdate===:pTradingAccountPasswordUpdate:CThostFtdcTradingAccountPasswordUpdateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspUserAuthMethod(self, pRspUserAuthMethod:CThostFtdcRspUserAuthMethodField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspUserAuthMethod(copy.deepcopy(POINTER(CThostFtdcRspUserAuthMethodField).from_param(pRspUserAuthMethod).contents) if pRspUserAuthMethod else CThostFtdcRspUserAuthMethodField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspUserAuthMethod(self, pRspUserAuthMethod:CThostFtdcRspUserAuthMethodField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 查询用户当前支持的认证模式的回复 """
        print('===OnRspUserAuthMethod===:pRspUserAuthMethod:CThostFtdcRspUserAuthMethodField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspGenUserCaptcha(self, pRspGenUserCaptcha:CThostFtdcRspGenUserCaptchaField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspGenUserCaptcha(copy.deepcopy(POINTER(CThostFtdcRspGenUserCaptchaField).from_param(pRspGenUserCaptcha).contents) if pRspGenUserCaptcha else CThostFtdcRspGenUserCaptchaField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspGenUserCaptcha(self, pRspGenUserCaptcha:CThostFtdcRspGenUserCaptchaField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 获取图形验证码请求的回复 """
        print('===OnRspGenUserCaptcha===:pRspGenUserCaptcha:CThostFtdcRspGenUserCaptchaField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspGenUserText(self, pRspGenUserText:CThostFtdcRspGenUserTextField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspGenUserText(copy.deepcopy(POINTER(CThostFtdcRspGenUserTextField).from_param(pRspGenUserText).contents) if pRspGenUserText else CThostFtdcRspGenUserTextField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspGenUserText(self, pRspGenUserText:CThostFtdcRspGenUserTextField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 获取短信验证码请求的回复 """
        print('===OnRspGenUserText===:pRspGenUserText:CThostFtdcRspGenUserTextField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspOrderInsert(self, pInputOrder:CThostFtdcInputOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspOrderInsert(copy.deepcopy(POINTER(CThostFtdcInputOrderField).from_param(pInputOrder).contents) if pInputOrder else CThostFtdcInputOrderField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspOrderInsert(self, pInputOrder:CThostFtdcInputOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 报单录入请求响应 """
        print('===OnRspOrderInsert===:pInputOrder:CThostFtdcInputOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspParkedOrderInsert(self, pParkedOrder:CThostFtdcParkedOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspParkedOrderInsert(copy.deepcopy(POINTER(CThostFtdcParkedOrderField).from_param(pParkedOrder).contents) if pParkedOrder else CThostFtdcParkedOrderField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspParkedOrderInsert(self, pParkedOrder:CThostFtdcParkedOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 预埋单录入请求响应 """
        print('===OnRspParkedOrderInsert===:pParkedOrder:CThostFtdcParkedOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspParkedOrderAction(self, pParkedOrderAction:CThostFtdcParkedOrderActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspParkedOrderAction(copy.deepcopy(POINTER(CThostFtdcParkedOrderActionField).from_param(pParkedOrderAction).contents) if pParkedOrderAction else CThostFtdcParkedOrderActionField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspParkedOrderAction(self, pParkedOrderAction:CThostFtdcParkedOrderActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 预埋撤单录入请求响应 """
        print('===OnRspParkedOrderAction===:pParkedOrderAction:CThostFtdcParkedOrderActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspOrderAction(self, pInputOrderAction:CThostFtdcInputOrderActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspOrderAction(copy.deepcopy(POINTER(CThostFtdcInputOrderActionField).from_param(pInputOrderAction).contents) if pInputOrderAction else CThostFtdcInputOrderActionField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspOrderAction(self, pInputOrderAction:CThostFtdcInputOrderActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 报单操作请求响应 """
        print('===OnRspOrderAction===:pInputOrderAction:CThostFtdcInputOrderActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryMaxOrderVolume(self, pQryMaxOrderVolume:CThostFtdcQryMaxOrderVolumeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryMaxOrderVolume(copy.deepcopy(POINTER(CThostFtdcQryMaxOrderVolumeField).from_param(pQryMaxOrderVolume).contents) if pQryMaxOrderVolume else CThostFtdcQryMaxOrderVolumeField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryMaxOrderVolume(self, pQryMaxOrderVolume:CThostFtdcQryMaxOrderVolumeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 查询最大报单数量响应 """
        print('===OnRspQryMaxOrderVolume===:pQryMaxOrderVolume:CThostFtdcQryMaxOrderVolumeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspSettlementInfoConfirm(self, pSettlementInfoConfirm:CThostFtdcSettlementInfoConfirmField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspSettlementInfoConfirm(copy.deepcopy(POINTER(CThostFtdcSettlementInfoConfirmField).from_param(pSettlementInfoConfirm).contents) if pSettlementInfoConfirm else CThostFtdcSettlementInfoConfirmField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspSettlementInfoConfirm(self, pSettlementInfoConfirm:CThostFtdcSettlementInfoConfirmField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 投资者结算结果确认响应 """
        print('===OnRspSettlementInfoConfirm===:pSettlementInfoConfirm:CThostFtdcSettlementInfoConfirmField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspRemoveParkedOrder(self, pRemoveParkedOrder:CThostFtdcRemoveParkedOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspRemoveParkedOrder(copy.deepcopy(POINTER(CThostFtdcRemoveParkedOrderField).from_param(pRemoveParkedOrder).contents) if pRemoveParkedOrder else CThostFtdcRemoveParkedOrderField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspRemoveParkedOrder(self, pRemoveParkedOrder:CThostFtdcRemoveParkedOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 删除预埋单响应 """
        print('===OnRspRemoveParkedOrder===:pRemoveParkedOrder:CThostFtdcRemoveParkedOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspRemoveParkedOrderAction(self, pRemoveParkedOrderAction:CThostFtdcRemoveParkedOrderActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspRemoveParkedOrderAction(copy.deepcopy(POINTER(CThostFtdcRemoveParkedOrderActionField).from_param(pRemoveParkedOrderAction).contents) if pRemoveParkedOrderAction else CThostFtdcRemoveParkedOrderActionField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspRemoveParkedOrderAction(self, pRemoveParkedOrderAction:CThostFtdcRemoveParkedOrderActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 删除预埋撤单响应 """
        print('===OnRspRemoveParkedOrderAction===:pRemoveParkedOrderAction:CThostFtdcRemoveParkedOrderActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspExecOrderInsert(self, pInputExecOrder:CThostFtdcInputExecOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspExecOrderInsert(copy.deepcopy(POINTER(CThostFtdcInputExecOrderField).from_param(pInputExecOrder).contents) if pInputExecOrder else CThostFtdcInputExecOrderField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspExecOrderInsert(self, pInputExecOrder:CThostFtdcInputExecOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 执行宣告录入请求响应 """
        print('===OnRspExecOrderInsert===:pInputExecOrder:CThostFtdcInputExecOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspExecOrderAction(self, pInputExecOrderAction:CThostFtdcInputExecOrderActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspExecOrderAction(copy.deepcopy(POINTER(CThostFtdcInputExecOrderActionField).from_param(pInputExecOrderAction).contents) if pInputExecOrderAction else CThostFtdcInputExecOrderActionField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspExecOrderAction(self, pInputExecOrderAction:CThostFtdcInputExecOrderActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 执行宣告操作请求响应 """
        print('===OnRspExecOrderAction===:pInputExecOrderAction:CThostFtdcInputExecOrderActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspForQuoteInsert(self, pInputForQuote:CThostFtdcInputForQuoteField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspForQuoteInsert(copy.deepcopy(POINTER(CThostFtdcInputForQuoteField).from_param(pInputForQuote).contents) if pInputForQuote else CThostFtdcInputForQuoteField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspForQuoteInsert(self, pInputForQuote:CThostFtdcInputForQuoteField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 询价录入请求响应 """
        print('===OnRspForQuoteInsert===:pInputForQuote:CThostFtdcInputForQuoteField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQuoteInsert(self, pInputQuote:CThostFtdcInputQuoteField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQuoteInsert(copy.deepcopy(POINTER(CThostFtdcInputQuoteField).from_param(pInputQuote).contents) if pInputQuote else CThostFtdcInputQuoteField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQuoteInsert(self, pInputQuote:CThostFtdcInputQuoteField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 报价录入请求响应 """
        print('===OnRspQuoteInsert===:pInputQuote:CThostFtdcInputQuoteField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQuoteAction(self, pInputQuoteAction:CThostFtdcInputQuoteActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQuoteAction(copy.deepcopy(POINTER(CThostFtdcInputQuoteActionField).from_param(pInputQuoteAction).contents) if pInputQuoteAction else CThostFtdcInputQuoteActionField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQuoteAction(self, pInputQuoteAction:CThostFtdcInputQuoteActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 报价操作请求响应 """
        print('===OnRspQuoteAction===:pInputQuoteAction:CThostFtdcInputQuoteActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspBatchOrderAction(self, pInputBatchOrderAction:CThostFtdcInputBatchOrderActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspBatchOrderAction(copy.deepcopy(POINTER(CThostFtdcInputBatchOrderActionField).from_param(pInputBatchOrderAction).contents) if pInputBatchOrderAction else CThostFtdcInputBatchOrderActionField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspBatchOrderAction(self, pInputBatchOrderAction:CThostFtdcInputBatchOrderActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 批量报单操作请求响应 """
        print('===OnRspBatchOrderAction===:pInputBatchOrderAction:CThostFtdcInputBatchOrderActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspOptionSelfCloseInsert(self, pInputOptionSelfClose:CThostFtdcInputOptionSelfCloseField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspOptionSelfCloseInsert(copy.deepcopy(POINTER(CThostFtdcInputOptionSelfCloseField).from_param(pInputOptionSelfClose).contents) if pInputOptionSelfClose else CThostFtdcInputOptionSelfCloseField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspOptionSelfCloseInsert(self, pInputOptionSelfClose:CThostFtdcInputOptionSelfCloseField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 期权自对冲录入请求响应 """
        print('===OnRspOptionSelfCloseInsert===:pInputOptionSelfClose:CThostFtdcInputOptionSelfCloseField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspOptionSelfCloseAction(self, pInputOptionSelfCloseAction:CThostFtdcInputOptionSelfCloseActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspOptionSelfCloseAction(copy.deepcopy(POINTER(CThostFtdcInputOptionSelfCloseActionField).from_param(pInputOptionSelfCloseAction).contents) if pInputOptionSelfCloseAction else CThostFtdcInputOptionSelfCloseActionField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspOptionSelfCloseAction(self, pInputOptionSelfCloseAction:CThostFtdcInputOptionSelfCloseActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 期权自对冲操作请求响应 """
        print('===OnRspOptionSelfCloseAction===:pInputOptionSelfCloseAction:CThostFtdcInputOptionSelfCloseActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspCombActionInsert(self, pInputCombAction:CThostFtdcInputCombActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspCombActionInsert(copy.deepcopy(POINTER(CThostFtdcInputCombActionField).from_param(pInputCombAction).contents) if pInputCombAction else CThostFtdcInputCombActionField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspCombActionInsert(self, pInputCombAction:CThostFtdcInputCombActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 申请组合录入请求响应 """
        print('===OnRspCombActionInsert===:pInputCombAction:CThostFtdcInputCombActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryOrder(self, pOrder:CThostFtdcOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryOrder(copy.deepcopy(POINTER(CThostFtdcOrderField).from_param(pOrder).contents) if pOrder else CThostFtdcOrderField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryOrder(self, pOrder:CThostFtdcOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询报单响应 """
        print('===OnRspQryOrder===:pOrder:CThostFtdcOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryTrade(self, pTrade:CThostFtdcTradeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryTrade(copy.deepcopy(POINTER(CThostFtdcTradeField).from_param(pTrade).contents) if pTrade else CThostFtdcTradeField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryTrade(self, pTrade:CThostFtdcTradeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询成交响应 """
        print('===OnRspQryTrade===:pTrade:CThostFtdcTradeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryInvestorPosition(self, pInvestorPosition:CThostFtdcInvestorPositionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryInvestorPosition(copy.deepcopy(POINTER(CThostFtdcInvestorPositionField).from_param(pInvestorPosition).contents) if pInvestorPosition else CThostFtdcInvestorPositionField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryInvestorPosition(self, pInvestorPosition:CThostFtdcInvestorPositionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询投资者持仓响应 """
        print('===OnRspQryInvestorPosition===:pInvestorPosition:CThostFtdcInvestorPositionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryTradingAccount(self, pTradingAccount:CThostFtdcTradingAccountField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryTradingAccount(copy.deepcopy(POINTER(CThostFtdcTradingAccountField).from_param(pTradingAccount).contents) if pTradingAccount else CThostFtdcTradingAccountField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryTradingAccount(self, pTradingAccount:CThostFtdcTradingAccountField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询资金账户响应 """
        print('===OnRspQryTradingAccount===:pTradingAccount:CThostFtdcTradingAccountField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryInvestor(self, pInvestor:CThostFtdcInvestorField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryInvestor(copy.deepcopy(POINTER(CThostFtdcInvestorField).from_param(pInvestor).contents) if pInvestor else CThostFtdcInvestorField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryInvestor(self, pInvestor:CThostFtdcInvestorField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询投资者响应 """
        print('===OnRspQryInvestor===:pInvestor:CThostFtdcInvestorField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryTradingCode(self, pTradingCode:CThostFtdcTradingCodeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryTradingCode(copy.deepcopy(POINTER(CThostFtdcTradingCodeField).from_param(pTradingCode).contents) if pTradingCode else CThostFtdcTradingCodeField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryTradingCode(self, pTradingCode:CThostFtdcTradingCodeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询交易编码响应 """
        print('===OnRspQryTradingCode===:pTradingCode:CThostFtdcTradingCodeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryInstrumentMarginRate(self, pInstrumentMarginRate:CThostFtdcInstrumentMarginRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryInstrumentMarginRate(copy.deepcopy(POINTER(CThostFtdcInstrumentMarginRateField).from_param(pInstrumentMarginRate).contents) if pInstrumentMarginRate else CThostFtdcInstrumentMarginRateField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryInstrumentMarginRate(self, pInstrumentMarginRate:CThostFtdcInstrumentMarginRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询合约保证金率响应 """
        print('===OnRspQryInstrumentMarginRate===:pInstrumentMarginRate:CThostFtdcInstrumentMarginRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryInstrumentCommissionRate(self, pInstrumentCommissionRate:CThostFtdcInstrumentCommissionRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryInstrumentCommissionRate(copy.deepcopy(POINTER(CThostFtdcInstrumentCommissionRateField).from_param(pInstrumentCommissionRate).contents) if pInstrumentCommissionRate else CThostFtdcInstrumentCommissionRateField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryInstrumentCommissionRate(self, pInstrumentCommissionRate:CThostFtdcInstrumentCommissionRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询合约手续费率响应 """
        print('===OnRspQryInstrumentCommissionRate===:pInstrumentCommissionRate:CThostFtdcInstrumentCommissionRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryExchange(self, pExchange:CThostFtdcExchangeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryExchange(copy.deepcopy(POINTER(CThostFtdcExchangeField).from_param(pExchange).contents) if pExchange else CThostFtdcExchangeField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryExchange(self, pExchange:CThostFtdcExchangeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询交易所响应 """
        print('===OnRspQryExchange===:pExchange:CThostFtdcExchangeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryProduct(self, pProduct:CThostFtdcProductField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryProduct(copy.deepcopy(POINTER(CThostFtdcProductField).from_param(pProduct).contents) if pProduct else CThostFtdcProductField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryProduct(self, pProduct:CThostFtdcProductField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询产品响应 """
        print('===OnRspQryProduct===:pProduct:CThostFtdcProductField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryInstrument(self, pInstrument:CThostFtdcInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryInstrument(copy.deepcopy(POINTER(CThostFtdcInstrumentField).from_param(pInstrument).contents) if pInstrument else CThostFtdcInstrumentField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryInstrument(self, pInstrument:CThostFtdcInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询合约响应 """
        print('===OnRspQryInstrument===:pInstrument:CThostFtdcInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryDepthMarketData(self, pDepthMarketData:CThostFtdcDepthMarketDataField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryDepthMarketData(copy.deepcopy(POINTER(CThostFtdcDepthMarketDataField).from_param(pDepthMarketData).contents) if pDepthMarketData else CThostFtdcDepthMarketDataField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryDepthMarketData(self, pDepthMarketData:CThostFtdcDepthMarketDataField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询行情响应 """
        print('===OnRspQryDepthMarketData===:pDepthMarketData:CThostFtdcDepthMarketDataField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryTraderOffer(self, pTraderOffer:CThostFtdcTraderOfferField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryTraderOffer(copy.deepcopy(POINTER(CThostFtdcTraderOfferField).from_param(pTraderOffer).contents) if pTraderOffer else CThostFtdcTraderOfferField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryTraderOffer(self, pTraderOffer:CThostFtdcTraderOfferField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询交易员报盘机响应 """
        print('===OnRspQryTraderOffer===:pTraderOffer:CThostFtdcTraderOfferField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQrySettlementInfo(self, pSettlementInfo:CThostFtdcSettlementInfoField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQrySettlementInfo(copy.deepcopy(POINTER(CThostFtdcSettlementInfoField).from_param(pSettlementInfo).contents) if pSettlementInfo else CThostFtdcSettlementInfoField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQrySettlementInfo(self, pSettlementInfo:CThostFtdcSettlementInfoField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询投资者结算结果响应 """
        print('===OnRspQrySettlementInfo===:pSettlementInfo:CThostFtdcSettlementInfoField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryTransferBank(self, pTransferBank:CThostFtdcTransferBankField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryTransferBank(copy.deepcopy(POINTER(CThostFtdcTransferBankField).from_param(pTransferBank).contents) if pTransferBank else CThostFtdcTransferBankField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryTransferBank(self, pTransferBank:CThostFtdcTransferBankField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询转帐银行响应 """
        print('===OnRspQryTransferBank===:pTransferBank:CThostFtdcTransferBankField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryInvestorPositionDetail(self, pInvestorPositionDetail:CThostFtdcInvestorPositionDetailField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryInvestorPositionDetail(copy.deepcopy(POINTER(CThostFtdcInvestorPositionDetailField).from_param(pInvestorPositionDetail).contents) if pInvestorPositionDetail else CThostFtdcInvestorPositionDetailField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryInvestorPositionDetail(self, pInvestorPositionDetail:CThostFtdcInvestorPositionDetailField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询投资者持仓明细响应 """
        print('===OnRspQryInvestorPositionDetail===:pInvestorPositionDetail:CThostFtdcInvestorPositionDetailField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryNotice(self, pNotice:CThostFtdcNoticeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryNotice(copy.deepcopy(POINTER(CThostFtdcNoticeField).from_param(pNotice).contents) if pNotice else CThostFtdcNoticeField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryNotice(self, pNotice:CThostFtdcNoticeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询客户通知响应 """
        print('===OnRspQryNotice===:pNotice:CThostFtdcNoticeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQrySettlementInfoConfirm(self, pSettlementInfoConfirm:CThostFtdcSettlementInfoConfirmField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQrySettlementInfoConfirm(copy.deepcopy(POINTER(CThostFtdcSettlementInfoConfirmField).from_param(pSettlementInfoConfirm).contents) if pSettlementInfoConfirm else CThostFtdcSettlementInfoConfirmField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQrySettlementInfoConfirm(self, pSettlementInfoConfirm:CThostFtdcSettlementInfoConfirmField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询结算信息确认响应 """
        print('===OnRspQrySettlementInfoConfirm===:pSettlementInfoConfirm:CThostFtdcSettlementInfoConfirmField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryInvestorPositionCombineDetail(self, pInvestorPositionCombineDetail:CThostFtdcInvestorPositionCombineDetailField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryInvestorPositionCombineDetail(copy.deepcopy(POINTER(CThostFtdcInvestorPositionCombineDetailField).from_param(pInvestorPositionCombineDetail).contents) if pInvestorPositionCombineDetail else CThostFtdcInvestorPositionCombineDetailField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryInvestorPositionCombineDetail(self, pInvestorPositionCombineDetail:CThostFtdcInvestorPositionCombineDetailField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询投资者持仓明细响应 """
        print('===OnRspQryInvestorPositionCombineDetail===:pInvestorPositionCombineDetail:CThostFtdcInvestorPositionCombineDetailField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryCFMMCTradingAccountKey(self, pCFMMCTradingAccountKey:CThostFtdcCFMMCTradingAccountKeyField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryCFMMCTradingAccountKey(copy.deepcopy(POINTER(CThostFtdcCFMMCTradingAccountKeyField).from_param(pCFMMCTradingAccountKey).contents) if pCFMMCTradingAccountKey else CThostFtdcCFMMCTradingAccountKeyField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryCFMMCTradingAccountKey(self, pCFMMCTradingAccountKey:CThostFtdcCFMMCTradingAccountKeyField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 查询保证金监管系统经纪公司资金账户密钥响应 """
        print('===OnRspQryCFMMCTradingAccountKey===:pCFMMCTradingAccountKey:CThostFtdcCFMMCTradingAccountKeyField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryEWarrantOffset(self, pEWarrantOffset:CThostFtdcEWarrantOffsetField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryEWarrantOffset(copy.deepcopy(POINTER(CThostFtdcEWarrantOffsetField).from_param(pEWarrantOffset).contents) if pEWarrantOffset else CThostFtdcEWarrantOffsetField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryEWarrantOffset(self, pEWarrantOffset:CThostFtdcEWarrantOffsetField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询仓单折抵信息响应 """
        print('===OnRspQryEWarrantOffset===:pEWarrantOffset:CThostFtdcEWarrantOffsetField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryInvestorProductGroupMargin(self, pInvestorProductGroupMargin:CThostFtdcInvestorProductGroupMarginField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryInvestorProductGroupMargin(copy.deepcopy(POINTER(CThostFtdcInvestorProductGroupMarginField).from_param(pInvestorProductGroupMargin).contents) if pInvestorProductGroupMargin else CThostFtdcInvestorProductGroupMarginField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryInvestorProductGroupMargin(self, pInvestorProductGroupMargin:CThostFtdcInvestorProductGroupMarginField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询投资者品种/跨品种保证金响应 """
        print('===OnRspQryInvestorProductGroupMargin===:pInvestorProductGroupMargin:CThostFtdcInvestorProductGroupMarginField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryExchangeMarginRate(self, pExchangeMarginRate:CThostFtdcExchangeMarginRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryExchangeMarginRate(copy.deepcopy(POINTER(CThostFtdcExchangeMarginRateField).from_param(pExchangeMarginRate).contents) if pExchangeMarginRate else CThostFtdcExchangeMarginRateField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryExchangeMarginRate(self, pExchangeMarginRate:CThostFtdcExchangeMarginRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询交易所保证金率响应 """
        print('===OnRspQryExchangeMarginRate===:pExchangeMarginRate:CThostFtdcExchangeMarginRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryExchangeMarginRateAdjust(self, pExchangeMarginRateAdjust:CThostFtdcExchangeMarginRateAdjustField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryExchangeMarginRateAdjust(copy.deepcopy(POINTER(CThostFtdcExchangeMarginRateAdjustField).from_param(pExchangeMarginRateAdjust).contents) if pExchangeMarginRateAdjust else CThostFtdcExchangeMarginRateAdjustField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryExchangeMarginRateAdjust(self, pExchangeMarginRateAdjust:CThostFtdcExchangeMarginRateAdjustField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询交易所调整保证金率响应 """
        print('===OnRspQryExchangeMarginRateAdjust===:pExchangeMarginRateAdjust:CThostFtdcExchangeMarginRateAdjustField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryExchangeRate(self, pExchangeRate:CThostFtdcExchangeRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryExchangeRate(copy.deepcopy(POINTER(CThostFtdcExchangeRateField).from_param(pExchangeRate).contents) if pExchangeRate else CThostFtdcExchangeRateField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryExchangeRate(self, pExchangeRate:CThostFtdcExchangeRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询汇率响应 """
        print('===OnRspQryExchangeRate===:pExchangeRate:CThostFtdcExchangeRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQrySecAgentACIDMap(self, pSecAgentACIDMap:CThostFtdcSecAgentACIDMapField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQrySecAgentACIDMap(copy.deepcopy(POINTER(CThostFtdcSecAgentACIDMapField).from_param(pSecAgentACIDMap).contents) if pSecAgentACIDMap else CThostFtdcSecAgentACIDMapField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQrySecAgentACIDMap(self, pSecAgentACIDMap:CThostFtdcSecAgentACIDMapField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询二级代理操作员银期权限响应 """
        print('===OnRspQrySecAgentACIDMap===:pSecAgentACIDMap:CThostFtdcSecAgentACIDMapField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryProductExchRate(self, pProductExchRate:CThostFtdcProductExchRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryProductExchRate(copy.deepcopy(POINTER(CThostFtdcProductExchRateField).from_param(pProductExchRate).contents) if pProductExchRate else CThostFtdcProductExchRateField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryProductExchRate(self, pProductExchRate:CThostFtdcProductExchRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询产品报价汇率 """
        print('===OnRspQryProductExchRate===:pProductExchRate:CThostFtdcProductExchRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryProductGroup(self, pProductGroup:CThostFtdcProductGroupField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryProductGroup(copy.deepcopy(POINTER(CThostFtdcProductGroupField).from_param(pProductGroup).contents) if pProductGroup else CThostFtdcProductGroupField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryProductGroup(self, pProductGroup:CThostFtdcProductGroupField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询产品组 """
        print('===OnRspQryProductGroup===:pProductGroup:CThostFtdcProductGroupField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryMMInstrumentCommissionRate(self, pMMInstrumentCommissionRate:CThostFtdcMMInstrumentCommissionRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryMMInstrumentCommissionRate(copy.deepcopy(POINTER(CThostFtdcMMInstrumentCommissionRateField).from_param(pMMInstrumentCommissionRate).contents) if pMMInstrumentCommissionRate else CThostFtdcMMInstrumentCommissionRateField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryMMInstrumentCommissionRate(self, pMMInstrumentCommissionRate:CThostFtdcMMInstrumentCommissionRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询做市商合约手续费率响应 """
        print('===OnRspQryMMInstrumentCommissionRate===:pMMInstrumentCommissionRate:CThostFtdcMMInstrumentCommissionRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryMMOptionInstrCommRate(self, pMMOptionInstrCommRate:CThostFtdcMMOptionInstrCommRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryMMOptionInstrCommRate(copy.deepcopy(POINTER(CThostFtdcMMOptionInstrCommRateField).from_param(pMMOptionInstrCommRate).contents) if pMMOptionInstrCommRate else CThostFtdcMMOptionInstrCommRateField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryMMOptionInstrCommRate(self, pMMOptionInstrCommRate:CThostFtdcMMOptionInstrCommRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询做市商期权合约手续费响应 """
        print('===OnRspQryMMOptionInstrCommRate===:pMMOptionInstrCommRate:CThostFtdcMMOptionInstrCommRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryInstrumentOrderCommRate(self, pInstrumentOrderCommRate:CThostFtdcInstrumentOrderCommRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryInstrumentOrderCommRate(copy.deepcopy(POINTER(CThostFtdcInstrumentOrderCommRateField).from_param(pInstrumentOrderCommRate).contents) if pInstrumentOrderCommRate else CThostFtdcInstrumentOrderCommRateField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryInstrumentOrderCommRate(self, pInstrumentOrderCommRate:CThostFtdcInstrumentOrderCommRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询报单手续费响应 """
        print('===OnRspQryInstrumentOrderCommRate===:pInstrumentOrderCommRate:CThostFtdcInstrumentOrderCommRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQrySecAgentTradingAccount(self, pTradingAccount:CThostFtdcTradingAccountField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQrySecAgentTradingAccount(copy.deepcopy(POINTER(CThostFtdcTradingAccountField).from_param(pTradingAccount).contents) if pTradingAccount else CThostFtdcTradingAccountField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQrySecAgentTradingAccount(self, pTradingAccount:CThostFtdcTradingAccountField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询资金账户响应 """
        print('===OnRspQrySecAgentTradingAccount===:pTradingAccount:CThostFtdcTradingAccountField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQrySecAgentCheckMode(self, pSecAgentCheckMode:CThostFtdcSecAgentCheckModeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQrySecAgentCheckMode(copy.deepcopy(POINTER(CThostFtdcSecAgentCheckModeField).from_param(pSecAgentCheckMode).contents) if pSecAgentCheckMode else CThostFtdcSecAgentCheckModeField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQrySecAgentCheckMode(self, pSecAgentCheckMode:CThostFtdcSecAgentCheckModeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询二级代理商资金校验模式响应 """
        print('===OnRspQrySecAgentCheckMode===:pSecAgentCheckMode:CThostFtdcSecAgentCheckModeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQrySecAgentTradeInfo(self, pSecAgentTradeInfo:CThostFtdcSecAgentTradeInfoField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQrySecAgentTradeInfo(copy.deepcopy(POINTER(CThostFtdcSecAgentTradeInfoField).from_param(pSecAgentTradeInfo).contents) if pSecAgentTradeInfo else CThostFtdcSecAgentTradeInfoField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQrySecAgentTradeInfo(self, pSecAgentTradeInfo:CThostFtdcSecAgentTradeInfoField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询二级代理商信息响应 """
        print('===OnRspQrySecAgentTradeInfo===:pSecAgentTradeInfo:CThostFtdcSecAgentTradeInfoField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryOptionInstrTradeCost(self, pOptionInstrTradeCost:CThostFtdcOptionInstrTradeCostField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryOptionInstrTradeCost(copy.deepcopy(POINTER(CThostFtdcOptionInstrTradeCostField).from_param(pOptionInstrTradeCost).contents) if pOptionInstrTradeCost else CThostFtdcOptionInstrTradeCostField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryOptionInstrTradeCost(self, pOptionInstrTradeCost:CThostFtdcOptionInstrTradeCostField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询期权交易成本响应 """
        print('===OnRspQryOptionInstrTradeCost===:pOptionInstrTradeCost:CThostFtdcOptionInstrTradeCostField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryOptionInstrCommRate(self, pOptionInstrCommRate:CThostFtdcOptionInstrCommRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryOptionInstrCommRate(copy.deepcopy(POINTER(CThostFtdcOptionInstrCommRateField).from_param(pOptionInstrCommRate).contents) if pOptionInstrCommRate else CThostFtdcOptionInstrCommRateField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryOptionInstrCommRate(self, pOptionInstrCommRate:CThostFtdcOptionInstrCommRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询期权合约手续费响应 """
        print('===OnRspQryOptionInstrCommRate===:pOptionInstrCommRate:CThostFtdcOptionInstrCommRateField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryExecOrder(self, pExecOrder:CThostFtdcExecOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryExecOrder(copy.deepcopy(POINTER(CThostFtdcExecOrderField).from_param(pExecOrder).contents) if pExecOrder else CThostFtdcExecOrderField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryExecOrder(self, pExecOrder:CThostFtdcExecOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询执行宣告响应 """
        print('===OnRspQryExecOrder===:pExecOrder:CThostFtdcExecOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryForQuote(self, pForQuote:CThostFtdcForQuoteField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryForQuote(copy.deepcopy(POINTER(CThostFtdcForQuoteField).from_param(pForQuote).contents) if pForQuote else CThostFtdcForQuoteField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryForQuote(self, pForQuote:CThostFtdcForQuoteField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询询价响应 """
        print('===OnRspQryForQuote===:pForQuote:CThostFtdcForQuoteField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryQuote(self, pQuote:CThostFtdcQuoteField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryQuote(copy.deepcopy(POINTER(CThostFtdcQuoteField).from_param(pQuote).contents) if pQuote else CThostFtdcQuoteField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryQuote(self, pQuote:CThostFtdcQuoteField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询报价响应 """
        print('===OnRspQryQuote===:pQuote:CThostFtdcQuoteField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryOptionSelfClose(self, pOptionSelfClose:CThostFtdcOptionSelfCloseField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryOptionSelfClose(copy.deepcopy(POINTER(CThostFtdcOptionSelfCloseField).from_param(pOptionSelfClose).contents) if pOptionSelfClose else CThostFtdcOptionSelfCloseField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryOptionSelfClose(self, pOptionSelfClose:CThostFtdcOptionSelfCloseField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询期权自对冲响应 """
        print('===OnRspQryOptionSelfClose===:pOptionSelfClose:CThostFtdcOptionSelfCloseField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryInvestUnit(self, pInvestUnit:CThostFtdcInvestUnitField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryInvestUnit(copy.deepcopy(POINTER(CThostFtdcInvestUnitField).from_param(pInvestUnit).contents) if pInvestUnit else CThostFtdcInvestUnitField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryInvestUnit(self, pInvestUnit:CThostFtdcInvestUnitField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询投资单元响应 """
        print('===OnRspQryInvestUnit===:pInvestUnit:CThostFtdcInvestUnitField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryCombInstrumentGuard(self, pCombInstrumentGuard:CThostFtdcCombInstrumentGuardField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryCombInstrumentGuard(copy.deepcopy(POINTER(CThostFtdcCombInstrumentGuardField).from_param(pCombInstrumentGuard).contents) if pCombInstrumentGuard else CThostFtdcCombInstrumentGuardField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryCombInstrumentGuard(self, pCombInstrumentGuard:CThostFtdcCombInstrumentGuardField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询组合合约安全系数响应 """
        print('===OnRspQryCombInstrumentGuard===:pCombInstrumentGuard:CThostFtdcCombInstrumentGuardField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryCombAction(self, pCombAction:CThostFtdcCombActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryCombAction(copy.deepcopy(POINTER(CThostFtdcCombActionField).from_param(pCombAction).contents) if pCombAction else CThostFtdcCombActionField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryCombAction(self, pCombAction:CThostFtdcCombActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询申请组合响应 """
        print('===OnRspQryCombAction===:pCombAction:CThostFtdcCombActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryTransferSerial(self, pTransferSerial:CThostFtdcTransferSerialField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryTransferSerial(copy.deepcopy(POINTER(CThostFtdcTransferSerialField).from_param(pTransferSerial).contents) if pTransferSerial else CThostFtdcTransferSerialField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryTransferSerial(self, pTransferSerial:CThostFtdcTransferSerialField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询转帐流水响应 """
        print('===OnRspQryTransferSerial===:pTransferSerial:CThostFtdcTransferSerialField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryAccountregister(self, pAccountregister:CThostFtdcAccountregisterField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryAccountregister(copy.deepcopy(POINTER(CThostFtdcAccountregisterField).from_param(pAccountregister).contents) if pAccountregister else CThostFtdcAccountregisterField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryAccountregister(self, pAccountregister:CThostFtdcAccountregisterField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询银期签约关系响应 """
        print('===OnRspQryAccountregister===:pAccountregister:CThostFtdcAccountregisterField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspError(self, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspError(copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspError(self, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 错误应答 """
        print('===OnRspError===:pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRtnOrder(self, pOrder:CThostFtdcOrderField):
        self.OnRtnOrder(copy.deepcopy(POINTER(CThostFtdcOrderField).from_param(pOrder).contents) if pOrder else CThostFtdcOrderField())
    def OnRtnOrder(self, pOrder:CThostFtdcOrderField):
        """ 报单通知 """
        print('===OnRtnOrder===:pOrder:CThostFtdcOrderField')
    
    def __OnRtnTrade(self, pTrade:CThostFtdcTradeField):
        self.OnRtnTrade(copy.deepcopy(POINTER(CThostFtdcTradeField).from_param(pTrade).contents) if pTrade else CThostFtdcTradeField())
    def OnRtnTrade(self, pTrade:CThostFtdcTradeField):
        """ 成交通知 """
        print('===OnRtnTrade===:pTrade:CThostFtdcTradeField')
    
    def __OnErrRtnOrderInsert(self, pInputOrder:CThostFtdcInputOrderField, pRspInfo:CThostFtdcRspInfoField):
        self.OnErrRtnOrderInsert(copy.deepcopy(POINTER(CThostFtdcInputOrderField).from_param(pInputOrder).contents) if pInputOrder else CThostFtdcInputOrderField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField())
    def OnErrRtnOrderInsert(self, pInputOrder:CThostFtdcInputOrderField, pRspInfo:CThostFtdcRspInfoField):
        """ 报单录入错误回报 """
        print('===OnErrRtnOrderInsert===:pInputOrder:CThostFtdcInputOrderField, pRspInfo:CThostFtdcRspInfoField')
    
    def __OnErrRtnOrderAction(self, pOrderAction:CThostFtdcOrderActionField, pRspInfo:CThostFtdcRspInfoField):
        self.OnErrRtnOrderAction(copy.deepcopy(POINTER(CThostFtdcOrderActionField).from_param(pOrderAction).contents) if pOrderAction else CThostFtdcOrderActionField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField())
    def OnErrRtnOrderAction(self, pOrderAction:CThostFtdcOrderActionField, pRspInfo:CThostFtdcRspInfoField):
        """ 报单操作错误回报 """
        print('===OnErrRtnOrderAction===:pOrderAction:CThostFtdcOrderActionField, pRspInfo:CThostFtdcRspInfoField')
    
    def __OnRtnInstrumentStatus(self, pInstrumentStatus:CThostFtdcInstrumentStatusField):
        self.OnRtnInstrumentStatus(copy.deepcopy(POINTER(CThostFtdcInstrumentStatusField).from_param(pInstrumentStatus).contents) if pInstrumentStatus else CThostFtdcInstrumentStatusField())
    def OnRtnInstrumentStatus(self, pInstrumentStatus:CThostFtdcInstrumentStatusField):
        """ 合约交易状态通知 """
        print('===OnRtnInstrumentStatus===:pInstrumentStatus:CThostFtdcInstrumentStatusField')
    
    def __OnRtnBulletin(self, pBulletin:CThostFtdcBulletinField):
        self.OnRtnBulletin(copy.deepcopy(POINTER(CThostFtdcBulletinField).from_param(pBulletin).contents) if pBulletin else CThostFtdcBulletinField())
    def OnRtnBulletin(self, pBulletin:CThostFtdcBulletinField):
        """ 交易所公告通知 """
        print('===OnRtnBulletin===:pBulletin:CThostFtdcBulletinField')
    
    def __OnRtnTradingNotice(self, pTradingNoticeInfo:CThostFtdcTradingNoticeInfoField):
        self.OnRtnTradingNotice(copy.deepcopy(POINTER(CThostFtdcTradingNoticeInfoField).from_param(pTradingNoticeInfo).contents) if pTradingNoticeInfo else CThostFtdcTradingNoticeInfoField())
    def OnRtnTradingNotice(self, pTradingNoticeInfo:CThostFtdcTradingNoticeInfoField):
        """ 交易通知 """
        print('===OnRtnTradingNotice===:pTradingNoticeInfo:CThostFtdcTradingNoticeInfoField')
    
    def __OnRtnErrorConditionalOrder(self, pErrorConditionalOrder:CThostFtdcErrorConditionalOrderField):
        self.OnRtnErrorConditionalOrder(copy.deepcopy(POINTER(CThostFtdcErrorConditionalOrderField).from_param(pErrorConditionalOrder).contents) if pErrorConditionalOrder else CThostFtdcErrorConditionalOrderField())
    def OnRtnErrorConditionalOrder(self, pErrorConditionalOrder:CThostFtdcErrorConditionalOrderField):
        """ 提示条件单校验错误 """
        print('===OnRtnErrorConditionalOrder===:pErrorConditionalOrder:CThostFtdcErrorConditionalOrderField')
    
    def __OnRtnExecOrder(self, pExecOrder:CThostFtdcExecOrderField):
        self.OnRtnExecOrder(copy.deepcopy(POINTER(CThostFtdcExecOrderField).from_param(pExecOrder).contents) if pExecOrder else CThostFtdcExecOrderField())
    def OnRtnExecOrder(self, pExecOrder:CThostFtdcExecOrderField):
        """ 执行宣告通知 """
        print('===OnRtnExecOrder===:pExecOrder:CThostFtdcExecOrderField')
    
    def __OnErrRtnExecOrderInsert(self, pInputExecOrder:CThostFtdcInputExecOrderField, pRspInfo:CThostFtdcRspInfoField):
        self.OnErrRtnExecOrderInsert(copy.deepcopy(POINTER(CThostFtdcInputExecOrderField).from_param(pInputExecOrder).contents) if pInputExecOrder else CThostFtdcInputExecOrderField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField())
    def OnErrRtnExecOrderInsert(self, pInputExecOrder:CThostFtdcInputExecOrderField, pRspInfo:CThostFtdcRspInfoField):
        """ 执行宣告录入错误回报 """
        print('===OnErrRtnExecOrderInsert===:pInputExecOrder:CThostFtdcInputExecOrderField, pRspInfo:CThostFtdcRspInfoField')
    
    def __OnErrRtnExecOrderAction(self, pExecOrderAction:CThostFtdcExecOrderActionField, pRspInfo:CThostFtdcRspInfoField):
        self.OnErrRtnExecOrderAction(copy.deepcopy(POINTER(CThostFtdcExecOrderActionField).from_param(pExecOrderAction).contents) if pExecOrderAction else CThostFtdcExecOrderActionField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField())
    def OnErrRtnExecOrderAction(self, pExecOrderAction:CThostFtdcExecOrderActionField, pRspInfo:CThostFtdcRspInfoField):
        """ 执行宣告操作错误回报 """
        print('===OnErrRtnExecOrderAction===:pExecOrderAction:CThostFtdcExecOrderActionField, pRspInfo:CThostFtdcRspInfoField')
    
    def __OnErrRtnForQuoteInsert(self, pInputForQuote:CThostFtdcInputForQuoteField, pRspInfo:CThostFtdcRspInfoField):
        self.OnErrRtnForQuoteInsert(copy.deepcopy(POINTER(CThostFtdcInputForQuoteField).from_param(pInputForQuote).contents) if pInputForQuote else CThostFtdcInputForQuoteField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField())
    def OnErrRtnForQuoteInsert(self, pInputForQuote:CThostFtdcInputForQuoteField, pRspInfo:CThostFtdcRspInfoField):
        """ 询价录入错误回报 """
        print('===OnErrRtnForQuoteInsert===:pInputForQuote:CThostFtdcInputForQuoteField, pRspInfo:CThostFtdcRspInfoField')
    
    def __OnRtnQuote(self, pQuote:CThostFtdcQuoteField):
        self.OnRtnQuote(copy.deepcopy(POINTER(CThostFtdcQuoteField).from_param(pQuote).contents) if pQuote else CThostFtdcQuoteField())
    def OnRtnQuote(self, pQuote:CThostFtdcQuoteField):
        """ 报价通知 """
        print('===OnRtnQuote===:pQuote:CThostFtdcQuoteField')
    
    def __OnErrRtnQuoteInsert(self, pInputQuote:CThostFtdcInputQuoteField, pRspInfo:CThostFtdcRspInfoField):
        self.OnErrRtnQuoteInsert(copy.deepcopy(POINTER(CThostFtdcInputQuoteField).from_param(pInputQuote).contents) if pInputQuote else CThostFtdcInputQuoteField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField())
    def OnErrRtnQuoteInsert(self, pInputQuote:CThostFtdcInputQuoteField, pRspInfo:CThostFtdcRspInfoField):
        """ 报价录入错误回报 """
        print('===OnErrRtnQuoteInsert===:pInputQuote:CThostFtdcInputQuoteField, pRspInfo:CThostFtdcRspInfoField')
    
    def __OnErrRtnQuoteAction(self, pQuoteAction:CThostFtdcQuoteActionField, pRspInfo:CThostFtdcRspInfoField):
        self.OnErrRtnQuoteAction(copy.deepcopy(POINTER(CThostFtdcQuoteActionField).from_param(pQuoteAction).contents) if pQuoteAction else CThostFtdcQuoteActionField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField())
    def OnErrRtnQuoteAction(self, pQuoteAction:CThostFtdcQuoteActionField, pRspInfo:CThostFtdcRspInfoField):
        """ 报价操作错误回报 """
        print('===OnErrRtnQuoteAction===:pQuoteAction:CThostFtdcQuoteActionField, pRspInfo:CThostFtdcRspInfoField')
    
    def __OnRtnForQuoteRsp(self, pForQuoteRsp:CThostFtdcForQuoteRspField):
        self.OnRtnForQuoteRsp(copy.deepcopy(POINTER(CThostFtdcForQuoteRspField).from_param(pForQuoteRsp).contents) if pForQuoteRsp else CThostFtdcForQuoteRspField())
    def OnRtnForQuoteRsp(self, pForQuoteRsp:CThostFtdcForQuoteRspField):
        """ 询价通知 """
        print('===OnRtnForQuoteRsp===:pForQuoteRsp:CThostFtdcForQuoteRspField')
    
    def __OnRtnCFMMCTradingAccountToken(self, pCFMMCTradingAccountToken:CThostFtdcCFMMCTradingAccountTokenField):
        self.OnRtnCFMMCTradingAccountToken(copy.deepcopy(POINTER(CThostFtdcCFMMCTradingAccountTokenField).from_param(pCFMMCTradingAccountToken).contents) if pCFMMCTradingAccountToken else CThostFtdcCFMMCTradingAccountTokenField())
    def OnRtnCFMMCTradingAccountToken(self, pCFMMCTradingAccountToken:CThostFtdcCFMMCTradingAccountTokenField):
        """ 保证金监控中心用户令牌 """
        print('===OnRtnCFMMCTradingAccountToken===:pCFMMCTradingAccountToken:CThostFtdcCFMMCTradingAccountTokenField')
    
    def __OnErrRtnBatchOrderAction(self, pBatchOrderAction:CThostFtdcBatchOrderActionField, pRspInfo:CThostFtdcRspInfoField):
        self.OnErrRtnBatchOrderAction(copy.deepcopy(POINTER(CThostFtdcBatchOrderActionField).from_param(pBatchOrderAction).contents) if pBatchOrderAction else CThostFtdcBatchOrderActionField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField())
    def OnErrRtnBatchOrderAction(self, pBatchOrderAction:CThostFtdcBatchOrderActionField, pRspInfo:CThostFtdcRspInfoField):
        """ 批量报单操作错误回报 """
        print('===OnErrRtnBatchOrderAction===:pBatchOrderAction:CThostFtdcBatchOrderActionField, pRspInfo:CThostFtdcRspInfoField')
    
    def __OnRtnOptionSelfClose(self, pOptionSelfClose:CThostFtdcOptionSelfCloseField):
        self.OnRtnOptionSelfClose(copy.deepcopy(POINTER(CThostFtdcOptionSelfCloseField).from_param(pOptionSelfClose).contents) if pOptionSelfClose else CThostFtdcOptionSelfCloseField())
    def OnRtnOptionSelfClose(self, pOptionSelfClose:CThostFtdcOptionSelfCloseField):
        """ 期权自对冲通知 """
        print('===OnRtnOptionSelfClose===:pOptionSelfClose:CThostFtdcOptionSelfCloseField')
    
    def __OnErrRtnOptionSelfCloseInsert(self, pInputOptionSelfClose:CThostFtdcInputOptionSelfCloseField, pRspInfo:CThostFtdcRspInfoField):
        self.OnErrRtnOptionSelfCloseInsert(copy.deepcopy(POINTER(CThostFtdcInputOptionSelfCloseField).from_param(pInputOptionSelfClose).contents) if pInputOptionSelfClose else CThostFtdcInputOptionSelfCloseField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField())
    def OnErrRtnOptionSelfCloseInsert(self, pInputOptionSelfClose:CThostFtdcInputOptionSelfCloseField, pRspInfo:CThostFtdcRspInfoField):
        """ 期权自对冲录入错误回报 """
        print('===OnErrRtnOptionSelfCloseInsert===:pInputOptionSelfClose:CThostFtdcInputOptionSelfCloseField, pRspInfo:CThostFtdcRspInfoField')
    
    def __OnErrRtnOptionSelfCloseAction(self, pOptionSelfCloseAction:CThostFtdcOptionSelfCloseActionField, pRspInfo:CThostFtdcRspInfoField):
        self.OnErrRtnOptionSelfCloseAction(copy.deepcopy(POINTER(CThostFtdcOptionSelfCloseActionField).from_param(pOptionSelfCloseAction).contents) if pOptionSelfCloseAction else CThostFtdcOptionSelfCloseActionField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField())
    def OnErrRtnOptionSelfCloseAction(self, pOptionSelfCloseAction:CThostFtdcOptionSelfCloseActionField, pRspInfo:CThostFtdcRspInfoField):
        """ 期权自对冲操作错误回报 """
        print('===OnErrRtnOptionSelfCloseAction===:pOptionSelfCloseAction:CThostFtdcOptionSelfCloseActionField, pRspInfo:CThostFtdcRspInfoField')
    
    def __OnRtnCombAction(self, pCombAction:CThostFtdcCombActionField):
        self.OnRtnCombAction(copy.deepcopy(POINTER(CThostFtdcCombActionField).from_param(pCombAction).contents) if pCombAction else CThostFtdcCombActionField())
    def OnRtnCombAction(self, pCombAction:CThostFtdcCombActionField):
        """ 申请组合通知 """
        print('===OnRtnCombAction===:pCombAction:CThostFtdcCombActionField')
    
    def __OnErrRtnCombActionInsert(self, pInputCombAction:CThostFtdcInputCombActionField, pRspInfo:CThostFtdcRspInfoField):
        self.OnErrRtnCombActionInsert(copy.deepcopy(POINTER(CThostFtdcInputCombActionField).from_param(pInputCombAction).contents) if pInputCombAction else CThostFtdcInputCombActionField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField())
    def OnErrRtnCombActionInsert(self, pInputCombAction:CThostFtdcInputCombActionField, pRspInfo:CThostFtdcRspInfoField):
        """ 申请组合录入错误回报 """
        print('===OnErrRtnCombActionInsert===:pInputCombAction:CThostFtdcInputCombActionField, pRspInfo:CThostFtdcRspInfoField')
    
    def __OnRspQryContractBank(self, pContractBank:CThostFtdcContractBankField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryContractBank(copy.deepcopy(POINTER(CThostFtdcContractBankField).from_param(pContractBank).contents) if pContractBank else CThostFtdcContractBankField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryContractBank(self, pContractBank:CThostFtdcContractBankField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询签约银行响应 """
        print('===OnRspQryContractBank===:pContractBank:CThostFtdcContractBankField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryParkedOrder(self, pParkedOrder:CThostFtdcParkedOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryParkedOrder(copy.deepcopy(POINTER(CThostFtdcParkedOrderField).from_param(pParkedOrder).contents) if pParkedOrder else CThostFtdcParkedOrderField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryParkedOrder(self, pParkedOrder:CThostFtdcParkedOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询预埋单响应 """
        print('===OnRspQryParkedOrder===:pParkedOrder:CThostFtdcParkedOrderField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryParkedOrderAction(self, pParkedOrderAction:CThostFtdcParkedOrderActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryParkedOrderAction(copy.deepcopy(POINTER(CThostFtdcParkedOrderActionField).from_param(pParkedOrderAction).contents) if pParkedOrderAction else CThostFtdcParkedOrderActionField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryParkedOrderAction(self, pParkedOrderAction:CThostFtdcParkedOrderActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询预埋撤单响应 """
        print('===OnRspQryParkedOrderAction===:pParkedOrderAction:CThostFtdcParkedOrderActionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryTradingNotice(self, pTradingNotice:CThostFtdcTradingNoticeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryTradingNotice(copy.deepcopy(POINTER(CThostFtdcTradingNoticeField).from_param(pTradingNotice).contents) if pTradingNotice else CThostFtdcTradingNoticeField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryTradingNotice(self, pTradingNotice:CThostFtdcTradingNoticeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询交易通知响应 """
        print('===OnRspQryTradingNotice===:pTradingNotice:CThostFtdcTradingNoticeField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryBrokerTradingParams(self, pBrokerTradingParams:CThostFtdcBrokerTradingParamsField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryBrokerTradingParams(copy.deepcopy(POINTER(CThostFtdcBrokerTradingParamsField).from_param(pBrokerTradingParams).contents) if pBrokerTradingParams else CThostFtdcBrokerTradingParamsField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryBrokerTradingParams(self, pBrokerTradingParams:CThostFtdcBrokerTradingParamsField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询经纪公司交易参数响应 """
        print('===OnRspQryBrokerTradingParams===:pBrokerTradingParams:CThostFtdcBrokerTradingParamsField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryBrokerTradingAlgos(self, pBrokerTradingAlgos:CThostFtdcBrokerTradingAlgosField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryBrokerTradingAlgos(copy.deepcopy(POINTER(CThostFtdcBrokerTradingAlgosField).from_param(pBrokerTradingAlgos).contents) if pBrokerTradingAlgos else CThostFtdcBrokerTradingAlgosField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryBrokerTradingAlgos(self, pBrokerTradingAlgos:CThostFtdcBrokerTradingAlgosField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询经纪公司交易算法响应 """
        print('===OnRspQryBrokerTradingAlgos===:pBrokerTradingAlgos:CThostFtdcBrokerTradingAlgosField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQueryCFMMCTradingAccountToken(self, pQueryCFMMCTradingAccountToken:CThostFtdcQueryCFMMCTradingAccountTokenField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQueryCFMMCTradingAccountToken(copy.deepcopy(POINTER(CThostFtdcQueryCFMMCTradingAccountTokenField).from_param(pQueryCFMMCTradingAccountToken).contents) if pQueryCFMMCTradingAccountToken else CThostFtdcQueryCFMMCTradingAccountTokenField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQueryCFMMCTradingAccountToken(self, pQueryCFMMCTradingAccountToken:CThostFtdcQueryCFMMCTradingAccountTokenField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询监控中心用户令牌 """
        print('===OnRspQueryCFMMCTradingAccountToken===:pQueryCFMMCTradingAccountToken:CThostFtdcQueryCFMMCTradingAccountTokenField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRtnFromBankToFutureByBank(self, pRspTransfer:CThostFtdcRspTransferField):
        self.OnRtnFromBankToFutureByBank(copy.deepcopy(POINTER(CThostFtdcRspTransferField).from_param(pRspTransfer).contents) if pRspTransfer else CThostFtdcRspTransferField())
    def OnRtnFromBankToFutureByBank(self, pRspTransfer:CThostFtdcRspTransferField):
        """ 银行发起银行资金转期货通知 """
        print('===OnRtnFromBankToFutureByBank===:pRspTransfer:CThostFtdcRspTransferField')
    
    def __OnRtnFromFutureToBankByBank(self, pRspTransfer:CThostFtdcRspTransferField):
        self.OnRtnFromFutureToBankByBank(copy.deepcopy(POINTER(CThostFtdcRspTransferField).from_param(pRspTransfer).contents) if pRspTransfer else CThostFtdcRspTransferField())
    def OnRtnFromFutureToBankByBank(self, pRspTransfer:CThostFtdcRspTransferField):
        """ 银行发起期货资金转银行通知 """
        print('===OnRtnFromFutureToBankByBank===:pRspTransfer:CThostFtdcRspTransferField')
    
    def __OnRtnRepealFromBankToFutureByBank(self, pRspRepeal:CThostFtdcRspRepealField):
        self.OnRtnRepealFromBankToFutureByBank(copy.deepcopy(POINTER(CThostFtdcRspRepealField).from_param(pRspRepeal).contents) if pRspRepeal else CThostFtdcRspRepealField())
    def OnRtnRepealFromBankToFutureByBank(self, pRspRepeal:CThostFtdcRspRepealField):
        """ 银行发起冲正银行转期货通知 """
        print('===OnRtnRepealFromBankToFutureByBank===:pRspRepeal:CThostFtdcRspRepealField')
    
    def __OnRtnRepealFromFutureToBankByBank(self, pRspRepeal:CThostFtdcRspRepealField):
        self.OnRtnRepealFromFutureToBankByBank(copy.deepcopy(POINTER(CThostFtdcRspRepealField).from_param(pRspRepeal).contents) if pRspRepeal else CThostFtdcRspRepealField())
    def OnRtnRepealFromFutureToBankByBank(self, pRspRepeal:CThostFtdcRspRepealField):
        """ 银行发起冲正期货转银行通知 """
        print('===OnRtnRepealFromFutureToBankByBank===:pRspRepeal:CThostFtdcRspRepealField')
    
    def __OnRtnFromBankToFutureByFuture(self, pRspTransfer:CThostFtdcRspTransferField):
        self.OnRtnFromBankToFutureByFuture(copy.deepcopy(POINTER(CThostFtdcRspTransferField).from_param(pRspTransfer).contents) if pRspTransfer else CThostFtdcRspTransferField())
    def OnRtnFromBankToFutureByFuture(self, pRspTransfer:CThostFtdcRspTransferField):
        """ 期货发起银行资金转期货通知 """
        print('===OnRtnFromBankToFutureByFuture===:pRspTransfer:CThostFtdcRspTransferField')
    
    def __OnRtnFromFutureToBankByFuture(self, pRspTransfer:CThostFtdcRspTransferField):
        self.OnRtnFromFutureToBankByFuture(copy.deepcopy(POINTER(CThostFtdcRspTransferField).from_param(pRspTransfer).contents) if pRspTransfer else CThostFtdcRspTransferField())
    def OnRtnFromFutureToBankByFuture(self, pRspTransfer:CThostFtdcRspTransferField):
        """ 期货发起期货资金转银行通知 """
        print('===OnRtnFromFutureToBankByFuture===:pRspTransfer:CThostFtdcRspTransferField')
    
    def __OnRtnRepealFromBankToFutureByFutureManual(self, pRspRepeal:CThostFtdcRspRepealField):
        self.OnRtnRepealFromBankToFutureByFutureManual(copy.deepcopy(POINTER(CThostFtdcRspRepealField).from_param(pRspRepeal).contents) if pRspRepeal else CThostFtdcRspRepealField())
    def OnRtnRepealFromBankToFutureByFutureManual(self, pRspRepeal:CThostFtdcRspRepealField):
        """ 系统运行时期货端手工发起冲正银行转期货请求，银行处理完毕后报盘发回的通知 """
        print('===OnRtnRepealFromBankToFutureByFutureManual===:pRspRepeal:CThostFtdcRspRepealField')
    
    def __OnRtnRepealFromFutureToBankByFutureManual(self, pRspRepeal:CThostFtdcRspRepealField):
        self.OnRtnRepealFromFutureToBankByFutureManual(copy.deepcopy(POINTER(CThostFtdcRspRepealField).from_param(pRspRepeal).contents) if pRspRepeal else CThostFtdcRspRepealField())
    def OnRtnRepealFromFutureToBankByFutureManual(self, pRspRepeal:CThostFtdcRspRepealField):
        """ 系统运行时期货端手工发起冲正期货转银行请求，银行处理完毕后报盘发回的通知 """
        print('===OnRtnRepealFromFutureToBankByFutureManual===:pRspRepeal:CThostFtdcRspRepealField')
    
    def __OnRtnQueryBankBalanceByFuture(self, pNotifyQueryAccount:CThostFtdcNotifyQueryAccountField):
        self.OnRtnQueryBankBalanceByFuture(copy.deepcopy(POINTER(CThostFtdcNotifyQueryAccountField).from_param(pNotifyQueryAccount).contents) if pNotifyQueryAccount else CThostFtdcNotifyQueryAccountField())
    def OnRtnQueryBankBalanceByFuture(self, pNotifyQueryAccount:CThostFtdcNotifyQueryAccountField):
        """ 期货发起查询银行余额通知 """
        print('===OnRtnQueryBankBalanceByFuture===:pNotifyQueryAccount:CThostFtdcNotifyQueryAccountField')
    
    def __OnErrRtnBankToFutureByFuture(self, pReqTransfer:CThostFtdcReqTransferField, pRspInfo:CThostFtdcRspInfoField):
        self.OnErrRtnBankToFutureByFuture(copy.deepcopy(POINTER(CThostFtdcReqTransferField).from_param(pReqTransfer).contents) if pReqTransfer else CThostFtdcReqTransferField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField())
    def OnErrRtnBankToFutureByFuture(self, pReqTransfer:CThostFtdcReqTransferField, pRspInfo:CThostFtdcRspInfoField):
        """ 期货发起银行资金转期货错误回报 """
        print('===OnErrRtnBankToFutureByFuture===:pReqTransfer:CThostFtdcReqTransferField, pRspInfo:CThostFtdcRspInfoField')
    
    def __OnErrRtnFutureToBankByFuture(self, pReqTransfer:CThostFtdcReqTransferField, pRspInfo:CThostFtdcRspInfoField):
        self.OnErrRtnFutureToBankByFuture(copy.deepcopy(POINTER(CThostFtdcReqTransferField).from_param(pReqTransfer).contents) if pReqTransfer else CThostFtdcReqTransferField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField())
    def OnErrRtnFutureToBankByFuture(self, pReqTransfer:CThostFtdcReqTransferField, pRspInfo:CThostFtdcRspInfoField):
        """ 期货发起期货资金转银行错误回报 """
        print('===OnErrRtnFutureToBankByFuture===:pReqTransfer:CThostFtdcReqTransferField, pRspInfo:CThostFtdcRspInfoField')
    
    def __OnErrRtnRepealBankToFutureByFutureManual(self, pReqRepeal:CThostFtdcReqRepealField, pRspInfo:CThostFtdcRspInfoField):
        self.OnErrRtnRepealBankToFutureByFutureManual(copy.deepcopy(POINTER(CThostFtdcReqRepealField).from_param(pReqRepeal).contents) if pReqRepeal else CThostFtdcReqRepealField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField())
    def OnErrRtnRepealBankToFutureByFutureManual(self, pReqRepeal:CThostFtdcReqRepealField, pRspInfo:CThostFtdcRspInfoField):
        """ 系统运行时期货端手工发起冲正银行转期货错误回报 """
        print('===OnErrRtnRepealBankToFutureByFutureManual===:pReqRepeal:CThostFtdcReqRepealField, pRspInfo:CThostFtdcRspInfoField')
    
    def __OnErrRtnRepealFutureToBankByFutureManual(self, pReqRepeal:CThostFtdcReqRepealField, pRspInfo:CThostFtdcRspInfoField):
        self.OnErrRtnRepealFutureToBankByFutureManual(copy.deepcopy(POINTER(CThostFtdcReqRepealField).from_param(pReqRepeal).contents) if pReqRepeal else CThostFtdcReqRepealField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField())
    def OnErrRtnRepealFutureToBankByFutureManual(self, pReqRepeal:CThostFtdcReqRepealField, pRspInfo:CThostFtdcRspInfoField):
        """ 系统运行时期货端手工发起冲正期货转银行错误回报 """
        print('===OnErrRtnRepealFutureToBankByFutureManual===:pReqRepeal:CThostFtdcReqRepealField, pRspInfo:CThostFtdcRspInfoField')
    
    def __OnErrRtnQueryBankBalanceByFuture(self, pReqQueryAccount:CThostFtdcReqQueryAccountField, pRspInfo:CThostFtdcRspInfoField):
        self.OnErrRtnQueryBankBalanceByFuture(copy.deepcopy(POINTER(CThostFtdcReqQueryAccountField).from_param(pReqQueryAccount).contents) if pReqQueryAccount else CThostFtdcReqQueryAccountField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField())
    def OnErrRtnQueryBankBalanceByFuture(self, pReqQueryAccount:CThostFtdcReqQueryAccountField, pRspInfo:CThostFtdcRspInfoField):
        """ 期货发起查询银行余额错误回报 """
        print('===OnErrRtnQueryBankBalanceByFuture===:pReqQueryAccount:CThostFtdcReqQueryAccountField, pRspInfo:CThostFtdcRspInfoField')
    
    def __OnRtnRepealFromBankToFutureByFuture(self, pRspRepeal:CThostFtdcRspRepealField):
        self.OnRtnRepealFromBankToFutureByFuture(copy.deepcopy(POINTER(CThostFtdcRspRepealField).from_param(pRspRepeal).contents) if pRspRepeal else CThostFtdcRspRepealField())
    def OnRtnRepealFromBankToFutureByFuture(self, pRspRepeal:CThostFtdcRspRepealField):
        """ 期货发起冲正银行转期货请求，银行处理完毕后报盘发回的通知 """
        print('===OnRtnRepealFromBankToFutureByFuture===:pRspRepeal:CThostFtdcRspRepealField')
    
    def __OnRtnRepealFromFutureToBankByFuture(self, pRspRepeal:CThostFtdcRspRepealField):
        self.OnRtnRepealFromFutureToBankByFuture(copy.deepcopy(POINTER(CThostFtdcRspRepealField).from_param(pRspRepeal).contents) if pRspRepeal else CThostFtdcRspRepealField())
    def OnRtnRepealFromFutureToBankByFuture(self, pRspRepeal:CThostFtdcRspRepealField):
        """ 期货发起冲正期货转银行请求，银行处理完毕后报盘发回的通知 """
        print('===OnRtnRepealFromFutureToBankByFuture===:pRspRepeal:CThostFtdcRspRepealField')
    
    def __OnRspFromBankToFutureByFuture(self, pReqTransfer:CThostFtdcReqTransferField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspFromBankToFutureByFuture(copy.deepcopy(POINTER(CThostFtdcReqTransferField).from_param(pReqTransfer).contents) if pReqTransfer else CThostFtdcReqTransferField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspFromBankToFutureByFuture(self, pReqTransfer:CThostFtdcReqTransferField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 期货发起银行资金转期货应答 """
        print('===OnRspFromBankToFutureByFuture===:pReqTransfer:CThostFtdcReqTransferField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspFromFutureToBankByFuture(self, pReqTransfer:CThostFtdcReqTransferField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspFromFutureToBankByFuture(copy.deepcopy(POINTER(CThostFtdcReqTransferField).from_param(pReqTransfer).contents) if pReqTransfer else CThostFtdcReqTransferField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspFromFutureToBankByFuture(self, pReqTransfer:CThostFtdcReqTransferField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 期货发起期货资金转银行应答 """
        print('===OnRspFromFutureToBankByFuture===:pReqTransfer:CThostFtdcReqTransferField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQueryBankAccountMoneyByFuture(self, pReqQueryAccount:CThostFtdcReqQueryAccountField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQueryBankAccountMoneyByFuture(copy.deepcopy(POINTER(CThostFtdcReqQueryAccountField).from_param(pReqQueryAccount).contents) if pReqQueryAccount else CThostFtdcReqQueryAccountField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQueryBankAccountMoneyByFuture(self, pReqQueryAccount:CThostFtdcReqQueryAccountField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 期货发起查询银行余额应答 """
        print('===OnRspQueryBankAccountMoneyByFuture===:pReqQueryAccount:CThostFtdcReqQueryAccountField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRtnOpenAccountByBank(self, pOpenAccount:CThostFtdcOpenAccountField):
        self.OnRtnOpenAccountByBank(copy.deepcopy(POINTER(CThostFtdcOpenAccountField).from_param(pOpenAccount).contents) if pOpenAccount else CThostFtdcOpenAccountField())
    def OnRtnOpenAccountByBank(self, pOpenAccount:CThostFtdcOpenAccountField):
        """ 银行发起银期开户通知 """
        print('===OnRtnOpenAccountByBank===:pOpenAccount:CThostFtdcOpenAccountField')
    
    def __OnRtnCancelAccountByBank(self, pCancelAccount:CThostFtdcCancelAccountField):
        self.OnRtnCancelAccountByBank(copy.deepcopy(POINTER(CThostFtdcCancelAccountField).from_param(pCancelAccount).contents) if pCancelAccount else CThostFtdcCancelAccountField())
    def OnRtnCancelAccountByBank(self, pCancelAccount:CThostFtdcCancelAccountField):
        """ 银行发起银期销户通知 """
        print('===OnRtnCancelAccountByBank===:pCancelAccount:CThostFtdcCancelAccountField')
    
    def __OnRtnChangeAccountByBank(self, pChangeAccount:CThostFtdcChangeAccountField):
        self.OnRtnChangeAccountByBank(copy.deepcopy(POINTER(CThostFtdcChangeAccountField).from_param(pChangeAccount).contents) if pChangeAccount else CThostFtdcChangeAccountField())
    def OnRtnChangeAccountByBank(self, pChangeAccount:CThostFtdcChangeAccountField):
        """ 银行发起变更银行账号通知 """
        print('===OnRtnChangeAccountByBank===:pChangeAccount:CThostFtdcChangeAccountField')
    
    def __OnRspQryClassifiedInstrument(self, pInstrument:CThostFtdcInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryClassifiedInstrument(copy.deepcopy(POINTER(CThostFtdcInstrumentField).from_param(pInstrument).contents) if pInstrument else CThostFtdcInstrumentField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryClassifiedInstrument(self, pInstrument:CThostFtdcInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询分类合约响应 """
        print('===OnRspQryClassifiedInstrument===:pInstrument:CThostFtdcInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryCombPromotionParam(self, pCombPromotionParam:CThostFtdcCombPromotionParamField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryCombPromotionParam(copy.deepcopy(POINTER(CThostFtdcCombPromotionParamField).from_param(pCombPromotionParam).contents) if pCombPromotionParam else CThostFtdcCombPromotionParamField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryCombPromotionParam(self, pCombPromotionParam:CThostFtdcCombPromotionParamField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求组合优惠比例响应 """
        print('===OnRspQryCombPromotionParam===:pCombPromotionParam:CThostFtdcCombPromotionParamField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryRiskSettleInvstPosition(self, pRiskSettleInvstPosition:CThostFtdcRiskSettleInvstPositionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryRiskSettleInvstPosition(copy.deepcopy(POINTER(CThostFtdcRiskSettleInvstPositionField).from_param(pRiskSettleInvstPosition).contents) if pRiskSettleInvstPosition else CThostFtdcRiskSettleInvstPositionField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryRiskSettleInvstPosition(self, pRiskSettleInvstPosition:CThostFtdcRiskSettleInvstPositionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 投资者风险结算持仓查询响应 """
        print('===OnRspQryRiskSettleInvstPosition===:pRiskSettleInvstPosition:CThostFtdcRiskSettleInvstPositionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryRiskSettleProductStatus(self, pRiskSettleProductStatus:CThostFtdcRiskSettleProductStatusField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryRiskSettleProductStatus(copy.deepcopy(POINTER(CThostFtdcRiskSettleProductStatusField).from_param(pRiskSettleProductStatus).contents) if pRiskSettleProductStatus else CThostFtdcRiskSettleProductStatusField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryRiskSettleProductStatus(self, pRiskSettleProductStatus:CThostFtdcRiskSettleProductStatusField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 风险结算产品查询响应 """
        print('===OnRspQryRiskSettleProductStatus===:pRiskSettleProductStatus:CThostFtdcRiskSettleProductStatusField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQrySPBMFutureParameter(self, pSPBMFutureParameter:CThostFtdcSPBMFutureParameterField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQrySPBMFutureParameter(copy.deepcopy(POINTER(CThostFtdcSPBMFutureParameterField).from_param(pSPBMFutureParameter).contents) if pSPBMFutureParameter else CThostFtdcSPBMFutureParameterField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQrySPBMFutureParameter(self, pSPBMFutureParameter:CThostFtdcSPBMFutureParameterField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ SPBM期货合约参数查询响应 """
        print('===OnRspQrySPBMFutureParameter===:pSPBMFutureParameter:CThostFtdcSPBMFutureParameterField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQrySPBMOptionParameter(self, pSPBMOptionParameter:CThostFtdcSPBMOptionParameterField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQrySPBMOptionParameter(copy.deepcopy(POINTER(CThostFtdcSPBMOptionParameterField).from_param(pSPBMOptionParameter).contents) if pSPBMOptionParameter else CThostFtdcSPBMOptionParameterField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQrySPBMOptionParameter(self, pSPBMOptionParameter:CThostFtdcSPBMOptionParameterField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ SPBM期权合约参数查询响应 """
        print('===OnRspQrySPBMOptionParameter===:pSPBMOptionParameter:CThostFtdcSPBMOptionParameterField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQrySPBMIntraParameter(self, pSPBMIntraParameter:CThostFtdcSPBMIntraParameterField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQrySPBMIntraParameter(copy.deepcopy(POINTER(CThostFtdcSPBMIntraParameterField).from_param(pSPBMIntraParameter).contents) if pSPBMIntraParameter else CThostFtdcSPBMIntraParameterField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQrySPBMIntraParameter(self, pSPBMIntraParameter:CThostFtdcSPBMIntraParameterField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ SPBM品种内对锁仓折扣参数查询响应 """
        print('===OnRspQrySPBMIntraParameter===:pSPBMIntraParameter:CThostFtdcSPBMIntraParameterField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQrySPBMInterParameter(self, pSPBMInterParameter:CThostFtdcSPBMInterParameterField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQrySPBMInterParameter(copy.deepcopy(POINTER(CThostFtdcSPBMInterParameterField).from_param(pSPBMInterParameter).contents) if pSPBMInterParameter else CThostFtdcSPBMInterParameterField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQrySPBMInterParameter(self, pSPBMInterParameter:CThostFtdcSPBMInterParameterField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ SPBM跨品种抵扣参数查询响应 """
        print('===OnRspQrySPBMInterParameter===:pSPBMInterParameter:CThostFtdcSPBMInterParameterField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQrySPBMPortfDefinition(self, pSPBMPortfDefinition:CThostFtdcSPBMPortfDefinitionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQrySPBMPortfDefinition(copy.deepcopy(POINTER(CThostFtdcSPBMPortfDefinitionField).from_param(pSPBMPortfDefinition).contents) if pSPBMPortfDefinition else CThostFtdcSPBMPortfDefinitionField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQrySPBMPortfDefinition(self, pSPBMPortfDefinition:CThostFtdcSPBMPortfDefinitionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ SPBM组合保证金套餐查询响应 """
        print('===OnRspQrySPBMPortfDefinition===:pSPBMPortfDefinition:CThostFtdcSPBMPortfDefinitionField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQrySPBMInvestorPortfDef(self, pSPBMInvestorPortfDef:CThostFtdcSPBMInvestorPortfDefField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQrySPBMInvestorPortfDef(copy.deepcopy(POINTER(CThostFtdcSPBMInvestorPortfDefField).from_param(pSPBMInvestorPortfDef).contents) if pSPBMInvestorPortfDef else CThostFtdcSPBMInvestorPortfDefField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQrySPBMInvestorPortfDef(self, pSPBMInvestorPortfDef:CThostFtdcSPBMInvestorPortfDefField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 投资者SPBM套餐选择查询响应 """
        print('===OnRspQrySPBMInvestorPortfDef===:pSPBMInvestorPortfDef:CThostFtdcSPBMInvestorPortfDefField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryInvestorPortfMarginRatio(self, pInvestorPortfMarginRatio:CThostFtdcInvestorPortfMarginRatioField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryInvestorPortfMarginRatio(copy.deepcopy(POINTER(CThostFtdcInvestorPortfMarginRatioField).from_param(pInvestorPortfMarginRatio).contents) if pInvestorPortfMarginRatio else CThostFtdcInvestorPortfMarginRatioField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryInvestorPortfMarginRatio(self, pInvestorPortfMarginRatio:CThostFtdcInvestorPortfMarginRatioField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 投资者新型组合保证金系数查询响应 """
        print('===OnRspQryInvestorPortfMarginRatio===:pInvestorPortfMarginRatio:CThostFtdcInvestorPortfMarginRatioField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspQryInvestorProdSPBMDetail(self, pInvestorProdSPBMDetail:CThostFtdcInvestorProdSPBMDetailField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryInvestorProdSPBMDetail(copy.deepcopy(POINTER(CThostFtdcInvestorProdSPBMDetailField).from_param(pInvestorProdSPBMDetail).contents) if pInvestorProdSPBMDetail else CThostFtdcInvestorProdSPBMDetailField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryInvestorProdSPBMDetail(self, pInvestorProdSPBMDetail:CThostFtdcInvestorProdSPBMDetailField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 投资者产品SPBM明细查询响应 """
        print('===OnRspQryInvestorProdSPBMDetail===:pInvestorProdSPBMDetail:CThostFtdcInvestorProdSPBMDetailField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    