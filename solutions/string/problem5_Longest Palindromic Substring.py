class Solution:
    # method1: re-construction, concise and understandable
    def longestPalindrome(self, s):
        ans = ''

        def helper(s, left, right):
            while left >= 0 and right < len(s) and s[left]==s[right]:
                left -= 1
                right += 1

            return s[left+1:right] #[left+1, right)

        for ci in range(len(s)):
            temp = helper(s, ci, ci) #extend odd length, 'aba'
            if len(temp) > len(ans):
                ans = temp

            temp = helper(s, ci, ci+1) #extend even length,'abba'
            if len(temp) > len(ans):
                ans = temp

        return ans


    # method1: expand around center, written by myself, ugly
    # def longestPalindrome(self, s):
    #     def expandAroundCenter(s, left, right, palindrome_word_length, current_pa):
    #         for side_idx in range(1, palindrome_word_length + 1):
    #             if s[left - side_idx] == s[right + side_idx]:
    #                 current_pa = s[left - side_idx] + current_pa + s[right + side_idx]
    #             else:
    #                 break
    #
    #         return current_pa
    #
    #     longest_pa = ''
    #
    #     if len(s) == 0:
    #         return s
    #
    #     string_len = len(s)
    #     for center_idx in range(string_len):
    #         pa1 = ''
    #         if center_idx+1 < string_len and s[center_idx]==s[center_idx+1]:
    #             palindrome_word_length = min(center_idx, string_len-center_idx-2)
    #             current_pa = s[center_idx] + s[center_idx+1]
    #             pa1 = expandAroundCenter(s, center_idx, center_idx+1, palindrome_word_length, current_pa)
    #
    #         palindrome_word_length = min(center_idx, string_len-center_idx-1)
    #         current_pa = s[center_idx]
    #         pa2 = expandAroundCenter(s, center_idx, center_idx, palindrome_word_length, current_pa)
    #
    #         candi = pa2 if len(pa2) > len(pa1) else pa1
    #         longest_pa = candi if len(candi)>len(longest_pa) else longest_pa
    #
    #     return longest_pa

    # method2: sliding window, brute force


s = Solution()
print(s.longestPalindrome("abba"))