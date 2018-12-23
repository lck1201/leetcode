class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minBuyin = 1000000000
        maxProfit = 0
        for p in prices:
            minBuyin = min(p, minBuyin)
            maxProfit = max(p-minBuyin, maxProfit)

        return maxProfit


sol = Solution()
re = sol.maxProfit([3,7,1,2])
print(re)