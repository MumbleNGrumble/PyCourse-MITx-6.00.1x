# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 21:41:46 2017

@author: Daniel.Le
"""

class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object 
            occurs 0 times in self. """
        self.vals = {}

    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1

    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s

class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of 
            times it occurs in self by 1. Otherwise does nothing. """
        
        if e in self.vals:
            self.vals[e] -= 1

    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        
        if e in self.vals:
            return self.vals[e]
        else:
            return 0

    def __add__(self, other):
        newBag = Bag()
        
        for item in self.vals:
            if item in newBag.vals:
                newBag.vals[item] += self.vals[item]
            else:
                newBag.vals[item] = self.vals[item]
        
        for item in other.vals:
            if item in newBag.vals:
                newBag.vals[item] += other.vals[item]
            else:
                newBag.vals[item] = other.vals[item]
        
        return newBag