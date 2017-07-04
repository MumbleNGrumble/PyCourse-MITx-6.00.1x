# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 22:54:35 2017

@author: Daniel
"""

def print_without_vowels(x):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    
    # Your code here
    
    noVowelString = ""
    
    for letter in x:
        if not (letter.lower() == "a" or letter.lower() == "e" 
                or letter.lower() == "i" or letter.lower() == "o"
                or letter.lower() == "u"):
            noVowelString += letter
    
    print(noVowelString)