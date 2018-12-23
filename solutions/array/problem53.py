import sys
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        totalSum = -sys.maxsize -1
        tempSum = 0
        for n in nums:
            tempSum += n
            totalSum = max(tempSum, totalSum)
            if tempSum < 0:
                tempSum = 0

        return totalSum
