#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 20:18:03 2019

@author: ankusmanish
"""

#Write a Python program to create multiple plots

"""The subplots method creates the figure along with the subplots that are then stored in the ax array"""
import matplotlib.pyplot as plt

x = range(10)
y = range(10)

fig, ax = plt.subplots(nrows=2, ncols=2, sharex=True, sharey=True)

ax[0,0].plot(x,y)
ax[0,1].plot(x,y, color = 'r')
ax[1,0].plot(x,y, color = 'y')
ax[1,1].plot(x,y, color = 'k')