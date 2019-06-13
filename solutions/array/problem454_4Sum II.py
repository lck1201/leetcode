import collections
class Solution:
    def fourSumCount(self, A: 'List[int]', B: 'List[int]', C: 'List[int]', D: 'List[int]') -> int:
        AB = collections.Counter(a + b for a in A for b in B)
        print(AB)
        return sum(AB[-c - d] for c in C for d in D)

A = [1, 2]
B = [-2, -1]
C = [-1, 2]
D = [0, 2]
Solution().fourSumCount(A,B,C,D)