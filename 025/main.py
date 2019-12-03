def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


for n, f in enumerate(fibonacci(), start=1):
    if len(str(f)) == 1000:
        print(n)
        break
