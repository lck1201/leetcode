class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in sorted(nums):
            toadd = [item + [num] for item in res]
            res += toadd
        return res


# example
# DFS recursively, brute force
def subsets1(nums):
    res = []
    dfs(sorted(nums), 0, [], res)
    return res

def dfs(nums, index, path, res):
    print(path)
    res.append(path)
    for i in range(index, len(nums)):
        dfs(nums, i + 1, path + [nums[i]], res)


# Bit Manipulation
def subsets2(nums):
    res = []
    nums.sort()
    for i in range(1 << len(nums)):
        tmp = []
        for j in range(len(nums)):
            if i & 1 << j:  # if i >> j & 1:
                tmp.append(nums[j])
        res.append(tmp)
    return res


# Iteratively, best!!!!!!
def subsets(nums):
    res = [[]]
    for num in sorted(nums):
        toadd = [item + [num] for item in res]
        # print(res)
        # print(toadd)
        res += toadd
        # print(res)
    return res
