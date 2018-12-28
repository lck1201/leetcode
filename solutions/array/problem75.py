class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # The idea is to sweep all 0s to the left and all 2s to the right,
        # then all 1s are left in the middle.
        two_p = len(nums)-1
        zero_p = 0
        idx = 0
        while idx <= two_p:
            if nums[idx] == 0:
                nums[idx], nums[zero_p] = nums[zero_p], nums[idx] #换过来的肯定不是 0
                zero_p += 1
            elif nums[idx] == 2:
                nums[idx], nums[two_p] = nums[two_p], nums[idx] #换过来的可能是 2
                two_p -= 1
                idx -= 1 # stay
            idx += 1

# brilliant
# example, to find section that [0,i) [i, j) [j, k) are 0s, 1s and 2s
def sortColors(nums):
    i = j = 0
    for k in range(len(nums)):
        v = nums[k]
        nums[k] = 2
        if v < 2:
            nums[j] = 1
            j += 1
        if v == 0:
            nums[i] = 0
            i += 1
    return nums
