class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = list()

        end_idx = len(nums) - 1
        for idx in range(len(nums)):
            if nums[idx] > target:
                end_idx = idx - 1
                break

        for idx1 in range(end_idx+1):
            for idx2 in range(end_idx+1):
                if idx1 == idx2:
                    continue

                if nums[idx1] + nums[idx2] == target:
                    return [idx1, idx2]

#example
class Solution_example(object):
    def twoSum(self, nums, target):

        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i
