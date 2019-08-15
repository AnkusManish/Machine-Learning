#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 13:02:37 2019

@author: ankusmanish
"""

#Write a Python program to create an array which looks like below array

import numpy as np

a = np.tril([[1,1,1],[1,1,1],[1,1,1]], k = -1)

print(a)