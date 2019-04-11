class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        p = 1
        for idx in range(len(nums)): # store the multiplication of left-side elements
            result.append(p)
            p = p*nums[idx]

        p = 1
        for idx in range(len(nums)-1,-1,-1): # store the multiplication of right-side elements
            result[idx] *= p
            p = p * nums[idx]

        return result


re = Solution().productExceptSelf([2,2,3,4,2])
print(re)