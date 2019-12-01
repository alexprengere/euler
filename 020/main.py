def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def get_digits(n):
    for digit in str(n):
        yield int(digit)


print(sum(get_digits(factorial(10))))
print(sum(get_digits(factorial(100))))
