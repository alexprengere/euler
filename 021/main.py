def proper_divisors(n):
    for i in range(1, n):
        if n % i == 0:
            yield i


total = 0
for n in range(1, 10001):
    sum_of_divisors = sum(proper_divisors(n))
    if sum_of_divisors != n:
        if sum(proper_divisors(sum_of_divisors)) == n:
            total += n

print(total)
