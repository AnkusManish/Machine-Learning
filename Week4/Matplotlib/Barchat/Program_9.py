#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 20:26:41 2019

@author: ankusmanish
"""

# Write a Python programming to display a bar chart of the popularity of programming Languages. Increase bottom margin

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
import numpy as np

data = pd.read_clipboard(sep = ',')
print(data)

b = np.arange(len(data['Popularity ']))

plt.bar(b, height = data['Popularity '], color = 'y', edgecolor = 'b', linewidth = 2)
plt.xticks(b, data['Languages'])
plt.subplots_adjust(bottom=0.8, top=0.9) 

plt.show()