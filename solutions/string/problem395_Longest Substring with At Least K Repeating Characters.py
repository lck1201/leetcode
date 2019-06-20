class Solution:
    # If every character appears at least k times, the whole string is ok. Otherwise split by a less
    # frequent character (because it will always be too infrequent and thus can't be part of any ok substring)
    # and make the most out of the splits.
    def longestSubstring2(self, s: str, k: int) -> int:
        '''
        python style code, not algorithm-oriented(hard-coded)
        '''
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)

    # same idea
    def longestSubstring(self, s: str, k: int) -> int:
        return self.helper(s, 0, len(s), k)

    def helper(self, s, beg, end, k):
        if end - beg < k:
            return 0

        cnt = [0] * 26
        for i in range(beg, end):
            cnt[ord(s[i]) - ord('a')] += 1

        for i in range(beg, end):
            if 0 < cnt[ord(s[i]) - ord('a')] < k: #split at s[i]
                l = self.helper(s, beg, i, k)
                r = self.helper(s, i + 1, end, k)
                return max(l, r)
        return end - beg
