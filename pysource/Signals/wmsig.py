#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# LUX et VERITAS
# Create On: 2022/11/09 10:18:40

from Signals._zzsig import ZZSignal


class WMSignal(ZZSignal):
    """W/M Signal
    
    Usage:
    >>> zzso = WMSignal(5)  # 对于每个品种，首先实例化ZZSignal。
    >>> for cur_zigzag, cur_price in (zigzag_list, price_data):   # 无论是回测还是实盘，都按照时间先后顺序逐个高低点进行传入。
    >>>     zzso.recognize(cur_zigzag)
    >>>     signal_list = zzo.signal_list_
    >>>     do something......
    """
    
    def __init__(self, zigzag_count=5):
        super().__init__(zigzag_count)
        
        
    def _rule(self):
        gen_sig = False
        if (
            self._cur_status == 0 
            and self._zigzag_list[4]["type"] == 1
            and self._zigzag_list[3]["price"] > self._zigzag_list[1]["price"]
            and self._zigzag_list[2]["price"] > self._zigzag_list[4]["price"]
            and self._cur_close < self._zigzag_list[3]["price"]
        ):
            self._type = 0
            gen_sig = True
        elif (
            self._cur_status == 0 
            and self._zigzag_list[4]["type"] == 0
            and self._zigzag_list[2]["price"] > self._zigzag_list[0]["price"]
            and self._zigzag_list[1]["price"] > self._zigzag_list[3]["price"]
            and self._cur_close < self._zigzag_list[2]["price"]
        ):
            self._type = 0
            gen_sig = True
        elif (
            self._cur_status == 1 
            and self._zigzag_list[4]["type"] == 1
            and self._zigzag_list[3]["price"] > self._zigzag_list[1]["price"]
            and self._zigzag_list[0]["price"] > self._zigzag_list[2]["price"]
            and self._cur_close > self._zigzag_list[2]["price"]
        ):
            self._type = 1
            gen_sig = True
        elif (
            self._cur_status == 1 
            and self._zigzag_list[4]["type"] == 0
            and self._zigzag_list[4]["price"] > self._zigzag_list[2]["price"]
            and self._zigzag_list[1]["price"] > self._zigzag_list[3]["price"]
            and self._cur_close > self._zigzag_list[3]["price"]
        ):
            self._type = 1
            gen_sig = True
        
        return gen_sig

