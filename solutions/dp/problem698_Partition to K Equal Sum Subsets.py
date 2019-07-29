class Solution:
    def canPartitionKSubsets(self, nums: 'List[int]', k: int) -> 'bool':
        sNums = sum(nums)
        if sNums % k != 0 or k <= 0:
            return False

        visited = [False] * len(nums)

        def canPartition(start, nums, visited, k, sm, target):
            if k == 1:
                return True
            if sm == target:  # next DFS
                return canPartition(0, nums, visited, k - 1, 0, target)

            for i in range(start, len(nums)):
                if not visited[i]:
                    visited[i] = True
                    if canPartition(i + 1, nums, visited, k, sm + nums[i], target):
                        return True
                    visited[i] = False

            return False

        return k >= 0 and sNums % k == 0 and canPartition(0, nums, visited, k, 0, sNums // k)
