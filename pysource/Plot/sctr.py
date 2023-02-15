#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# LUX et VERITAS
# Create On: 2022/11/09 13:51:41

from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Line, Bar, Kline, Grid, Scatter


def plot_scatter(price_data):
    """Plot Scatter for high or low

    Parameters
    -----------
        price_data : pandas.DataFrame 
            price data order by time, column include columns: date_time, price, close, type.

    Returns
    --------
        sct_base : charts
            Scatter Chart.
    
    """

    sct_base = (
        Scatter(init_opts=opts.InitOpts(height="600px", width="1400px"))
        .add_xaxis(xaxis_data=price_data["date_time"].tolist())
        .add_yaxis(
            series_name="",
            y_axis=[
                opts.ScatterItem(
                    name="",
                    value=x[0],
                    itemstyle_opts={
                        "color": "#ef232a" if x[1] == 1 else "#14b143"
                    }
                )
                for x in price_data[["price", "type"]].values.tolist()
            ],
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            yaxis_opts=opts.AxisOpts(
                is_scale=True
            ),
            toolbox_opts=opts.ToolboxOpts(),
            datazoom_opts=opts.DataZoomOpts(),
        )
    )

    return sct_base
