#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 16:21:37 2019

@author: ankusmanish
"""

from fractions import Fraction

statement_1 = Fraction(1, 100)

statement_2 = Fraction(90, 100)

statement_3 = Fraction(8, 100)

statement_4 = Fraction(99, 100)

print('Given conditions : ')
print('\n')
print('One percent of women over 50 have breast cancer : {}'.format(statement_1))
print('Ninety percent of women who have breast cancer test positive on mammograms : {}'.format(statement_2))
print('Eight percent of women will have false positives : {}'.format(statement_3))
print('Probability not having cancer : {}'.format(statement_4))
print()
result = Fraction((statement_2 * statement_1), (statement_2 * statement_1) + (statement_3 * statement_4))
print('Probability that a woman has cancer if she has a positive mammogram : {}'.format(result))