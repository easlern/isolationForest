import random


class Leaf:
    def __init__(self, locationAsArray, item):
        self.LocationAsArray = locationAsArray
        self.Item = item
        self.Depth = None


class Node:
    def __init__(self, dimensions, depth, randomGenerator, leaves):
        self._dimensions = dimensions
        self._depth = depth
        self._randomGenerator = randomGenerator
        self._left = None
        self._right = None
        self._partitionValue = None
        self._add(leaves)
        self._id = self._randomGenerator.getrandbits(64)

    def getLeaves(self):
        leaves = []
        for n in [self._left, self._right]:
            if isinstance(n, Leaf):
                leaves.append(n)
            elif isinstance(n, Node):
                leaves.extend(n.getLeaves())
        return leaves

    def countLeaves(self):
        return len(self.getLeaves())

    def _getPartitionValue(self, leaves):
        return self._getPartitionValueUsingRandomStrategy(leaves)

    def _getPartitionValueUsingDensityStrategy(self, leaves):
        if len(leaves) == 2:
            return None
        assert(len(leaves) > 2)

        leaves.sort(key=lambda l: self._getDimensionValueToUseForThisDepth(l.LocationAsArray))

        def getDensity(l):
            start = self._getDimensionValueToUseForThisDepth(l[0].LocationAsArray)
            end = self._getDimensionValueToUseForThisDepth(l[-1].LocationAsArray)
            width = end - start
            return len(l)*1.0 / width

        for count in range(1, len(leaves)-1):
            r = getDensity(leaves[:count]) / getDensity(leaves[count:])

    def _getPartitionValueUsingRandomStrategy(self, leaves):
        minValue = min(map(lambda l: self._getDimensionValueToUseForThisDepth(l.LocationAsArray), leaves))
        maxValue = max(map(lambda l: self._getDimensionValueToUseForThisDepth(l.LocationAsArray), leaves))
        # Instead of partitioning by a random value, try to find a partition that increases the ratio of number of
        # points beyond a certain threshold?
        partitionValue = self._randomGenerator.uniform(minValue, maxValue)
        return partitionValue

    def _add(self, leaves):
        self._partitionValue = self._getPartitionValue(leaves)
        # print('min ' + str(minValue) + ' max ' + str(maxValue) + ' partition ' + str(partitionValue))
        lefts = list()
        rights = list()
        for l in leaves:
            if self._shouldUseLeft(l.LocationAsArray):
                lefts.append(l)
            else:
                rights.append(l)

        def _addBranch(leavesList):
            if len(leavesList) == 1:
                leavesList[0].Depth = self._depth
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

    def countLeaves(self):
        return self._rootNode.countLeaves()
