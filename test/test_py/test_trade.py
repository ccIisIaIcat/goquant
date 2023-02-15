#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# LUX et VERITAS
# Create On: 2022/12/13 15:10:10

import os
import sys
from ctypes import *
import platform
import threading
import time
import itertools
import base64

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
import time
from CtpApi.base.enums import (
    OrderType, InstrumentStatus, 
    DirectType, OffsetType, 
    HedgeType, TradeTypeType
)
from CtpApi.base.structs import (
    InfoField, InstrumentField, 
    OrderField, OrderStatus, 
    PositionField, TradeField, 
    TradingAccount, PositionDetail
)
from CtpApi.base.structs import InfoField, Tick

def OnRspQryInstrument(pInstrument, pRspInfo, nRequestID, bIsLast):
    print(pInstrument.ExchangeID.decode("gbk"))
    print(pInstrument.InstrumentName.decode("gbk"))
    print(pInstrument.InstrumentID.decode("gbk"))


if __name__ == "__main__":
    front_trade = 'tcp://180.168.146.187:10202'
    front_quote = 'tcp://180.168.146.187:10212'
    # front_trade = 'tcp://180.168.146.187:10130'
    # front_quote = "tcp://180.168.146.187:10131"
    broker = '9999'
    investor = '008107'
    pwd = '1'
    appid = 'simnow_client_test'
    auth_code = '0000000000000000'

    t = Trade()

    t.OnFrontConnected = lambda : print("Front Connect")
    t.OnRspAuthenticate = lambda pRspAuthenticateField, pRspInfo, nRequestID, bIsLast: print(pRspInfo.ErrorMsg.decode("gbk"))
    t.OnRspUserLogin = lambda pRspUserLogin, pRspInfo, nRequestID, bIsLast: print(pRspInfo.ErrorMsg.decode("gbk"))
    t.OnRspQryInstrument = OnRspQryInstrument
    t.CreateApi()
    t.CreateSpi()

    print("Current System: " + csys)
    print("Trade Api Version: " + t.GetApiVersion())
    print("DataCollect Version: " + t.CTP_GetDataCollectApiVersion())
    pSystemInfo = TThostFtdcClientSystemInfoType()
    nLen = TThostFtdcSystemInfoLenType(273)
    ret = t.CTP_GetSystemInfo(pSystemInfo, nLen)
    print("DataCollect Return:", ret)
    t.RegisterSpi()
    t.RegisterFront(front_trade)
    t.SubscribePrivateTopic(1)
    t.SubscribePublicTopic(1)
    t.Init()
    # 认证
    f = CThostFtdcReqAuthenticateField()
    f.BrokerID = bytes(broker, encoding="ascii")
    f.UserID = bytes(investor, encoding="ascii")
    f.AppID = bytes(appid, encoding="ascii")
    f.AuthCode = bytes(auth_code, encoding="ascii")
    # print(f.value)
    while t.ReqAuthenticate(f, 1) != None:
        print("Retry Auth")
        time.sleep(1)

    f1 = CThostFtdcReqUserLoginField()
    f1.UserID = bytes(investor, encoding="ascii")
    f1.BrokerID = bytes(broker, encoding="ascii")
    f1.Password = bytes(pwd, encoding="ascii")

    ## Macos
    while t.ReqUserLogin(f1, 2) != None:
        print("Retry Login")
        time.sleep(1)
    
    # ## Other
    # while t.ReqUserLogin(f1, 1) != None:
    #     print("Retry Login")
    #     time.sleep(1)

    f5 = CThostFtdcQryInstrumentField()
    while t.ReqQryInstrument(f5, 2) != None:
        print("Retry")
        time.sleep(1)

    input()
