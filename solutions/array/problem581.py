class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_num = [n for n in nums]
        new_num.sort()

        condition = list()
        for idx in range(len(nums)):
            if new_num[idx] != nums[idx]:
                condition.append(idx)

        if len(condition) == 0:
            return 0
        else:
            return condition[-1] - condition[0] + 1

# same thinking, but more concise
class Solution_example:
    def findUnsortedSubarray(self, nums):
        is_same = [a == b for a, b in zip(nums, sorted(nums))]
        return 0 if all(is_same) else len(nums) - is_same.index(False) - is_same[::-1].index(False)

# one-pass solution
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/discuss/103057/Java-O(n)-Time-O(1)-Space