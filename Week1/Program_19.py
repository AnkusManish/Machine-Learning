#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 12:59:13 2019

@author: ankusmanish
"""

import os.path
import time
#getmtime() method returns the modification time of the file
print("Last modified: {}".format(time.ctime(os.path.getmtime('/Users/ankusmanish/Desktop/Training'))))
#getctime() method returns the time of the file creation
print("Created: {}".format(time.ctime(os.path.getctime('/Users/ankusmanish/Desktop/Training'))))