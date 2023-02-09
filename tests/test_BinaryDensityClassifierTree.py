import unittest
from BinaryDensityClassifierTree import *
from Leaf import *

from TestTools import *


class BinaryDensityClassifierTreeTests(unittest.TestCase):
    def test_init(self):
        tree = BinaryDensityClassifierTree(1)
        assert isinstance(tree, BinaryDensityClassifierTree)




if __name__ == '__main__':
    unittest.main()
