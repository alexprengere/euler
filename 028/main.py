n = 500

# This is the final formula after lots of counting.
# First notice how squares are on the upper right diagonal,
# then work you way towards the total.
print(int(1 + 2 / 3 * n * (8 * n ** 2 + 15 * n + 13)))
