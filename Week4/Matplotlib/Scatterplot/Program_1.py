#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 21:54:11 2019

@author: ankusmanish
"""

#Write a Python program to draw a scatter graph taking a random distribution in X and Y and plotted against each other

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.1,.8,.1)

plt.figure(figsize = (7,6))
plt.scatter(x = x, y = x**2, marker = '*', alpha = 1)
plt.show()
