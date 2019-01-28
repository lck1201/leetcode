class Solution2:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ansStack = [['', 1]]
        num = ''

        for ch in s:
            if ch.isdigit():
                num += ch
            elif ch == '[':
                ansStack.append(['', int(num)])
                num = ''
            elif ch == ']':
                ss, k = ansStack.pop()
                ansStack[-1][0] += ss*k
            else:
                ansStack[-1][0] += ch

        return ansStack[0][0]

class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.s = s
        self.idx = 0
        return self.dfs()

    def dfs(self):
        ans = ''
        while self.idx < len(self.s) and self.s[self.idx] != ']':
            if self.s[self.idx].isalpha():
                ans += self.s[self.idx]
                self.idx += 1
                continue
            num = ''
            while self.s[self.idx].isdigit():
                num += self.s[self.idx]
                self.idx += 1
            self.idx += 1
            ret = self.dfs()
            self.idx += 1
            ans += ret * int(num)
        return ans

print(Solution().decodeString("3[a]2[bc]") == "aaabcbc")
print(Solution().decodeString("3[a2[c]]") == "accaccacc")
print(Solution().decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef")