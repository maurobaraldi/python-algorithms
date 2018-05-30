#!/usr/bin/env python

def fibonacci_recursive(n):
    '''This is a O(2^n) solution.'''

    if n <= 1:
        return n
    return fibonacci_recursive(n -1) + fibonacci_recursive(n -2)


def fibonacci_for(n):
    '''This is a O(n) solution.'''
    # There is no negative fibonacci numbers.
    if n <= 0:
        return 0

    # Fibonacci of 1 and 2 are 1
    if 3 > n > 0:
        return 1

    result = 0
    last = 1
    penult = 1

    for i in range(2, n):
        result = last + penult
        penult = last
        last = result

    return result
