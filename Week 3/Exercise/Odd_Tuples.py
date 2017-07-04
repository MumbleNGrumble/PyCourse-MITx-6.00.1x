# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 10:55:09 2017

@author: Daniel
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    
    l = []
    
    for index, value in enumerate(aTup):
        if index % 2 == 0:
            l.append(value)
    
    return tuple(l)