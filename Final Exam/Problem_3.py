# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 16:02:23 2017

@author: Daniel.Le
"""

def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
        If there are no digits in s it raises a ValueError exception. """
    
    numOfDigits = 0
    answer = 0
    
    for letter in s:
        if letter.isnumeric():
            answer += int(letter)
            numOfDigits +=  1
        
    if numOfDigits == 0:
        raise ValueError
    else:
        return answer