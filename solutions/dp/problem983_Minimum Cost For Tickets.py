class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        lastDay = days[-1]
        dp = [0] * (lastDay + 1)

        for i in range(1, len(dp)):
            if i in days:
                if i >= 1 and i <= 7:
                    oneDayTicket = dp[i - 1] + costs[0]
                    sevenDayTicket = dp[0] + costs[1]
                    dp[i] = min(oneDayTicket, sevenDayTicket)
                elif i > 7 and i <= 30:
                    oneDayTicket = dp[i - 1] + costs[0]
                    sevenDayTicket = dp[i - 7] + costs[1]
                    thirtyDayTicket = dp[0] + costs[2]
                    dp[i] = min([oneDayTicket, sevenDayTicket, thirtyDayTicket])
                else: # i > 30
                    oneDayTicket = dp[i - 1] + costs[0]
                    sevenDayTicket = dp[i - 7] + costs[1]
                    thirtyDayTicket = dp[i - 30] + costs[2]
                    dp[i] = min([oneDayTicket, sevenDayTicket, thirtyDayTicket])
            else:
                dp[i] = dp[i - 1]

        return dp[lastDay]

