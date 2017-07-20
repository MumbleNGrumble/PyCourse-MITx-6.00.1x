# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 23:58:28 2017

@author: Daniel
"""

def fancy_divide(list_of_numbers, index):
    denom = list_of_numbers[index]
    return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
    try:
        return item / denom
    except ZeroDivisionError:
        return 0

# Test Case
print(fancy_divide([0, 2, 4], 0))