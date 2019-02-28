class Solution:
    def dfs_fill(self, i, j):
        if i >= 0 and j >= 0 and i < len(self.map) and j < len(self.map[0]):
            if self.map[i][j] == '1':
                self.map[i][j] = '0'
                self.dfs_fill(i, j + 1)
                self.dfs_fill(i, j - 1)
                self.dfs_fill(i + 1, j)
                self.dfs_fill(i - 1, j)

    def numIslands(self, grid: 'List[List[str]]') -> 'int':
        if not grid or not grid[0]:
            return 0
        self.map = grid
        self.ans = 0

        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                if self.map[i][j] == '1':
                    self.ans += 1
                    self.dfs_fill(i, j)

        return self.ans


