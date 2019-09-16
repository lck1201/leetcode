# class Solution:
#     def findTargetSumWays(self, nums, S):
#         """
#         :type nums: List[int]
#         :type S: int
#         :rtype: int
#         """
#         def subsetSum(nums, target):
#             dp = [0] * (target+1)
#             dp[0] = 1
#             for n in nums:
#                 for i in range(target, n-1,-1):
#                     dp[i] += dp[i-n]
#
#             return dp[target]
#
#
#         ns = sum(nums)
#         return 0 if ns<S or (S + ns)%2>0 else subsetSum(nums, (S+ns)//2)


class Solution2(object):
    def findTargetSumWays(self, nums, S):
        if not nums:
            return 0
        dic = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0: 2}
        for i in range(1, len(nums)):
            tdic = {}
            for d in dic:
                tdic[d + nums[i]] = tdic.get(d + nums[i], 0) + dic.get(d, 0)
                tdic[d - nums[i]] = tdic.get(d - nums[i], 0) + dic.get(d, 0)
            dic = tdic
        return dic.get(S, 0)