import copy
class Solution:
    def spiralOrder(self, matrix: 'List[List[int]]') -> 'List[int]':
        '''
        Excellent Solution https://leetcode.com/problems/spiral-matrix/discuss/20571/1-liner-in-Python-%2B-Ruby
        '''
        return matrix and list(matrix.pop(0)) + self.spiralOrder(list(zip(*matrix))[::-1]) #python2 style
        # return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1]) #python3 style

    def spiralOrder2(self, matrix: 'List[List[int]]') -> 'List[int]':
        '''
        Ordinary solution
        '''
        if not matrix or not matrix[0]:
            return list()
        ans = copy.deepcopy(matrix[0])
        m = len(matrix)
        n = len(matrix[0])
        dir = [[1, 0], [0, -1], [-1, 0], [0, 1]] #move direction
        d = 0
        pos = [0, n-1] #start location
        remain = (m-1) * n
        while remain>0:
            for i in range(1, m):
                pos[0] += dir[d][0]
                pos[1] += dir[d][1]
                ans.append(matrix[pos[0]][pos[1]])
                remain -= 1
            m -= 1
            m,n = n, m
            d = (d+1)%4
        return ans

inp = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Solution().spiralOrder2(inp)