#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 14:29:59 2019

@author: ankusmanish
"""

import os.path
import time

print('File         :', '/Users/ankusmanish/Desktop/Training/temp')
print('Access time  :', time.ctime(os.path.getatime('/Users/ankusmanish/Desktop/Training/temp')))
print('Modified time:', time.ctime(os.path.getmtime('/Users/ankusmanish/Desktop/Training/temp')))
print('Change time  :', time.ctime(os.path.getctime('/Users/ankusmanish/Desktop/Training/temp')))
print('Size         :', os.path.getsize('/Users/ankusmanish/Desktop/Training/temp'))