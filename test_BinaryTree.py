import unittest
from BinaryTree import *


class MyTestCase(unittest.TestCase):
    def test_init(self):
        tree = BinaryTree(1)
        assert isinstance(tree, BinaryTree)

    def test_addOneItemOneDimension(self):
        tree = BinaryTree(1)
        tree.add([0], 'testItem')
        leaves = tree.getLeaves()
        stringified = self.leavesListToString(leaves)
        self.assertSame(['[0] testItem'], stringified)

    def test_addTwoItemsOneDimension_leftThenRight(self):
        tree = BinaryTree(1)
        tree.add([0], 'testItem1')
        tree.add([1], 'testItem2')
        leaves = tree.getLeaves()
        s = self.leavesListToString(leaves)
        self.assertSame(['[0] testItem1', '[1] testItem2'], s)

    def test_addTwoItemsOneDimension_leftThenLeft(self):
        tree = BinaryTree(1)
        tree.add([0], 'testItem1')
        tree.add([-1], 'testItem2')
        leaves = tree.getLeaves()
        s = self.leavesListToString(leaves)
        self.assertSame(['[-1] testItem2', '[0] testItem1'], s)

    def test_addThreeItemsOneDimension_leftThenLeftThenLeft(self):
        tree = BinaryTree(1)
        tree.add([0], 'testItem1')
        tree.add([-1], 'testItem2')
        tree.add([1], 'testItem3')
        leaves = tree.getLeaves()
        s = self.leavesListToString(leaves)
        self.assertSame(['[-1] testItem2', '[0] testItem1', '[1] testItem3'], s)

    def test_addOneItemTwoDimensions(self):
        tree = BinaryTree(2)
        tree.add([0,0], 'testItem1')
        leaves = tree.getLeaves()
        s = self.leavesListToString(leaves)
        self.assertSame(['[0, 0] testItem1'], s)

    def test_addTwoItemsTwoDimensions(self):
        tree = BinaryTree(2)
        tree.add([0, 0], 'testItem1')
        tree.add([1, 0], 'testItem2')
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
