#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 19:59:07 2019

@author: ankusmanish
"""

#Write a Python program to draw a line using given axis values with suitable label in the x axis , y axis and a title

import matplotlib.pyplot as plt
import numpy as np

x = list(range(1,51))
func = lambda x : np.sqrt(x)
y = list(map(func, x))

plt.plot(x,y)
plt.xlabel('Numbers between 1-50')
plt.xticks([1,5,10,15,20,25,30,35,40,45,50])
plt.ylabel('Square root of numbers between 1-50')
plt.title('Plot for square root of numbers')
plt.show()