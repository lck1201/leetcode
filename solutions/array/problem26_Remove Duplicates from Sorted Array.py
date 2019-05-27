class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1

        ptr1 = ptr2 = 0
        while ptr2 < len(nums):
            ptr1 = ptr2
            while ptr2<len(nums) and nums[ptr1] == nums[ptr2]:
                ptr2 += 1
            numDuplicate = ptr2 - ptr1 - 1
            for _ in range(numDuplicate):
                nums.pop(ptr1)

            ptr2 -= numDuplicate

        return len(nums)
