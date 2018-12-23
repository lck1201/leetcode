class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """

        result = 0
        jewel_type = set()
        for char in J:
            jewel_type.add(char)
        for stone in S:
            if stone in jewel_type:
                result += 1

        return result

# one-line solution
# class Solution:
#     def numJewelsInStones(self, J, S):
#         return sum(map(S.count, J))

# s = Solution()
# print(s.numJewelsInStones("z", "ZZ"))
