from BinaryClassifierTree import *
import DensityStrategyFunctions


class BinaryDensityClassifierTree(BinaryClassifierTree):
    def __init__(self, dimensions):
        super().__init__(dimensions)

    def _getPartitionValue(self, leaves):
        return DensityStrategyFunctions.getDensity(leaves)
