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
            elif isinstance(n, Node):
                leaves.extend(n.getLeaves())
        return leaves

    def add(self, locationAsArray, item):
        if self._partitionValue is None:
            self._partitionValue = self._getDimensionValueToUseForThisDepth(locationAsArray)
        if self._shouldUseLeft(locationAsArray):
            self._left = self._addItem(self._left, locationAsArray, item)
        else:
            self._right = self._addItem(self._right, locationAsArray, item)

    def _getDimensionValueToUseForThisDepth(self, locationAsArray):
        return locationAsArray[self._depth % self._dimensions]

    def _shouldUseLeft(self, locationAsArray):
        # print('partition value is ' + str(self._partitionValue))
        # print('locationAsArray is ' + str(locationAsArray))
        value = self._getDimensionValueToUseForThisDepth(locationAsArray)
        return value <= self._partitionValue

    def _createNodeFromLeaf(self, leaf, partitionValue):
        node = Node(self._dimensions, self._depth+1)
        node._partitionValue = partitionValue
        node.add(leaf.LocationAsArray, leaf.Item)
        return node

    def _addItem(self, branch, locationAsArray, item):
        if isinstance(branch, Leaf):
            halfway = (self._getDimensionValueToUseForThisDepth(locationAsArray) + self._getDimensionValueToUseForThisDepth(branch.LocationAsArray)) / 2.0
            branch = self._createNodeFromLeaf(branch, halfway)
        if branch is None:
            branch = Leaf()
        branch.add(locationAsArray, item)
        return branch


class BinaryTree(Node):
    def __init__(self, dimensions):
        super().__init__(dimensions, 0)
