class Solution:
    def moreThanHalfNum(self, nums):
        if not nums:
            return 0

        result = nums[0]
        times = 1
        for i in range(1, len(nums)):
            if times == 0:
                result = nums[i]
                times = 1
            elif nums[i] == result:
                times += 1
            else:
                times -= 1

        if not self.checkMoreThanHalf(result, nums):
            # what if no digit appears more than half
            result = 0

        return result
