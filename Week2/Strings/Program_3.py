#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 10:41:23 2019

@author: ankusmanish
"""

string = 'restart'

#holds first letter of the string
char = string[0]
#replaces the 2nd occurrence of first letter in the string
str1 = string.replace(char, '$')
#conbing the first letter and the replaced string
str2 = char + str1[1:]

print(str2)