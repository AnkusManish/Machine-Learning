#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 11:09:46 2019

@author: ankusmanish
"""

string = 'HEY MANISH HERE'

num = int(input('Enter the number '))

#indexing from 0 to given number
str1 = string[:num]

#indexing from given number to the end of the string
str0 = string[num:]

#converting the string to lowercase upto the give number 
str1 = str1.lower()

#combing the lists
result = str1 + str0

print(result)