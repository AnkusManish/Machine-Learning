#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 13:38:07 2019

@author: ankusmanish
"""

import sys

str_1 = 'Manish'
num_1 = 123

#sys.getsizeof() method returns the size of the value in bytes
print("The size of", str_1 ,"in bytes is : {}".format(sys.getsizeof(str_1)))
print("The size of", num_1 ,"in bytes is : {}".format(sys.getsizeof(num_1)))