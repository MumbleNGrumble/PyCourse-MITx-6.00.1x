# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 10:41:29 2017

@author: Daniel
"""

import math

def polysum(n, s):
    area = (0.25 * n * s**2) / math.tan(math.pi/n)
    perimeterSquared = (n * s) ** 2
    return round(area + perimeterSquared, 4)