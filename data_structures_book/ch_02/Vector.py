
class Vector:
    """ Represent a vector in a multidimensional space."""

    def __init__(self, d):
        self._coords = [0] * d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, item):
        return self._coords[item]

    def __setitem__(self, key, value):
        self._coords[key] = value

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))

        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return f'< {str(self._coords)[:-1]}>'


v = Vector(7)
v[1] = 290
v[-1] = 78
c = Vector(7)
c[2] = 29
c[1] = 89
c[-1] = 90
print(v)
print(c)
g = c + v
print(g)


