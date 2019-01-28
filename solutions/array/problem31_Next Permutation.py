class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        i1 = len(nums) - 1
        while i1 >= 1:
            if nums[i1 - 1] < nums[i1]:
                break
            i1 -= 1

        print(i1)
        i2 = len(nums) - 1
        if i1 != 0:
            while i2 >= i1:
                if nums[i1-1] < nums[i2]:
                    nums[i1-1], nums[i2] = nums[i2], nums[i1-1]
                    break
                i2 -= 1

        nums[i1::] = list(reversed(nums[i1:]))

s = Solution()
s.nextPermutation([1,2,3,9,8,6])

# 在当前序列中，从尾端往前寻找两个相邻元素，前一个记为first，后一个记为second，
# 并且满足first 小于 second。然后再从尾端寻找另一个元素number，如果满足first 小于number，
# 即将第first个元素与number元素对调，并将second元素之后（包括second）的所有元素颠倒排序，即求出下一个序列

# example:
# 6，3，4，9，8，7，1
# 此时 first ＝ 4，second = 9
# 从尾巴到前找到第一个大于first的数字，就是7
# 交换4和7，即上面的swap函数，此时序列变成6，3，7，9，8，4，1
# 再将second＝9以及以后的序列重新排序，让其从小到大排序，使得整体最小，即reverse一下（因为此时肯定是递减序列）
# 得到最终的结果：6，3，7，1，4，8，9
