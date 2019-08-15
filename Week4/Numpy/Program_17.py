#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 12:59:33 2019

@author: ankusmanish
"""

#Write a Python program to change the data type of an array

import numpy as np

a = np.array([[2,4,6],[6,8,10]])

a = a.astype('float')

print(a)