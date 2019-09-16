class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3
        for x in range(4, n + 1):
            dp[x] = max([dp[x - i] * dp[i] for i in range(2, int(x / 2 + 0.5) + 1)])

        print(dp)
        return dp[n]


re = Solution().integerBreak(10)
print(re)
