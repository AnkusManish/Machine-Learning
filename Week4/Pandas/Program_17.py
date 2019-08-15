#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 19:51:57 2019

@author: ankusmanish
"""

#Write a Python program to append a new row 'k' to data frame with given values for each column. 
#Now delete the new row and return the original DataFrame

import pandas as pd
import numpy as np

data = pd.DataFrame(data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']},
index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])


data.loc['k'] = ['Manish',22,3,'yes']

print(data)

data.drop('k',axis = 0)

print(data)