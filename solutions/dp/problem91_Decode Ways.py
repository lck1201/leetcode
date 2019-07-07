class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        62
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0

        for i in range(1, len(s)):
            onePhase = int(s[i:i + 1]) #start loop from s[1], correspond to dp[2]
            twoPhase = int(s[i - 1:i + 1])
            if onePhase >= 1 and onePhase <= 9:
                dp[i + 1] += dp[i]
            if twoPhase >= 10 and twoPhase <= 26:
                dp[i + 1] += dp[i - 1]

        return dp[len(s)]
