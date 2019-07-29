#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 12:48:39 2019

@author: ankusmanish
"""

def func(x):
    from subprocess import call
    call(x)
    
#function that takes external commands and outputs them accordingly
func('ls')  

