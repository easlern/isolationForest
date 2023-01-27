import random


class Leaf:
    def __init__(self, locationAsArray, item):
        self.LocationAsArray = locationAsArray
        self.Item = item


class Node:
    def __init__(self, dimensions, depth, randomGenerator, leaves):
        self._dimensions = dimensions
        self._depth = depth
        self._randomGenerator = randomGenerator
        self._left = None
        self._right = None
        self._partitionValue = None
        self._add(leaves)

    def getLeaves(self):
        leaves = []
        for n in [self._left, self._right]:
            if isinstance(n, Leaf):
                leaves.append(n)
            elif isinstance(n, Node):
                leaves.extend(n.getLeaves())
        return leaves

    def _add(self, leaves):
        minValue = min(map(lambda l: self._getDimensionValueToUseForThisDepth(l.LocationAsArray), leaves))
        maxValue = max(map(lambda l: self._getDimensionValueToUseForThisDepth(l.LocationAsArray), leaves))
        partitionValue = self._randomGenerator.uniform(minValue, maxValue)
        self._partitionValue = partitionValue
        lefts = list()
        rights = list()
        for l in leaves:
            if self._shouldUseLeft(l.LocationAsArray):
                lefts.append(l)
            else:
                rights.append(l)

        def _addBranch(leavesList):
            if len(leavesList) == 1:
                return leavesList[0]
            if len(leavesList) > 1:
                node = Node(self._dimensions, self._depth+1, self._randomGenerator, leavesList)
                return node
            return None
        self._left = _addBranch(lefts)
        self._right = _addBranch(rights)

    def _getDimensionValueToUseForThisDepth(self, locationAsArray):
        return locationAsArray[self._depth % self._dimensions]

    def _shouldUseLeft(self, locationAsArray):
        value = self._getDimensionValueToUseForThisDepth(locationAsArray)
        return value <= self._partitionValue


class BinaryClassifierTree:
    def __init__(self, randomSeed=None):
        self._rootNode = None
        self._randomGenerator = random.Random()
        if randomSeed is not None:
            self._randomGenerator.seed(randomSeed)

    # All leaves must have the same number of dimensions in their locations
    def populate(self, leaves):
        dimensions = len(leaves[0].LocationAsArray)
        self._rootNode = Node(dimensions, 0, self._randomGenerator, leaves)

    def getLeaves(self):
        return self._rootNode.getLeaves()
