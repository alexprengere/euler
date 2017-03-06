#!/usr/bin/env python

"""
$ python main.py 1000
21124
"""

import sys

def spell(n):
    digits = [
        'zero', 'one', 'two', 'three', 'four',
        'five', 'six', 'seven', 'eight', 'nine',
        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
        'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'
    ]
    tens = [
        None, None, 'twenty', 'thirty', 'forty',
        'fifty', 'sixty', 'seventy', 'eighty', 'ninety'
    ]
    K, M, G = 1000, 1000000, 1000000000

    if n < 20:
        return digits[n]

    if n < 100:
        if n % 10 == 0:
            return tens[n // 10]
        else:
            return tens[n // 10] + '-' + digits[n % 10]

    if n < K:
        if n % 100 == 0:
            return digits[n // 100] + ' hundred'
        else:
            return digits[n // 100] + ' hundred and ' + spell(n % 100)

    if n < M:
        if n % K == 0:
            return spell(n // K) + ' thousand'
        else:
            return spell(n // K) + ' thousand, ' + spell(n % K)

    if n < G:
        if n % M == 0:
            return spell(n // M) + ' million'
        else:
            return spell(n // M) + ' million, ' + spell(n % M)

    if n % G == 0:
        return spell(n // G) + ' billion'
    else:
        return spell(n // G) + ' billion, ' + spell(n % G)


if __name__ == '__main__':
    n = int(sys.argv[1])
    total = 0
    for i in range(1, n + 1):
        total += len([c for c in spell(i) if c.isalpha()])
    print(total)
