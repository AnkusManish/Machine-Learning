#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 10:32:23 2019

@author: ankusmanish
"""

a = (1,2,3,4,5)

a = list(a)

lis = []

#loop that appends values to lis in reverse order
for i in range(len(a),0,-1):
    lis.append(i)
    
print('Reversed tuple is : {}'.format(tuple(lis)))    