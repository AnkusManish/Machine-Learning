#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 10:46:40 2019

@author: ankusmanish
"""

string = 'string'

#checks if string length is greater than 3
if len(string) >= 3:
    #condition checking if the string ends with 'ing'
    if string.endswith('ing'):
        string = string + 'ly'
    else:
        string = string + 'ing'
        
print(string)        