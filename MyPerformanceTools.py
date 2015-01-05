# -*- coding: utf-8 -*-
r"""
This toolset is designed to enhance scripting performance.

Much inspiration was drawn from Peter Norvig's Udacity 
class "Design of Computer Programs" 
(www.https://www.udacity.com/course/viewer#!/c-cs212/)

Created on Thu Jan 01 17:40:08 2015
@author: J

"""

from MyDevTools.MyDecorator import decorator

__all__ = [

            "memo",
            "combined_gen",
            "get_histogram",
            "n_ary"

]

def main():
    stuff = [range(10) for x in range(10)]
    print unpack(stuff)

@decorator
def memo(f):
    """Decorator that caches the return value for each call to f(args).
    Then when called again with same args, we can just look it up."""
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            result = f(*args)
            cache[args] = result
            return result
        except TypeError:
            # some element of args can't be a dict key
            return f(*args)
    _f.cache = cache
    return _f


def combined_gen(args, non_redundant=True):
    cache = {}
    redundant = not non_redundant
    while non_redundant and args:
        for arg in args:
            try:
                res = arg.next()
                cache[res]
            except StopIteration:
                args = tuple(new_arg for new_arg in args if new_arg != arg)                
            except KeyError:
                cache[res] = res
                yield res
    while redundant:
        for arg in args:
            yield arg.next()
            
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

@decorator
def n_ary(f):
    """Given binary function f(x, y), return an n_ary function such
    that f(x, y, z) = f(x, f(y,z)), etc. Also allow f(x) = x."""
    def n_ary_f(x, *args):
        return x if not args else f(x, n_ary_f(*args))
    return n_ary_f

def unpack(items):
    def _unpack(items):
        try:
    #        print items[0], len(items[0])
            return (items if len(items[0]) <= 1 
                else unpack(items[0][:1]) + unpack(items[0][1:]))
        except TypeError:
            return items
    cache = []
    for item in items:
        cache += _unpack(item)
    return cache
        


if __name__=='__main__':
    main()
