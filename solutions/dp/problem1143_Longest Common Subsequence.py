class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dpTable = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dpTable[i][j] = dpTable[i - 1][j - 1] + 1
                else:
                    dpTable[i][j] = max(dpTable[i - 1][j], dpTable[i][j - 1])

        return dpTable[-1][-1]