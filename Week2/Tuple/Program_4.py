#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 10:15:56 2019

@author: ankusmanish
"""

from copy import deepcopy
#create a tuple
tuplex = ("HELLO", 5, [], True) 
#deepcopy() lets you to copy the tuple into a variable
tuplex_colon = deepcopy(tuplex)
tuplex_colon[2].append(50)
print(tuplex_colon)
print(tuplex)