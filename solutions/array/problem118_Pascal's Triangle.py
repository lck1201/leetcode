class Solution:
    def generate(self, numRows: int) -> 'List[List[int]]':
        if numRows == 0:
            return list()
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]

        ans = [[1],[1,1]]
        for r in range(2, numRows):
            temp = [1] * (r+1)
            for c in range(1, r):
                # print('r',r,'c',c)
                temp[c] = ans[r-1][c] + ans[r-1][c-1]

            ans.append(temp)

        # print(ans)
        return ans

Solution().generate(5)