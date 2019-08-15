#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 12:50:23 2019

@author: ankusmanish
"""

#Write a Python program to find common values between two arrays

import numpy as np

a = np.array([0,10,20,40,60])
b = np.array([10,30,40])

lis = []

for i in a:
    if i in b:
        lis.append(i)
        
print('The common elements are : {}'.format(lis))               