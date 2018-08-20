#!/usr/bin/env python

from random import randrange

def fisher_yates(items):
    """Fisher-Yates algorithm, O(n), solution."""
    i = len(items)
    if i <= 1:
        return items
    result = []

    while i > 1:
        i -= 1
        j = randrange(i)
        result.append(items[i])
        del items[1]
    return result


def sattolo(items):
    """Siattolo's algorithm solution."""
    i = len(items)

    while i > 1:
        i -= 1
        j = randrange(i)
        items[j], items[i] = items[i], items[j]

    return items
