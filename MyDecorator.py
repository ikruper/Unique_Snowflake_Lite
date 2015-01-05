# -*- coding: utf-8 -*-
"""

This module contains the decorator-decorator which
updates the wrapped function with the information 
of the wrapper function.  

Credit goes to Peter Norvig.

Created on Thu Jan 01 18:11:20 2015

@author: J
"""

import functools

def decorator(d):
    """Make function d a decorator: d wraps a function fn."""
    def _d(fn):
        return functools.update_wrapper(d(fn), fn)
    return _d
decorator = decorator(decorator)