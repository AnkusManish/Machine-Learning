#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 09:45:56 2019

@author: ankusmanish
"""

a = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']


x = a[0]
y = a[4]
z = a[5]

#remove() method deletes specified value from the list
a.remove(x)
a.remove(y)
a.remove(z)

print(a)