from numpy import dot
from scipy.optimize import minimize

from .quadric import find_closest, q_func, weight
from constants import q_closest_num


def minimize_func_x(x, points, weights, weightsum, qs, d):
    """
    Implementation of the function (11).
    The argument x is a 1D numpy array containing
    rows of the matrix A, vector b and scalar c.
    It contains 9 + 3 + 1 = 13 entried.
    The function is called by numpy.minimize in order to find minimum
    of the function.
    """
    A = [x[0:3], x[3:6], x[6:9]]
    b = x[9:12]
    c = x[12]
    first_sum = 0
    for i in range(len(points)):
        p = points[i]
        weight = weights[i]
        first_sum += weight * q_func(A, b, c)(p)**2
    first_sum /= weightsum
    second_sum = 0
    for q in qs:
        second_sum += (q_func(A, b, c)(q) - d[q])**2
    second_sum /= len(qs)
    return first_sum + second_sum


def general_quadric_fit(points, cell):
    """
    Return matrix A, vector b and scalar c that determine the
    quadric in a general fit.
    The current cell is given a tuple (center_point, qs).
    # TODO: uskladi z Martinom.
    """
    c, qs = cell[0], cell[1:]
    d = dict()
    remaining_qs = []
    for q in qs:
        closest_points = find_closest(q, points, q_closest_num)
        dot_products = [dot(p.normal, q - p) >= 0 for p in closest_points]
        signs = [dp >= 0 for dp in dot_products]
        if all(signs) or not any(signs):
            remaining_qs.append(q)
            d[q] = 1/6 * sum(dot_products)
    if len(remaining_qs) == 0:
        # TODO: subdivide cell, recurse into subdivided cells
        pass
    else:
        weights = [weight(p) for p in points]
        weights_sum = sum(weights)
        # TODO: Find more appropriate x0
        x0 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        res = minimize(minimize_func_x,
                       x0,
                       args=(points, weights, weights_sum, remaining_qs, d))
        A = [res.x[0:3], res.x[3:6], res.x[6:9]]
        b = [res.x[9:12]]
        c = res.x[13]
        return (A, b, c)
