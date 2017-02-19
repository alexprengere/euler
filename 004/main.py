#!/usr/bin/env python

"""
$ python main.py 3
906609 = 913 * 993
"""

import sys
from math import sqrt


def is_palindrome(i):
    return str(i) == str(i)[::-1]


def get_divisors(i):
    for j in range(1, 1 + int(sqrt(i))):
        if i % j == 0:
            yield j, i // j


def find_palindrome(digits):
    for i in range((10 ** digits) ** 2, 0, -1):
        if is_palindrome(i):
            for a, b in get_divisors(i):
                if len(str(a)) == digits and len(str(b)) == digits:
                    return a, b


if __name__ == '__main__':
    digits = int(sys.argv[1])
    a, b = find_palindrome(digits)
    print('{} = {} * {}'.format(a * b, a, b))
