import random

import DensityStrategyFunctions


class Node:
    def __init__(self, dimensions, depth, randomGenerator, leaves):
        self._dimensions = dimensions
        self._depth = depth
        self._randomGenerator = randomGenerator
        self._leftNode = None
        self._rightNode = None
        self._partitionValue = None
        self._leaves = []
        self._add(leaves)
        self._id = self._randomGenerator.getrandbits(64)

    def __lt__(self, other):
        return str(self) < str(other)

    def getGroups(self):
        if len(self._leaves) > 0:
            return [self._leaves]
        groups = []
        if self._leftNode is not None:
            groups.extend(self._leftNode.getGroups())
        if self._rightNode is not None:
            groups.extend(self._rightNode.getGroups())
        return groups

    def _getPartitionValue(self, leaves):
        partitionPoint = DensityStrategyFunctions.getPartition(list(map(lambda l: self._getDimensionValueToUseForThisDepth(l.LocationAsArray), leaves)))
        if partitionPoint is None:
            return None
        return self._getDimensionValueToUseForThisDepth(leaves[partitionPoint].LocationAsArray)

    def _add(self, leaves):
        if len(leaves) < 1:
            return
        self._partitionValue = self._getPartitionValue(leaves)
        if self._partitionValue is None:
            self._leaves = leaves
            return

        # print('min ' + str(minValue) + ' max ' + str(maxValue) + ' partition ' + str(partitionValue))
        lefts = list()
        rights = list()
        for l in leaves:
            if self._shouldUseLeft(l.LocationAsArray):
                lefts.append(l)
            else:
                rights.append(l)

        def _addBranch(leavesList):
            node = Node(self._dimensions, self._depth+1, self._randomGenerator, leavesList)
            return node
        self._leftNode = _addBranch(lefts)
        self._rightNode = _addBranch(rights)

    def _getDimensionValueToUseForThisDepth(self, locationAsArray):
        return locationAsArray[self._depth % self._dimensions]

    def _shouldUseLeft(self, locationAsArray):
        value = self._getDimensionValueToUseForThisDepth(locationAsArray)
        return value < self._partitionValue


class BinaryDensityClassifierTree:
    def __init__(self, randomSeed=None):
        self._rootNode = None
        self._randomGenerator = random.Random()
        if randomSeed is not None:
            self._randomGenerator.seed(randomSeed)

    # All leaves must have the same number of dimensions in their locations
    def populate(self, leaves):
        dimensions = len(leaves[0].LocationAsArray)
        self._rootNode = Node(dimensions, 0, self._randomGenerator, leaves)

    def getGroups(self):
        return self._rootNode.getGroups()
