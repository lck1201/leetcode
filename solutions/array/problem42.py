class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        water = 0
        maxLeft = maxRight = 0
        while left < right:
            if height[left] <= height[right]:
                if maxLeft < height[left]:
                    maxLeft = height[left]
                else:
                    water += maxLeft - height[left]
                left += 1
            else:
                if maxRight < height[right]:
                    maxRight = height[right]
                else:
                    water += maxRight - height[right]
                right -= 1

        return water
