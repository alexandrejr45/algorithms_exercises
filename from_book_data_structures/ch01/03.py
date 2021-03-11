# Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution.

import random

data = []


def minmax(numbers):
    numbers.sort()
    min_max = (numbers[0], numbers[-1])
    return min_max


# Generate 50 randoms numbers to populate the list
for x in range(1, 50):
    n = random.randrange(1, 10000)
    data.append(n)

print(minmax(data))
