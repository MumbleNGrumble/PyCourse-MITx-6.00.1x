# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 23:05:30 2017

@author: Daniel
"""

def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    
    # Your code here
    
    freq = {}
    
    for num in L:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    largestNumList = []
    
    for k,v in freq.items():
        if v % 2 == 1:
            largestNumList.append(k)
    
    if largestNumList != []:
        return max(largestNumList)