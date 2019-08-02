#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 23:50:39 2019

@author: ankusmanish
"""

a = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

#sorting elements based on the last element in the tuple
print(sorted(a, key = lambda x : x[1]))