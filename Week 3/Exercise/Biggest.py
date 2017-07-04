# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 16:22:04 2017

@author: Daniel
"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    
    mostValues = [None, 0]
    
    for k, v in aDict.items():
        if len(v) > mostValues[1]:
            mostValues[0] = k
            mostValues[1] = len(v)
    
    return mostValues[0]