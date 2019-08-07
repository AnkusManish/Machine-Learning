#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 15:30:42 2019

@author: ankusmanish
"""

from fractions import Fraction

#Total number of playing cards
no_of_cards = 52

#number of ace cards in a deck
ace_cards = 4

#number of ace cards after drawing ace card in the first attempt
ace_card_negative = 3

print('Total number of cards in a playing deck are : {}'.format(no_of_cards))

print('Number of Ace cards in a playing deck : {}'.format(ace_cards))

print('Number of Ace cards after after Ace has been drawn : {}'.format(ace_card_negative))

#probability of drawing an Ace * probability of drawing an ace after ace has been drawn
result = Fraction(ace_cards, no_of_cards) * Fraction(ace_card_negative, no_of_cards)

print('Probability of drawing an ace after drawing an ace on the first draw : {}'.format(result))