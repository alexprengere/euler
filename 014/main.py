#!/usr/bin/env python

"""
$ python main.py 1000000
(1, 1)
(2, 2)
(3, 8)
(6, 9)
...
(837799, 525)
"""

import sys


def len_collatz_seq(n, lengths):
    len_ = 1

    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1

        if n not in lengths:
            len_ += 1
        else:
            len_ += lengths[n]
            break

    return len_


if __name__ == '__main__':
    limit = int(sys.argv[1])

    max_len = -1
    lengths = {}

    for n in range(1, limit + 1):
        lengths[n] = len_collatz_seq(n, lengths)
        if lengths[n] > max_len:
            max_len = lengths[n]
            print(n, lengths[n])
