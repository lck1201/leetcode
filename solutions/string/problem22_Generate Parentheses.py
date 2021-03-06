class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        def back_tracking(path, left, right):
            nonlocal n
            if len(path) == 2 * n:
                ans.append(path)
                return
            if left < n: #MUST add left first
                back_tracking(path + '(', left + 1, right)
            if right < left: # if right==left, we cannot add right. So right must < left
                back_tracking(path + ')', left, right + 1)

        back_tracking('', 0, 0)
        return ans

print(Solution().generateParenthesis(3))