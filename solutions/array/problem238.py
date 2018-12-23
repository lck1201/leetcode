class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        p = 1
        for idx in range(len(nums)):
            result.append(p)
            p = p*nums[idx]

        p = 1
        for idx in range(len(nums)-1,-1,-1):
            result[idx] *= p
            p = p * nums[idx]

        return result