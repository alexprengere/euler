#!/usr/bin/env python

"""
$ python main.py 10001
104743
"""

import sys
from math import sqrt
import itertools


def is_prime(p):
    return all(p % i != 0 for i in range(2, 1 + int(sqrt(p))))


def get_primes():
    for p in itertools.count(2):
        if is_prime(p):
            yield p


if __name__ == '__main__':
    n = int(sys.argv[1])

    for i, prime in enumerate(get_primes(), start=1):
        if i == n:
            print(prime)
            break
