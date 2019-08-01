#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 09:58:52 2019

@author: ankusmanish
"""

a = [1,2,3,4,5,2]
b = [6,7,8,9,0,1,4]

lis = []
#loop that checks for common items in the given lists
for i in range(len(a)):
    if a[i] in b:
        lis.append(a[i])
        
print(lis)     