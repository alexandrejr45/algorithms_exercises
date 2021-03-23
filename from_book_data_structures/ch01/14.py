# Write a short Python function that takes a sequence of integer values and
# determines if there is a distinct pair of numbers in the sequence whose
# product is odd

numbers = [40, 75, 7, 748, 4, 85, 9, 3, 56]
odd_product = [(x * y) for x in numbers for y in numbers if x != y and (x * y) % 2 != 0]

# another solution
#
# for x in numbers:
#     for y in numbers:
#         if x != y:
#             if (x * y) % 2 != 0:
#                 print(str(x) + " x " + str(y) + " = " + str(x * y))

print(odd_product)
