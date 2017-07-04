# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 01:55:41 2017

@author: Daniel
"""

def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    
    # Your code here
    
    if len(L1) != len(L2):
        return False
    else:
        d1 = {}
        for item in L1:
            if item in d1:
                d1[item] += 1
            else:
                d1[item] = 1
        
        d2 = {}
        for item in L2:
            if item in d2:
                d2[item] += 1
            else:
                d2[item] = 1
        
        highestOccurance = 0
        for k, v in d1.items():
            if d1[k] != d2[k]:
                return False
            else:
                if d1[k] > highestOccurance:
                    highestOccurance = d1[k]
                    element = k
        
        if highestOccurance > 0:
            return (element, highestOccurance, type(element))
        else:
            return (None, None, None)