#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 12:44:17 2019

@author: ankusmanish
"""

import os

def func(x):
    print(os.path.exists(x))
    
func('/Users/ankusmanish/Desktop/SAS')    

#returns a boolean value True if the file exists else returns False