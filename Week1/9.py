#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 12:41:02 2019

@author: ankusmanish
"""

given_list = [int(x) for x in input('Enter the numbers').split(',')]
lis = []
for i in given_list:
    lis.append(str(i))
print(lis)  