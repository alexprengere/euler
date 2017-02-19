#!/usr/bin/env python

"""
$ python main.py 1000
31875000 = 200 * 375 * 425
"""

import sys
from math import sqrt


def find_pythagorean(total):
    for b in range(1, total):
        for a in range(1, b):
            c2 = a ** 2 + b ** 2
            c = sqrt(c2)
            if c.is_integer() and a + b + c == total:
                return a, b, int(c)
    raise ValueError('Could not find Pythagorean triplet')

if __name__ == '__main__':
    total = int(sys.argv[1])
    a, b, c = find_pythagorean(total)
    print('{} = {} * {} * {}'.format(a * b * c, a, b, c))
