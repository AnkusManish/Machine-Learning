#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 21:56:18 2019

@author: ankusmanish
"""

#Write a Python program to draw a scatter plot comparing two subject marks of Mathematics and Science.
#Use marks of 10 students

import matplotlib.pyplot as plt

math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.figure(figsize = (7,7))
plt.scatter(marks_range, math_marks, color = 'r', s = 100, label = 'Math Marks')
plt.scatter(marks_range, science_marks, color = 'b', s = 100, label = 'Science Marks')
plt.legend()
plt.show()


