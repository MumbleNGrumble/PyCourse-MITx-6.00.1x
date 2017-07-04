# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 11:17:09 2017

@author: Daniel
"""

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
        
testList = [1, -4, 8, -9]

def applyToEach1(x):
    '''
    Returns the absolute value.
    testList should become [1, 4, 8, 9].
    '''
    
    return abs(x)

def applyToEach2(x):
    '''
    Adds one to the value.
    testList should become [2, -3, 9, -8].
    '''
    
    return x + 1

def applyToEach3(x):
    '''
    Squares the value.
    testList should become [1, 16, 64, 81].
    '''
    
    return x*x