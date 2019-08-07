#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 15:35:33 2019

@author: ankusmanish
"""

from fractions import Fraction

#A be the event of getting atleast one head
#B be the event of getting atleast two heads

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

A = Fraction(7, total_outcomes)

B = Fraction(4, total_outcomes)

print('Probability of getting atleast one head will be : {}'.format(A))

print('Probability of getting atleast two heads will be : {}'.format(B))

result = Fraction(B, A)

print('Probability that you observe at least two heads, given that you have observed at least one head : {}'.format(result))

