#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 13:43:50 2019

@author: ankusmanish
"""

import requests

link = "http://www.towardsdatascience.com"
#get() method returns the complete html script for the given page
f = requests.get(link)
print(f.text)