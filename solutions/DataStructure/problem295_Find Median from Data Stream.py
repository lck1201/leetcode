from heapq import * #it's a min heap

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small_part = []
        self.big_part = []

    def addNum(self, num: int) -> None:
        heappush(self.small_part, -heappushpop(self.big_part, num))
        if len(self.big_part) < len(self.small_part):
            heappush(self.big_part, -heappop(self.small_part))
        print(self.small_part, self.big_part)

    def findMedian(self) -> float:
        if len(self.big_part) > len(self.small_part):
            return float(self.big_part[0])
        return (self.big_part[0] - self.small_part[0]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# nums = [3,5,8,4,2,87,0,2,5,7,-3,7,4]
# for x in nums:
#     obj.addNum(x)
# param_2 = obj.findMedian()