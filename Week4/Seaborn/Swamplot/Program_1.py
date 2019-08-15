#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 22:14:22 2019

@author: ankusmanish
"""

#Write a program to draw a swarm plot of total bill against size  for a  given dataset

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sea

data = pd.read_csv('tips.csv')

x = data['size']
y = data['total_bill']

plt.figure(figsize = (8,8))
sea.swarmplot(x,y)
plt.xlabel('Size', fontsize = 20)
plt.ylabel('Total Bill', fontsize = 20)
plt.show()