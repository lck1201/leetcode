class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for x in nums:
            result = result^x

        return result