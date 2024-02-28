from timeit import timeit


def print_numbers_version_one():
    number = 2

    while number <= 100:
        if number % 2 == 0:
            pass

        number += 1


def print_numbers_version_two():
    number = 2

    while number <= 100:
        number += 2


def print_numbers_version_three():
    for i in range(2, 102, 2):
        pass


print(timeit('print_numbers_version_one()', number=1, globals=globals()))
print('\n')
print(timeit('print_numbers_version_two()', number=1, globals=globals()))
print('\n')
print(timeit('print_numbers_version_three()', number=1, globals=globals()))
