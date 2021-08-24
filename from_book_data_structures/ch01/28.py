# Give an implementation of a function named norm such that norm(v, p) returns the p-norm
# value of v and norm(v) returns the Euclidean norm of v. You may assume that v is a list of numbers.

def norm(v, p=2):
    p_norm = 0
    for x in v:
        p_norm += v**p

    p_norm
