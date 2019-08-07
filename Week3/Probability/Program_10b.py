#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 16:36:58 2019

@author: ankusmanish
"""

µ = 30
σ = 4
x = 21
result = (x - µ) /σ
print('z = (x - µ) /σ')
print(' ','= (21 - 30) / 4')
print(' ','= ',result)
print()
print('Total are - area to the left')
#Z() = 0.0122
final_result = 1 - 0.0122
print()
#The area to the left of 2.5
print('P(z > -2.5) = ',final_result)