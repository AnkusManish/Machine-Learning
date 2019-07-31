#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 22:54:38 2019

@author: ankusmanish
"""

a = set([1,2,3,4,5,6])

#discard() method removes the item from the set if exists and does not raise any error if not exists
a.discard(9)

print(a)