class Solution:
    def calculate(self, s: str) -> int:
        stack = list()
        num = 0
        sign = '+'
        for i in range(len(s)):
            if s[i].isnumeric():
                num = num * 10 + int(s[i])
            if not s[i].isnumeric() and s[i] != ' ' or i == len(s) - 1:
                if sign == '-':
                    stack.append(-num)
                if sign == '+':
                    stack.append(num)
                if sign == '*':
                    stack.append(stack.pop(-1) * num)
                if sign == '/':
                    stack.append(int(stack.pop(-1) / num))

                sign = s[i]
                num = 0
        ans = 0
        for item in stack:
            ans += item

        # print(stack)
        # print(ans)
        return ans


cmd = "14-3/2"
Solution().calculate(cmd)
