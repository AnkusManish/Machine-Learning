#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 12:55:13 2019

@author: ankusmanish
"""

#Write a Python program to create a contiguous flattened array

import numpy as np

a = np.array([[10,20,30],[20,40,50]])

a = np.ravel(a)

print(a)