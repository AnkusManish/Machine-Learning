#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 11:00:51 2019

@author: ankusmanish
"""

import textwrap
string = '''
  The body was found floating near Hoige Bazar at around 6.30am. The next process will go as per law and 
  family members have been informed," Mangaluru police commissioner (city) Sandeep Patil said.
  Nethravathi river is located on the outskirts of Mangaluru - 350km from Bengaluru and very close to the Arabian Sea.
  '''
#fill() method takes the given string and prints within the given width
print(textwrap.fill(string, width=30))