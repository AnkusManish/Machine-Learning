#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 12:18:26 2019

@author: ankusmanish
"""

first_name = input('Enter your first Name ')
last_name = input('Enter your last name ')
string = first_name + ' ' + last_name
word_list = string.split(' ')
words = [word[::-1] for word in word_list]
words = ' '.join(words)
print('The reverse string is : {}'.format(words))