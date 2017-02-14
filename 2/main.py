#!/usr/bin/env python

"""
$ python main.py 4000000
4613732
"""

import sys


def fibonacci(n):
    a, b = 0, 1
    while True:
        if b > n:
            break
        a, b = b, a + b
        yield b


if __name__ == '__main__':
    n = int(sys.argv[1])
    print(sum(i for i in fibonacci(n) if i % 2 == 0))
