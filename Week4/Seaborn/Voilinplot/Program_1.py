#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 22:07:58 2019

@author: ankusmanish
"""

#Write a program to draw a violin plot of sex against total_bill  for a  given dataset 

import matplotlib.pyplot as plt
import seaborn as sea
import pandas as pd

data = pd.read_csv('tips.csv')

x = data['sex']
y = data['total_bill']

plt.figure(figsize = (8,8))
sea.violinplot(x,y, hue = x)
plt.xlabel('Sex')
plt.ylabel('Total Bill')