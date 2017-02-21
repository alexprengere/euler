#!/usr/bin/env python

"""
$ python main.py 500
76576500
"""

import sys
import itertools
from math import sqrt


def get_triangle_numbers():
    total = 0
    for i in itertools.count(1):
        total += i
        yield total


def get_divisors(i):
    for j in range(1, 1 + int(sqrt(i))):
        if i % j == 0:
            yield j
            if j != i // j:
                yield i // j


if __name__ == '__main__':
    n = int(sys.argv[1])

    for t in get_triangle_numbers():
        divisors = list(get_divisors(t))
        if len(divisors) > n:
            print(t)
            break
