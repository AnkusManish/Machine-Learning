#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 16:44:53 2019

@author: ankusmanish
"""

print('The Correlation coefficient between two variables is given by : ')
print('r = (n∑(xy) - (∑x)(∑y)) / √(n∑x^2)-(∑x^2)√(n∑y^2)-(∑y^2)')
print()
print('From the given data we get :')
print('n = 9')
print('∑x = 622')
print('∑y = 773')
print('∑xy = 53,336')
print('∑x^2 = 43,206')
print('∑y^2 = 68,007')
print()
print('Substituting the above values in the formula we get :')
print('r = (9 * 53336 - 662 * 773) / √9(43206)-(43206) * √9(68007)-(68007)')
r = (9 * (53336 - 62) - (662 * 773)) / (9 * (43206)-(43206))**1/2 * (9 * (68007)-(68007))**(1/2)
print(' '*2,'= -782 / 5350.89')
print(' '*2,'= -0.15')