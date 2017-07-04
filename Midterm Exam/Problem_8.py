# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 01:31:01 2017

@author: Daniel
"""

def general_poly (L):
    """
    L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0
    """
    
    #YOUR CODE HERE
    
    def coefficient(x):
        k = len(L) - 1
        ans = 0
        
        for n in L:
            ans += n * x**k
            k -= 1
        
        return ans
    
    return coefficient