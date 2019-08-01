#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 10:19:38 2019

@author: ankusmanish
"""

a = (1,2,3,4,4,5,29,56,3,5,2,86)

lis = []
#loop for checking repeated items in a tuple
for i in range(len(a)):
    if a.count(a[i]) > 1:
           lis.append(a[i])
            
print(tuple(set(lis)))