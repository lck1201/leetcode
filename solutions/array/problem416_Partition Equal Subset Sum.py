class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums)%2 == 1:
            return False

        target = sum(nums) // 2
        table = [0] * (target+1)
        table[0] = 1

        for x in nums:
            for i in range(len(table)-1, -1, -1):
                if i - x >= 0 and table[i-x] == 1:
                    table[i] = 1

        return table[target] == 1