#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 21:28:58 2019

@author: ankusmanish
"""

data = [{'id': 1, 'success': True, 'name': 'Lary'},
         {'id': 2, 'success': False, 'name': 'Rabi'},
         {'id': 3, 'success': True, 'name': 'Alex'}]

a = 0
#loop that counts the 'true' value
for i in range(len(data)):
    if data[i]['success'] == True:
        a = a + 1

print('The count of true value is : {}'.format(a))  
