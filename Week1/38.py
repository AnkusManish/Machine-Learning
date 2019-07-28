#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 16:02:36 2019

@author: ankusmanish
"""

str_str = 'Hi this is Manish' 
str_list = str_str.split(' ')
lis = []
num = int(input('Enter the number of zeros you want to add before the string '))
for i in range(num):
     lis.append(str(i*0))
add = lis + str_list 
words = ' '.join(add)
print(words)