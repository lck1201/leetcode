# 全排列
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []

        # NOTE: use visit to control visibility, more general if same digit/char appear twice or more
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

        # NOTE: use set to control visibility
        def dfs(path, nums):
            if len(nums) == 0:
                ans.append(path)

            for x in nums:
                dfs(path + [x], nums - {x})

        #NOTE: better method, because there may be duplicates in nums,
        # so using set is not completely correct
        def dfs2(nums, path):
            if not nums:
                ans.append(path)
                # return # backtracking
            for i in range(len(nums)):
                dfs2(nums[:i] + nums[i + 1:], path + [nums[i]])

        dfs2(nums, [])

        return ans


# All Combination
def func(nums):
    ans = [[]]
    for x in nums:
        ans += [char + [x] for char in ans]

    return ans


print(Solution().permute([1, 2, 3]))
