class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        def extendPalindrome(s, left, right):
            global count
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1

        if not s:
            return 0

        global count
        count = 0

        for ci in range(len(s)):
            extendPalindrome(s, ci, ci)
            extendPalindrome(s, ci, ci+1)

        return count
