import sys
class Solution:
    def maxSubArray2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = float("-inf")
        tempSum = 0
        for n in nums:
            tempSum += n
            ans = max(tempSum, ans)
            if tempSum < 0:
                tempSum = 0

        return ans

    def maxSubArray(self, nums):
        table = [0] * len(nums)
        ans = table[0] = nums[0]
        for i in range(1, len(nums)):
            if table[i - 1] > 0:
                table[i] = table[i - 1] + nums[i]
            else:
                table[i] = nums[i]

            ans = max(ans, table[i])
        return ans


inp = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Solution().maxSubArray(inp)
