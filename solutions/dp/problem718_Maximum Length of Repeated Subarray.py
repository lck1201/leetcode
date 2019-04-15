# Same idea of Longest Common Substring
class Solution:
    def findLength(self, A: 'List[int]', B: 'List[int]') -> 'int':
        dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]

        maxLen = 0
        for r in range(1, len(A) + 1):
            for c in range(1, len(B) + 1):
                # NOTE 若要求Continous substring, 那么这么做是对的
                if A[r - 1] == B[c - 1]:
                    dp[r][c] = dp[r - 1][c - 1] + 1
                # NOTE 若没要求Continous substring，则需要
                # else:
                #     dp[r][c] = max(dp[r-1][c], dp[r][c-1])


                maxLen = max(maxLen, dp[r][c])

        return maxLen

A = [1, 2, 3, 2, 1]
B = [3, 2, 1, 4, 7]
Solution().findLength(A, B)
