import seqiter

class Vector:
#"""represent a vector in multidimensional space."""

    def __init__(self,d):        
        """create d-dimensional vector of zeros."""
        self._coords = d

    def __len__(self):
        """Specifies a __len__ method for Vector: Returns the length of Vector"""
        return len(self._coords)

    def __getitem__(self,j):
        """Return jth coordinate of Vector."""
        return self._coords[j]

    def __setitem__(self,j,val):
        """Set jth coordinate of vector to given value."""
        self._coords[j] = val

    def __add__(self,other):
        """Return sum of two vectors."""
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector([0]*len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __mul__(self,other):
        if len(self) != 3:
            raise ValueError('Dimension must be 3')
        if len(self) != len(other):
            raise ValueError('Both dimensions must be 3 and must agree')
        result = Vector([0]*len(self))
        if len(self) == 3:
            result[0] = self[1]*other[2] - self[2]*other[1]
            result[1] = self[2]*other[0] - self[0]*other[2]
            result[2] = self[0]*other[1] - self[1]*other[0]
            return result

    def __neg__(self):
        result = Vector([0]*len(self))
        for i in range(len(self)):
        	result[i] = -self[i]
        return result


    def __eq__(self,other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords

    def __ne__(self,other):
        """Return True if vector differs from other."""
        return not (self == other)

    def __str__(self):
        """Produce string representation of vector."""
        return '<' + str(self._coords)[1:-1] +  '>' 

