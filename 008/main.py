#!/usr/bin/env python

"""
$ python main.py digits.txt 13
23514624000
"""

import sys
from operator import mul
from functools import reduce


if __name__ == '__main__':
    filename, n = sys.argv[1], int(sys.argv[2])

    with open(filename) as f:
        digits = [int(i) for row in f for i in row.strip()]

    max_ = -1
    for i, _ in enumerate(digits):
        product = reduce(mul, digits[i:i + n])
        if product > max_:
            max_ = product

    print(max_)
