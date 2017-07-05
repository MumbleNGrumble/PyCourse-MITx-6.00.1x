# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 18:18:30 2017

@author: Daniel
"""

if type(varA) == type("string") or type(varB) == type("string"):
    print("string involved")
elif varA > varB:
    print("bigger")
elif varA == varB:
    print("equal")
elif varA < varB:
    print("smaller")