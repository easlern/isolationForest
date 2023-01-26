import unittest
from BinaryTree import *


class MyTestCase(unittest.TestCase):
    def test_init(self):
        tree = BinaryTree(1)
        assert isinstance(tree, BinaryTree)

    def test_add(self):
        tree = BinaryTree(1)
        tree.add([0], 'testItem')
        leaves = tree.getLeaves()
        stringified = str(list(map(lambda l: l.LocationAsArray, leaves)))
        assert stringified == '[[0]]'


if __name__ == '__main__':
    unittest.main()
