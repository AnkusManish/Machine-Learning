#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 12:41:02 2019

@author: ankusmanish
"""
#taking input(int) from the user and splitting it with a comma
given_list = [int(x) for x in input('Enter the numbers ').split(',')]
lis = []
#looping the given list, converting the numbers to string and storing them in the lis variable
for i in given_list:
    lis.append(str(i))
print('The given string is {}'.format(' '.join(lis)))  