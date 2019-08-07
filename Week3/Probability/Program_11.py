#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 16:44:20 2019

@author: ankusmanish
"""

print('Conditions given : ')
print('\n')
print('µ = 90')
print('σ = 10')
print('x = 100')
µ = 90
σ = 10
x = 100
print('z = (x - µ) /σ')
print(' ','= (100 - 90) / 10')
result = (x - µ) / σ
print(' ','= ',result)
print()
print('P(Z > 100) = Total area - Area to the left of 1')
#Z(1) = 0.8413
print(' '*10,'= 1 - 0.8413')
final_result = 1 - 0.8413
print(' '*10,'= ',final_result)