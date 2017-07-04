# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 21:50:10 2017

@author: Daniel
"""

def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    #YOUR CODE HERE
    
    total = 1
    i = 1
    
    while total < k:
        i += 1
        total += i
    
    if total == k:
        return True
    else:
        return False