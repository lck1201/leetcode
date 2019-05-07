# math, prime factorization
class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        dp = [0] * (n + 1)

        for i in range(1, n+1):
            dp[i] = i
            for j in range(i-1, 1, -1):
                if i%j==0: #NOTE: j是i的一个因子，正常来说，这题要找质数因子。但是这里是bottom-up的dp，因此已经包含在过程中了，在找到一个之后就break
                    dp[i] = min(dp[j] + (i//j), dp[i])
                    break

        return dp[n]


# find prime factorization
class Solution2():
    def minSteps(self, n):
        ans = 0
        d = 2
        while n > 1:
            while n % d == 0:
                ans += d
                n /= d
            d += 1
        return ans