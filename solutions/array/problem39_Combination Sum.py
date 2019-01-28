#Tag: back-tracking, dfs

class Solution:
    # in fact, this method visits all possibilities, nearly brute force
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], result)
        return result

    def dfs(self, nums, target, index, path, result):
        if target < 0:
            return

        if target == 0:
            result.append(path)

        for i in range(index, len(nums)):
            # param "index", different from problem78,which is "i+1"
            # I think because in this problem, number can be repeated.

            # besides, different from c++ version which maintain "path"
            # individually, and push_back & pop_back around self.dfs
            # Here in python version, path+[nums[i]] doesn't modify path in-place
            self.dfs(nums, target-nums[i], i, path+[nums[i]], result)
