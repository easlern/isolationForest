import unittest
from BinaryDensityClassifierTree import *
from TestTools import *
from Leaf import *


def leaf(num):
    if not isinstance(num, list):
        num = [num]
    return Leaf(num, str(num))

class BinaryDensityClassifierTreeTests(unittest.TestCase):
    def test_init(self):
        tree = self._createSubject()
        assert isinstance(tree, BinaryDensityClassifierTree)

    def test_addItemMakesGetGroupsReturnSimilarGroups(self):
        tree = self._createSubject()
        leaves = [leaf(1),leaf(2),leaf(3), leaf(20),leaf(21),leaf(22)]
        tree.populate(leaves)
        a, b, c, d, e, f = leaves
        assertSame([[a,b,c], [d,e,f]], tree.getGroups())

    def test_addingTwoGroupsInTwoDimensions_MakesGetGroupsReturnTwoGroups(self):
        tree = self._createSubject()
        leaves = [leaf([1,0]),leaf([2,0]),leaf([3,0]), leaf([20,0]),leaf([21,0]),leaf([22,0])]
        tree.populate(leaves)
        a, b, c, d, e, f = leaves
        assertSame([[a,b,c], [d,e,f]], tree.getGroups())

    def test_addingThreeGroupsInTwoDimensions_MakesGetGroupsReturnThreeGroups(self):
        tree = self._createSubject()
        leaves = [leaf([1,0]),leaf([2,0]),leaf([3,0]), leaf([20,0]),leaf([21,0]),leaf([22,0])]
        tree.populate(leaves)
        a, b, c, d, e, f = leaves
        assertSame([[a,b,c], [d,e,f]], tree.getGroups())

    def test_addingThreeGroups_MakesGetGroupsReturnThreeGroups(self):
        tree = self._createSubject()
        leaves = [leaf(1),leaf(2),leaf(3), leaf(20),leaf(21),leaf(22), leaf(30),leaf(31),leaf(32)]
        tree.populate(leaves)
        a, b, c, d, e, f, g, h, i = leaves
        assertSame([[a,b,c], [d,e,f], [g,h,i]], tree.getGroups())

    def test_addingRegurlarlyDistributedPoints_MakesGetGroupsReturnOneGroup(self):
        tree = self._createSubject()
        leaves = [leaf(1),leaf(2),leaf(3),leaf(4),leaf(5)]
        tree.populate(leaves)
        a, b, c, d, e = leaves
        assertSame([[a,b,c,d,e]], tree.getGroups())

    def _createSubject(self, dimensions=1):
        return BinaryDensityClassifierTree(dimensions)


if __name__ == '__main__':
    unittest.main()
