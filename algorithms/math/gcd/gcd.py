#!/usr/bin/env python

def gcd_mod(a, b):
    '''
    Divison based version.

    From:  The Art of Computer Programming, Volume 2, pages 319-320
    '''
    while b > 1:
        # t holds the value of b while the next remainder b is being calculated.
        t = b
        b = a % b
        a = t
    return a

def gcd_sub(a, b):
    '''
    Subtraction based version.

    From:  The Art of Computer Programming, Volume 2, pages 318-319
    '''
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def gcd_recursive(a, b):
    '''
    Recursive based version.

    From: Numbers and Geometry, Stillwell, page 14
    '''
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)

