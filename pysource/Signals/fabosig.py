#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# LUX et VERITAS
# Create On: 2022/11/15 13:18:44

from Signals._zzsig import ZZSignal


class FABOSignal(ZZSignal):
    """New ZigZag Signal
    
    Usage:
    >>> zzso = FABOSignal(2)  # 对于每个品种，首先实例化ZZSignal。
    >>> for cur_zigzag, cur_price in (zigzag_list, price_data):   # 无论是回测还是实盘，都按照时间先后顺序逐个高低点进行传入。
    >>>     zzso.recognize(cur_zizag)
    >>>     signal_list = zzo.signal_list_
    >>>     do something......
    """
    
    def __init__(self, zigzag_count=2):
        super().__init__(zigzag_count)


    def recognize(self, zigzag_dict, price_dict: dict=dict()):
        """Recognize

        Parameters
        -----------
            zigzag_dict : dictionary
                样例, {
                    "date_time": date_time,
                    "price": price,
                    "close": close,
                    "volume": volume, 
                    "dist": dist,
                    "type": type
                }
                其中，type取值，0：低点；1：高点

            price_dict : dictionary，默认为空的字典
                样例, {
                    "date_time": date_time,
                    "open": open,
                    "high": high,
                    "low": low,
                    "close": close,
                    "volume": volumne
                }
                至少有以上6项
        """
        
        zigzag_dict = zigzag_dict.copy()
        # 在使用self._cur_price时应当判断是否传入当前的价格数据。
        self._cur_price = price_dict.copy()
        # 计算当前价格的最小和最大值
        self._cur_high = self._cur_price["high"]
        self._cur_low = self._cur_price["low"]
        # 初始化状态高低点价格信息列表为空
        if len(self._zigzag_list) == 0:
            self._zigzag_list.append(zigzag_dict.copy())
            self._prev_zigzag = self._zigzag_list[-1]
        
        self._cur_status = zigzag_dict["type"]
        self._cur_close = self._cur_price["close"]
        # 如果传入的价格信息与之前最后一个的type一致，则更新最后一个，否则，则向zigzag_list中添加该信息
        if self._prev_zigzag["type"] == zigzag_dict["type"]:
            self._zigzag_list[-1] = zigzag_dict.copy()
        elif self._prev_zigzag["type"] != zigzag_dict["type"]:
            self._zigzag_list.append(zigzag_dict.copy())

        self._prev_zigzag = self._zigzag_list[-1]
        if len(self._zigzag_list) == self._zigzag_count:
            # 判断当前的zigzag_list是否为信号
            gen_sig = self._rule()
            # 当 是信号 并且 信号点的开始时间和上一个信号开始时间不相同时，才更新当前信号
            if gen_sig and self._start_time != self._zigzag_list[0]["date_time"]:
               # 合成当前signal的字典
                cur_signal = dict()
                for idx, cdic in enumerate(self._zigzag_list, 1):
                    cur_signal[f"p{idx}_price"] = cdic["price"]
                    cur_signal[f"p{idx}_time"] = cdic["date_time"]
                if self._type == 0:
                    cur_signal[f"p{idx+1}_price"] = self._cur_high
                elif self._type == 1:
                    cur_signal[f"p{idx+1}_price"] = self._cur_low
                cur_signal[f"p{idx+1}_time"] = self._cur_price["date_time"]
                cur_signal["type"] = self._type
                self._signal_list.append(cur_signal.copy())
                self._start_time = self._zigzag_list[0]["date_time"]


    def _rule(self):
        """Rule of new ZigZag signal
        
        最主要使用self._zigzag_list中的量价关系进行策略信号的编写，
        然后对是否为信号（gen_sig）和信号所预示的涨跌（self._type）进行判断，并返回当前状态是否为信号（gen_sig）

        Rate: 0.236, 0.382, 0.50, 0.618, 0.764, 0.886, 1.00, 1.272, 1.618, 2.00, 2.618
        RateNB: 0.382, 0.5, 0.618, 0.886, 1, 1.414, 1.618, 2, 2.618, 3.618
        """
        
        gen_sig = False
        self._type = 0
        
        # 
        cur_sts = self._zigzag_list[-1]["type"]
        hl0 = self._zigzag_list[-2]["price"]
        hl1 = self._zigzag_list[-1]["price"]
        delta0 = abs(hl0 - hl1)
        if cur_sts == 0:
            delta1 = self._cur_high - hl1
            rate0 = delta1/delta0
            if rate0 > 0.48 and rate0 < 0.52:
                self._type = 0
                gen_sig = True
        elif cur_sts == 1:
            delta1 = hl1 - self._cur_low
            rate0 = delta1/delta0
            if rate0 > 0.48 and rate0 < 0.52:
                self._type = 1
                gen_sig = True
        
        return gen_sig