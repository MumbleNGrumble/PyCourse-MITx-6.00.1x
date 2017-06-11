# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 08:30:54 2017

@author: Daniel
"""

# Test Case: s = 'azcbobobegghakl'

s = 'azcbobobegghakl'

longestSubstring = ""
startingSlice = 0

while startingSlice <= len(s) - 1:
    currentSubstring = ""
    
    for letter in s[startingSlice:]:
        if letter >= currentSubstring[-1:]:
            currentSubstring += letter
        else:
            break
    
    startingSlice += len(currentSubstring)
    
    if len(currentSubstring) > len(longestSubstring):
        longestSubstring = currentSubstring

print("Longest substring in alphabetical order is: " + longestSubstring)