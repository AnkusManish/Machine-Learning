#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 23:13:13 2019

@author: ankusmanish
"""

a = set([1,2,3,4,5])
b = set([2,4,7,8,5])

#differecne() method returns a set of values only consisting in first set
res = a.difference(b)
print(res)

#second way of doing the same
c = a-b
print(c)