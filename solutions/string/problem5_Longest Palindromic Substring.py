# review
class Solution:
    # method1: re-construction, concise and understandable
    def longestPalindrome(self, s):
        ans = ''

        def helper(s, left, right):
            while left >= 0 and right < len(s) and s[left]==s[right]:
                left -= 1
                right += 1

            return s[left+1:right] #[left+1, right-1]

        for ci in range(len(s)):
            temp = helper(s, ci, ci) #extend odd length, 'aba'
            if len(temp) > len(ans):
                ans = temp

            temp = helper(s, ci, ci+1) #extend even length,'abba'
            if len(temp) > len(ans):
                ans = temp

        return ans

s = Solution()
print(s.longestPalindrome("abba"))