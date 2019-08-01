#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 10:53:10 2019

@author: ankusmanish
"""

#takes the values with comma seperated and stores them in a list
string = [x for x in input('Enter your string values ').split(',')]

#sorts the list alphanumerically 
string = set(sorted(string))

print(string)