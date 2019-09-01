class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        ans = 0
        if not M or not M[0]:
            return ans

        visited = [0]*len(M)

        def dfs(M, i):
            nonlocal visited
            for j in range(len(M)):
                if M[i][j] == 1 and visited[j] == 0:
                    visited[j] = 1
                    dfs(M, j)

        for i in range(len(M)):
            if not visited[i]:
                dfs(M ,i)
                ans += 1

        return ans