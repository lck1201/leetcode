from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        if not nums or k <= 1:
            return nums

        length = len(nums)
        maxQueue = deque()
        ans = [0] * (length - k + 1)
        ri = 0
        for i in range(length):
            # remove numbers out of range k
            while len(maxQueue) and maxQueue[0] <= i-k:
                maxQueue.popleft()

            # remove smaller numbers in k range as they are useless
            while len(maxQueue) and nums[maxQueue[-1]] < nums[i]:
                maxQueue.pop()

            # maxQueue contains index; ans contains content;
            maxQueue.append(i)
            if i >= k-1:
                ans[ri] = nums[maxQueue[0]]
                ri += 1

        return ans
