class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = list()
        left = ['(','[','{']
        for x in s:
            if x in left:
                stack.append(x)
            else:
                if not stack:
                    return False
                elif x == ")":
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
                elif x == "]":
                    if stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
                elif x == "}":
                    if stack[-1] == "{":
                        stack.pop()
                    else:
                        return False

        return len(stack)==0

print(Solution().isValid("]"))