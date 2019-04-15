class Solution:
    def minFallingPathSum(self, A: 'List[List[int]]') -> 'int':
        nRows = len(A)
        nCols = len(A[0])
        if not nRows or not nCols:
            return 0

        if nCols == 1:
            return sum([item[0] for item in A])

        A = [[0]*nCols] + A
        dp = [[0]*nCols for _ in range(nRows+1)]
        for r in range(1,nRows+1):
            for c in range(nCols):
                if c > 0 and c < nCols - 1:
                    dp[r][c] = min([dp[r-1][c-1], dp[r-1][c], dp[r-1][c+1]]) + A[r][c]
                elif c == 0:
                    dp[r][c] = min(dp[r-1][c], dp[r-1][c + 1]) + A[r][c]
                elif c == nCols - 1:
                    dp[r][c] = min(dp[r-1][c], dp[r-1][c - 1]) + A[r][c]

        return min(dp[-1])