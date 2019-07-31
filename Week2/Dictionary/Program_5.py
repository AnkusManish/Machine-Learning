#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 20:59:10 2019

@author: ankusmanish
"""

a = {}

#anonymous function that squares the given value
func = lambda x : x*x

num = int(input('Enter a number : '))

for i in range(1,num+1):
    a[i] = func(i)
        
print(a)    