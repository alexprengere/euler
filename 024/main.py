import itertools

for i, p in enumerate(itertools.permutations('0123456789'), start=1):
    if i == 1_000_000:
        print(''.join(p))
