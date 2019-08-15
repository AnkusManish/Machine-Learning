#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 12:44:11 2019

@author: ankusmanish
"""

#Write a Python program to convert a list and tuple into arrays

import numpy as np

a = [1,2,3,4,5,6,7]

print('a is a',type(a),'object')

a = np.array(a)

print('After converting it into array the type is : {}'.format(type(a)))

print('-------------------------------------------------------------------')

b = (1,2,3,4,5)

print('a is a',type(b),'object')

b = np.array(b)

print('After converting it into array the type is : {}'.format(type(b)))