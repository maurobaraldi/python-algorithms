#!/usr/bin/env python3

def sort(array):
    """
    The most naive version of Selection Sorting algorithm.
    """

    length = len(array)

    # Traverse through all elements in array
    for i in range(len(array)):

        # Find the minimum element in remaining unsorted array
        index = i

        for j in range(i+1, len(array)):

            if array[index] > array[j]:
                index = j

        # Swap the found minimum element with the first element.
        array[i], array[index] = array[index], array[i]

    return array

def index(array, i, j):
    """
    Return minimum index.
    """
    if i == j:
        return i

    k = index(array, i+1, j)

    return i if array[i] < array[k] else k

def recursive(array, length, idx=0):

    if idx == length:
        return -1

    current = index(array, idx, length-1)

    if current != index:
        array[current], array[idx] = array[idx], array[current]

    recursive(array, length, idx+1)
