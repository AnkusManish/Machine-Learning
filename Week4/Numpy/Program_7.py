#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 12:42:56 2019

@author: ankusmanish
"""

#Write a Python program to create a 8x8 matrix and fill it with a checkerboard pattern

import numpy as np

a = np.zeros((8,8))

a[:-1:2,:-1:2] = 1 

a[1::2,:] = 1

a[1::2,::2] = 0

print(a)