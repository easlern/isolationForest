class Leaf:
    def __init__(self):
        self.LocationAsArray = None
        self.Item = None

    def add(self, locationAsArray, item):
        self.LocationAsArray = locationAsArray
        self.Item = item


class Node:
    def __init__(self, dimensions, depth):
        self._dimensions = dimensions
        self._depth = depth
        self._left = None
        self._right = None
        self._partitionValue = None

    def getLeaves(self):
        leaves = []
        for n in [self._left, self._right]:
            if isinstance(n, Leaf):
                leaves.append(n)
            else:
                leaves.extend(n.getAll())
        return leaves

    def add(self, locationAsArray, item):
        if self._shouldUseLeft(locationAsArray):
            self._left = self._addItem(self._left, locationAsArray, item)
        else:
            self._right = self._addItem(self._right, locationAsArray, item)

    def _getDimensionValueToUseForThisDepth(self, pointVectorAsArray):
        return pointVectorAsArray[self._depth % self._dimensions]

    def _shouldUseLeft(self, pointVectorAsArray):
        return self._getDimensionValueToUseForThisDepth(pointVectorAsArray) <= self._partitionValue

    def _createNodeFromLeaf(self, leaf):
        node = Node(self._dimensions, self._depth+1)
        node.add(leaf.LocationAsArray, leaf.Item)
        return node

    def _addItem(self, branch, locationAsArray, item):
        if isinstance(branch, Leaf):
            branch = self._createNodeFromLeaf(branch)
        if branch is None:
            branch = Leaf()
        branch.add(locationAsArray, item)
        return branch


class BinaryTree:
    def __init__(self, dimensions):
        self._rootNode = Node(dimensions, 0)
        self.add = self._rootNode.add

    def getLeaves(self):
        return self._rootNode.getAll()
