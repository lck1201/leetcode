class Solution:
    # method1: expand around center
    def longestPalindrome(self, s):
        def expandAroundCenter(s, left, right, palindrome_word_length, current_pa):
            for side_idx in range(1, palindrome_word_length + 1):
                if s[left - side_idx] == s[right + side_idx]:
                    current_pa = s[left - side_idx] + current_pa + s[right + side_idx]
                else:
                    break

            return current_pa

        longest_pa = ''

        if len(s) == 0:
            return s

        string_len = len(s)
        for center_idx in range(string_len):
            pa1 = ''
            if center_idx+1 < string_len and s[center_idx]==s[center_idx+1]:
                palindrome_word_length = min(center_idx, string_len-center_idx-2)
                current_pa = s[center_idx] + s[center_idx+1]
                pa1 = expandAroundCenter(s, center_idx, center_idx+1, palindrome_word_length, current_pa)

            palindrome_word_length = min(center_idx, string_len-center_idx-1)
            current_pa = s[center_idx]
            pa2 = expandAroundCenter(s, center_idx, center_idx, palindrome_word_length, current_pa)

            candi = pa2 if len(pa2) > len(pa1) else pa1
            longest_pa = candi if len(candi)>len(longest_pa) else longest_pa

        return longest_pa

    # method2: sliding window, brute force

    # method3: DP
    # def longestPalindrome(self, s):
    #     import numpy as np
    #     string_len = len(s)
    #     dp_table = np.zeros((string_len, string_len))
    #     for i in range(string_len):
    #         dp_table[i, i] = 1
    #         if i+1 < string_len and s[i] == s[i+1]:
    #             dp_table[i, i+1] = 1


s = Solution()
print(s.longestPalindrome(""))