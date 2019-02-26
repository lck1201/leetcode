class Solution:
    def findAnagrams(self, s: str, p: 'str') -> 'List[int]':
        # exception
        ans = []
        if not s or not p or len(p)>len(s):
            return ans

        hash = [0] * 256
        for c in p:
            hash[ord(c)] += 1

        begin = 0
        end = 0
        count = len(p)
        # chuankang's code
        while end < len(s):
            if hash[ord(s[end])] >= 1:
                count -= 1
            hash[ord(s[end])] -= 1
            end += 1

            if count == 0:
                ans.append(begin)

            if end - begin == len(p):
                if hash[ord(s[begin])] >= 0:
                    count += 1
                hash[ord(s[begin])] += 1
                begin += 1

        # jianting's code
        # while end<len(p):
        #     if hash[ord(s[end])] >= 1:
        #         count -= 1
        #
        #     hash[ord(s[end])] -= 1
        #     end += 1
        #
        # while end<len(s):
        #     if count == 0:
        #         ans.append(begin)
        #
        #     if hash[ord(s[begin])] >= 0:
        #         count += 1
        #     hash[ord(s[begin])] += 1
        #     begin += 1
        #
        #     if hash[ord(s[end])] >= 1:
        #         count -= 1
        #     hash[ord(s[end])] -= 1
        #     end += 1
        #
        # if count == 0:
        #     ans.append(begin)

        return ans