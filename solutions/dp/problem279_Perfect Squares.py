from math import sqrt


# Recursively
class Solution2:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp_table = [0] * (n + 1)
        insider_sqer_num = []
        for x in range(1, int(sqrt(n)) + 1):
            insider_sqer_num.append(x * x)

        reversed(insider_sqer_num)

        def dfs(target):
            if target == 0:
                return 0

            if dp_table[target] != 0:
                return dp_table[target]

            minX = target
            for x in insider_sqer_num:
                if x == target:
                    minX = 1
                    break
                elif x < target:
                    minX = min(minX, dfs(target - x) + 1)
                else:
                    pass

            dp_table[target] = minX

            return minX

        dfs(n)
        return dp_table[n]

# iterative, bottom-up
import sys
from math import sqrt
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0

        dp_table = [sys.maxsize] * (n + 1)
        dp_table[0] = 0
        for i in range(1, n+1):
            for j in range(1, int(sqrt(i)) + 1):
                dp_table[i] = min(dp_table[i], dp_table[i - j * j] + 1)

        return dp_table[n]
