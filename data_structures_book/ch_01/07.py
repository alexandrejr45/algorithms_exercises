# Give a single command that computes the sum from Exercise R-1.6, rely-
# ing on Python’s comprehension syntax and the built-in sum function

def odd_squares(n: int):
    return sum([pow(x, 2) for x in range(1, n) if x % 2 != 0])


print(odd_squares(4))
print(odd_squares(4002))
print(odd_squares(833))
print(odd_squares(6))
print(odd_squares(112))

