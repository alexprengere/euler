def proper_divisors(n):
    for i in range(1, n):
        if n % i == 0:
            yield i


def is_perfect(n):
    return n == sum(proper_divisors(n))


def is_deficient(n):
    return n > sum(proper_divisors(n))


def is_abundant(n):
    return n < sum(proper_divisors(n))


abundants = set()
for n in range(1, 28123):
    if is_abundant(n):
        abundants.add(n)

abundants_sums = set(n + m for n in abundants for m in abundants)

total = 0
for n in range(1, 28123):
    if n not in abundants_sums:
        total += n
print(total)
