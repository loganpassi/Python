#Logan Passi
#CPSC-34000
#08/28/19
#negatedVector.py
#Implement the neg method for the Vector class of Section 2.3.3, so
#that the expression −v returns a new vector instance whose coordinates
#are all the negated values of the respective coordinates of v.

class Vector:

    def __init__(self, d):
        self._coords = [0] * d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, val):
        self._coords[j] = val

    def __add(self,  other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'

myVec = Vector(3)
