class Solution:
    def climbStairs2(self, n: 'int') -> 'int':
        '''
        dp table
        '''
        if n <= 1:
            return 1

        table = [0] * (n + 1)
        table[0] = 1
        table[1] = 1

        for stair in range(2, n + 1):
            table[stair] = table[stair - 1] + table[stair - 2]

        return table[n]

    def climbStairs(self, n: 'int') -> 'int':
        '''
        dfs
        '''
        if n <= 1:
            return 1

        return self.climbStairs(n-1) + self.climbStairs(n-2)
