# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 08:15:57 2017

@author: Daniel
"""

# Test Case: s = 'azcbobobegghakl'

i = 0
j = i + 3
bobCounter = 0

while j <= len(s) + 1:
    if s[i:j] == 'bob':
        bobCounter += 1
    i += 1
    j += 1

print("Number of times bob occurs is : " + str(bobCounter))