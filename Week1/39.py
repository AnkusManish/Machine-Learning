#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 16:42:39 2019

@author: ankusmanish
"""

import os 
  
# This is to get the directory that the program  
dir_path = '/Users/ankusmanish/Desktop/Training/temp'
  
for root, dirs, files in os.walk(dir_path): 
    for file in files:  
  
        # change the extension from '.pages' to  
        # the one of your choice. 
        if file.endswith('.pages'): 
            print(dir_path+'/'+str(file))
        
            
            
           