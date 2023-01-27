import unittest
from BinaryClassifierTree import *


class MyTestCase(unittest.TestCase):
    def test_init(self):
        tree = BinaryClassifierTree(1)
        assert isinstance(tree, BinaryClassifierTree)

    def test_addOneItemOneDimension(self):
        tree = BinaryClassifierTree(1)
        tree.populate([Leaf([0], 'testItem')])
        leaves = tree.getLeaves()
        stringified = self.leavesListToString(leaves)
        self.assertSame(['[0] testItem'], stringified)

    def test_addTwoItemsOneDimension_leftThenRight(self):
        tree = BinaryClassifierTree(1)
        tree.populate([Leaf([0], 'testItem1'), Leaf([1], 'testItem2')])
        leaves = tree.getLeaves()
        s = self.leavesListToString(leaves)
        self.assertSame(['[0] testItem1', '[1] testItem2'], s)

    def test_addTwoItemsOneDimension_leftThenLeft(self):
        tree = BinaryClassifierTree(1)
        tree.populate([Leaf([0], 'testItem1'), Leaf([-1], 'testItem2')])
        leaves = tree.getLeaves()
        s = self.leavesListToString(leaves)
        self.assertSame(['[-1] testItem2', '[0] testItem1'], s)

    def test_addThreeItemsOneDimension_leftThenLeftThenLeft(self):
        tree = BinaryClassifierTree(1)
        tree.populate([Leaf([0], 'testItem1'), Leaf([-1], 'testItem2'), Leaf([1], 'testItem3')])
        leaves = tree.getLeaves()
        s = self.leavesListToString(leaves)
        self.assertSame(['[-1] testItem2', '[0] testItem1', '[1] testItem3'], s)

    def test_addOneItemTwoDimensions(self):
        tree = BinaryClassifierTree(2)
        tree.populate([Leaf([0, 0], 'testItem1')])
        leaves = tree.getLeaves()
        s = self.leavesListToString(leaves)
        self.assertSame(['[0, 0] testItem1'], s)

    def test_addTwoItemsTwoDimensions(self):
        tree = BinaryClassifierTree(2)
        tree.populate([Leaf([0, 0], 'testItem1'), Leaf([1, 0], 'testItem2')])
        leaves = tree.getLeaves()
        s = self.leavesListToString(leaves)
        self.assertSame(['[0, 0] testItem1', '[1, 0] testItem2'], s)

    def leavesListToString(self, leavesList):
        return str(list(map(lambda l: str(l.LocationAsArray) + ' ' + str(l.Item), leavesList)))

    def assertSame(self, expect, got):
        if str(expect) != str(got):
            print('Expect: ' + str(expect) + '. Got: ' + str(got))
        assert str(expect) == str(got)


if __name__ == '__main__':
    unittest.main()
