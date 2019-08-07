#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 17:37:38 2019

@author: ankusmanish
"""

from random import randint
from fractions import Fraction

#lis contains 10 randomly obtined outcomes between 2 to 7
lis = []
for i in range(10):
    lis.append(randint(2,7))
    
print('The outcomes for 10 random samples are: ',lis)    
print()   
#lis1 contains common items for randomly obtained outcomes 
lis1 = list(set(lis))
for i in range(len(lis1)):
    print('Probability of ',lis1[i],'is ', Fraction(lis.count(lis1[i]), len(lis)))