class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        nRows = len(matrix)
        nCols = len(matrix[0])

        i = 0
        j = nCols - 1
        while i < nRows and j >= 0:
            if target < matrix[i][j]:
                j -= 1
            elif target > matrix[i][j]:
                i += 1
            else:
                return True

        return False
