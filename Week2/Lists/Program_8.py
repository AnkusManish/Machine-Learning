#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 00:04:42 2019

@author: ankusmanish
"""

a = ['Manish','Ria','Yedukondalu', 'Omshanthiom','Advik','gggszdgsgr','sshdgre']

num = int(input('Enter your number '))

#loop that checks for the length of strings in the list
for i in range(len(a)):
    if len(a[i]) > num:
        print(a[i])