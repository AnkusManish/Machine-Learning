#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 20:52:26 2019

@author: ankusmanish
"""

dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50,6:60}
result = {}

result.update(dic1)
result.update(dic2)
result.update(dic3)

print(result)