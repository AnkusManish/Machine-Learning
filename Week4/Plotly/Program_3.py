#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 22:19:09 2019

@author: ankusmanish
"""

#Write a program to draw a scatter plot for random 500 x and y coordinates and style it

import plotly as py
import plotly.graph_objs as go
import numpy as np

py.offline.init_notebook_mode(connected = True)

t = np.linspace(0, 10, 500)
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
    marker_color = 'black',
    marker_size = 2.5
)

fig = go.Figure(data = [trace1], layout = layout)

py.offline.iplot(fig)