#!/ur/bin/en python3

def lcm(a, b):
    '''
    Brute force form.

    Just for educational purposes.
    '''

    i = 1
    check = False
    while not check:
        if i >= a and i >= b:
            if i % a == 0 and i % b == 0:
                return i
        i += 1

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def lcm_by_gcd(a, b):
    '''
    Reducion by the GCD.

    Because gcd(a, b) is a divisor of both a and b.
    Most efficient form.
    '''

    return (a * b) / gcd(a, b)
