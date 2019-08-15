#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 20:05:38 2019

@author: ankusmanish
"""

#Write a Python program to plot several lines with different format styles in one command using arrays

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,0.5,0.05)

plt.plot(x, x**2,'b--', x, x**3,'r*', x, x**4, 'yo')

plt.show()