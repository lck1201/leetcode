import math
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        mindiff = float('inf')
        result = 0
        for idx in range(len(nums) - 2):
            if idx > 0 and (nums[idx] == nums[idx-1]): #skip same number
                continue

            lo = idx + 1 # i->N
            hi = len(nums) - 1 # N->i

            while lo < hi:
                threeSum = nums[idx] + nums[lo] + nums[hi]
                diff = target - threeSum
                if abs(diff) < mindiff:
                    mindiff = abs(diff)
                    result = threeSum

                if diff > 0:
                    lo += 1
                elif diff < 0:
                    hi -= 1
                elif diff == 0:
                    return threeSum

        return result

Solution().threeSumClosest([-1,0,1,1,55], 3)