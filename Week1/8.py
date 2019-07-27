#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 12:38:03 2019

@author: ankusmanish
"""

import matplotlib.pyplot as plt

given_list = [int(x) for x in input('Enter the numbers ').split(',')]

plt.hist(given_list, bins=5, color='y', edgecolor='b', alpha=0.4)

plt.xlabel('Given list of values')
plt.ylabel('Number count')
plt.title('Histogram')