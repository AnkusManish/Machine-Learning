#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 16:26:05 2019

@author: ankusmanish
"""

print('Given Conditions : ')
print('\n')
#A be the evnet of prescribes narcotic patient
print('P(A) : {}'.format(0.1))
#B be the event of addict
print('P(B) : {}'.format(0.5))
print('Probability of addicts given narcotic patient : {}'.format(0.8))
print()
print('P(A | B) = P(B|A)P(A)/ P(B)')
result = (0.8 * 0.1) / 0.5
print()
print('P(A | B) = {}'.format(result))