#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 13:04:02 2019

@author: ankusmanish
"""

#Write a Python program to concatenate two 2-dimensional arrays

import numpy as np

a = np.array([[0, 1, 3], [5, 7, 9]])
b = np.array([[0, 2, 4], [6, 8, 10]])

a = np.array([np.append(a[0],a[1])])
b = np.array([np.append(b[0],b[1])])

result = np.concatenate((a,b))

print(result)