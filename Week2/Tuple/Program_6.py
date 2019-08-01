#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 10:21:28 2019

@author: ankusmanish
"""

a = (1,2,3,4,4,5,29,56,3,5,2,86)

num = int(input('Enter a number '))

#condition for checking if given number is present in the tuple
if num in a:
    print(num,'is present in a')        
else:
    print('Sorry',num,'is not present in a')