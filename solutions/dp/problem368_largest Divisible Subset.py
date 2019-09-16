class Solution:
    def largestDivisibleSubset(self, nums: 'List[int]') -> 'List[int]':
        if not nums or len(nums) == 1:
            return nums

        n = len(nums)
        cnt = [1] * n  # count set size
        pre = [-1] * n  # track path
        nums.sort()
        mx, index = 0, -1
        for i in range(1, n):  # from 0 -> right
            for j in range(i - 1, -1, -1):  # from i -> 0
                if nums[i] % nums[j] == 0:
                    if cnt[j] + 1 > cnt[i]:
                        cnt[i] = cnt[j] + 1
                        pre[i] = j

            if cnt[i] > mx:
                mx = cnt[i]
                index = i

        ans = list()
        while index != -1:
            ans.append(nums[index])
            index = pre[index]

        return ans


print(sum(list(range(6, 16))))
