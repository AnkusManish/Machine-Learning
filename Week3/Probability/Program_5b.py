#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 15:41:05 2019

@author: ankusmanish
"""

from fractions import Fraction

rain_given_trafic_and_late = Fraction(1,12)

print('Probability going late given rain nad traffic : {}'.format(rain_given_trafic_and_late))

late_given_no_trafic_and_rain = Fraction(1, 24)

print('Prbability going late given rain and no traffic : {}'.format(late_given_no_trafic_and_rain))

late_given_trafic_and_no_rain = Fraction(1,24)

print('Pobability going late given not raining and heavy trafic : {}'.format(late_given_trafic_and_no_rain))

late_given_no_trafic_and_no_rain = Fraction(1,16)

print('Probability going late given no rain and no traffic : {}'.format(late_given_no_trafic_and_no_rain))

result = late_given_no_trafic_and_no_rain + late_given_no_trafic_and_rain + late_given_trafic_and_no_rain + rain_given_trafic_and_late

print('Probability of not being late : {}'.format(result))