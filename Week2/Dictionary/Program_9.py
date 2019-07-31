#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 21:23:50 2019

@author: ankusmanish
"""

my_dict = {'C1':[1,2,3],'C2':[5,6,9],'C3':[9,10,11]}

import pandas as pd

#DataFrame() method stores the data in a tabular format with given columns
data = pd.DataFrame(my_dict)

print(data)