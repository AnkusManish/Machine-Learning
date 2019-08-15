#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 13:09:31 2019

@author: ankusmanish
"""

#Write a Python program to convert a NumPy array into Python list structure

import numpy as np

a = np.array([0.26153123,0.52760141,0.5718299,0.5927067,0.7831874,0.69746349,0.35399976,0.99469633,0.0694458,0.54711478])

lis = []

for i in a:
    lis.append('{:.3f}'.format(i))
    
print(lis)    