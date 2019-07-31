#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 20:30:19 2019

@author: ankusmanish
"""
import array as arr

a = arr.array('i',[10, 20, 30, 40, 50])
b = arr.array('i',[])

for i in range(len(a) - 1,-1,-1):
    b.append(a[i])
print('Actuacl array : {}'.format(a))    
print('Reversed array : {}'.format(b))    