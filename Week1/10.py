#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 12:43:15 2019

@author: ankusmanish
"""

color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"])

list3 = [a for a in color_list_1 if a not in color_list_2]    
print(set(list3))