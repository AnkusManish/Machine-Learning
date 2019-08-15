#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 13:05:45 2019

@author: ankusmanish
"""

#Write a Python program to make an array immutable (read-only)

import numpy as np

a = np.ones((3,3))

a.flags.writeable = False

a[0] = 3