#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 13:13:00 2019

@author: ankusmanish
"""

#Write a Python program to remove specific elements in a numpy array

import numpy as np

a = np.array([10,20,30,40,50,60,70,80,90,100])

a = np.delete(a, [1,4,5])

print(a)