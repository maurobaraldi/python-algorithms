#!/usr/bin/env python

def product(set_a, set_b):
    '''
    Trivial O(n²) version.

    '''
    result = []
    for i in set_a:
        for j in set_b:
            result.append([i, j])

    return result


def list_comprehension(set_a, set_b):
    '''
    Trivial version, but list comprehension based.
    '''

    return [[i, j] for i in set_a for j in set_b]


def product_n(*lists):
    '''
    Multiple sets version.

    Use recursive approach this way, is easier than brute force. Really!
    '''
    if lists:
        head, tail = lists[0], lists[1:]

        for i in head:
            for j in product_n(*tail):
                yield [i] + list(j)
    else:
        yield []

