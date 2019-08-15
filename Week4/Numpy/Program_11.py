#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 12:48:49 2019

@author: ankusmanish
"""

#
# Write a Python program to find the number of elements of an array, length of one array
# element in bytes and total bytes consumed by the elements

import numpy as np
import sys

a = np.array([1,2,3])

lis = []

print('Length of the array is : {}'.format(len(a)))
print('Size of one element is : {}'.format(sys.getsizeof(a[0])))
for i in a:
    lis.append(sys.getsizeof(i))
    
print('Total size of the array is : {}'.format(sum(lis)))    
