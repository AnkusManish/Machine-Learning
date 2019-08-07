#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 16:20:18 2019

@author: ankusmanish
"""

from fractions import Fraction

late_given_trafic_and_rain = Fraction(1,12)

print('Probability going late given raining and traffic : {}'.format(late_given_trafic_and_rain))

late_given_no_trafic_and_rain = Fraction(1,24)

print('Probability going late given rain and no traffic : {}'.format(late_given_no_trafic_and_rain))

probability_being_late = Fraction(11,48)

print('Probability of going late : {}'.format(probability_being_late))

result = Fraction((late_given_trafic_and_rain + late_given_no_trafic_and_rain),(probability_being_late))

print('Probability going late given that is rains : {}'.format(result))