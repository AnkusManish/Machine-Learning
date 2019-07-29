#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 12:19:30 2019

@author: ankusmanish
"""

#taking the input(int) from the user and splitting the nos with a comma
a = [int(x) for x in input("Enter the numbers ").split(',')]

#converting the given numbers to tupple
print('The tuple is : {}'.format(tuple(a)))
#converting the given numbers to list
print('The list is : {}'.format(list(a)))
