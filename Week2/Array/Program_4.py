#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 20:35:14 2019

@author: ankusmanish
"""

import array as arr

a = arr.array('i',[1,3,4,5,7,3,5])

print('The list is : {}'.format(a))

rem = int(input('Enter the number you want to remove from the list '))
a.remove(rem)
print('The list after removing',rem,'is : {}'.format(a))