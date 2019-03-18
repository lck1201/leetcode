# see https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14435/Clever-idea-making-it-simple
# hard in medium
class Solution:
    # def search(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: int
    #     """
    #     lo, hi = 0, len(nums)
    #     while lo < hi:
    #         mid = (hi + lo)//2
    #         if (nums[0] <= nums[mid]) == (nums[0] <= target):
    #             act_mid = nums[mid]
    #         else:
    #             if target < nums[0]:
    #                 act_mid = float('-inf')
    #             else:
    #                 act_mid = float('inf')
    #
    #         if act_mid < target:
    #             lo = mid + 1
    #         elif act_mid > target:
    #             hi = mid
    #         else:
    #             return mid
    #
    #     return -1


    def search(self, nums, target):
        lo, hi = 0, len(nums)

        # low & high will definitely converge to the same side
        while lo < hi:
            mid = (lo + hi) // 2

            # If nums[mid] and target are "on the same side" of nums[0], just take nums[mid]

            # nums[mid] and target, ON THE SAME SIDE
            if (nums[mid] < nums[0]) == (target < nums[0]):
                if (nums[mid] < target):
                    lo = mid + 1
                elif (nums[mid] > target):
                    hi = mid
                else:
                    return mid # only return condition. It can always converge to the right 'mid'
            else:
                # nums[mid] and target, ON DIFFERENCE SIDE
                if target < nums[0]:
                    lo = mid + 1
                else:
                    hi = mid

        return -1