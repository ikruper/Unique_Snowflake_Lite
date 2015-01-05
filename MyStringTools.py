# -*- coding: utf-8 -*-
r"""
This toolset is designed to aid in manipulating strings.

Created on Thu Jan 01 17:40:08 2015
@author: J

"""

from MyDevTools.MyDecorator import decorator
import MyDevTools.MyDebug as debug


def is_palindrome(s):
    """
    is_palindrome(str) -> bool 
    e.g. is_palindrome(9009) == True
    """
    s_has_palindrome = str(s) == str(s)[::-1]
    return True if s_has_palindrome else False
    
#def right_justify(s,filler=" "):
#    return "{s:{filler}>70}".format(s=s,filler=filler)
#    
#def left_justify(s, filler=" "):
#    return "{s:{filler}}
    
def justify(s, justification="^", filler=" ",space=70):
    """justify(s, justification, filler, space) --> outputted string
    
    Justifies string.
    
    Defaults --
        justification -- center
        filler -- " "
        space -- 70 (usually the whole screen)
        
    For justification, use the string formatter commands --
        right -- ">"
        left -- "<"
        center(default) -- "^"
    
    Inspiration taken from 
    """
    return "{s:{filler}{justification}{space}}".format(s=s,
                                                justification=justification,
                                                filler=filler,
                                                space=space)
if __name__ == '__main__':
    s = justify('hey', filler = "*",space=20)
    print justify(s,justification=">")

    