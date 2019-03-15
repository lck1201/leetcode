class Solution:
    def wordBreak(self, s: str, wordDict: 'List[str]') -> 'bool':
        dp_table = [False]*(len(s)+1)
        dp_table[0] = True

        for i in range(1, len(s)+1):
            for word in wordDict:
                if len(word) <= i:
                    if dp_table[i-len(word)] and word == s[i-len(word):i]:
                        dp_table[i] = True

        return dp_table[len(s)]


wordDict = ["leet", "code"]
s = 'leetcode'

print(Solution().wordBreak(s, wordDict))