#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 15:32:25 2019

@author: ankusmanish
"""

from fractions import Fraction

'''
H H H
H H T
H T H
H T T
T T T
T H T
T T H
T H H
'''
total_outcomes = 8

'''
H H H
'''
possible_outcomes = 1

print('The possible outcomes are : {}'.format(possible_outcomes))

result = Fraction(1, total_outcomes)

print('Probability of obtaining H H H is : {}'.format(result))

