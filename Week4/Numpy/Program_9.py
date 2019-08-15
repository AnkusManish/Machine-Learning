#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 12:46:12 2019

@author: ankusmanish
"""

#Write a Python program to append values to the end of an array

import numpy as np

a = np.array([10, 20, 30] )

a = np.append(a, [40,50,60,70,80,90])

print(a)