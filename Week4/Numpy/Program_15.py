#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 12:54:17 2019

@author: ankusmanish
"""

#Write a Python program compare two arrays using numpy
import numpy as np 

a = np.array([1,2])
b = np.array([4,5])

print(a > b)
print(a >= b)
print(b > a)
print(b >= a)