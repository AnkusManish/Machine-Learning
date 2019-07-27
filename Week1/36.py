#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 14:33:48 2019

@author: ankusmanish
"""

try:
    y = 2  #if y is not defined it returns variable is not defined
except NameError:
    print("Variable is not defined....!")
else:
    print("Variable is defined.")