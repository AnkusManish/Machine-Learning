#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 22:11:08 2019

@author: ankusmanish
"""

#Write a program to draw box plot of life expectancy by continent for a data set given in a url 

import matplotlib.pyplot as plt
import seaborn as sea
import pandas as pd

data = pd.read_csv('year_data.csv')

x = data['continent']
y = data['lifeExp']

plt.figure(figsize = (8,8))
sea.boxplot(x,y, saturation = 0.5)
plt.xlabel('Continent', fontsize = 20)
plt.ylabel('Life Expectancy', fontsize = 20)
plt.show()