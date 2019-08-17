class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # # bit manipulation, very good
        # ans = 0
        # for i in range(len(nums)):
        #     ans ^= i
        #     ans ^= nums[i]
        #
        # return ans

        # O(N)
        # gaussian sum
        # totolSum = 0.5 * len(nums) * (len(nums)+1)
        # currentSum = sum(nums)
        # return int(totolSum - currentSum)

        # O(N * LogN)
        # binary search
        nums.sort()
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] != mid:
                if mid == 0 or nums[mid - 1] == mid - 1:
                    return mid
                right = mid - 1
            else:
                left = mid + 1

        return left
