import unittest
from BinaryDensityClassifierTree import *
from TestTools import *
from Leaf import *


class BinaryDensityClassifierTreeTests(unittest.TestCase):
    def test_init(self):
        tree = self._createSubject()
        assert isinstance(tree, BinaryDensityClassifierTree)

    def test_addItemMakesGetGroupsReturnSimilarGroups(self):
        tree = self._createSubject()

        def leaf(num):
            return Leaf([num], str(num))
        leaves = [leaf(1),leaf(2),leaf(3), leaf(20),leaf(21),leaf(22)]
        tree.populate(leaves)
        a, b, c, d, e, f = leaves
        assertSame([[a,b,c], [d,e,f]], tree.getGroups())

    def _createSubject(self, dimensions=1):
        return BinaryDensityClassifierTree(dimensions)


if __name__ == '__main__':
    unittest.main()
