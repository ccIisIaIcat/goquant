#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# LUX et VERITAS
# Create On: 2022/12/13 15:10:10

import os
import sys
from ctypes import *
import platform
import threading

sys.path.append("../../pysource/")
csys = platform.system()

if csys == "Darwin":
    from CtpApi.macos.ctp_datatype import *
    from CtpApi.macos.ctp_struct import *
    from CtpApi.macos.ctpquote_api import *
    from CtpApi.macos.ctptrade_api import *
elif csys == "Windows":
    from CtpApi.windows.ctp_datatype import *
    from CtpApi.windows.ctp_struct import *
    from CtpApi.windows.ctpquote_api import *
    from CtpApi.windows.ctptrade_api import *
elif csys == "Linux":
    from CtpApi.linux.ctp_datatype import *
    from CtpApi.linux.ctp_struct import *
    from CtpApi.linux.ctpquote_api import *
    from CtpApi.linux.ctptrade_api import *

from CtpApi.base.structs import InfoField, Tick

class CtpQuote(object):
    """"""

    def __init__(self):
        self.q = Quote()
        self.inst_tick = {}
        self.logined = False
        self.nRequestID = 0

    def ReqConnect(self, pAddress: str):
        """连接行情前置

        :param pAddress:
        """
        self.q.CreateApi()
        self.q.CreateSpi()
        self.q.RegisterSpi()

        self.q.OnFrontConnected = self._OnFrontConnected
        self.q.OnFrontDisconnected = self._OnFrontDisConnected
        self.q.OnRspUserLogin = self._OnRspUserLogin
        self.q.OnRtnDepthMarketData = self._OnRtnDepthMarketData
        self.q.OnRspSubMarketData = self._OnRspSubMarketData

        self.q.RegisterFront(pAddress)
        self.q.Init()

    def ReqUserLogout(self):
        """退出接口(正常退出,不会触发OnFrontDisconnected)"""
        self.q.Release()
        # 确保隔夜或重新登录时的第1个tick不被发送到客户端
        self.inst_tick.clear()
        self.logined = False
        threading.Thread(target=self.OnDisConnected, args=(self, 0)).start()

    def ReqUserLogin(self, user: str, pwd: str, broker: str):
        """登录

        :param user:
        :param pwd:
        :param broker:
        """
        f = CThostFtdcReqUserLoginField()
        f.BrokerID = bytes(broker, encoding='ascii')
        f.UserID = bytes(user, encoding='ascii')
        f.Password = bytes(pwd, encoding='ascii')
        f.UserProductInfo = bytes("@hf", encoding='ascii')
        self.nRequestID += 1
        self.q.ReqUserLogin(f, self.nRequestID)

    def ReqSubscribeMarketData(self, pInstrument: list):
        """订阅合约行情

        :param pInstrument: 行情列表
        """
        inst_p = (c_char_p * len(pInstrument))()
        for x in range(len(pInstrument)):
            inst_p[x] = bytes(pInstrument[x], encoding='ascii')
        self.q.SubscribeMarketData(inst_p, len(pInstrument))

    def _OnFrontConnected(self):
        """"""
        threading.Thread(target=self.OnConnected, args=(self,)).start()

    def _OnFrontDisConnected(self, reason: int):
        """"""
        # 确保隔夜或重新登录时的第1个tick不被发送到客户端
        self.inst_tick.clear()
        self.logined = False
        threading.Thread(target=self.OnDisConnected, args=(self, reason)).start()

    def _OnRspUserLogin(self, pRspUserLogin: CThostFtdcRspUserLoginField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        """"""
        info = InfoField()
        info.ErrorID = pRspInfo.ErrorID
        info.ErrorMsg = pRspInfo.ErrorMsg
        self.logined = True
        threading.Thread(target=self.OnUserLogin, args=(self, info)).start()

    def _OnRspSubMarketData(self, pSpecificInstrument: CThostFtdcSpecificInstrumentField, pRspInfo: CThostFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        pass

    def _OnRtnDepthMarketData(self, pDepthMarketData: CThostFtdcDepthMarketDataField):
        """"""
        tick: Tick = None
        # 这个逻辑交由应用端处理更合理 ==> 第一个tick不送给客户端(以处理隔夜早盘时收到夜盘的数据的问题)
        inst = pDepthMarketData.InstrumentID
        if inst not in self.inst_tick:
            tick = Tick()
            self.inst_tick[inst] = tick
        else:
            tick = self.inst_tick[inst]

        tick.AskPrice = pDepthMarketData.AskPrice1
        tick.AskVolume = pDepthMarketData.AskVolume1
        tick.AveragePrice = pDepthMarketData.AveragePrice
        tick.BidPrice = pDepthMarketData.BidPrice1
        tick.BidVolume = pDepthMarketData.BidVolume1
        tick.Instrument = pDepthMarketData.InstrumentID
        tick.LastPrice = pDepthMarketData.LastPrice
        tick.OpenInterest = pDepthMarketData.OpenInterest
        tick.Volume = pDepthMarketData.Volume

        # 用tradingday替代Actionday不可取
        # day = pDepthMarketData.TradingDay
        # str = day + ' ' + pDepthMarketData.UpdateTime
        # if day is None or day == ' ':
        #     str = time.strftime('%Y%m%d %H:%M:%S', time.localtime())
        # tick.UpdateTime = str  # time.strptime(str, '%Y%m%d %H:%M:%S')

        tick.UpdateTime = pDepthMarketData.UpdateTime
        tick.UpdateMillisec = pDepthMarketData.UpdateMillisec
        tick.UpperLimitPrice = pDepthMarketData.UpperLimitPrice
        tick.LowerLimitPrice = pDepthMarketData.LowerLimitPrice
        tick.PreOpenInterest = pDepthMarketData.PreOpenInterest

        # 用线程会导入多数据入库时报错
        # threading.Thread(target=self.OnTick, args=(self, tick))
        self.OnTick(self, tick)

    def OnDisConnected(self, obj, error: int):
        """"""
        print(f'=== [QUOTE] OnDisConnected===\nerror: {str(error)}')

    def OnConnected(self, obj):
        """"""
        print('=== [QUOTE] OnConnected ===')

    def OnUserLogin(self, obj, info: InfoField):
        """"""
        print(f'=== [QUOTE] OnUserLogin ===\n{info}')

    def OnTick(self, obj, f: Tick):
        """"""
        print(f'=== [QUOTE] OnTick ===\n{f.__dict__}')

    def GetApiVersion(self):
        print(self.q.GetApiVersion())
    
    def Release(self):
        self.q.Release()

def connected(obj):
    print('connected')
    obj.ReqUserLogin('008105', '1', '9999')


def logged(obj, info):
    print(info)


def connected(obj):
    print('connected')
    obj.ReqUserLogin('008105', '1', '9999')


def logged(obj, info):
    print(info)

def onLogin(obj, info):
    print(info)
    obj.ReqSubscribeMarketData(["rb2305"])

def main():
    q = CtpQuote()
    q.OnConnected = lambda obj: q.ReqUserLogin("008105", "1", "9999")
    q.OnUserLogin = onLogin
    q.OnTick = lambda obj, t : print(t)
    q.ReqConnect('tcp://180.168.146.187:10131')   # tcp://180.168.146.187:10212  tcp://180.168.146.187:10131
    q.GetApiVersion()
    input()
    q.Release()
    input()


if __name__ == '__main__':
    main()