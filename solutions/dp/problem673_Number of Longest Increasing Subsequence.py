class Solution(object):
    def findNumberOfLIS(self, nums):
        N = len(nums)
        if N <= 1:
            return N
        lengths = [1] * N  # lengths[i] = length of longest sub-string ending in nums[i]
        counts = [1] * N  # count[i] = number of longest ending in nums[i]

        for j, num in enumerate(nums):
            for i in range(j):
                if nums[i] < nums[j]:
                    if lengths[i] >= lengths[j]:  # NOTE: what does this line mean?
                        # NOTE: num[j] > num[i], so appending after i forms a longer string
                        lengths[j] = lengths[i] + 1
                        counts[j] = counts[i]
                    elif lengths[i] + 1 == lengths[j]:
                        #NOTE: lengths[j] has been already generated, so it means there're other
                        # increasing substring with the same length
                        counts[j] += counts[i]

        longest = max(lengths)
        return sum(c for i, c in enumerate(counts) if lengths[i] == longest)

Solution().findNumberOfLIS([1,3,5,4,7])