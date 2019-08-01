#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 10:25:54 2019

@author: ankusmanish
"""

a = (1,2,3,4,5)

#as tuples are immutable we cannot change tuples so I converted to a list
a = list(a)

num = int(input('Enter the number you want to remove '))

#remove() method removes the given element for the list
a.remove(num)

print('Tuple after removing',num,'is : {}'.format(tuple(a)))