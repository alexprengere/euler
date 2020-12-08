# Integers avoid having to rely on decimal.Decimal
# to handle rounding errors
COINS = 1, 2, 5, 10, 20, 50, 100, 200
TARGET = 200


visited = set()
solutions = []
stack = [(0, (0,) * len(COINS))]

while stack:
    total, state = stack.pop()
    for cn, coin in enumerate(COINS):
        new_total = total + coin
        if new_total > TARGET:
            continue
        new_state = list(state)
        new_state[cn] += 1
        new_state = tuple(new_state)
        if new_state not in visited:
            visited.add(new_state)
            if new_total == TARGET:
                solutions.append(new_state)
            else:  # < TARGET
                stack.append((new_total, new_state))

print(len(solutions))
