# -*- coding: utf-8 -*-
r"""
This is a collection of math tools I find useful.

Much inspiration was drawn from Peter Norvig's Udacity 
class "Design of Computer Programs" 
(www.https://www.udacity.com/course/viewer#!/c-cs212/)

Created on Thu Jan 01 17:40:08 2015
@author: J

"""
from MyDevTools.MyDecorator import decorator
from MyDevTools.MyAnalysisTools import histogram
from MyDevTools.MyPerformanceTools import *
from MyDevTools.MyDebug import *
import itertools

import math

__all__ = [
            "makeInt",
            "root_",
            "has_factors",
            "get_greatest_factor",
            "get_gcf",
            "is_prime",
            "get_factors",
            "get_prime_factors",
            "get_greatest_factor"
        ]


def main():
    values = 10, 20, 32
#    printStuff(get_prime_factors_test(10))
#    printStuff(get_all_prime_factors_test(values))

#    for _ in get_all_factors(10):
#        print _
#    printStuff(get_all_factors_test((5,2)))
    printStuff(get_common_prime_factors(*values))

@decorator
def makeInt(f):
    """Forces the function to return an int"""
    def wrapper(*args,**kw):
        return int(f(*args,**kw))
    return wrapper

@makeInt
def root_(n):
    """Returns the square root of n, rounded up."""
    return math.sqrt(n)+1
    
def has_factors(n, low=None, high=None):
    """Returns True if n is factorable in the specified range."""
    if n == 1: 
        raise MyDevTools.UnintendedUseError(n, "1 is prime")
    if not high: high = n+1
    if low < 2: low = 2    
    search_range = xrange(low, high)
    for num in search_range:
        if n % num == 0 and low < n/num < high:
            print num, n/num
            return True
    return False

def get_gcf(values):
    """Returns the greatest common factor of the numbers given."""
    return max(get_common_factors(values))

def get_factors(*nums):
    """Returns all factors of n excluding n."""
    
    def factor_(n):    
        assert isinstance(n,int)
        possible_factors = (num for num in xrange(2,root_(n)))
        yield 1
        try:
            while possible_factors:
                p = possible_factors.next()
                q,r = divmod(n, p)        
                try:
                    p_not_a_factor = r != 0
                    assert p_not_a_factor
                except AssertionError:
                    yield p
                    yield q
        finally:
            yield n
    return combined_gen([factor_(num) for num in nums])    

def get_common_factors(*nums):
    factors = get_factors(*nums)
    low_num = min(nums)        
    return (factor for factor in factors 
            if not sum([num % factor for num in nums]))
                

def get_prime_factors(*nums):
    return (factor for factor in get_factors(*nums) if is_prime(factor))
    
def get_common_prime_factors(*nums):
    return (factor for factor in get_common_factors(*nums) 
                                        if is_prime(factor)
            )
    
@decorator
def prime(f):
    def wrapper(*args,**kw):
        return (_ for _ in f(*args,**kw) if is_prime(_))
    return wrapper

    
def is_prime(n):
    """Tests to see if n is prime"""
    
    if n == 2: return True
    if n % 2 == 0: 
        return False
    root_n = int(math.sqrt(n))+1
    up_to_root_n = root_n
    quotients = map(lambda divisor: n % divisor, 
                    range(3, up_to_root_n))
    n_is_evenly_divisible = 0 in quotients
    return False if n_is_evenly_divisible else True
    
def get_common_multiples_of(args, stop_value=None):
    
    num_multiples = len(args)
    current_max = 0
    multiple_gens = [get_multiples_of(arg) for arg in args]
    multiples = histogram()
    common_multiples = []    
    STOP = False
    while True:        
        if STOP == True: break
        for gen in multiple_gens:
            current_multiple = gen.next()
            multiples.push(current_multiple)
            is_common_multiple = multiples[current_multiple] == num_multiples
            not_already_yielded = current_multiple not in common_multiples
            if stop_value != None and current_multiple > stop_value: 
                STOP = True                
                break        
            if is_common_multiple and not_already_yielded:
                yield current_multiple

def get_n_ary_multiples(nums, stop=None):
    multiples = tuple([get_multiples_of(num, stop) for num in nums])
    return combine_gens(multiples)    
    
def get_multiples_of(n, stop_value=None):
        counter = 0
        while True:
            counter += 1
#            print "counter: {}, n*counter: {}".format(counter, n*counter)
            multiple = n * counter
            if stop_value != None and multiple >= stop_value: break
            yield n * counter
            
if __name__ == '__main__':
    main()