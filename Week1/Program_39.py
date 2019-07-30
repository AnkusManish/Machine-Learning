#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 16:42:39 2019

@author: ankusmanish
"""

import os 
  
# This is to get the directory of the folder/file
dir_path = '/Users/ankusmanish/Desktop'

for fname in os.listdir(dir_path):
    path = os.path.join(dir_path, fname)
    if os.path.isfile(path):
        print(dir_path + '/' + fname)
        
            
            
           