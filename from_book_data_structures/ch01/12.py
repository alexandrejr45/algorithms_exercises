# Python’s random module includes a function choice(data) that returns a random element from a non-empty sequence.
# The random module includes a more basic function randrange, with parameterization similar to the built-in range
# function, that return a random choice from the given range. Using only the randrange function, implement
# your own version of the choice function.

import random


def random_choice(seq: list):
    choice = random.randrange(len(seq))
    return seq[choice]


test_list = []

for x in range(0, 100):
    test_list.append("xxx" * x)

print(random_choice(test_list))
