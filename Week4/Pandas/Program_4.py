#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 19:32:43 2019

@author: ankusmanish
"""

#Write a Python program to get the powers of an array values element-wise

import pandas as pd

data = pd.Series([0,1,2,3,4,5,6])

lis = []

func = lambda x : x**2

for i in data:
    lis.append(func(i))
    
print(lis)    