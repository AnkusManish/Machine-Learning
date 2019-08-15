#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 22:05:57 2019

@author: ankusmanish
"""

#Write a program to draw a scatter plot of “day” against “total bill” for a dataset given in a url 

import matplotlib.pyplot as plt
import seaborn as sea
import pandas as pd

data = pd.read_csv('tips.csv')

x = data['day']
y = data['total_bill']

plt.figure(figsize = (8,6))
sea.scatterplot(x,y, hue = x)
plt.xlabel('Day')
plt.ylabel('Total Bill')