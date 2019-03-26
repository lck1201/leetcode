class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return

        nRows = len(matrix)
        nCols = len(matrix[0])

        for r in range(nRows):
            flag = False
            for c in range(nCols):
                if matrix[r][c] == 0:
                    flag = True
                    break

            if flag:
                for c in range(nCols):
                    if matrix[r][c] != 0:
                        matrix[r][c] = None

        for c in range(nCols):
            flag = False
            for r in range(nRows):
                if matrix[r][c] == 0:
                    flag = True
                    break

            if flag:
                for r in range(nRows):
                    if matrix[r][c] != 0:
                        matrix[r][c] = None

        for r in range(nRows):
            for c in range(nCols):
                if matrix[r][c] == None:
                    matrix[r][c] = 0
