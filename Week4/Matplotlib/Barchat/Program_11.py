#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 20:28:03 2019

@author: ankusmanish
"""

#Write a Python program to create bar plot from a DataFrame

"""
a,b,c,d,e
2,4,8,5,7,6
4,2,3,4,2,6
6,4,7,4,7,8
8,2,6,4,8,6
10,2,4,3,3,2
"""

import pandas as pd

data = pd.read_clipboard(sep = ',')

data.plot(kind = 'bar')