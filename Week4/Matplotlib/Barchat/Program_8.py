#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 20:25:37 2019

@author: ankusmanish
"""

#Write a Python programming to display a bar chart of the popularity of programming Languages. 
#Select the width of each bar and their positions

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
print(data)

b = np.arange(len(data['Popularity ']))
pos = [1,5,8,10,15,17]

plt.bar(pos, height = data['Popularity '], width = [0.2,0.4,0.6,0.8,1,1.2])
plt.xticks(b, data['Languages'])

plt.show()