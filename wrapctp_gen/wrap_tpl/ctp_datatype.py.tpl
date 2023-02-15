#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# LUX et VERITAS
# Create On: 2022/12/12 14:16:31

from enum import Enum
from ctypes import c_int32, c_double, c_char, c_short

# 自定义Python的Constant声明方式
class _const:
    def __setattr__(self, name, value):
        if self.__dict__.__contains__(name):
            raise Exception(f"Can't reassignment constant {name}")
        self.__dict__[name]=value

const =_const()

class THOST_TE_RESUME_TYPE(Enum):
    THOST_TERT_RESTART = 0
    THOST_TERT_RESUME = 1
    THOST_TERT_QUICK = 2
    THOST_TERT_NONE = 3
[[/*处理枚举*/]]
[[ range .]][[ if gt (len .FuncFields) 0]]
[[ .FuncName ]] = [[ .FuncTypeName|baseType ]]
"""[[ .Comment ]]"""
[[ range .FuncFields ]]
const.[[ .FieldType ]] = "[[ .FieldName ]]"
"""[[ .Comment ]]"""    [[ end ]]
[[ else]][[/*自定义类型*/]]
[[ .FuncName ]] = [[ .FuncTypeName|baseType ]]
"""[[ .Comment ]]"""[[ end ]]
[[ end ]]