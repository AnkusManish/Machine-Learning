#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 13:06:48 2019

@author: ankusmanish
"""

# Write a Python program to create an array of (3, 4) shape,
#multiply every element value by 3 and display the new array

import numpy as np

a = np.array([[0,1,2,3],
              [4,5,6,7],
              [8,9,10,11]])

a = a * 3

print(a)