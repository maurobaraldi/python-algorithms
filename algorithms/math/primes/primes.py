#!/usr/bin/env python

import random 

def six_k_form(num):
    '''
    Check pime number using 6k+-1 form.

    This algorithm is used for learning purposes only.
    '''
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False

    i = 5

    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i = i + 6

    return True


def agk_form(num):
    '''
    Check pime number using Agrawal–Kayal–Saxena.

    Variant of the classic O(sqrt(N)) algorithm.
    '''
    if 1 < num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= num:
        if num % i == 0:
            return False
        i += w
        w = 6 - w

    return True


def little_fermat_form(num, times):
    '''Little Fermat Theorem to check primality.'''

    # Corner cases
    if num <= 1 or num == 4:
        return False

    if num <= 3:
        return True

    # Corner case, num > 5
    if num == 5:
        return True

    while times > 0:
        a = 2 + random.randint(2, num-4)

        # Fermat's magic
        if not  (a**(num-1)) % num == 1:
            return False
        times -= 1
    return True

def sieve_of_erastosthenes(n):
    '''
    Sieve of Erastosthenes generate a list of prime numbers.

    It may used to verify primality, by checking if n i in list.
    '''

    primes = [True for i in range(n+1)]
    p = 2

    while (p * p <= n):

        # If prime[p] is not changed, then it is a prime
        if primes[p] is True:

            # Update all multiples of p
            for i in range(p*2, n+1, p):
                primes[i] = False

        p += 1

    return [j for j in range(2, n) if primes[j]]
