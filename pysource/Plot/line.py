#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# LUX et VERITAS
# Create On: 2022/11/09 13:51:37

from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Line, Bar, Kline, Grid, Scatter


def plot_line(time_data, price_data, stype):
    """Plot line for signal

    Parameters
    -----------
        time_data : list
            current signal time list.
        
        price_data : list
            current signal price list

        stype : int 0 or 1
            current signal type 0:down 1:up.
        

    Returns
    --------
        line_base : charts
            Line Chart
    
    """

    line_base = (
        Line()
        .add_xaxis(time_data)
        .add_yaxis(
            series_name="", 
            y_axis=price_data,
            linestyle_opts = opts.LineStyleOpts(
                width=2,
                color="red" if stype == 1 else "green"
            )
        )
        .set_global_opts(
            yaxis_opts=opts.AxisOpts(
                is_scale=True
            ),
            toolbox_opts=opts.ToolboxOpts(),
            datazoom_opts=opts.DataZoomOpts(),
        )
    )

    return line_base
