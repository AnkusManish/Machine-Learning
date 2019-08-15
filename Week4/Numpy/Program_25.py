#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 13:10:38 2019

@author: ankusmanish
"""

#Write a Python program to suppresses the use of scientific notation for small numbers in numpy array

import numpy as np

a = np.array([1.60000000e-10,1.60000000e+00,1.20000000e+03,2.35000000e-01])

np.set_printoptions(suppress = True)

print(a)