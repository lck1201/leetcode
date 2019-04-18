class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        minBuyin = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            maxProfit = max(prices[i] - minBuyin, maxProfit) #should sell first
            minBuyin = min(prices[i], minBuyin) # then update BuyIn Price

        return maxProfit