# -*- coding: utf-8 -*-
"""
:Author:
    J. Tolton
Created on Sun Jan 04 15:53:50 2015

=======
MyTools
=======

Contents
--------
------------
- combined_gen

"""

def main():
    a = (num for num in xrange(0,10,2))
    b = (num for num in xrange(1,10,2))
    print "combined_gen test: ", [item for item in combine_gens((a,b))]

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
            
if __name__ == '__main__':
    main()