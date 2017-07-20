# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 19:21:45 2017

@author: Daniel
"""

def genPrimes():
    primeNums = []
    x = 1
    
    while True:
        x += 1
        isPrime = True
        
        for num in primeNums:
            if (x % num) == 0:
                isPrime = False
        
        if isPrime:
            primeNums.append(x)
            yield x