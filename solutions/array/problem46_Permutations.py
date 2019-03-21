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
        nums = set(nums)
        def dfs(path, nums):
            if len(nums) == 0:
                ans.append(path)

            for x in nums:
                dfs(path + [x], nums - {x})

        dfs([], nums)

        return ans

# 所有组合
def func(nums):
    ans = [[]]
    for x in nums:
        ans += [char + [x] for char in ans]

    return ans

print(func([1,2,3]))