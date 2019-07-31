#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 23:40:33 2019

@author: ankusmanish
"""

a = ['abc', 'xyz', 'aba', '1221']

count = 0
lis = []

#loop that considers items in the 
for i in a:
    lis.append(list(i))
        
    
for i in range(len(a)):
    if lis[i][0] == lis[i][-1]:
        count += 1
    
print(count)  