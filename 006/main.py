#!/usr/bin/env python

"""
$ python main.py 100
25164150
"""

import sys


if __name__ == '__main__':
    n = int(sys.argv[1])

    r = range(1, n + 1)
    print(sum(r) ** 2 - sum(i ** 2 for i in r))
