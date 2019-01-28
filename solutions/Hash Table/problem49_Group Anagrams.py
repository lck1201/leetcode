from functools import reduce

# use string(length 26, counting string) as key
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = []
        letterDict = {}

        for word in strs:
            encode = [0]*26
            for l in word:
                encode[ord(l)-ord('a')] += 1
            encode = reduce(lambda x,y:str(x)+str(y), encode)

            if encode not in letterDict:
                letterDict[encode] = list()
            letterDict[encode].append(word)

        for k,v in letterDict.items():
            result.append(v)

        return result

# use letter tuple as key
class Solution2:
    def groupAnagrams(self, strs):
        d = {}
        for w in sorted(strs):
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
        return d.values()