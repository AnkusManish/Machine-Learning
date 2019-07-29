#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 16:42:39 2019

@author: ankusmanish
"""

import os 
  
# This is to get the directory of the folder/file
dir_path = '/Users/ankusmanish/Desktop/Training/temp'
  
for root, dirs, files in os.walk(dir_path): 
    for file in files:    
        #endswith() method helps us to search the fie with any extension
        if file.endswith('.pages'): 
            print(file)
        
            
            
           