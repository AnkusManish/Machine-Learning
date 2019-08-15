#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 22:09:52 2019

@author: ankusmanish
"""

#Write a program to draw a violin plot of “species” against “sepal length” for a dataset given in a url 

import matplotlib.pyplot as plt
import seaborn as sea
import pandas as pd

data = pd.read_csv('iris.csv')

x = data['species']
y = data['sepal_length']

plt.figure(figsize = (8,8))
sea.violinplot(x,y, hue = x)
plt.xlabel('Sex')
plt.ylabel('Total Bill')