def bi_search(nums, target, start, end):
    if start == end:
        return start

    mid = (start + end)//2
    if target > nums[mid]:
        start = mid + 1
        return bi_search(nums, target, start, end)
    else:
        end = mid
        return bi_search(nums, target, start, end)

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]

        start = 0
        end = len(nums)

        left = bi_search(nums, target, start, end)
        if target in nums[left:left+1]:
            return [left, bi_search(nums, target+1, start, end) - 1]
        else:
            return [-1, -1]


# example
#  Otherwise, I ask search(target+1), which tells me the first index where I could insert target+1,
#  which of course is one index behind the last index containing target, so all I have left to do is subtract 1.
def searchRange(nums, target):
    def search(n):
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] >= n:
                hi = mid
            else:
                lo = mid + 1
        return lo
    lo = search(target)
    return [lo, search(target+1)-1] if target in nums[lo:lo+1] else [-1, -1]


# example. non-recursive
class Solution_eg:
    # returns leftmost (or rightmost) index at which `target` should be inserted in sorted
    # array `nums` via binary search.
    def extreme_insertion_index(self, nums, target, left):
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target or (left and target == nums[mid]): #second half of this line is quite complicated, not recommend
                hi = mid
            else:
                lo = mid+1

        return lo


    def searchRange(self, nums, target):
        left_idx = self.extreme_insertion_index(nums, target, True)

        # assert that `left_idx` is within the array bounds and that `target`
        # is actually in `nums`.
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, self.extreme_insertion_index(nums, target, False)-1]