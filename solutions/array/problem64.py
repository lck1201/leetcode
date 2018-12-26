# TAG: dp, dfs, back_tracking

# dfs exceed time limit, if large grid, consumes infinite time
import sys
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.minPath = sys.maxsize
        self.nRows = len(grid)
        self.nCols = len(grid[0])

        self.dfs(grid, 0, 0, 0)
        return self.minPath

    def dfs(self, grid, passPath, row, col):
        if row >= self.nRows:
            return
        if col >= self.nCols:
            return

        passPath += grid[row][col]
        if col == self.nCols - 1 and row == self.nRows - 1:
            self.minPath = min(self.minPath, passPath)
        else:
            self.dfs(grid, passPath, row + 1, col)
            self.dfs(grid, passPath, row, col + 1)

# DP
class Solution_dp:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        #init
        for r in range(1, m):
            grid[r][0] += grid[r-1][0]

        for c in range(1, n):
            grid[0][c] += grid[0][c-1]

        for r in range(1,m):
            for c in range(1,n):
                grid[r][c] += min(grid[r-1][c], grid[r][c-1])

        return grid[-1][-1]

