#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 23:21:03 2019

@author: ankusmanish
"""

a = set([1,2,3,4,5])
b = set([2,4,7,8,5])

#symmetric_difference returns a set from set-a and set-b except the common items
res = a.symmetric_difference(b)

print(res)