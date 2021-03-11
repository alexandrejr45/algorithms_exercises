# Write a short Python function, is even(k), that takes an integer value and
# returns True if k is even, and False otherwise. However, your function
# cannot use the multiplication, modulo, or division operators

def is_even(k):
    even_nums = [0, 2, 4, 6, 8]
    string_k = str(k)
    string_list = [c for c in string_k]
    last_number = string_list[-1] if len(string_list) > 1 else string_list[0]
    print(k)
    try:
        even_nums.index(int(last_number))
        return True
    except ValueError:
        return False


print(is_even(4))
print(is_even(1))
print(is_even(2))
print(is_even(12190032890))
print(is_even(10000))
print(is_even(54759))
print(is_even(98))
print(is_even(66))
print(is_even(-29579482))
print(is_even(-222266))
