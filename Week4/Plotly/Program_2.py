#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 22:18:23 2019

@author: ankusmanish
"""

#Write a program to draw line and scatter plots for random 100 x and y coordinates

import plotly as py
import plotly.graph_objs as go
import numpy as np

py.offline.init_notebook_mode(connected = True)

N = 1000
t = np.linspace(0, 10, 100)
y = np.sin(t)

#create layout graph object

layout = go.Layout(
    title = 'Sin Plot',
    yaxis = dict(
        title = 'sin of value'
    ),
    xaxis = dict(
        title = 'value'
    )
)

trace1 = go.Scatter(
    x = t,
    y = y,
    mode = 'markers',
    name = 'sin(x)',
)

trace2 = go.Scatter(
    x = t,
    y = y,
    mode = 'lines',
    name = 'sin(x)',
)

trace3 = go.Scatter(
    x = t,
    y = y,
    mode = 'markers+lines',
    name = 'sin(x)',
)

fig1 = go.Figure(data = [trace1], layout = layout)

fig2 = go.Figure(data = [trace2], layout = layout)

fig3 = go.Figure(data = [trace3], layout = layout)

py.offline.iplot(fig1)
py.offline.iplot(fig2)
py.offline.iplot(fig3)