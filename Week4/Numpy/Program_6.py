#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 12:41:26 2019

@author: ankusmanish
"""

#Write a Python program to add a border (filled with 0's) around an existing array.

import numpy as np

a = np.ones((3,3))

c = np.ones((1,3))

a = np.pad(a, pad_width = 1, mode = 'constant')

print(a)