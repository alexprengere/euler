from math import sqrt


def is_prime(p):
    if p <= 1:
        return False
    return all(p % i != 0 for i in range(2, 1 + int(sqrt(p))))


N = 1000
data = {}
for a in range(-N, N + 1):
    for b in range(-N, N + 1):
        n = 0
        while is_prime(n ** 2 + a * n + b):
            n += 1
        data[a, b] = n

print(max(data, key=lambda k: data[k]))
