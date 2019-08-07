#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 15:34:53 2019

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
H T T
T H T
T T H
'''
possible_outcomes = 3

result = Fraction(possible_outcomes, total_outcomes)

print('Probability of obtaining one head : {}'.format(result))