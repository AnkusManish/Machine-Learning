#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 20:29:28 2019

@author: ankusmanish
"""

# Write a Python program to create bar plots with errorbars on the same figure. Attach a text label above each bar displaying men means (integer value)

import numpy as np
import matplotlib.pyplot as plt

Mean_Velocity= [0.2474, 0.1235, 0.1737, 0.1824]


Standard_Deviation=[0.3314, 0.2278, 0.2836, 0.2645]


index = np.arange(len(Mean_Velocity))    

width = 0.35   
plt.bar(index, Mean_Velocity,yerr=Standard_Deviation, color='red') #yerr will add errorbars to the bar tips with + and - sizes relative to the data
plt.ylabel('Scores')
plt.xlabel('Velocity')
plt.title('Scores by Velocity')
plt.show()