"""Octree container for 3D points."""

import numpy as np
OCTANTS = [(1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1),
           (-1, 1, 1), (-1, 1, -1), (-1, -1, 1), (-1, -1, -1)]


class OcTree(object):
    """Class for octree container of 3D points."""
    def __init__(self, points, bounds=None):
        "Initialize Octree from set of points"
        self.points = points
        if bounds:
            self.bounds = bounds
        else:
            self.bounds = self.get_bounds()
        self.center = (self.bounds[0] + self.bounds[1])/2
        self.children = {}

    def get_bounds(self):
        "Return bounding box of all the points"
        if len(self.points) <= 0:
            return (-np.inf, np.inf)
        else:
            dim = len(self.points[0].coordinates)
            bound_min = np.zeros(dim)
            bound_max = np.zeros(dim)
            for i in range(dim):
                bound_min[i] = min(x.coordinates[i] for x in self.points)
                bound_max[i] = max(x.coordinates[i] for x in self.points)
            return (bound_min, bound_max)

    def generate_octants(self):
        "Split current box into new octants"
        diagonal = self.bounds[1] - self.bounds[0]
        for octant in OCTANTS:
            bounds = np.array([self.center + octant*diagonal, self.center])
            bounds = (bounds.min(0), bounds.max(0))
            self.children[octant] = OcTree(np.array([]), bounds)

    def classify_point(self, point):
        """Classify in which octant the point is included."""
        diagonal = point.coordinates - self.center
        octant = tuple(1 if x >= 0 else -1 for x in diagonal)
        return octant

    def append_point(self, point):
        "Append point into the tree."
        octant = self.classify_point(point)
        if len(self.children) <= 0:
            self.points.append(point)
        else:
            self.children[octant].append_point(point)

    def fill_octree(self):
        """Fills points into the tree."""
        if len(self.children) <= 0:
            self.generate_octants()
        for point in self.points:
            self.append_point(point)
        self.points = np.array([])

    def all_points(self):
        "Return an array of all points in the tree"
        if len(self.children) <= 0:
            return self.points
        points = []
        for octree in self.children:
            points.append(octree.all_points())
        return points
