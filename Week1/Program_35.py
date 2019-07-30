#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 14:31:27 2019

@author: ankusmanish
"""

a = [30, 129, 125, 90, 150, 56, 75, 89, 43, 66, 135]

#anonymous function
func = lambda a: a % 15

for i in a:
    #condition to check if the number is exactly divisible by 15
    if func(i) == 0:
        print(i)