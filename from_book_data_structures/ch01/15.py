# Write a Python function that takes a sequence of numbers and determines
# if all the numbers are different from each other (that is, they are distinct).


import random


def random_numbers_list():
    numbers = []
    for i in range(0, 40):
        numbers.append(random.randrange(10000))
    return numbers


def check_different_numbers(num):
    numbers = len(num)
    numbers_distinct = len(set(num))
    if numbers_distinct == numbers:
        return True
    else:
        return False


print(check_different_numbers(random_numbers_list()))
