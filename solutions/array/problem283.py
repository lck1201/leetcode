class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        cnt = 0
        for digit in nums:
            if digit==0:
                cnt += 1
        for _ in range(cnt):
            nums.remove(0)
            nums.append(0)

#  3-lines solution, fully utilize python feature & build-in function
# count=nums.count(0)
# nums[:]=[i for i in nums if i != 0]
# nums+=[0]*count


# jave O(N) solution
# public void moveZeroes(int[] nums) {
#     if (nums == null || nums.length == 0) return;
#
#     int insertPos = 0;
#     for (int num: nums) {
#         if (num != 0) nums[insertPos++] = num;
#     }
#
#     while (insertPos < nums.length) {
#         nums[insertPos++] = 0;
#     }
# }