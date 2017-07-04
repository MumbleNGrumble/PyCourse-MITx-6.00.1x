# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 09:23:27 2017

@author: Daniel
"""

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    
    if exp == 0:
        return 1
    else:
        return recurPower(base, exp - 1) * base