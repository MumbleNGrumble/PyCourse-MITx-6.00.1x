# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 09:41:45 2017

@author: Daniel
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    
    if aStr == "":
        return False
    elif len(aStr) == 1:
        if char == aStr:
            return True
        else:
            return False
    
    midChar = len(aStr)//2
    
    if char == aStr[midChar]:
        return True
    elif char < aStr[midChar]:
        return isIn(char, aStr[:midChar])
    else:
        return isIn(char,aStr[midChar + 1:])