#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 12:57:58 2019

@author: ankusmanish
"""

import time
start_time = time.time()

#Sample program
color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"])

list3 = [a for a in color_list_1 if a not in color_list_2]    
print(set(list3))

total_time = time.time() - start_time

print("{} seconds".format(total_time))