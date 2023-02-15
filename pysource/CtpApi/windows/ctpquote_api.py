#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# LUX et VERITAS
# Create On: 2022/12/13 13:21:04

import os
import copy
import platform
from ctypes import *
from .ctp_struct import *


class Quote(object):

    def __init__(self, logdir="./log/") -> None:
        dllpath = os.path.join(os.path.abspath(os.path.dirname(__file__)), "../../../libs/ctpapi")
        if "Windows" in platform.system():
            dln = "ctpquote_api.dll"
        elif "Linux" in platform.system():
            dln = "libctpquote_api.so"
        elif "Darwin" in platform.system():
            dln = "libctpquote_api.dylib"
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

        self.h.qCreateApi.argtypes = [c_char_p, c_bool, c_bool]
        self.h.qCreateApi.restype = c_void_p

        self.h.qCreateSpi.argtypes = []
        self.h.qCreateSpi.restype = c_void_p

        self.h.qGetApiVersion.argtypes = []
        self.h.qGetApiVersion.restype = c_char_p

        self.h.qGetTradingDay.argtypes = [c_void_p]
        self.h.qGetTradingDay.restype = c_char_p

        self.api = None
        self.pSpi = None

        #################### 请求函数 #######################
        # 创建MdApi
        self.h.qRelease.argtypes = [c_void_p]
        self.h.qRelease.restype = c_void_p
        # 初始化
        self.h.qInit.argtypes = [c_void_p]
        self.h.qInit.restype = c_void_p
        # 等待接口线程结束运行
        self.h.qJoin.argtypes = [c_void_p]
        self.h.qJoin.restype = c_void_p
        # 注册前置机网络地址
        self.h.qRegisterFront.argtypes = [c_void_p, c_void_p]
        self.h.qRegisterFront.restype = c_void_p
        # @remark RegisterNameServer优先于RegisterFront
        self.h.qRegisterNameServer.argtypes = [c_void_p, c_void_p]
        self.h.qRegisterNameServer.restype = c_void_p
        # 注册名字服务器用户信息
        self.h.qRegisterFensUserInfo.argtypes = [c_void_p, c_void_p]
        self.h.qRegisterFensUserInfo.restype = c_void_p
        # 注册回调接口
        self.h.qRegisterSpi.argtypes = [c_void_p, c_void_p]
        self.h.qRegisterSpi.restype = c_void_p
        # 订阅行情。
        self.h.qSubscribeMarketData.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.qSubscribeMarketData.restype = c_void_p
        # 退订行情。
        self.h.qUnSubscribeMarketData.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.qUnSubscribeMarketData.restype = c_void_p
        # 订阅询价。
        self.h.qSubscribeForQuoteRsp.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.qSubscribeForQuoteRsp.restype = c_void_p
        # 退订询价。
        self.h.qUnSubscribeForQuoteRsp.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.qUnSubscribeForQuoteRsp.restype = c_void_p
        # 用户登录请求
        self.h.qReqUserLogin.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.qReqUserLogin.restype = c_void_p
        # 登出请求
        self.h.qReqUserLogout.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.qReqUserLogout.restype = c_void_p
        # 请求查询组播合约
        self.h.qReqQryMulticastInstrument.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.qReqQryMulticastInstrument.restype = c_void_p
        
        os.chdir(cur_path)

    def CreateApi(self):
        self.api = self.h.qCreateApi(c_char_p(self.logdir.encode("utf-8")), c_bool(False), c_bool(False))

    def CreateSpi(self):
        self.pSpi = self.h.qCreateSpi()
        #################### 响应函数 #########################
        # 当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。
        self.h.qOnFrontConnected.argtypes = [c_void_p, c_void_p]
        self.h.qOnFrontConnected.restype = None
        self.FP_OnFrontConnected = CFUNCTYPE(None)(self.__OnFrontConnected)
        self.h.qOnFrontConnected(self.pSpi, self.FP_OnFrontConnected)
        # 当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。
        self.h.qOnFrontDisconnected.argtypes = [c_void_p, c_void_p]
        self.h.qOnFrontDisconnected.restype = None
        self.FP_OnFrontDisconnected = CFUNCTYPE(None, c_int32)(self.__OnFrontDisconnected)
        self.h.qOnFrontDisconnected(self.pSpi, self.FP_OnFrontDisconnected)
        # 心跳超时警告。当长时间未收到报文时，该方法被调用。
        self.h.qOnHeartBeatWarning.argtypes = [c_void_p, c_void_p]
        self.h.qOnHeartBeatWarning.restype = None
        self.FP_OnHeartBeatWarning = CFUNCTYPE(None, c_int32)(self.__OnHeartBeatWarning)
        self.h.qOnHeartBeatWarning(self.pSpi, self.FP_OnHeartBeatWarning)
        # 登录请求响应
        self.h.qOnRspUserLogin.argtypes = [c_void_p, c_void_p]
        self.h.qOnRspUserLogin.restype = None
        self.FP_OnRspUserLogin = CFUNCTYPE(None, POINTER(CThostFtdcRspUserLoginField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspUserLogin)
        self.h.qOnRspUserLogin(self.pSpi, self.FP_OnRspUserLogin)
        # 登出请求响应
        self.h.qOnRspUserLogout.argtypes = [c_void_p, c_void_p]
        self.h.qOnRspUserLogout.restype = None
        self.FP_OnRspUserLogout = CFUNCTYPE(None, POINTER(CThostFtdcUserLogoutField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspUserLogout)
        self.h.qOnRspUserLogout(self.pSpi, self.FP_OnRspUserLogout)
        # 请求查询组播合约响应
        self.h.qOnRspQryMulticastInstrument.argtypes = [c_void_p, c_void_p]
        self.h.qOnRspQryMulticastInstrument.restype = None
        self.FP_OnRspQryMulticastInstrument = CFUNCTYPE(None, POINTER(CThostFtdcMulticastInstrumentField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryMulticastInstrument)
        self.h.qOnRspQryMulticastInstrument(self.pSpi, self.FP_OnRspQryMulticastInstrument)
        # 错误应答
        self.h.qOnRspError.argtypes = [c_void_p, c_void_p]
        self.h.qOnRspError.restype = None
        self.FP_OnRspError = CFUNCTYPE(None, POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspError)
        self.h.qOnRspError(self.pSpi, self.FP_OnRspError)
        # 订阅行情应答
        self.h.qOnRspSubMarketData.argtypes = [c_void_p, c_void_p]
        self.h.qOnRspSubMarketData.restype = None
        self.FP_OnRspSubMarketData = CFUNCTYPE(None, POINTER(CThostFtdcSpecificInstrumentField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspSubMarketData)
        self.h.qOnRspSubMarketData(self.pSpi, self.FP_OnRspSubMarketData)
        # 取消订阅行情应答
        self.h.qOnRspUnSubMarketData.argtypes = [c_void_p, c_void_p]
        self.h.qOnRspUnSubMarketData.restype = None
        self.FP_OnRspUnSubMarketData = CFUNCTYPE(None, POINTER(CThostFtdcSpecificInstrumentField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspUnSubMarketData)
        self.h.qOnRspUnSubMarketData(self.pSpi, self.FP_OnRspUnSubMarketData)
        # 订阅询价应答
        self.h.qOnRspSubForQuoteRsp.argtypes = [c_void_p, c_void_p]
        self.h.qOnRspSubForQuoteRsp.restype = None
        self.FP_OnRspSubForQuoteRsp = CFUNCTYPE(None, POINTER(CThostFtdcSpecificInstrumentField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspSubForQuoteRsp)
        self.h.qOnRspSubForQuoteRsp(self.pSpi, self.FP_OnRspSubForQuoteRsp)
        # 取消订阅询价应答
        self.h.qOnRspUnSubForQuoteRsp.argtypes = [c_void_p, c_void_p]
        self.h.qOnRspUnSubForQuoteRsp.restype = None
        self.FP_OnRspUnSubForQuoteRsp = CFUNCTYPE(None, POINTER(CThostFtdcSpecificInstrumentField), POINTER(CThostFtdcRspInfoField), c_int32, c_bool)(self.__OnRspUnSubForQuoteRsp)
        self.h.qOnRspUnSubForQuoteRsp(self.pSpi, self.FP_OnRspUnSubForQuoteRsp)
        # 深度行情通知
        self.h.qOnRtnDepthMarketData.argtypes = [c_void_p, c_void_p]
        self.h.qOnRtnDepthMarketData.restype = None
        self.FP_OnRtnDepthMarketData = CFUNCTYPE(None, POINTER(CThostFtdcDepthMarketDataField))(self.__OnRtnDepthMarketData)
        self.h.qOnRtnDepthMarketData(self.pSpi, self.FP_OnRtnDepthMarketData)
        # 询价通知
        self.h.qOnRtnForQuoteRsp.argtypes = [c_void_p, c_void_p]
        self.h.qOnRtnForQuoteRsp.restype = None
        self.FP_OnRtnForQuoteRsp = CFUNCTYPE(None, POINTER(CThostFtdcForQuoteRspField))(self.__OnRtnForQuoteRsp)
        self.h.qOnRtnForQuoteRsp(self.pSpi, self.FP_OnRtnForQuoteRsp)
        

    def GetApiVersion(self):
        v = str(self.h.qGetApiVersion(), encoding="utf-8")
        return str(v)

    def GetTradingDay(self):
        v = str(self.h.qGetTradingDay(self.api), encoding="utf-8")
        return str(v)

    #################### 请求函数 #######################
    
    def Release(self): 
        """ 创建MdApi """
        self.h.qRelease(self.api)  
    
    def Init(self): 
        """ 初始化 """
        self.h.qInit(self.api)  
    
    def Join(self): 
        """ 等待接口线程结束运行 """
        return self.h.qJoin(self.api)  
    
    def RegisterFront(self, pszFrontAddress:str): 
        """ 注册前置机网络地址 """
        self.h.qRegisterFront(self.api, bytes(pszFrontAddress, encoding='ascii'))  
    
    def RegisterNameServer(self, pszNsAddress:str): 
        """ @remark RegisterNameServer优先于RegisterFront """
        self.h.qRegisterNameServer(self.api, bytes(pszNsAddress, encoding='ascii'))  
    
    def RegisterFensUserInfo(self,  pFensUserInfo:CThostFtdcFensUserInfoField): 
        """ 注册名字服务器用户信息 """
        self.h.qRegisterFensUserInfo(self.api, byref( pFensUserInfo))  
    
    def RegisterSpi(self): 
        """ 注册回调接口 """
        self.h.qRegisterSpi(self.api, self.pSpi)  
    
    def SubscribeMarketData(self, ppInstrumentID:str, nCount:int): 
        """ 订阅行情。 """
        return self.h.qSubscribeMarketData(self.api, ppInstrumentID, nCount)  
    
    def UnSubscribeMarketData(self, ppInstrumentID:str, nCount:int): 
        """ 退订行情。 """
        return self.h.qUnSubscribeMarketData(self.api, ppInstrumentID, nCount)  
    
    def SubscribeForQuoteRsp(self, ppInstrumentID:str, nCount:int): 
        """ 订阅询价。 """
        return self.h.qSubscribeForQuoteRsp(self.api, ppInstrumentID, nCount)  
    
    def UnSubscribeForQuoteRsp(self, ppInstrumentID:str, nCount:int): 
        """ 退订询价。 """
        return self.h.qUnSubscribeForQuoteRsp(self.api, ppInstrumentID, nCount)  
    
    def ReqUserLogin(self, pReqUserLoginField:CThostFtdcReqUserLoginField, nRequestID:int): 
        """ 用户登录请求 """
        return self.h.qReqUserLogin(self.api, byref(pReqUserLoginField), nRequestID)  
    
    def ReqUserLogout(self, pUserLogout:CThostFtdcUserLogoutField, nRequestID:int): 
        """ 登出请求 """
        return self.h.qReqUserLogout(self.api, byref(pUserLogout), nRequestID)  
    
    def ReqQryMulticastInstrument(self, pQryMulticastInstrument:CThostFtdcQryMulticastInstrumentField, nRequestID:int): 
        """ 请求查询组播合约 """
        return self.h.qReqQryMulticastInstrument(self.api, byref(pQryMulticastInstrument), nRequestID)  
    
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
    
    def __OnRspQryMulticastInstrument(self, pMulticastInstrument:CThostFtdcMulticastInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspQryMulticastInstrument(copy.deepcopy(POINTER(CThostFtdcMulticastInstrumentField).from_param(pMulticastInstrument).contents) if pMulticastInstrument else CThostFtdcMulticastInstrumentField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspQryMulticastInstrument(self, pMulticastInstrument:CThostFtdcMulticastInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 请求查询组播合约响应 """
        print('===OnRspQryMulticastInstrument===:pMulticastInstrument:CThostFtdcMulticastInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspError(self, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspError(copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspError(self, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 错误应答 """
        print('===OnRspError===:pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspSubMarketData(self, pSpecificInstrument:CThostFtdcSpecificInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspSubMarketData(copy.deepcopy(POINTER(CThostFtdcSpecificInstrumentField).from_param(pSpecificInstrument).contents) if pSpecificInstrument else CThostFtdcSpecificInstrumentField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspSubMarketData(self, pSpecificInstrument:CThostFtdcSpecificInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 订阅行情应答 """
        print('===OnRspSubMarketData===:pSpecificInstrument:CThostFtdcSpecificInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspUnSubMarketData(self, pSpecificInstrument:CThostFtdcSpecificInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspUnSubMarketData(copy.deepcopy(POINTER(CThostFtdcSpecificInstrumentField).from_param(pSpecificInstrument).contents) if pSpecificInstrument else CThostFtdcSpecificInstrumentField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspUnSubMarketData(self, pSpecificInstrument:CThostFtdcSpecificInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 取消订阅行情应答 """
        print('===OnRspUnSubMarketData===:pSpecificInstrument:CThostFtdcSpecificInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspSubForQuoteRsp(self, pSpecificInstrument:CThostFtdcSpecificInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspSubForQuoteRsp(copy.deepcopy(POINTER(CThostFtdcSpecificInstrumentField).from_param(pSpecificInstrument).contents) if pSpecificInstrument else CThostFtdcSpecificInstrumentField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspSubForQuoteRsp(self, pSpecificInstrument:CThostFtdcSpecificInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 订阅询价应答 """
        print('===OnRspSubForQuoteRsp===:pSpecificInstrument:CThostFtdcSpecificInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRspUnSubForQuoteRsp(self, pSpecificInstrument:CThostFtdcSpecificInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        self.OnRspUnSubForQuoteRsp(copy.deepcopy(POINTER(CThostFtdcSpecificInstrumentField).from_param(pSpecificInstrument).contents) if pSpecificInstrument else CThostFtdcSpecificInstrumentField(), copy.deepcopy(POINTER(CThostFtdcRspInfoField).from_param(pRspInfo).contents) if pRspInfo else CThostFtdcRspInfoField(), nRequestID, bIsLast)
    def OnRspUnSubForQuoteRsp(self, pSpecificInstrument:CThostFtdcSpecificInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool):
        """ 取消订阅询价应答 """
        print('===OnRspUnSubForQuoteRsp===:pSpecificInstrument:CThostFtdcSpecificInstrumentField, pRspInfo:CThostFtdcRspInfoField, nRequestID:int, bIsLast:bool')
    
    def __OnRtnDepthMarketData(self, pDepthMarketData:CThostFtdcDepthMarketDataField):
        self.OnRtnDepthMarketData(copy.deepcopy(POINTER(CThostFtdcDepthMarketDataField).from_param(pDepthMarketData).contents) if pDepthMarketData else CThostFtdcDepthMarketDataField())
    def OnRtnDepthMarketData(self, pDepthMarketData:CThostFtdcDepthMarketDataField):
        """ 深度行情通知 """
        print('===OnRtnDepthMarketData===:pDepthMarketData:CThostFtdcDepthMarketDataField')
    
    def __OnRtnForQuoteRsp(self, pForQuoteRsp:CThostFtdcForQuoteRspField):
        self.OnRtnForQuoteRsp(copy.deepcopy(POINTER(CThostFtdcForQuoteRspField).from_param(pForQuoteRsp).contents) if pForQuoteRsp else CThostFtdcForQuoteRspField())
    def OnRtnForQuoteRsp(self, pForQuoteRsp:CThostFtdcForQuoteRspField):
        """ 询价通知 """
        print('===OnRtnForQuoteRsp===:pForQuoteRsp:CThostFtdcForQuoteRspField')
    