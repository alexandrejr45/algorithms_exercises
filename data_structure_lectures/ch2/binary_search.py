from random import randint
from typing import List


def binary_search(array: List, search_value: int) -> int | None:
    lower_bound = 0
    upper_bound = len(array) - 1

    while lower_bound <= upper_bound:
        midpoint = int((upper_bound + lower_bound) / 2)
        value_at_mindpoint = array[midpoint]

        if search_value == value_at_mindpoint:
            return midpoint
        elif search_value < value_at_mindpoint:
            upper_bound = midpoint - 1
        elif search_value > value_at_mindpoint:
            lower_bound = midpoint + 1

    return None


ordered_list = [randint(0, 600) for i in range(0, 1000)]
ordered_list.sort()

print(ordered_list)
poco = binary_search(ordered_list, 350)
print(poco)
