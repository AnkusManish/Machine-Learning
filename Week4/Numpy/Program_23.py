#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 13:08:04 2019

@author: ankusmanish
"""

#Write a Python program to convert a NumPy array into Python list structure

import numpy as np

a = np.array([[0,1],
              [2,3],
              [4,5]])

print(type(a))

a = np.ndarray.tolist(a)

print(a)
print(type(a))