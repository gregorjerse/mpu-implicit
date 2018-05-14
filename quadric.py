# Fit quadric surface to a set of points
import numpy as np

def find_closest(q, points, n=6):
    distances = [(np.norm(p-q),p) for p in points]
    return [e[1] for e in distances.sort()[:n]]

def test_q(q, closest_points):
    signs = []
    for p in closest_points:
        #TODO: find normal!
        n = 0
        signs.append(np.dot(n, q-p) >= 0)
    return all(signs) or not any(signs)

def weigth(p):
    # Weigth function at point p
    # TODO: implement
    return 0

def general_quadric_fit(points, cell):
    
    # Return matrix A, vector b and scalar c.
    # Quadric form.
    # Q(x) = x^{T}Ax +b^T + c
    # TODO: p.normal
    c, q1, q2, q3, q4 = cell
    qs = [q1, q2, q3, q4]
    d = dict()
    for q in list(qs):
        closest = find_closest(q, points, n)
        if not test_q(q, closest):
            qs.remove(q)
        else:
            # TODO: normal
            d[q] = 1/6 * sum(np.dot(n, q-p))
    
    # qs contains suitable auxiliary points
    # d[q] is the distance d_i
    
    
    
    
            
        
    
    
    