#!/usr/bin/env python

"""
$ python main.py 1000
233168
"""

import sys


def is_divisible(i, args):
    """Returns True if i is divisible by any element of args"""
    return any(i % a == 0 for a in args)


if __name__ == '__main__':
    n = int(sys.argv[1])
    print(sum(i for i in range(n) if is_divisible(i, (3, 5))))
