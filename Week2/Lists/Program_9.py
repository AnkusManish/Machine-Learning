#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 00:08:29 2019

@author: ankusmanish
"""

a = [1,2,3,4,5,45]
b = [6,7,8,9,0,325,572,45,11]

#functing that returns true if atleast 1 value from list-a consists in list-b
def func(a,b):
    for i in range(len(a)):
        if bool(a[i] in b) == True:
            return True
        
func(a,b)       