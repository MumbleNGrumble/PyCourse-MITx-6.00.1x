# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 17:29:19 2017

@author: Daniel.Le
"""

def max_val(t): 
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """ 
    
    maxList = []
    
    if type(t) == int:
        return t
    else:
        for element in t:
            maxList.append(max_val(element))
    
    return max(maxList)