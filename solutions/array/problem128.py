class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        linkDict = {}
        for x in nums:
            if x not in linkDict:
                linkDict[x] = x

                rx = x + 1
                if rx in linkDict:
                    right_end = linkDict[rx]
                    linkDict[right_end] = x
                    linkDict[x] = right_end

                lx = x - 1
                if lx in linkDict:
                    left_end = linkDict[lx]
                    right_end = linkDict[x]
                    linkDict[left_end] = right_end
                    linkDict[right_end] = left_end

        result = 0
        for k, v in linkDict.items():
            result = max(abs(k-v)+1, result)

        return result