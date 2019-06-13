class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # # bit manipulation
        # ans = 0
        # i = 0
        # while i < len(nums):
        #     ans = i ^ nums[i] ^ ans
        #     i += 1
        #
        # return ans ^ i

        # gaussian sum
        # totolSum = 0.5* len(nums) * (len(nums)+1)
        # currentSum = sum(nums)
        # return totolSum - currentSum

        # binary search
        nums.sort()
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid]>mid:
                right = mid
            elif nums[mid]==mid:
                left = mid+1

        return left
