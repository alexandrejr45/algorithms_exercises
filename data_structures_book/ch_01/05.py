# Give a single command that computes the sum from Exercise R-1.4, rely-
# ing on Python’s comprehension syntax and the built-in sum function

def int_squares_simple(n: int):
    return sum([pow(x, 2) for x in range(1, n)])


print(int_squares_simple(4))
print(int_squares_simple(4002))
print(int_squares_simple(833))
print(int_squares_simple(6))
print(int_squares_simple(112))

