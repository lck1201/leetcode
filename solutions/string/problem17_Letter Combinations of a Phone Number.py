class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return list()

        phone = {'2':['a','b','c'],
                   '3':['d','e','f'],
                   '4':['g','h','i'],
                   '5':['j','k','l'],
                   '6':['m','n','o'],
                   '7':['p','q','r','s'],
                   '8':['t','u','v'],
                   '9':['w','x','y','z']}

        result = []
        def dfs(path, idx):
            if idx == len(digits):
                result.append(path)
                return

            for char in phone[digits[idx]]:
                dfs(path + char, idx+1)

        dfs('', 0)
        return result