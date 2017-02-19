#!/usr/bin/env python

"""
$ python main.py grid.txt 4
70600674
"""

import sys
from operator import mul
from functools import reduce


def get_adjacents(grid, a, b, size):
    x_range = range(a, a + size)
    y_range = range(b, b + size)
    y_range_rev = range(b, b - size, -1)

    yield [grid[a][y] for y in y_range]
    yield [grid[x][b] for x in x_range]
    yield [grid[x][y] for x, y in zip(x_range, y_range)]
    yield [grid[x][y] for x, y in zip(x_range, y_range_rev)]


if __name__ == '__main__':
    filename, size = sys.argv[1], int(sys.argv[2])

    with open(filename) as f:
        grid = [
            [int(i) for i in row.split()]
            for row in f
        ]

    x_max, y_max = len(grid), len(grid[0])

    max_ = -1
    for a in range(size - 1, x_max - size + 1):
        for b in range(size - 1, y_max - size + 1):
            for line in get_adjacents(grid, a, b, size):
                product = reduce(mul, line)
                if product > max_:
                    max_ = product

    print(max_)
