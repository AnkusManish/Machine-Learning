
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 15:23:26 2019

@author: ankusmanish
"""

from fractions import Fraction

ace = int(input('Enter the number of ace cards in a deck '))
no_of_cards = int(input('Enter the total number of cards in a deck '))
print()

#function that returns the probability of drawing an ACE from a deck of cards
def func(ace,no_of_cards):
    
    print('Total number of cards in a playing deck are : {}'.format(no_of_cards))
    
    print('Total number of Ace cards in a playing deck is : {}'.format(ace))
    
    result = Fraction(ace, no_of_cards)

    print('The probability of drawing an Ace card is : {}'.format(result))
    
func(ace,no_of_cards)    