#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 20:31:18 2019

@author: ankusmanish
"""

import array as arr

a = arr.array('i',[10, 20, 30, 40, 50, 50, 20, 20, 20])

m = list(set(a))
for i in range(len(m)):
    print('The count of',a[i],'is : {}'.format(a.count(m[i])))