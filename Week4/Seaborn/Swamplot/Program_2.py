#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 22:15:25 2019

@author: ankusmanish
"""

#Write a program to draw swarm plot of “total bill” against day for a dataset given in url

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sea

data = pd.read_csv('tips.csv')

x = data['day']
y = data['total_bill']

plt.figure(figsize = (8,8))
sea.swarmplot(x,y)
plt.xlabel('Day', fontsize = 20)
plt.ylabel('Total Bill', fontsize = 20)
plt.show()