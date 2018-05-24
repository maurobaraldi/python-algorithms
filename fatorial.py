#!/usr/bin/env python

def fatorial_1(number):
    """Fatorial using for."""
    result = 1

    for n in range(1, number + 1):
        result *= n

    return result

def fatorial_2(number):
    """Fatorial calculation using while."""
    num = 1
    while number >= 1:
        num = num * number
        number = number - 1
    return num

def fatorial_3(number):
    """Fatorial calculation recursively."""
    if number == 0:
        return 1
    else:
        return number * fatorial_3(number - 1)
