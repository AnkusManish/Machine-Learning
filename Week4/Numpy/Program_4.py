#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 12:36:15 2019

@author: ankusmanish
"""

#Write a Python program to reverse an array (first element becomes last)
import numpy as np

a = np.array([12,13,14,15,16,17,18,19,20])

first_element = a[0]
last_element = a[-1]

a[0] = last_element
a[-1] = first_element

print(a)