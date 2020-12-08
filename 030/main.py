N = 5

total = 0
for n in range(10, 1000000):
    digits = [int(d) for d in str(n)]
    if sum(d ** N for d in digits) == n:
        total += n

print(total)
