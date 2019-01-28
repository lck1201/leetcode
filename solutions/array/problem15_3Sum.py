class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        for idx in range(len(nums) - 2):
            if idx > 0 and (nums[idx] == nums[idx-1]):
                continue

            lo = idx + 1
            hi = len(nums) - 1
            while lo < hi:
                target = nums[idx] + nums[lo] + nums[hi]
                if target < 0:
                    lo += 1
                elif target > 0:
                    hi -= 1
                else:
                    result.append([nums[idx], nums[lo], nums[hi]])
                    while lo < hi and nums[lo] == nums[lo+1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi-1]:
                        hi -= 1

                    lo += 1
                    hi -= 1

        return result