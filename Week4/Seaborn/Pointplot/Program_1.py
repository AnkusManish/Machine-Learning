#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 22:04:47 2019

@author: ankusmanish
"""

#Write a program to draw a point plot for sex against survived for a dataset given in url

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sea

data = pd.read_csv('titanic.csv')

x = data['sex'].values

plt.figure(figsize = (8,6))
sea.pointplot(x, y = data['survived'].values, hue = data['class'])
plt.ylabel('Survived')
plt.show()