#!/usr/bin/env python

"""
$ python main.py 1000
1366
"""

import sys


if __name__ == '__main__':
    n = int(sys.argv[1])
    print(sum(int(i) for i in str(2 ** n)))
