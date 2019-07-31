#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 23:56:21 2019

@author: ankusmanish
"""

a = [1,2,3,4,5,4,5]

lis = []
#loop that checks for repeated elements in the list
for i in a:
    if i not in lis:
        lis.append(i)
        
print(lis)        