#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 15:38:22 2019

@author: ankusmanish
"""

from fractions import Fraction

not_raining = Fraction(2,3)

print('Probability it is not raining : {}'.format(not_raining))

No_rain_heavy_traffic = Fraction(1,4)

print('Probability not raining given heavy traffic : {}'.format(No_rain_heavy_traffic))

Not_late_given_no_rain_intersection_traffic = Fraction(3,4)

print('Probability not getting late given no rain intersection heavy traffic : {}'.format(Not_late_given_no_rain_intersection_traffic))

result = not_raining * No_rain_heavy_traffic * Not_late_given_no_rain_intersection_traffic

print("Probability that it is not raining, heavy traffic and I'm not late : {}".format(result))