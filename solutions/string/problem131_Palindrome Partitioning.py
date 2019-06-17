class Solution:
    def partition(self, s: str) -> 'List[List[str]]':
        self.ans = []
        self.dfs(s, 0, [])
        return self.ans

    def dfs(self, s, pos, path):
        if pos == len(s):
            self.ans.append(path)
        else:
            for i in range(pos, len(s)):
                if self.isPal(s, pos, i):
                    self.dfs(s, i + 1, path + [s[pos:i + 1]])

    def isPal(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

# inp = 'aab'
# re = Solution().partition(inp)
# print(re)
