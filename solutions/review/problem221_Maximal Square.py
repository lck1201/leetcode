class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        result = 0
        rows = len(matrix)
        cols = len(matrix[0])
        dp_table = [[0 for _ in range(cols)] for _ in range(rows)]
        for nRow in range(rows):
            for nCol in range(cols):
                if matrix[nRow][nCol] == '1':
                    if nRow >= 1 and nCol >= 1:
                        dp_table[nRow][nCol] = min([dp_table[nRow-1][nCol], dp_table[nRow][nCol-1], dp_table[nRow-1][nCol-1]]) + 1
                    else:
                        dp_table[nRow][nCol] = 1

                    result = max(result, dp_table[nRow][nCol])

        return result**2