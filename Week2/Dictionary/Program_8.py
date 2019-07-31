#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 21:15:43 2019

@author: ankusmanish
"""

string = 'Hey Manish here'
#lower() method converts the string to lowercase
string = string.lower()
a = {}
#words variable stores every character in the string in a list
words = [word for word in string]

#loops over every element present in words list
for i in words:
    #stores the element and the count in the dictionary a
    a[i] = words.count(i)
    
print(a)    