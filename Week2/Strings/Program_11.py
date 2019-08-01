#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 11:05:25 2019

@author: ankusmanish
"""

string = 'Manish Ankus'

words = string.split(' ')

#Reversing the given string
string = [word[::-1] for word in words]

#joining the strings from the list
print(' '.join(string))    