# review
# CORE: to keep tracking og start pointer of sub-string

# https://leetcode.com/problems/minimum-window-substring/discuss/26808/
# Here-is-a-10-line-template-that-can-solve-most-'substring'-problems

# hash table
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        HashMap = dict()
        start = -1
        for idx in range(len(s)):
            if s[idx] in HashMap:
                start = max(start, HashMap[s[idx]])
            HashMap[s[idx]] = idx
            ans = max(ans, idx - start)

        return ans

print(Solution().lengthOfLongestSubstring('abba'))

# excellent solution
def lengthOfLongestSubstring(s):
    table = [-1] * 256 # -1 is unvisited
    start = -1
    ans = 0
    for idx in range(len(s)):
        if table[ord(s[idx])] > start:
            start = table[ord(s[idx])]
        table[ord(s[idx])] = idx
        ans = max(ans, idx - start)
    return ans