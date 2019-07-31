#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 22:36:38 2019

@author: ankusmanish
"""

my_dict = {'C1':[1,2,3],'C2':'Manish','C3':[9,10,11]}

lis = []
#condition for checking the type is list or not
for k,v in my_dict.items():
    if type(v) == list:
        lis.append(v)
        
print('The count of lists in dictionary is : {}'.format(len(lis)))