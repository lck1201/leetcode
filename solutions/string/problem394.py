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
