#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 12:34:42 2019

@author: ankusmanish
"""

a = [int(x) for x in input('Enter the list of numbers ').split(',')]

print('Given list is : {}'.format(a))

num_check = int(input('Enter the number you want to check : '))
if num_check in a:
    print(num_check,'is present in the list')
else:
    print('Sorry, the given number in not in the list')
    

    
