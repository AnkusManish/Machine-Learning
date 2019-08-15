#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 20:07:05 2019

@author: ankusmanish
"""

#Write a Python program to create multiple types of charts

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,0.5,0.05)

plt.plot(x, x**2)

plt.scatter(x, x**3)
plt.show()

lis = ['one','two','three','four','five','six','seven','eight','nine','ten']
plt.show()

plt.pie(x, labels = lis, colors = 'rbgyk')

plt.show()



