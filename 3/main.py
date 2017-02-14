#!/usr/bin/env python

"""
$ python main.py 600851475143
[71, 839, 1471, 6857]
"""

import sys
from math import sqrt


def is_prime(p):
    return all(p % i != 0 for i in range(2, 1 + int(sqrt(p))))


def find_prime_factors(n):
    p = 2
    while n != 1:
        if is_prime(p) and n % p == 0:
            yield p
            n = n // p
        else:
            p += 1


if __name__ == '__main__':
    n = int(sys.argv[1])
    print(list(find_prime_factors(n)))
