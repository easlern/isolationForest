import BinaryClassifierTree
import DensityStrategyFunctions


class BinaryDensityClassifierTree(BinaryClassifierTree):
    def _getPartitionValue(self, leaves):
        return DensityStrategyFunctions.getDensity(leaves)
