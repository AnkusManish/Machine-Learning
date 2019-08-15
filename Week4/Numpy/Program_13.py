#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 12:51:16 2019

@author: ankusmanish
"""

#Write a Python program to find the set difference of two arrays.
#The set difference will return the sorted, unique values in array1 that are not in array2

import numpy as np

a = np.array([0,10,20,40,60,80])
b = np.array([10, 30, 40, 50, 70, 90])

result = set(a) - set(b)

print('The set difference is : {}'.format(result))