#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 09:50:34 2019

@author: ankusmanish
"""

a = [1,2,3,4,5,2]
b = [6,7,8,9,0,1]

#Returns the difference between the list
print(list(set(a) - set(b)))