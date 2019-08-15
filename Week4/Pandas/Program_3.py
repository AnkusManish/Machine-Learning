#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 19:31:42 2019

@author: ankusmanish
"""

#Write a Python program to add, subtract, multiple and divide two Pandas Series

import pandas as pd

data = pd.Series([2, 4, 6, 8, 10])

data1 = pd.Series([1, 3, 5, 7, 9])

a = data + data1

b = data - data1

c = data * data1

d = data / data1

print(a)
print(b)
print(c)
print(d)