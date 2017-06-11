# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 08:00:50 2017

@author: Daniel
"""

# Test Case: s = 'azcbobobegghakl'

numVowels = 0

for letter in s:
    if letter == 'a' or letter == 'e' or letter =='i' or letter == 'o' or letter == 'u':
        numVowels += 1

print("Number of vowels: " + str(numVowels))