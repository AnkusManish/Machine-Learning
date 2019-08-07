#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 16:25:03 2019

@author: ankusmanish
"""

print('Conditions Given :')
print('\n')
print('Total number of bits in a data packet : {}'.format(1000))
print('Error Probability : {}'.format(0.1))
print()
µ = 0.1
print('Mean : {}'.format(µ))
variance = 'µ(1-µ) = 0.1(1-0.1) = 0.09'
print('Variance : {}'.format(variance))
print('P(Y > 120) = P(Y - nµ/√nSigma > 120 - nµ/√nSigma)')
print(' '*10,'=',' 1 - ø(20/√90)')
print(' '*10,'=','0.0222')