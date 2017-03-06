#!/usr/bin/env python

"""
$ python main.py 20 20
137846528820
"""

import sys


def number_of_routes(max_i, max_j):
    """Pascal triangle implementation to compute combinations."""
    routes = {}

    for i in range(1, max_i + 1):
        routes[(i, 0)] = 1
    for j in range(1, max_j + 1):
        routes[(0, j)] = 1

    for i in range(1, max_i + 1):
        for j in range(1, max_j + 1):
            routes[(i, j)] = routes[(i - 1, j)] + routes[(i, j - 1)]

    return routes[(max_i, max_j)]


if __name__ == '__main__':
    max_i, max_j = int(sys.argv[1]), int(sys.argv[2])
    print(number_of_routes(max_i, max_j))
