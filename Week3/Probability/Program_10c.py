#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 16:41:48 2019

@author: ankusmanish
"""

print('Given conditions : ')
print('\n')
print('µ = 30')
print('σ = 4')
print('x = 30')
µ = 30
σ = 4
x = 30
print()
print('z = (x - µ) /σ')
result = (x - µ) / σ
print(' ','= (30 - 30) / 4')
print(' ','= ',result)
#Now x = 35
print()
print('x = 35')
x = 35
print('z = (x - µ) /σ')
result1 = (x - µ) /σ
print(' ','= (35 - 30) / 4')
print(' ','= ',result1)
#Area to the left of z = 1.25 - area to the left of 0
print()
print('Area to the left of 1.25 -  area to the left of 0')
#Z(1.25 = 0.8944 and Z(0) = 0.5)
print('P(0 < Z < 1.25) = 0.8944 - 0.5')
final_result = 0.8944 - 0.5
print(' '*15,'= ',final_result)