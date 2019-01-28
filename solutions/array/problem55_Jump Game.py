# 74/75 pass, time limit exceed
class Solution_dfs_dp:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.accessable = [-1] * len(nums)
        self.accessable[-1] = 1

        if len(nums) <= 1:
            return True
        target = len(nums) - 1

        return self.dfs(0, nums, target)

    def dfs(self, index, nums, target):
        if target <= 0:
            return True

        max_jump = nums[index]
        if max_jump == 0:
            return False

        if self.accessable[index] == 0:
            return False
        elif self.accessable[index] == 1:
            return True
        else:
            for jp in range(1, max_jump+1):
                if self.dfs(index + jp, nums, target - jp):
                    self.accessable[index] = 1
                    return True

            self.accessable[index] = 0
            return False


# intelligent!!!!
class Solution:
    def canJump(self, nums):
        maxReach = 0
        for i, n in enumerate(nums):
            if i > maxReach:
                return False
            maxReach = max(maxReach, i + n)

        return True
        # or  return maxReach >= len(nums)-1


# go back from rightmost
class Solution2:
    def canJump(self, nums):
        goal = len(nums) - 1
        for i in range(len(nums))[::-1]:
            if i + nums[i] >= goal:
                goal = i
        return not goal

