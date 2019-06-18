class Solution:
    def increasingTriplet(self, nums: 'List[int]') -> bool:
        '''
        My solution, understandable, interpretable, but less concise
        :param nums:
        :return:
        '''
        if len(nums) < 3:
            return False

        ids = [0, -1, -1]
        visit = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[ids[0]]:
                ids[0] = i
                if ids[1] == -1:
                    ids[1:] = [-1, -1]
                else:
                    if max(nums[i:])>nums[ids[1]]:
                        return True
                visit = 0
                continue

            if visit == 0 and nums[i] > nums[i-1]:
                visit += 1
                ids[visit] = i
                continue

            if visit != 0 and nums[i] < nums[ids[visit]] and nums[i]>nums[ids[visit-1]]:
                ids[visit] = i
                continue

            if visit != 0 and nums[i] > nums[ids[visit]]:
                visit += 1
                ids[visit] = i
                if visit == 2:
                    return True
                continue

        # print(ids)
        return ids[-1] != -1

    def increasingTriplet2(self, nums):
        '''
        Solution from leetcode, concise and work, but logic not strict.
        Algorithm: Find first smallest, then find second smallest, then find the third and bingo.
        [1,2,0,3]这种case，c1/c2最后会是0/2，从算法逻辑上是错的。但实际上，到2这个数字时，已经经历过1了，c2已经生效了。
        换句话说：
        C1 = so far best candidate of end element of a one-cell subsequence to form a triplet subsequence
        C2 = so far best candidate of end element of a two-cell subsequence to form a triplet subsequence
        但是：
        If the problem requires us to return the index, then this code would not work.
        '''
        c1 = c2 = float('inf')
        for n in nums:
            if n <= c1:
                c1 = n
            elif n <= c2:
                c2 = n
            else:
                return True
        return False

inp = [5,4,1,2,-1,3,3]
re = Solution().increasingTriplet(inp)
print(re)