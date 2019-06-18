class Solution:
    def increasingTriplet(self, nums: 'List[int]') -> bool:
        if len(nums) < 3:
            return False

        ids = [0, -1, -1]
        visit = 0
        for i in range(1, len(nums)):
            print(i, visit)
            if nums[i] < nums[ids[0]]:
                ids[0] = i
                ids[1:] = [-1, -1]
                visit = 0
                continue

            if visit == 0 and nums[i] < nums[i-1]:
                ids[visit] = i
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

        print(ids)
        return ids[-1] != -1

inp = [5,4,1,2,-1,3,3]
# inp = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,3]
# print(inp[44],inp[48])
re = Solution().increasingTriplet(inp)
print(re)