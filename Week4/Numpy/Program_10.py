#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 12:47:23 2019

@author: ankusmanish
"""

#Write a Python program to find the real and imaginary parts of an array of complex numbers


a = [ 1.00000000+0.j, 0.70710678+0.70710678j] 

for i in a:
    print('Real number :',i.real)
    print('Imaginary number :',i.imag)