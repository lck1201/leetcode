from collections import Counter
class Solution:
    def intersect(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        c1 = Counter(nums1)
        c2 = Counter(nums2)

        common_key = c1.keys() & c2.keys()
        temp = [min(c1[k], c2[k])*[k] for k in common_key]
        ans = []
        for i in temp:
            ans.extend(i)
        return ans

Solution().intersect([1,2,2,1],[2,2])