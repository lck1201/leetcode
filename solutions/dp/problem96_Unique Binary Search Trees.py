class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.dp = [0] * (n + 1)
        self.dp[0] = 1

        return self.dfs(n)

    def dfs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1

        if self.dp[n] != 0:
            return self.dp[n]

        ans = 0
        for ln in range(0, n):
            ans += self.dfs(ln) * self.dfs(n - ln - 1)

        self.dp[n] = ans
        return ans


class Solution2:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[0] = 1

        for x in range(1, n + 1):
            for k in range(0, x):
                dp[x] += (dp[x-k-1] * dp[k])

        return dp[n]
