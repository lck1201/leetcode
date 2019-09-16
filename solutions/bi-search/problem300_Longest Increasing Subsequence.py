class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            lo, hi = 0, size
            while lo != hi:
                m = (lo + hi) // 2
                if tails[m] < x:
                    lo = m + 1
                else:
                    hi = m

            tails[lo] = x
            size = max(lo + 1, size)
            print(tails)
        return size


a = Solution().lengthOfLIS([10, 9, 2, 5, 4, 7, 101, 3])
