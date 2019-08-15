#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 12:33:55 2019

@author: ankusmanish
"""

#Write a Python program to create a null vector of size 10 and update sixth value to 11

import numpy as np

a = np.zeros(10)
a[5] = 11

print(a)