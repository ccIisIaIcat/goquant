#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# LUX et VERITAS
# Create On: 2022/11/09 10:59:57

from Signals._zzsig import ZZSignal


class HSDSignal(ZZSignal):
    """Head and Shoulders Signal
    
    Usage:
    >>> zzso = HSDSignal(7)  # 对于每个品种，首先实例化ZZSignal。
    >>> for cur_zigzag, cur_price in (zigzag_list, price_data):   # 无论是回测还是实盘，都按照时间先后顺序逐个高低点进行传入。
    >>>     zzso.recognize(cur_zigzag)
    >>>     signal_list = zzo.signal_list_
    >>>     do something......
    """
    
    def __init__(self, zigzag_count=7):
        super().__init__(zigzag_count)
    
    def _rule(self):
        """Rule of new ZigZag signal
        
        
        """
        
        pt0, pt1, pt2, pt3, pt4, pt5, pt6 = (
            self._zigzag_list[0],
            self._zigzag_list[1],
            self._zigzag_list[2],
            self._zigzag_list[3],
            self._zigzag_list[4],
            self._zigzag_list[5],
            self._zigzag_list[6],
        )
        
        gen_sig = False
        
        # 编写信号判断的逻辑
        if (
            pt0["type"] == 1 and pt1["type"] == 0
            and (pt2["price"]/pt1["price"] > 1 and pt2["price"]/pt1["price"] < 2)
            and pt3["price"] < pt1["price"]
            and (pt4["price"]/pt2["price"] > 0.985 and pt2["price"]/pt4["price"] > 0.985)
            and (pt5["price"]/pt1["price"] > 0.985 and pt1["price"]/pt5["price"] > 0.985)
            and pt6["price"] > pt4["price"]
        ):
            gen_sig = True
            self._type = 1
        elif (
            pt0["type"] == 0 and pt1["type"] == 1
            and (pt2["price"]/pt1["price"] > 0.5 and pt2["price"]/pt1["price"] < 1)
            and pt3["price"] > pt1["price"]
            and (pt4["price"]/pt2["price"] > 0.985 and pt2["price"]/pt4["price"] > 0.985)
            and (pt5["price"]/pt1["price"] > 0.985 and pt1["price"]/pt5["price"] > 0.985)
            and pt6["price"] < pt4["price"]
        ):
            gen_sig = True
            self._type = 0
        
        return gen_sig
