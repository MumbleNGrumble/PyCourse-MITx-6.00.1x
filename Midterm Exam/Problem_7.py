# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 01:22:03 2017

@author: Daniel
"""

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    #YOUR CODE HERE
    
    invertedDict = {}
    
    for k,v in d.items():
        if v in invertedDict:
            invertedDict[v].append(k)
        else:
            invertedDict[v] = [k]
    
    for k in invertedDict:
        invertedDict[k].sort()
    
    return invertedDict