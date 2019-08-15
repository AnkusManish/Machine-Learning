#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 12:53:11 2019

@author: ankusmanish
"""

#Write a Python program to find the set exclusive-or of two arrays. 
#Set exclusive-or will return the sorted, unique values that are in only one (not both) of the input arrays

import numpy as np

a = np.array([0,10,20,40,60,80])
b = np.array([10,30,40,50,70])

a = set(a)
b = set(b)

result = a.symmetric_difference(b)

print('The unique values of both the arrays are : {}'.format(result))