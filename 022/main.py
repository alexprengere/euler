import string
letter_scores = dict((l, pos) for pos, l in enumerate(string.ascii_uppercase, start=1))

def score(name):
    return sum(letter_scores[l] for l in name.upper())


with open("names.txt") as f:
    text = f.read().rstrip()
names = sorted(n.strip('"') for n in text.split(","))

total = 0
for i, name in enumerate(names, start=1):
    total += i * score(name)
print(total)
