class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        Which interval would be the best first (leftmost) interval to keep? One that ends first,
        as it leaves the most room for the rest. So take one with smallest end, remove all the bad ones
        overlapping it, and repeat (taking the one with smallest end of the remaining ones).
        For the overlap test, just keep track of the current end, initialized with negative infinity.
        '''
        end = float('-inf')
        ans = 0
        for i in sorted(intervals, key=lambda i: i[1]):
            if i[0] >= end:
                end = i[1]
            else:
                ans += 1

        return ans

# a = [[1,2],[2,3],[3,4],[1,3]]
# for i in sorted(a, key=lambda i: i[1]):
#     print(i)