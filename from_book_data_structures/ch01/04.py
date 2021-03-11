# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.

def int_squares(n):
    sum_squares = 0
    for x in range(1, n):
        sum_squares += pow(x, 2)

    return sum_squares


print(int_squares(4))
print(int_squares(4002))
print(int_squares(833))
print(int_squares(6))
print(int_squares(112))
