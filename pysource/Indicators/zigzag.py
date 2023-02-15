#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# LUX et VERITAS
# Create On: 2022/11/09 09:55:33


from collections import deque


class ZigZag(object):
    """Calculate ZigZag
    
    Usage:
    >>> zzo = ZigZag(20)  # 对于每个品种，首先实例化ZigZag。
    >>> for cur_price in price_data.to_dict(orient="records"):   # 无论是回测还是实盘，都按照时间先后顺序逐个bar进行传入。
    >>>     zzo.compute(cur_price)
    >>>     zigzag_list = zzo.zig_zag_
    >>>     do something......
    """
    
    def __init__(self, bar_count=20, status=0, cur_high: dict={}, cur_low: dict={}, pos=0, prev_pos=0):
        # 计算过去多少根bar的zigzag
        self._bar_count = bar_count
        # 存放bar_count跟bar的价格相关等数据
        self._price_list = deque(maxlen=self._bar_count)
        # zigzag信息列表，基础元素为字典
        self._zigzag_list = list()
        # highlow信息列表，基础元素字典
        self._highlow_list = list()
        # 当前zigzag状态， 0：下降；1：上升
        self._status = status
        # 当前高点价格信息，
        # 样例：{"date_time": date_time, "price": high/low/close, "close": close, "volume": volume, "dist": dist, "type": 1}
        # 0：低点；1：高点
        if len(cur_high) > 0:
            self._cur_high = cur_high.copy()
        else:
            self._cur_high = {
                "date_time": "1970-01-01",
                "price": float("-inf"),
                "close": float("-inf"),
                "volume": None,
                "dist": 1,  # 与前一个高/低点的距离，该距离包括了端点，因此最小为1
                "type": 1,
            }
        # 当前低点价格信息，
        # 样例：{"date_time": date_time, "price": high/low/close, "close": close, "volume": volume, "dist": dist, "type": 0}
        # 0：低点；1：高点
        if len(cur_low) > 0:
            self._cur_low = cur_low.copy()
        else:
            self._cur_low = {
                "date_time": "1970-01-01",
                "price": float("inf"),
                "close": float("inf"),
                "volume": None,
                "dist": 1,  # 与前一个高/低点的距离，该距离包括了端点，因此最小为1
                "type": 0,
            }
        # 初始化区间最大/最小为当前最大/最小
        self._inv_max = self._cur_high["price"]
        self._inv_min = self._cur_low["price"]
        # 当前高低点所在位次
        self._pos = pos
        # 前一个高低点价格位次
        self._prev_pos = prev_pos
        # 初始的位置
        self._preprev_pos = -1

    
    def compute(self, price_dict):
        """Compute
        
        Parameters
        -----------
            price_dict : dictionary
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

        price_dict = price_dict.copy()
        # zigzag上升状态
        if self._status == 1:
            # 在 当前bar的最高点大于上一个区间最大值且当前价格大于当前高点价格信息时，更新当前高点价格信息
            # 同时将高点价格信息更新到zigzag_list
            if price_dict["high"] > self._inv_max and price_dict["high"] > self._cur_high["price"]:
                self._cur_high["date_time"] = price_dict["date_time"]
                self._cur_high["price"] = price_dict["high"]
                self._cur_high["close"] = price_dict["close"]
                self._cur_high["volume"] = price_dict["volume"]
                self._cur_high["dist"] = self._pos - self._prev_pos + 1  # 这里的距离包括了两个端点
                self._prev_pos = self._pos
                self._zigzag_list.append(self._cur_high.copy())
            # 在 当前bar的最低点小于上一个区间最小值时 更新当前低点价格信息，同时更改zigzag状态为下降
            # 之后，将当前低点价格信息添加到zigzag列表中
            # 注：这里不认为一阴穿Nbar的状态会改变原zigzag状态
            elif price_dict["low"] < self._inv_min:
                self._cur_low["date_time"] = price_dict["date_time"]
                self._cur_low["price"] = price_dict["low"]
                self._cur_low["close"] = price_dict["close"]
                self._cur_low["volume"] = price_dict["volume"]
                self._cur_low["dist"] = self._pos - self._prev_pos + 1  # 这里的距离包括了两个端点
                # 更新当前zigzag的状态为下降
                self._status = 0
                self._prev_pos = self._pos
                self._zigzag_list.append(self._cur_low.copy())
        # zigzag下降状态
        elif self._status == 0:
            # 在 当前bar的最低点小于上一个区间最小值且当前价格小于当前低点价格信息时，更新当前低点价格信息
            # 同时将低点价格信息更新到zigzag_list
            if price_dict["low"] < self._inv_min and price_dict["low"] < self._cur_low["price"]:
                self._cur_low["date_time"] = price_dict["date_time"]
                self._cur_low["price"] = price_dict["low"]
                self._cur_low["close"] = price_dict["close"]
                self._cur_low["volume"] = price_dict["volume"]
                self._cur_low["dist"] = self._pos - self._prev_pos + 1  # 这里的距离包括了两个端点
                self._prev_pos = self._pos
                self._zigzag_list.append(self._cur_low.copy())
            # 在 当前bar的最高点大于上一个区间最大值时 更新当前高点价格信息，同时更改zigzag状态为上升
            # 之后，将当前高点价格信息添加到zigzag列表中
            # 注：这里不认为一阳穿Nbar会改变原zigzag状态
            elif price_dict["high"] > self._inv_max:
                self._cur_high["date_time"] = price_dict["date_time"]
                self._cur_high["price"] = price_dict["high"]
                self._cur_high["close"] = price_dict["close"]
                self._cur_high["volume"] = price_dict["volume"]
                self._cur_high["dist"] = self._pos - self._prev_pos + 1  # 这里的距离包括了两个端点
                # 更新当前zigzag的状态为上升
                self._status = 1
                self._prev_pos = self._pos
                self._zigzag_list.append(self._cur_high.copy())
        
        self._pos += 1
        # 更新区间价格列表，并更新区间最大值和最小值
        self._price_list.append(price_dict)
        self._inv_max = max(self._price_list, key=lambda x: x["high"])["high"]
        self._inv_min = min(self._price_list, key=lambda x: x["low"])["low"]

        # 第一条数据输送进入之后肯定会产生一个zigzag值
        if self._check_hl():
            if len(self._highlow_list):
                if self._highlow_list[-1] != self._zigzag_list[-2]:
                    self._highlow_list.append(self._zigzag_list[-2])
            else:
                self._highlow_list.append(self._zigzag_list[-2])

    def _check_hl(self):
        hl_flag = False
        if len(self._zigzag_list) > 1:
            hl_flag = (self._zigzag_list[-1]["type"] != self._zigzag_list[-2]["type"])

        return hl_flag  
    
    @property
    def zigzag_list_(self):
        return self._zigzag_list

    @property
    def highlow_list_(self):
        return self._highlow_list

    @property
    def current_high_(self):
        return self._cur_high
    
    @property
    def current_low_(self):
        return self._cur_low
    
    @property
    def status_(self):
        return self._status

    @property
    def current_zigzag_(self):
        if len(self._zigzag_list):
            return self._zigzag_list[-1]
            # # Get HL list batch NO USE
            # zz_df = pd.DataFrame(zzo.zigzag_list_)
            # zz_sftdf = zz_df.shift(1, fill_value=0)
            # hl_df = zz_sftdf[(zz_df["type"] != zz_sftdf["type"])]

    @property
    def current_highlow_(self):
        if len(self._highlow_list) > 1:
            return (self._highlow_list[-1], self._highlow_list[-2])

    

