#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 13:40:19 2019

@author: ankusmanish
"""

m = 'Hi this is Manish'
m = m.lower()
words = [word for word in m]
for i in words:
    print(i,'--',words.count(i))