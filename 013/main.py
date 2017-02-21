#!/usr/bin/env python

"""
$ python main.py numbers.txt
5537376230
"""

import sys


if __name__ == '__main__':
    filename = sys.argv[1]

    with open(filename) as f:
        numbers = [int(row) for row in f]

    total = sum(numbers)
    print(str(total)[:10])
