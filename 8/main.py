#!/usr/bin/env python

"""
$ python main.py digits.txt 13
23514624000
"""

import sys
from operator import mul


if __name__ == '__main__':
    filename, n = sys.argv[1], int(sys.argv[2])

    with open(filename) as f:
        digits = [int(i) for row in f for i in row.strip()]

    max_, max_i = -1, None
    for i, _ in enumerate(digits):
        product = reduce(mul, digits[i:i + n])
        if product > max_:
            max_, max_i = product, i

    print(max_, digits[max_i:max_i + n])
