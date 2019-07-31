#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 21:52:20 2019

@author: ankusmanish
"""

d = {'val_1':8,'val_2':21,'val_3':7,'val_4':20,'val_5':47,'val_6':53,'val_7':29,'val_8':88,'val_9':38}
 
#list of values to check in the dictionary
a = list({'val_1', 'val_2', 'val_3', 'val_4', 'val_5', 'val_6', 'val_7', 'val_4', 'val_9'})

#condition to check if all the elements are present in the Dictionary
result =  all(elem in list(d.keys()) for elem in a)

if result:
    print('Given keys are present in the Dictionary')
else:
    print('Given keys are not present in the dictionary')
        