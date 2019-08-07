#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 15:28:06 2019

@author: ankusmanish
"""

from fractions import Fraction

#Total number of playing cards
no_of_cards = 52

#number of cards after drawing a king on the first draw
card_negative = 51

#number of ace cards in a deck
ace_cards = 4

#number of king cards in a deck
king_cards = 4

print('Total number of cards in a playing deck are : {}'.format(no_of_cards))

print('Number of cards after after king has been drawn : {}'.format(card_negative))

#Probability of king give ace
king_given_ace = Fraction(king_cards, card_negative)

#Probability of drawing an Ace
ace = Fraction(ace_cards, no_of_cards)

#Probability of drawing ace given king has already drawn
Ace_intersecton_king = king_given_ace * ace

print('Drawing a King when Ace is already drawn : {}'.format(king_given_ace))

print('Probability of drawing an Ace is : {}'.format(ace))

print('Probability of drawing an ace after drawing a king on the first draw : {}'.format(Ace_intersecton_king))