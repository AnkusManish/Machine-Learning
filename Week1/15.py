#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 12:53:59 2019

@author: ankusmanish
"""

import os

def func(x):
    print(os.environ[x])
    
func('HOME')    