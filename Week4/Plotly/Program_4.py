#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 22:19:54 2019

@author: ankusmanish
"""

#Write a program to draw a scatter plot for a given dataset and show datalabels on hover

import plotly as py
import plotly.graph_objs as go
import numpy as np

py.offline.init_notebook_mode(connected = True)

data=pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv')

#create layout graph object

layout = go.Layout(
    title = 'USA Dataset',
    yaxis = dict(
        title = 'Population'
    ),
    xaxis = dict(
        title = 'Postal'
    )
)

trace1 = go.Scatter(
    x = data['Postal'],
    y = data['Population'],
    mode = 'markers',
    name = 'sin(x)',
    marker_color = 'blue',
    marker_size = 5.5
)

fig = go.Figure(data = [trace1], layout = layout)

py.offline.iplot(fig)