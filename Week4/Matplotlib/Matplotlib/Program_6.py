#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 20:04:05 2019

@author: ankusmanish
"""

#Write a Python program to plot two or more lines with legends, different widths and colors

import matplotlib.pyplot as plt

x = [25,34,32,26]
y = [12,42,16,67]

plt.plot(x,y, label = 'line1', linewidth = 5, color = 'b')

x1 = [53,13,75,29]
y1 = [46,73,26,16]

plt.plot(x1,y1, label = 'line2', linewidth = 7, color = 'r')

plt.legend()
plt.show()