#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 20:31:12 2019

@author: ankusmanish
"""

#Write a Python programming to create a pie chart with a title of the popularity of programming Languages

"""Languages,Popularity
Java,22.2
Python,17.6
PHP,8.8 
JavaScript,8
C#,7.7
C++,6.7
"""

import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_clipboard(sep = ',')

plt.pie(data['Popularity'], labels = data['Languages'])
plt.title('My Pie chart')
plt.show()