#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 19:27:26 2019

@author: ankusmanish
"""

#Write a Python program to create and display a one-dimensional
# array-like object containing an array of data using Pandas module

import pandas as pd

data = pd.Series(data = [1,2,3,4,5,6,7,8,9,10])

print(data)