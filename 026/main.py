def fraction_to_recurring_sequence(num, den):
    seq = ""
    seen_rem = {}
    rem = num % den
    while rem != 0 and rem not in seen_rem:
        seen_rem[rem] = len(seq)
        rem = rem * 10
        seq += str(rem // den)
        rem = rem % den

    if rem == 0:
        return ""
    else:
        return seq[seen_rem[rem] :]


i_max, _ = max(
    ((i, fraction_to_recurring_sequence(1, i)) for i in range(1, 1000)),
    key=lambda t: len(t[1])
)
print(i_max)
