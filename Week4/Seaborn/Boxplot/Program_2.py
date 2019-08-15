#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 22:13:52 2019

@author: ankusmanish
"""

#Write a program to draw a box plot of day by tips for a dataset given in a url

import matplotlib.pyplot as plt
import seaborn as sea
import pandas as pd

data = pd.read_csv('tips.csv')

x = data['day']
y = data['tip']

plt.figure(figsize = (8,8))
sea.boxplot(x,y, hue = x)
plt.xlabel('Day', fontsize = 20)
plt.ylabel('Tip', fontsize = 20)
plt.show()