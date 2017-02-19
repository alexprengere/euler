#!/usr/bin/env python

"""
$ python main.py 2000000
142913828922
"""

import sys
from math import sqrt


def is_prime(p):
    return all(p % i != 0 for i in range(2, 1 + int(sqrt(p))))


def sum_primes(n):
    total = 2
    for p in range(3, n + 1, 2):
        if is_prime(p):
            total += p
    return total


if __name__ == '__main__':
    n = int(sys.argv[1])
    print(sum_primes(n))
