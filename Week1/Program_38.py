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
#loop that converts the list of numbers to 0 and stores them in lis variable
for i in range(num):
     lis.append(str(i*0))
#adding the zeros list and string list     
add = lis + str_list 
words = ' '.join(add)
print(words)