#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 20:15:24 2019

@author: ankusmanish
"""

#Write a Python program to display the grid and draw line charts of the closing value of Alphabet Inc. 
#between October 3, 2016 to October 7, 2016. 
#Customized the grid lines with linestyle -, width .5. and color blue.

"""
Date,Close
03-10-16,772.559998
04-10-16,776.429993
05-10-16,776.469971
06-10-16,776.859985
07-10-16,775.080017
"""

import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_clipboard(sep = ',')
x = data['Date']
y = data['Close']
plt.plot(x,y)
plt.xlabel('Date')
plt.ylabel('Closing Value')
plt.grid(linewidth=0.5,linestyle='dashdot',color='k')
plt.title('closing value of Alphabet Inc')
plt.show()