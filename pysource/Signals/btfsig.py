#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# LUX et VERITAS
# Create On: 2022/11/09 10:58:56

from Signals._zzsig import ZZSignal


class BTFSignal(ZZSignal):
    """ButterFly Signal
    
    Usage:
    >>> zzso = BTFSignal(5)  # 对于每个品种，首先实例化ZZSignal。
    >>> for cur_zigzag, cur_price in (zigzag_list, price_data):   # 无论是回测还是实盘，都按照时间先后顺序逐个高低点进行传入。
    >>>     zzso.recognize(cur_zigzag, cur_price)
    >>>     signal_list = zzo.signal_list_
    >>>     do something......
    """
    
    def __init__(self, zigzag_count=5, bias_tolerance=1):
        self._bias_tolerance = bias_tolerance
        super().__init__(zigzag_count)
        
        
    def _rule(self):
        gen_sig = False
        if (
            self._zigzag_list[4]["type"] == 1
            and (abs((self._zigzag_list[2]["price"]-self._zigzag_list[1]["price"])/(self._zigzag_list[0]["price"]-self._zigzag_list[1]["price"])) <= (0.786 + self._bias_tolerance) and abs((self._zigzag_list[2]["price"]-self._zigzag_list[1]["price"])/(self._zigzag_list[0]["price"]-self._zigzag_list[1]["price"])) >=(0.786 - self._bias_tolerance))
            and (
                (abs((self._zigzag_list[4]["price"]-self._zigzag_list[2]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[3]["price"])) <= (1.618 + self._bias_tolerance) and abs((self._zigzag_list[4]["price"]-self._zigzag_list[2]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[3]["price"])) >= (1.618 - self._bias_tolerance)) 
                or (abs((self._zigzag_list[4]["price"]-self._zigzag_list[2]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[3]["price"])) <= (2 + self._bias_tolerance) and abs((self._zigzag_list[4]["price"]-self._zigzag_list[2]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[3]["price"])) >= (2 - self._bias_tolerance))
                or (abs((self._zigzag_list[4]["price"]-self._zigzag_list[2]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[3]["price"])) <= (2.236 + self._bias_tolerance) and abs((self._zigzag_list[4]["price"]-self._zigzag_list[2]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[3]["price"])) >= (2.236 - self._bias_tolerance))
                or (abs((self._zigzag_list[4]["price"]-self._zigzag_list[2]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[3]["price"])) <= (2.618 + self._bias_tolerance) and abs((self._zigzag_list[4]["price"]-self._zigzag_list[2]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[3]["price"])) >= (2.618 - self._bias_tolerance))
                or (abs((self._zigzag_list[4]["price"]-self._zigzag_list[2]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[3]["price"])) <= (3.141 + self._bias_tolerance) and abs((self._zigzag_list[4]["price"]-self._zigzag_list[2]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[3]["price"])) >= (3.141 - self._bias_tolerance))
                or (abs((self._zigzag_list[4]["price"]-self._zigzag_list[2]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[3]["price"])) <= (3.618 + self._bias_tolerance) and abs((self._zigzag_list[4]["price"]-self._zigzag_list[2]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[3]["price"])) >= (3.618 - self._bias_tolerance))
            )
            and (
                (abs((self._zigzag_list[4]["price"]-self._zigzag_list[3]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[1]["price"])) <= (1 + self._bias_tolerance) and abs((self._zigzag_list[4]["price"]-self._zigzag_list[3]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[1]["price"])) >= 1- self._bias_tolerance)
                or (abs((self._zigzag_list[4]["price"]-self._zigzag_list[3]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[1]["price"])) <= (1.272 + self._bias_tolerance) and abs((self._zigzag_list[4]["price"]-self._zigzag_list[3]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[1]["price"])) >= (1.272- self._bias_tolerance))
                or (abs((self._zigzag_list[4]["price"]-self._zigzag_list[3]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[1]["price"])) <= (1.414 + self._bias_tolerance) and abs((self._zigzag_list[4]["price"]-self._zigzag_list[3]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[1]["price"])) >= (1.414- self._bias_tolerance))
                or (abs((self._zigzag_list[4]["price"]-self._zigzag_list[3]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[1]["price"])) <= (1.126 + self._bias_tolerance) and abs((self._zigzag_list[4]["price"]-self._zigzag_list[3]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[1]["price"])) >= (1.126- self._bias_tolerance))
                or (abs((self._zigzag_list[4]["price"]-self._zigzag_list[3]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[1]["price"])) <= (1.618 + self._bias_tolerance) and abs((self._zigzag_list[4]["price"]-self._zigzag_list[3]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[1]["price"])) >= (1.618- self._bias_tolerance))
                or (abs((self._zigzag_list[4]["price"]-self._zigzag_list[3]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[1]["price"])) <= (2.236 + self._bias_tolerance) and abs((self._zigzag_list[4]["price"]-self._zigzag_list[3]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[1]["price"])) >= (2.236- self._bias_tolerance))
                or (abs((self._zigzag_list[4]["price"]-self._zigzag_list[3]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[1]["price"])) <= (2.618 + self._bias_tolerance) and abs((self._zigzag_list[4]["price"]-self._zigzag_list[3]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[1]["price"])) >= (2.618- self._bias_tolerance))
                or (abs((self._zigzag_list[4]["price"]-self._zigzag_list[3]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[1]["price"])) <= (3.141 + self._bias_tolerance) and abs((self._zigzag_list[4]["price"]-self._zigzag_list[3]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[1]["price"])) >= (3.141- self._bias_tolerance))
                or (abs((self._zigzag_list[4]["price"]-self._zigzag_list[3]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[1]["price"])) <= (3.618 + self._bias_tolerance) and abs((self._zigzag_list[4]["price"]-self._zigzag_list[3]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[1]["price"])) >= (3.618- self._bias_tolerance))
            )
            and ((abs((self._zigzag_list[4]["price"]-self._zigzag_list[1]["price"])/(self._zigzag_list[0]["price"]-self._zigzag_list[1]["price"])) <= (1.27 + self._bias_tolerance) and abs((self._zigzag_list[4]["price"]-self._zigzag_list[1]["price"])/(self._zigzag_list[0]["price"]-self._zigzag_list[1]["price"])) >= (1.27 - self._bias_tolerance)))
            and (abs((self._zigzag_list[2]["price"]-self._zigzag_list[3]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[1]["price"])) <= (0.886 + self._bias_tolerance) and abs((self._zigzag_list[2]["price"]-self._zigzag_list[3]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[1]["price"])) >= (0.382 - self._bias_tolerance))
        ):
            self._type = 0
            gen_sig = True
        elif (
            self._zigzag_list[4]["type"] == 0
            and (abs((self._zigzag_list[1]["price"]-self._zigzag_list[2]["price"])/(self._zigzag_list[1]["price"]-self._zigzag_list[0]["price"])) <= (0.786 + self._bias_tolerance) and abs((self._zigzag_list[1]["price"]-self._zigzag_list[2]["price"])/(self._zigzag_list[1]["price"]-self._zigzag_list[0]["price"])) >=(0.786 - self._bias_tolerance))
            and (
                (abs((self._zigzag_list[4]["price"]-self._zigzag_list[2]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[3]["price"])) <= (1.618 + self._bias_tolerance) and abs((self._zigzag_list[4]["price"]-self._zigzag_list[2]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[3]["price"])) >= (1.618 - self._bias_tolerance))
                or (abs((self._zigzag_list[4]["price"]-self._zigzag_list[2]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[3]["price"])) <= (2 + self._bias_tolerance) and abs((self._zigzag_list[4]["price"]-self._zigzag_list[2]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[3]["price"])) >= (2 - self._bias_tolerance))
                or (abs((self._zigzag_list[4]["price"]-self._zigzag_list[2]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[3]["price"])) <= (2.236 + self._bias_tolerance) and abs((self._zigzag_list[4]["price"]-self._zigzag_list[2]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[3]["price"])) >= (2.236 - self._bias_tolerance))
                or (abs((self._zigzag_list[4]["price"]-self._zigzag_list[2]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[3]["price"])) <= (2.618 + self._bias_tolerance) and abs((self._zigzag_list[4]["price"]-self._zigzag_list[2]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[3]["price"])) >= (2.618 - self._bias_tolerance))
                or (abs((self._zigzag_list[4]["price"]-self._zigzag_list[2]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[3]["price"])) <= (3.141 + self._bias_tolerance) and abs((self._zigzag_list[4]["price"]-self._zigzag_list[2]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[3]["price"])) >= (3.141 - self._bias_tolerance))
                or (abs((self._zigzag_list[4]["price"]-self._zigzag_list[2]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[3]["price"])) <= (3.618 + self._bias_tolerance) and abs((self._zigzag_list[4]["price"]-self._zigzag_list[2]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[3]["price"])) >= (3.618 - self._bias_tolerance))
            )
            and (
                (abs((self._zigzag_list[4]["price"]-self._zigzag_list[3]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[1]["price"])) <= (1 + self._bias_tolerance) and abs((self._zigzag_list[4]["price"]-self._zigzag_list[3]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[1]["price"])) >= 1- self._bias_tolerance)
                or (abs((self._zigzag_list[4]["price"]-self._zigzag_list[3]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[1]["price"])) <= (1.272 + self._bias_tolerance) and abs((self._zigzag_list[4]["price"]-self._zigzag_list[3]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[1]["price"])) >= (1.272- self._bias_tolerance))
                or (abs((self._zigzag_list[4]["price"]-self._zigzag_list[3]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[1]["price"])) <= (1.414 + self._bias_tolerance) and abs((self._zigzag_list[4]["price"]-self._zigzag_list[3]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[1]["price"])) >= (1.414- self._bias_tolerance))
                or (abs((self._zigzag_list[4]["price"]-self._zigzag_list[3]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[1]["price"])) <= (1.126 + self._bias_tolerance) and abs((self._zigzag_list[4]["price"]-self._zigzag_list[3]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[1]["price"])) >= (1.126- self._bias_tolerance))
                or (abs((self._zigzag_list[4]["price"]-self._zigzag_list[3]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[1]["price"])) <= (1.618 + self._bias_tolerance) and abs((self._zigzag_list[4]["price"]-self._zigzag_list[3]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[1]["price"])) >= (1.618- self._bias_tolerance))
                or (abs((self._zigzag_list[4]["price"]-self._zigzag_list[3]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[1]["price"])) <= (2.236 + self._bias_tolerance) and abs((self._zigzag_list[4]["price"]-self._zigzag_list[3]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[1]["price"])) >= (2.236- self._bias_tolerance))
                or (abs((self._zigzag_list[4]["price"]-self._zigzag_list[3]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[1]["price"])) <= (2.618 + self._bias_tolerance) and abs((self._zigzag_list[4]["price"]-self._zigzag_list[3]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[1]["price"])) >= (2.618- self._bias_tolerance))
                or (abs((self._zigzag_list[4]["price"]-self._zigzag_list[3]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[1]["price"])) <= (3.141 + self._bias_tolerance) and abs((self._zigzag_list[4]["price"]-self._zigzag_list[3]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[1]["price"])) >= (3.141- self._bias_tolerance))
                or (abs((self._zigzag_list[4]["price"]-self._zigzag_list[3]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[1]["price"])) <= (3.618 + self._bias_tolerance) and abs((self._zigzag_list[4]["price"]-self._zigzag_list[3]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[1]["price"])) >= (3.618- self._bias_tolerance))
            )
            and ((abs((self._zigzag_list[4]["price"]-self._zigzag_list[1]["price"])/(self._zigzag_list[0]["price"]-self._zigzag_list[1]["price"])) <= (1.27 + self._bias_tolerance) and abs((self._zigzag_list[4]["price"]-self._zigzag_list[1]["price"])/(self._zigzag_list[0]["price"]-self._zigzag_list[1]["price"])) >= (1.27 - self._bias_tolerance)))
            and (abs((self._zigzag_list[2]["price"]-self._zigzag_list[3]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[1]["price"])) <= (0.886 + self._bias_tolerance) and abs((self._zigzag_list[2]["price"]-self._zigzag_list[3]["price"])/(self._zigzag_list[2]["price"]-self._zigzag_list[1]["price"])) >= (0.382 - self._bias_tolerance))
        ):
            self._type = 1
            gen_sig = True
        
        return gen_sig