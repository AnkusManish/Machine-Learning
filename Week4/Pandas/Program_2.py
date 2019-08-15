#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 19:30:13 2019

@author: ankusmanish
"""

# Write a Python program to convert a Panda module Series to Python list and it's type

import pandas as pd

data = pd.Series(data = [1,2,3,4,5,6,7,8,9,10])

print(type(data))

data = list(data)

print(type(data))