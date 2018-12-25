class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # method1, transpose, flip horizontallly
        # n = len(matrix[0])
        # for i in range(n):
        #     for j in range(i, n):
        #         temp = matrix[i][j]
        #         matrix[i][j] = matrix[j][i]
        #         matrix[j][i] = temp
        # for row in range(n):
        #     matrix[row] = matrix[row][::-1]


        # method2, flip vertically, tranpose
        # zip(list instance) is a transpose operation
        # matrix[:] = zip(*matrix[::-1])


        # method3, ordinary swap 4 elements
        # divide and conquer, each operation only consider rotate 4 elements
        n = len(matrix[0])
        a = 0
        b = n-1
        while a < b:
            for i in range(0, b-a):
                matrix[a][a+i], matrix[a+i][b] = matrix[a+i][b], matrix[a][a+i]
                matrix[a][a+i], matrix[b][b-i] = matrix[b][b-i], matrix[a][a+i]
                matrix[a][a+i], matrix[b-i][a] = matrix[b-i][a], matrix[a][a+i]
            # from out-loop into inner-loop
            a += 1
            b -= 1

# ma = [[1,2,3],
#   [4,5,6],
#   [7,8,9]]
#
# s = Solution()
# s.rotate(ma)
# print(ma)

