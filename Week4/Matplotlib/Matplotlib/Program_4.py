#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 20:01:05 2019

@author: ankusmanish
"""

#Write a Python program to draw line charts of the financial data of Alphabet Inc. between October 3, 2016 to October 7, 2016

"""
Date,Open,High,Low,Close
03-10-16,774.25,776.065002,769.5,772.559998
04-10-16,776.030029,778.710022,772.890015,776.429993
05-10-16,779.309998,782.070007,775.650024,776.469971
06-10-16,779,780.47998,775.539978,776.859985
07-10-16,779.659973,779.659973,770.75,775.080017 
"""
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_clipboard(sep = ',')

data.plot()