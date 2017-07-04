# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 16:15:35 2017

@author: Daniel
"""

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    
    total = 0
    
    for k,v in aDict.items():
        total += len(v)
        
    return total