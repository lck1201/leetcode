# DFS with dp

# Do DFS from every cell
# Compare every 4 direction and skip cells that are out of boundary or smaller
# Get matrix max from every cell's max
# Use matrix[x][y] <= matrix[i][j] so we don't need a visited[m][n] array
# The key is to cache the distance because it's highly possible to revisit a cell

class Solution:
    def longestIncreasingPath(self, matrix: 'List[List[int]]') -> 'int':
        if not matrix or not matrix[0]:
            return 0

        nRows = len(matrix)
        nCols = len(matrix[0])
        dp = [[0] * nCols for _ in range(nRows)]

        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(
                    dfs(i - 1, j) if i >= 1 and val > matrix[i - 1][j] else 0,
                    dfs(i + 1, j) if i + 1 < nRows and val > matrix[i + 1][j] else 0,
                    dfs(i, j - 1) if j >= 1 and val > matrix[i][j - 1] else 0,
                    dfs(i, j + 1) if j + 1 < nCols and val > matrix[i][j + 1] else 0)
            return dp[i][j]

        return max([dfs(i, j) for i in range(nRows) for j in range(nCols)])

inp = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]

re = Solution().longestIncreasingPath(inp)
print(re)