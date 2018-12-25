class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # method1, DP solution
        aux = [[1 for x in range(n)] for x in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                aux[i][j] = aux[i][j - 1] + aux[i - 1][j]
        return aux[-1][-1]

    # permutation
    # math C(m+n-2,n-1)
    def uniquePaths1(self, m, n):
        import math
        if not m or not n:
            return 0
        return math.factorial(m + n - 2) / (math.factorial(n - 1) * math.factorial(m - 1))