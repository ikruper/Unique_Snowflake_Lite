# -*- coding: utf-8 -*-
"""
Created on Mon Jan 05 14:35:30 2015

@author: J
"""

def get_histogram(iterable):
    """Returns histogram of iterable"""
    
    hist = dict()    
    for item in iterable:
        try:
            hist[item] += 1
        except KeyError:
            hist[item] = 1
    return hist
    
class histogram(dict):
    
    def push(self,item):
        try:
            self[item] += 1
        except KeyError:
            self[item] = 1

    def push_all(self,iterable):
        """Returns histogram of iterable"""
        
        try:
            assert isinstance(iterable, (list, tuple))
        except AssertionError:
            "Histogram must be composed of finite list"
            raise AssertionError
                
        for item in iterable:
            try:
                self[item] += 1
            except KeyError:
                self[item] = 1
        return self
        
class loop(list):    
    def rotate(self):
        self.append(self.pop(0))
        
