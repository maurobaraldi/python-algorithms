#!/usr/bin/env python3

def naive(array):
    """
    The most naive version of Bubble Sorting algorithm.

    Yeah, I know, I should not use the sorted reserved word.
    But, let's say this is a security lock for unwanted used of it :-)
    """

    length = len(array) - 1
    sorted = False  # Let's assume it is unsorted yet

    while not sorted:
        sorted = True  # Now, assume it is sorted, to compare

        for i in range(length):
            if array[i] > array[i + 1]:
                sorted = False  # Elements compared are in wrong order
                a, b = array[i], array[i + 1]
                array[i], array[i + 1] = b, a  # Rearrange array to right order
    return array            

def improved(array):
    """This solution uses two `for` to use first as pointer.""" 
    length = len(array)

    for i in range(length):  # Traverse all elements in array (pointer)
        for j in range(0, length - i - 1): # All elements until i are already in place
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array

def recursive(array, l=None):
    """
    First of all: This solution does not work more efficently that others.

    The size of list must be updated every iteration, so `l` is needed.
    """
    length = l or len(array)

    if length < 2:
        return array

    for i in range(length - 1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
    recursive(array, length - 1)

    return array
