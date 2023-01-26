import unittest
from BinaryTree import *


class MyTestCase(unittest.TestCase):
    def tree_starts(self):
        tree = BinaryTree(1)
        assert isinstance(tree, BinaryTree)

    def tree_adds(self):
        tree = BinaryTree(1)
        assert str(tree.getAll()) == ''


if __name__ == '__main__':
    unittest.main()
