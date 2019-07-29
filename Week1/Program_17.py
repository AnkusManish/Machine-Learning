#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 12:57:58 2019

@author: ankusmanish
"""

import time
#time() method stores the number of seconds passed since epoch
start_time = time.time()
print(start_time)
#Sample program
color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"])

list3 = [a for a in color_list_1 if a not in color_list_2]    
print(set(list3))

#time difference between before and after executing the rogram
total_time = time.time() - start_time

print("{} seconds".format(total_time))