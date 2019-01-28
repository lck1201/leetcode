# Time limit exceed, but already O(N)
class Solution1:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        acc_num = 0
        accumulate_sum = []
        for idx in range(len(nums)):
            acc_num += nums[idx]
            accumulate_sum.append(acc_num)
            target = accumulate_sum[idx] - k
            if target == 0:
                result += 1
            result += accumulate_sum[0:idx].count(target) #maybe code of this line consumes much time

        return result

# use dict to store preSum and counts instead of list
# still slow, but pass all tests
class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        acc_num = 0
        dic = {0:1}
        for idx in range(len(nums)):
            acc_num += nums[idx]
            result += dic.get(acc_num - k, 0)
            dic[acc_num] = dic.get(acc_num,0) + 1

        return result



