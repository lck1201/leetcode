# common practice, use hash table to store frequency
class Solution1:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        frequencyDict = {}
        for n in nums:
            frequencyDict[n] = frequencyDict.get(n, 0) + 1

        sorted_frequencyDict = sorted(frequencyDict.items(), key=operator.itemgetter(1), reverse=True)
        for key, val in sorted_frequencyDict:
            if k == 0 :
                break
            result.append(key)
            k -= 1

        return result

# time O(N) method, use extra space
class Solution2:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frequencyDict = {}
        bucket = [0] * (len(nums) + 1)
        for n in nums:
            frequencyDict[n] = frequencyDict.get(n, 0) + 1

        for key in frequencyDict:
            freq = frequencyDict[key]
            if not isinstance(bucket[freq], list):
                bucket[freq] = list()
            bucket[freq].append(key)

        result = list()
        for idx in list(range(len(bucket)))[::-1]:
            if len(result)>=k:
                break
            if isinstance(bucket[idx], list):
                result.extend(bucket[idx])

        return result