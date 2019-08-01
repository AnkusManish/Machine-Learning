#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 10:49:01 2019

@author: ankusmanish
"""

string = 'Hey Manish here rgergnerger'

a = string.split(' ')

lis = []

#loop thats returns the length of the words present in the string
for i in range(len(a)):
    lis.append(len(a[i]))
    
print(max(lis))    