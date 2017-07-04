# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 09:37:39 2017

@author: Daniel
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)