# Write a short Python function that takes a sequence of integer values and
# determines if there is a distinct pair of numbers in the sequence whose
# product is odd

numbers = [40, 75, 7, 748, 4, 85, 9, 3, 56]


def distinct_odd(num: list):
    for x in range(len(num)):
        if x < len(num) - 1:
            if num[x] % 2 != 0 and num[x + 1] % 2 != 0:
                print(num[x] * num[x + 1])


distinct_odd(numbers)
