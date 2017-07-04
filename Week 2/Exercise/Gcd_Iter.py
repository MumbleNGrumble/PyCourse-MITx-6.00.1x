# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 09:31:08 2017

@author: Daniel
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    
    if a <= b:
        rangeStart = a
    else:
        rangeStart = b
    
    for num in range(rangeStart, 0, -1):
        if a % num == 0 and b % num == 0:
            return num