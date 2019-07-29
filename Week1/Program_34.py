#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 14:29:59 2019

@author: ankusmanish
"""

import os.path
import time

print('File         :', '/Users/ankusmanish/Desktop/Training/temp')
#printing the access time of the file with getatime() method
print('Access time  :', time.ctime(os.path.getatime('/Users/ankusmanish/Desktop/Training/temp')))
#printing the modification time of the file with getmtime() method
print('Modified time:', time.ctime(os.path.getmtime('/Users/ankusmanish/Desktop/Training/temp')))
#printing the size of the file
print('Size         :', os.path.getsize('/Users/ankusmanish/Desktop/Training/temp'))
