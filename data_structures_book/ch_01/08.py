# Python allows negative integers to be used as indices into a sequence,
# such as a string. If string s has length n, and expression s[k] is used for in-
# dex −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references
# the same element?

def string_index(s, k):
    length = len(s)
    pos_ind = length - abs(k)
    print(s)
    print(f'Negative index {k}, value: {s[k]}')
    print(f'Positive index {pos_ind}, value: {s[pos_ind]}')
    print("\n")


string_index("The end of the world", -5)
string_index("Arigato osmsmsm22m2", -9)
string_index("What if??", -1)
string_index("There a snake in my boot", -6)
string_index("Should I stay or should I go?", -8)
