# see https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14435/Clever-idea-making-it-simple
# hard in medium
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (hi + lo)//2
            if (nums[0] <= nums[mid]) == (nums[0] <= target):
                act_mid = nums[mid]
            else:
                if target < nums[0]:
                    act_mid = float('-inf')
                else:
                    act_mid = float('inf')

            if act_mid < target:
                lo = mid + 1
            elif act_mid > target:
                hi = mid
            else:
                return mid

        return -1
