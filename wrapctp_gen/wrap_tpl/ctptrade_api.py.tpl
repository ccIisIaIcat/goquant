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
[[if eq .Pf "macos"]]
        self.h.dCTP_GetSystemInfoUnAesEncode.argtypes = [c_char_p, c_int]
        self.h.dCTP_GetSystemInfoUnAesEncode.restype = c_int
[[end]]
        self.h.dCTP_GetDataCollectApiVersion.argtypes = []
        self.h.dCTP_GetDataCollectApiVersion.restype = c_char_p

        self.api = None
        self.pSpi = None

        #################### 请求函数 #######################
        [[ range .Fn ]]# [[ .Comment ]]
        self.h.t[[ .FuncName ]].argtypes = [c_void_p[[ range .FuncFields ]], [[ .FieldType|baseType ]][[ end ]]]
        self.h.t[[ .FuncName ]].restype = c_void_p
        [[ end ]]
        os.chdir(cur_path)

    def CreateApi(self):
        self.api = self.h.tCreateApi(c_char_p(self.logdir.encode("utf-8")))

    def CreateSpi(self):
        self.pSpi = self.h.tCreateSpi()
        #################### 响应函数 #########################
        [[ range .On ]]# [[ .Comment ]]
        self.h.t[[ .FuncName ]].argtypes = [c_void_p, c_void_p]
        self.h.t[[ .FuncName ]].restype = None
        self.FP_[[ .FuncName ]] = CFUNCTYPE(None[[ range $i,$v := .FuncFields ]], [[ .FieldType|evBaseType ]][[ end ]])(self.__[[ .FuncName ]])
        self.h.t[[ .FuncName ]](self.pSpi, self.FP_[[ .FuncName ]])
        [[ end ]]

    def GetApiVersion(self):
        v = str(self.h.tGetApiVersion(), encoding="utf-8")
        return str(v)

    def GetTradingDay(self):
        v = str(self.h.tGetTradingDay(self.api), encoding="utf-8")
        return str(v)

    def CTP_GetSystemInfo(self, pSystemInfo:TThostFtdcClientSystemInfoType, nLen:TThostFtdcSystemInfoLenType):
        res = self.h.dCTP_GetSystemInfo(pSystemInfo, nLen)
        return res
[[if eq .Pf "macos"]]
    def CTP_GetSystemInfoUnAesEncode(self, pSystemInfo:TThostFtdcClientSystemInfoType, nLen:TThostFtdcSystemInfoLenType):
        res = self.h.dCTP_GetSystemInfoUnAesEncode(pSystemInfo, nLen)
        return res
[[end]]
    def CTP_GetDataCollectApiVersion(self):
        v = str(self.h.dCTP_GetDataCollectApiVersion(), encoding="utf-8")
        return v
    #################### 请求函数 #######################
    [[ range .Fn ]][[ if eq .FuncName "RegisterSpi"]]
    def [[ .FuncName ]](self): [[ else if eq .FuncName "ReqUserLogin" ]]
    def [[ .FuncName ]](self[[ range $i,$v := .FuncFields ]][[ if lt $i 2 ]], [[ .FieldName|trimStar ]]:[[.FieldType|fnBaseType]][[ end ]][[ end ]]): [[ else ]]
    def [[ .FuncName ]](self[[ range .FuncFields ]], [[ .FieldName|trimStar ]]:[[.FieldType|fnBaseType]][[ end ]]): [[ end ]]
        """ [[ .Comment ]] """[[ if eq .FuncRtn "void"]]
        self.h.t[[ .FuncName ]](self.api[[ range .FuncFields ]], [[ param .FieldType (.FieldName|trimStar) ]][[ end ]])[[ else ]] [[ if eq $.Pf "macos"]][[if eq .FuncName "ReqUserLogin"]]
        systemInfo = TThostFtdcClientSystemInfoType()
        length = TThostFtdcSystemInfoLenType(273)
        self.CTP_GetSystemInfoUnAesEncode(systemInfo, length)
        systemInfo = systemInfo.value
        length = length.value[[end]][[end]]
        return self.h.t[[ .FuncName ]](self.api[[ range .FuncFields ]], [[ param .FieldType (.FieldName|trimStar) ]][[ end ]]) [[ end ]]
    [[ end ]]
    #################### 响应函数 #########################
    [[ range .On ]]
    def __[[ .FuncName ]](self[[ range .FuncFields ]], [[ .FieldName|trimStar ]]:[[.FieldType|fnBaseType]][[ end ]]):
        self.[[ .FuncName ]]([[ range $i,$v := .FuncFields ]][[if gt $i 0]], [[ end ]][[ onParam .FieldType (.FieldName|trimStar) ]][[ end ]])
    def [[ .FuncName ]](self[[ range .FuncFields ]], [[ .FieldName|trimStar ]]:[[.FieldType|fnBaseType]][[ end ]]):
        """ [[ .Comment ]] """
        print('===[[ .FuncName ]]===:[[ range $i,$v := .FuncFields ]][[if gt $i 0]], [[ end ]][[ .FieldName|trimStar ]]:[[.FieldType|fnBaseType]][[ end ]]')
    [[ end ]]