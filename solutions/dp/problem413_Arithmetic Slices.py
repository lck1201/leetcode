class Solution:
    def numberOfArithmeticSlices(self, A: 'List[int]') -> 'int':
        cur = 0
        ans = 0
        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                cur += 1
                ans += cur
            else:
                cur = 0

        return ans
