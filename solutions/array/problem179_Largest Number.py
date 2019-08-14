class Comparable:
    # object that can be sorted thanks to magic methods.
    def __init__(self, num):
        self.value = str(num)
    def __lt__(self, other):
        # '82' is before '824' because '82|824' is greater than '824|82'
        return self.value + other.value > other.value + self.value
    def __gt__(self, other):
        return self.value + other.value < other.value + self.value
    def __eq__(self, other):
        return self.value + other.value == other.value + self.value


class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        numStrings = [Comparable(n) for n in nums]
        numStrings.sort() # ascending
        output = ''.join((e.value for e in numStrings))
        return output.lstrip('0') or '0'

# python2
class Solution2:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        num = [str(x) for x in num]
        num.sort(cmp=lambda x, y: cmp(y+x, x+y))
        return ''.join(num).lstrip('0') or '0'

re = Solution2().largestNumber([3,30,34,5,9])
print(re)