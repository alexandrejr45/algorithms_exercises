# We have discussed that numeric types are immutable, and that use of the = operator in this context causes
# the creation of a new instance (not the mutation of an existing instance).
# How is it still possible, then, that our implementation of scale changes the
# actual parameter sent by the caller?


numbers = [3, 50, 1, 0, -5, 4, 67, 100]
x_factor = 4


def scale(data, factor):
    for j in range(len(data)):
        data[j] *= factor
    print(data)


scale(numbers, x_factor)
print(numbers)
print(id(numbers))
