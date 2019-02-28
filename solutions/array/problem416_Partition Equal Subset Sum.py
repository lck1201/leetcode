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
                if table[i] == 1:
                    if i+x < len(table):
                        table[i+x] = 1

        return table[-1]==1