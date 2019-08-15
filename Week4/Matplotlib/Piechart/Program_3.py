#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 20:31:51 2019

@author: ankusmanish
"""

#Write a Python programming to create a pie chart of gold medal achievements of five most successful countries in 2016 Summer Olympics. 
#Read the data from a csv file

"""
country,gold_medal
United States,46
Great Britain,27
China,26
Russia,19
Germany,17
"""

import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_clipboard(sep = ',')

plt.pie(data['gold_medal'], labels = data['country'], shadow = True,radius = 1.5)
plt.title('My Pie chart', pad = 40)
plt.show()