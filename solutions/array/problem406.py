from functools import cmp_to_key

def mycmp(a, b):
    if a[0] == b[0]:
        return b[1] - a[1]
    return a[0] - b[0]

class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        people.sort(key=cmp_to_key(mycmp), reverse=True)
        for h, k in people:
            ans.insert(k, [h,k])

        return ans

p = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2],[6,3]]
s = Solution()
s.reconstructQueue(p)
