#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 17:12:58 2019

@author: ankusmanish
"""

a = [45,24,6,2,63,77,22,56,44,52,73]

#finding the max number
max_num = 0

for i in a:
    if (i > max_num):
        max_num = i
print('The max number is',max_num)   

#finding the minimum number
min_num = a[0]

for i in a:
    if (i <= min_num):
        min_num = i
        
print('The min number is',min_num)  