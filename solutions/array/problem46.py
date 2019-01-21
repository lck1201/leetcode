class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []

        # use visit to control visibility
        # visit = [0] * len(nums)
        # def dfs(path, visit):
        #     if len(path) == len(nums):
        #         ans.append(path)
        #
        #     for idx in range(len(visit)):
        #         if not visit[idx]:
        #             visit[idx] = 1
        #             dfs(path + [nums[idx]], visit)
        #             visit[idx] = 0
        # dfs([], visit)

        # use set to control visibility
        nums = set(nums)
        def dfs(path, nums):
            if len(nums) == 0:
                ans.append(path)

            for x in nums:
                dfs(path + [x], nums-{x})

        dfs([], nums)


        return ans
