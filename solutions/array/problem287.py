class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(N) space&time solution
        # numDict={}
        # for n in nums:
        #     if n not in numDict:
        #         numDict[n] = 1
        #     else:
        #         numDict[n] += 1
        #
        # for k in numDict:
        #     if numDict[k] > 1:
        #         return k

        # O(NlogN) time & O(1) space
        low = 1
        high = len(nums) - 1

        while low < high:
            count = 0
            mid = (low+high)//2

            for n in nums:
                if n <= mid:
                    count += 1

            if count <= mid:
                low = mid + 1
            else:
                high = mid

        return low

# fast&slow pointer solution, O(N) time, O(1) space
# brilliant solution
def findDuplicate(nums):
    slow = nums[0]
    fast = nums[nums[0]]
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]

    fast = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow
