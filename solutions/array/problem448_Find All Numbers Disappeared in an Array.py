class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = list()
        for idx in range(1, len(nums)+1):
            if nums.count(idx)==0:
                result.append(idx)
        return result

# slow but python-featured code
# def findDisappearedNumbers(self, nums):
#     allNums = [i for i in range(1, len(nums)+1)]
#     return list(set(allNums) - set(nums))

# good python solution
# def findDisappearedNumbers(self, nums):
#     for i in range(len(nums)):
#         index = abs(nums[i]) - 1
#         nums[index] = - abs(nums[index])
#
#     return [i + 1 for i in range(len(nums)) if nums[i] > 0]
