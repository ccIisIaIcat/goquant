#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# LUX et VERITAS
# Create On: 2022/11/09 11:01:09

from Signals._zzsig import ZZSignal


class VSignal(ZZSignal):
    """V Signal
    
    Usage:
    >>> zzso = VSignal(3)  # 对于每个品种，首先实例化ZZSignal。
    >>> for cur_zigzag, cur_price in (zigzag_list, price_data):   # 无论是回测还是实盘，都按照时间先后顺序逐个高低点进行传入。
    >>>     zzso.recognize(cur_zigzag)
    >>>     signal_list = zzo.signal_list_
    >>>     do something......
    """
    
    def __init__(self, zigzag_count=3):
        super().__init__(zigzag_count)
    
    def _rule(self):
        """Rule of new ZigZag signal
        
        
        """
        
        gen_sig = False
        self._type = 0
        
        pt0, pt1, pt2 = (
            self._zigzag_list[0],
            self._zigzag_list[1],
            self._zigzag_list[2],
        )
        
        # 编写信号判断的逻辑
        if (
            pt0["price"] > 1.0125*pt1["price"]
            and pt2["price"] > 1.0125*pt1["price"]
            and (pt0["price"]/pt2["price"] > 0.985 and pt2["price"]/pt0["price"] > 0.985)
        ):
            gen_sig = True
            self._type = 1
        elif (
            pt1["price"] > 1.0125*pt0["price"]
            and pt1["price"] > 1.0125*pt2["price"]
            and (pt0["price"]/pt2["price"] > 0.985 and pt2["price"]/pt0["price"] > 0.985)
        ):
            gen_sig = True
            self._type = 0
        return gen_sig

