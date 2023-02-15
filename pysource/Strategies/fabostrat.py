#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# LUX et VERITAS
# Create On: 2022/12/05 13:26:14



class FaboStrat(object):
    
    def __init__(self, tp=0.382, sl=0.618, tole=0.001):
        """
        Parameters
        ------------
            tp : float
                take profit
            sl : float
                stop-losses
        """
        
        self._tp = tp
        self._sl = sl
        self._profit_dict = dict()
        self._signal_list = list()
        
    
    def profit(self, signal_dict, price_dict: dict=dict()):
        """
        
        """
        
        if len(self._signal_list):
            if self._signal_list[-1] != signal_dict:
                self._signal_list.append(signal_dict)
            del_list = list()
            for cur_idx, cur_signal in enumerate(self._signal_list):
                crtime = cur_signal["p3_time"]
                hl0 = cur_signal["p1_price"]
                hl1 = cur_signal["p2_price"]
                hl2 = cur_signal["p3_price"]
                crtype = cur_signal["type"]
                delta0 = abs(hl0 - hl1)
                delta1 = abs(hl1 - hl2)
                tp_rate, sl_rate = 0, 0
                
                if crtype == 0:
                    delta2 = hl2 - price_dict["close"]
                    if delta2 < 0:
                        delta3 = hl1 - price_dict["close"]
                        sl_rate = delta3/delta0
                    else:
                        tp_rate = delta2/delta1
                elif crtype == 1:
                    delta2 = price_dict["close"] - hl2
                    if delta2 < 0:
                        delta3 = price_dict["close"] - hl1
                        sl_rate = delta3/delta0
                    else:
                        tp_rate = delta2/delta1
                
                if ((tp_rate > self._tp) or (-sl_rate > self._sl)) and (not crtime in self._profit_dict):
                    self._profit_dict[crtime] = dict()
                    # 开仓价格
                    self._profit_dict[crtime]["open_price"] = hl2
                    # 平仓时间
                    self._profit_dict[crtime]["close_time"] = price_dict["date_time"]
                    # 平仓价格
                    self._profit_dict[crtime]["close_price"] = price_dict["close"]
                    # 收益金额
                    self._profit_dict[crtime]["profit"] = delta2
                    # 收益比例（不带杠杆）
                    self._profit_dict[crtime]["profit_rate"] = delta2/hl2
                    # 止盈点比例（FABO）
                    self._profit_dict[crtime]["tp_rate"] = tp_rate
                    # 止损点比例（FABO）
                    self._profit_dict[crtime]["sl_rate"] = sl_rate
                    # 交易类型（做多/做空）
                    self._profit_dict[crtime]["type"] = crtype
                    
                    if cur_idx < len(self._signal_list)-2:
                        del_list.append(cur_idx)
                if crtime in self._profit_dict:
                    if cur_idx < len(self._signal_list)-2:
                        del_list.append(cur_idx)

            for i in del_list:
                self._signal_list.pop(i)
            
        else:
            self._signal_list.append(signal_dict.copy())