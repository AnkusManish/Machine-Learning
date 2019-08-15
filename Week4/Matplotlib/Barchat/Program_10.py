#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 20:27:22 2019

@author: ankusmanish
"""

#Write a Python program to create bar plot of scores by group and gender. Use multiple X values on the same chart for men and women

import matplotlib.pyplot as plt
import numpy as np

men = [22, 30, 35, 35, 26]
women = [25, 32, 30, 35, 29]

x = np.arange(len(men))
y = np.arange(len(women))

plt.figure(figsize = (8,8))
plt.bar(y - 0.2, women, width = .4)
plt.bar(x + 0.2, men, width = .4)
plt.legend(['men','women'])