from numpy import dot


class Point:
    def __init__(self, coordinates, normal):
        """
        Coordinates and normals are numpy arrays.
        """
        self.coordinates = coordinates
        self.normal = normal

    def __add__(self, other):
        """
        Add points as vectors, return numpy array of the
        coordinates of the resulting vector.
        """
        return self.coordinates + other.coordinates

    def __sub__(self, other):
        """
        Subtract points (self - other) as vectors, return numpy array of the
        coordinates of the resulting vector.
        """
        return self.coordinates - other.coordinates

    def __mul__(self, other):
        """
        Compute a dot product of vectors with coordinates of
        point self and other.
        """
        return dot(self.coordinates, other.coordinates)
