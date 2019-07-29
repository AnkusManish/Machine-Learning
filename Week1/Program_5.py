#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 12:29:37 2019

@author: ankusmanish
"""


import calendar as cal
#Creating an instance for TextCalender()
c = cal.TextCalendar()
#calling formatmonth() method to print the respective month's calendar
strl = c.formatmonth(2025,1, w = 3)
print(strl)

