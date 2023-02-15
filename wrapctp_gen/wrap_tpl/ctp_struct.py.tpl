#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# LUX et VERITAS
# Create On: 2022/12/12 20:37:58


from ctypes import Structure
from .ctp_datatype import *

[[ range .]]
class  [[ .FuncTypeName ]](Structure):
    """[[ .Comment ]]"""
    _fields_ = [
        [[ range .FuncFields ]]("[[ .FieldName ]]", [[ .FieldType|baseType ]]),
        [[ end ]]
    ]
    [[ end ]]