#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# LUX et VERITAS
# Create On: 2022/11/09 10:11:30

from collections import deque



class ZZSignal(object):
    """Base class of ZigZag signal
    
    
    """
    
    def __init__(self, zigzag_count=5):
        # 计算信号所需要的高低点个数
        self._zigzag_count = zigzag_count
        # 计算信号所需要的高低点价格信息列表
        self._zigzag_list = deque(maxlen=self._zigzag_count)
        # 上一个高低点的价格信息，
        # 样例：{"date_time": date_time, "price": high/low/close, "close": close, "volume": volume, "dist": dist, "type": type}
        # 0：低点；1：高点
        self._prev_zigzag = dict()
        # {"date_time": date_time, "open": open, "high": high, "low": low, "close": close, "volume": volumne}
        # 至少有以上6项
        self._cur_price = dict()
        # 当前状态，0：低点；1：高点
        self._cur_status = None
        # 当前高低点的收盘价
        self._cur_close = None
        # 信号点列表，基础元素为字典，
        # 样例，{"pn_value": pn_value, "pn_time": pn_time, "type": type}
        # 其中type取值，0：跌；1：涨
        self._signal_list = list()
        # 信号起始点的时间
        self._start_time = None
        # 信号涨跌类型，其中取值，0：跌；1：涨
        self._type = None
    
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
                cur_signal["type"] = self._type
                self._signal_list.append(cur_signal.copy())
                self._start_time = self._zigzag_list[0]["date_time"]
    
    def _rule(self):
        """Rule of Signal
        """
        
        return False
    
    
    @property
    def signal_list_(self):
        return self._signal_list            
                
    @property
    def current_signal_(self):
        if len(self._signal_list):
            return self._signal_list[-1]


