#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 13:11:32 2019

@author: ankusmanish
"""

#Write a Python program to how to add an extra column to an numpy array

import numpy as np

a = np.array([[10,20,30],
              [40,50,60]])

b = np.array([[2],[3]])

a = np.append(a, b, axis = 1)

print(a)