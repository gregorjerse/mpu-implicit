# Fit quadric surface to a set of points
from numpy.linalg import norm
from numpy import transpose, matmul
from math import pi

from .general import general_quadric_fit
from constants import n_min


def find_closest(q, points, n):
    """
    Find n closest points from the list points to the point q.
    Points is a list of structures of type Point and q is
    a structure of type Point.
    """
    distances = [(norm(p - q), p) for p in points]
    distances.sort()
    return [e[1] for e in distances[:n]]


def weight(point):
    """
    Return the value of the weight function evaluated at the point
    point. The point is an object of type Point.
    """
    return 0


def get_maximal_angle_variation(points):
    """
    TODO implement algorithm above (a) on page 4.
    """
    angle_variation = 0
    # TODO: implement algorithm
    return angle_variation


def q_func(A, b, c):
    """
    Return a function which given a point x (a numpy array)
    computes the value of the function Q at the point x: Q(x).
    Q(x) =  x'A x + b' x + c
    where ' is a transpose operator.
    """
    def q(x):
        first = matmul(matmul(transpose(x), A), x)
        second = matmul(transpose(b), x)
        return first + second + c
    return q


def decide(points, cell):
    """
    Which quadric fit to apply?
    """
    if len(points) > 2 * n_min:
        angle_variation = get_maximal_angle_variation(points)
        if angle_variation > pi / 2:
            # Return implementation (a)
            return general_quadric_fit(points, cell)
        else:
            # TODO: implement (b)
            return general_quadric_fit(points, cell)
    else:
        # TODO: implement (c)
        return general_quadric_fit(points, cell)
