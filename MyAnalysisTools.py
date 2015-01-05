# -*- coding: utf-8 -*-
"""
Created on Sun Jan 04 09:38:32 2015

@author: J
"""

from MyDevTools.MyDecorator import decorator

__all__ = [
                "get_histogram",
                "histogram"
]
    
def main():
    
    a = 1,2,3
    a = histogram().push_all(a)
    a.push(5)
    print a
    print a[5]

def get_histogram(iterable):
    """histogram(iterable) --> dict
    
    Returns histogram of iterable"""
    
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
        """histogram(iterable) --> dict
        
        Returns histogram of iterable"""
        
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

if __name__ == '__main__':
    main()