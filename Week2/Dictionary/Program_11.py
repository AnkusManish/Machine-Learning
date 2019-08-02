#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 06:46:33 2019

@author: ankusmanish
"""

num_list = [1, 2, 3, 4]
#creating two empty dictionaries
current = new_dict = {}
#loop that stores one dictionary inside another
for name in num_list:
    current[name] = {}
    current = current[name]
print(new_dict)