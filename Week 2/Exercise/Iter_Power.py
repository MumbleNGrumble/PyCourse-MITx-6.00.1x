# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 09:19:36 2017

@author: Daniel
"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    
    ans = 1
    
    for i in range(exp):
        ans *= base
    
    return ans