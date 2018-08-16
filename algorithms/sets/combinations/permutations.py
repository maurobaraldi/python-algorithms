#!/usr/bin/env python


def permutation(lst):
    """Simple, beauty and recursive, solution."""
    if len(lst) == 0:
        return []

    if len(lst) == 1:
        return [lst]

    result = []

    for i in range(len(lst)):
        remaining = lst[:i] + lst[i + 1:]

        # Generating permutations where remaining is first element
        for p in permutation(remaining):
            result.append(lst[i: i + 1] + p)

    return result


def permutation_non_recursion(lst):
    """Simple, ugly and no recursive, soution."""
    if len(lst) <= 1:
        return lst

    r = [[]]

    for i in range(len(lst)):
        r = [[a] + b for a in lst for b in r if a not in b]

    return r
