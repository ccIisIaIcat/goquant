#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# LUX et VERITAS
# Create On: 2022/11/09 11:43:18


from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Line, Bar, Kline, Grid, Scatter


def plot_candle(price_data):
    """Plot Candlestick

    Parameters
    -----------
        price_data : pandas.DataFrame 
            price data order by time, column include columns: date_time, open, close, low, high.

    Returns
    --------
        kl_base : charts
            Candlestick Chart
    
    """


    kl_base = (
        Kline()
        .add_xaxis(price_data.date_time.tolist())
        .add_yaxis(
            "",
            price_data[["open", "close", "low", "high"]].values.tolist(),
            itemstyle_opts=opts.ItemStyleOpts(
                color="#ef232a",
                color0="#14b143",
                border_color="#ef232a",
                border_color0="#14b143",
            ),
        )
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(is_scale=True),
            yaxis_opts=opts.AxisOpts(
                is_scale=True,
                splitarea_opts=opts.SplitAreaOpts(
                    is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                ),
            ),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="line"),
            datazoom_opts=[
                opts.DataZoomOpts(
                    is_show=False, type_="inside", xaxis_index=[0, 0], range_start=0, range_end=100, filter_mode="weakFilter"
                ),
                opts.DataZoomOpts(
                    is_show=True, type_="slider", xaxis_index=[0, 1], range_start=0, range_end=100, pos_top="97%", filter_mode="weakFilter"
                ),
            ],
            title_opts=opts.TitleOpts(title="K Line"),
        )
    )

    return kl_base