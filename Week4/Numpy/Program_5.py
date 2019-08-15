#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 12:37:34 2019

@author: ankusmanish
"""

#Write a Python program to create a 2d array with 1 on the border and 0 inside

import numpy as np

a = np.ones((5,5))

a[1:-1,1:-1] = 0

print(a)