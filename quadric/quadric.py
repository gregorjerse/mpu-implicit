# Fit quadric surface to a set of points
from numpy.linalg import norm
from numpy import dot
from constants import n_min, q_closest_num


def find_closest(q, points, n):
    """
    Find n closest points from the list points to the point q.
    Points is a list of structures of type Point and q is
    a structure of type Point.
    """
    distances = [(norm(p - q), p) for p in points]
    distances.sort()
    return [e[1] for e in distances[:n]]


def test_q(q, closest_points):
    """
    Perform a test given by the equation (9).
    """
    # TODO: how about zero? Is 0, -1, -3 OK or not?
    signs = [dot(p.normal, q - p) >= 0
             for p in closest_points]
    return all(signs) or not any(signs)


def weigth(p):
    # Weigth function at point p
    # TODO: implement
    return 0


def get_maximal_angle_variation(points):
    """
    TODO implement algorithm above (a) on page 4.
    """
    angle_variation = 0
    # TODO: implement algorithm
    return angle_variation


def general_quadric_fit(points, cell):
    # Return matrix A, vector b and scalar c.
    # Quadric form.
    # Q(x) = x^{T}Ax +b^T + c
    # The cell is currently given as a tuple
    # center, corner points.
    c, qs = cell[0], cell[1:]
    d = dict()
    for q in qs:
        closest = find_closest(q, points, q_closest_num)
        if not test_q(q, closest):
            qs.remove(q)
        else:
            # TODO: normal
            d[q] = 1/6 * sum(np.dot(n, q-p))
    # qs contains suitable auxiliary points
    # d[q] is the distance d_i
    
    
def f(x):
    
    