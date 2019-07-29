class Solution:
    def numSubarraysWithSum(self, A: 'List[int]', S: 'int') -> 'int':
        s = 0
        res = 0
        counter = {0: 1}
        for x in A:
            s += x
            res += counter.get(s - S, 0)
            counter[s] = counter.get(s, 0) + 1

        return res

# import collections
# class Solution:
#     def numSubarraysWithSum(self, A, S):
#         c = collections.Counter({0: 1})
#         psum = res = 0
#         for i in A:
#             psum += i
#             res += c[psum - S]
#             c[psum] += 1
#         return res


# c = collections.Counter({0: 1})
# print(c[0], c[1])
