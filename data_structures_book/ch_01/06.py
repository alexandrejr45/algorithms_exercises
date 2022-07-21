# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the odd positive integers smaller than n.

def odd_squares(n: int):
    sum_numbers = 0
    for x in range(1, n):
        if x % 2 != 0:
            sum_numbers += pow(x, 2)
    return sum_numbers


print(odd_squares(9))
print(odd_squares(4002))
print(odd_squares(833))
print(odd_squares(6))
print(odd_squares(112))

