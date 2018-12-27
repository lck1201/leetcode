# back tracking: time limit exceed
class Solution_dfs:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        self.result = 0
        self.dfs(0, height)

        return self.result

    def dfs(self, start, height):
        for i in range(start + 1, len(height)):
            self.result = max(self.result, min(height[i], height[start]) * (i - start))
            self.dfs(i, height)


# Idea / Proof:
# 1. The widest container (using first and last line) is a good candidate,
#    because of its width. Its water level is the height of the smaller one of first and last line.
# 2. All other containers are less wide and thus would need a higher water level in order to hold more water.
# 3. The less wide couple of lines don't support a higher water level and
#    can thus be safely removed from further consideration.
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height)-1
        water = 0
        while left<right:
            water = max(water, (right-left)*min(height[left], height[right]))
            if height[left] <= height[right]:
                left += 1
            else:
                right -=1
        return water



