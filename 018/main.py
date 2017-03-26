#!/usr/bin/env python

"""
$ python main.py medium.txt
1074
"""

import sys


def main(rows):
    tmp = [0] * (1 + len(rows[-1]))
    for row in reversed(rows):
        tmp = [n + max(a, b) for n, (a, b) in zip(row, zip(tmp, tmp[1:]))]
    return tmp[0]


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        print(main([[int(n) for n in row.split()]
                   for row in f]))
