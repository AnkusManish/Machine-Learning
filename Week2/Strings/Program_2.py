#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 10:38:32 2019

@author: ankusmanish
"""

a = 'Hey Manish here'
a = a.lower()

b = {}
lis = list(a)
#loop that keeps a count on the characters present in the string
for i in lis:
    b[i] = lis.count(i)
    
print(b)    