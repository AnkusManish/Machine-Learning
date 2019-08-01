#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 10:03:06 2019

@author: ankusmanish
"""

a = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

new = []

#Removing duplicates from list of lists
for i in range(len(a)):
    for ele in a:
        if ele not in new:
            new.append(ele)
            
print(new)            