#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 12:32:51 2019

@author: ankusmanish
"""

from datetime import date
#creating date time object for the given date
first_date = date(2014, 7, 2)
last_date = date(2014, 7, 11)
num_of_days = last_date - first_date
#printing number of days
print(num_of_days.days)