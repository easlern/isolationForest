import unittest
import DensityStrategyFunctions

from TestTools import *


class DensityStrategyFunctionsTests(unittest.TestCase):
    def test_2ClustersWithSameDensity_shouldPartitionSecondCluster(self):
        pivot = DensityStrategyFunctions.getPartition([0,1,2, 10,11,12])
        # print('got pivot ' + str(pivot))
        assertSame(3, pivot)
    def test_3ClustersWithSameDensity_shouldPartitionSecondCluster(self):
        pivot = DensityStrategyFunctions.getPartition([0,1,2, 10,11,12, 20,21,22])
        assertSame(3, pivot)

    def test_1ClusterWithHighDensity_shouldNotPartition(self):
        pivot = DensityStrategyFunctions.getPartition([0,1,2])
        assertSame(None, pivot)

    def test_1ClusterWithOutlier_shouldPartitionAtOutlier(self):
        pivot = DensityStrategyFunctions.getPartition([0,1,2, 10])
        assertSame(3, pivot)

if __name__ == '__main__':
    unittest.main()
