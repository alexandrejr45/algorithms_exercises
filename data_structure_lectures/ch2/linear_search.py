from random import randint
from typing import List


def linear_search(array: List, search_value: int) -> None:
    for i in range(0, len(array)):
        if array[i] == search_value:
            print(i)
        elif array[i] > search_value:
            break
    return


ordered_list = [randint(0, 200) for i in range(0, 100)]
ordered_list.sort()


print(ordered_list)
linear_search(ordered_list, 120)
