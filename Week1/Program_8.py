#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 12:38:03 2019

@author: ankusmanish
"""

import matplotlib.pyplot as plt

#taking input(int) from the user and splitting it with a comma
given_list = [int(x) for x in input('Enter the numbers ').split(',')]

#plotting histogram with hist method by passing the data given by the user
plt.hist(given_list, bins=5, color='y', edgecolor='b', alpha=0.4)

#x-axis label
plt.xlabel('Given list of values')
#y-axis label
plt.ylabel('Number count')
#title for the histogram
plt.title('Histogram')