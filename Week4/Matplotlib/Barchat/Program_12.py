#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 20:28:45 2019

@author: ankusmanish
"""

#Write a Python program to create bar plots with error bars on the same figure.

"""
Mean_velocity,Standard_deviation
0.2474, 0.3314
0.1235, 0.2278
0.1737, 0.2836
0.1824, 0.2645
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_clipboard(sep = ',')

x = np.arange(len(data['Mean_velocity']))

plt.bar(x, height = data['Mean_velocity'], yerr = data['Standard_deviation'], capsize = 5)