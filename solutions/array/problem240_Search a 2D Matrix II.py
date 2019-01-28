class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if (not matrix) or len(matrix) < 1 or len(matrix[0]) < 1:
            return False

        row = 0
        col = len(matrix[0]) - 1
        while col>=0 and row <= len(matrix) - 1:
            print(row, col)
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                col -= 1
            elif target > matrix[row][col]:
                row += 1

        return False

print(Solution().searchMatrix([[1,1]],2))