#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 13:04:55 2019

@author: ankusmanish
"""

import glob
import os

#glob.glob() checks for all the files with extension .pages
#sort method arranges the files according to the last modifying time

files = glob.glob("/Users/ankusmanish/Desktop/Training/temp/*.pages")
files.sort(key=os.path.getmtime)
print("\n".join(files))
