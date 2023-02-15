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
        [[ range .Fn ]]# [[ .Comment ]]
        self.h.q[[ .FuncName ]].argtypes = [c_void_p[[ range .FuncFields ]], [[ .FieldType|baseType ]][[ end ]]]
        self.h.q[[ .FuncName ]].restype = c_void_p
        [[ end ]]
        os.chdir(cur_path)

    def CreateApi(self):
        self.api = self.h.qCreateApi(c_char_p(self.logdir.encode("utf-8")), c_bool(False), c_bool(False))

    def CreateSpi(self):
        self.pSpi = self.h.qCreateSpi()
        #################### 响应函数 #########################
        [[ range .On ]]# [[ .Comment ]]
        self.h.q[[ .FuncName ]].argtypes = [c_void_p, c_void_p]
        self.h.q[[ .FuncName ]].restype = None
        self.FP_[[ .FuncName ]] = CFUNCTYPE(None[[ range $i,$v := .FuncFields ]], [[ .FieldType|evBaseType ]][[ end ]])(self.__[[ .FuncName ]])
        self.h.q[[ .FuncName ]](self.pSpi, self.FP_[[ .FuncName ]])
        [[ end ]]

    def GetApiVersion(self):
        v = str(self.h.qGetApiVersion(), encoding="utf-8")
        return str(v)

    def GetTradingDay(self):
        v = str(self.h.qGetTradingDay(self.api), encoding="utf-8")
        return str(v)

    #################### 请求函数 #######################
    [[ range .Fn ]][[ if eq .FuncName "RegisterSpi"]]
    def [[ .FuncName ]](self): [[ else ]]
    def [[ .FuncName ]](self[[ range .FuncFields ]], [[ .FieldName|trimStar ]]:[[.FieldType|fnBaseType]][[ end ]]): [[ end ]]
        """ [[ .Comment ]] """[[ if eq .FuncRtn "void"]]
        self.h.q[[ .FuncName ]](self.api[[ range .FuncFields ]], [[ param .FieldType (.FieldName|trimStar) ]][[ end ]]) [[ else ]]
        return self.h.q[[ .FuncName ]](self.api[[ range .FuncFields ]], [[ param .FieldType (.FieldName|trimStar) ]][[ end ]]) [[ end ]] 
    [[ end ]]
    #################### 响应函数 #########################
    [[ range .On ]]
    def __[[ .FuncName ]](self[[ range .FuncFields ]], [[ .FieldName|trimStar ]]:[[.FieldType|fnBaseType]][[ end ]]):
        self.[[ .FuncName ]]([[ range $i,$v := .FuncFields ]][[if gt $i 0]], [[ end ]][[ onParam .FieldType (.FieldName|trimStar) ]][[ end ]])
    def [[ .FuncName ]](self[[ range .FuncFields ]], [[ .FieldName|trimStar ]]:[[.FieldType|fnBaseType]][[ end ]]):
        """ [[ .Comment ]] """
        print('===[[ .FuncName ]]===:[[ range $i,$v := .FuncFields ]][[if gt $i 0]], [[ end ]][[ .FieldName|trimStar ]]:[[.FieldType|fnBaseType]][[ end ]]')
    [[ end ]]