class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        notMajor = set()
        for digit in nums:
            if digit in notMajor:
                continue

            if nums.count(digit) > len(nums) // 2:
                return digit
            else:
                notMajor.add(digit)