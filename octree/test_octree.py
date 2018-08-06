import octree
import numpy as np

def test_init():
    oc_tree = octree.OcTree(np.array([[0, 0, 0], [1, 1, 1]]))
    assert (oc_tree.bounds == [[0, 0, 0], [1, 1, 1]]).all()
    oc_tree.generate_octants()
    assert len(oc_tree.children) == 8
