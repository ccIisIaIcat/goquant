#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# LUX et VERITAS
# Create On: 2022/11/09 13:51:10

from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Line, Bar, Kline, Grid, Scatter


def plot_bar(price_data):
    """Plot Bar for volume

    Parameters
    -----------
        price_data : pandas.DataFrame 
            price data order by time, column include columns: date_time, open, close, low, high, volume.

    Returns
    --------
        bar_base : charts
            Bar Chart.
    
    """

    bar_base = (
        Bar()
        .add_xaxis(price_data.date_time.tolist())
        .add_yaxis(
            series_name="",
            y_axis=[
                opts.BarItem(
                    name="",
                    value=x[2],
                    itemstyle_opts={
                        "color": "#ef232a" if x[1] >= x[0] else "#14b143" 
                    },
                )
                for x in price_data[["open", "close", "volume",]].values
            ],
            xaxis_index=1,
            yaxis_index=1,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            yaxis_opts=opts.AxisOpts(
                is_scale=True
            )
        )
    )

    return bar_base
