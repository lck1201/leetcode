class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        ax1, ay1, ax2, ay2 = rec1
        bx1, by1, bx2, by2 = rec2

        overlapX = abs(ax2 - ax1) + abs(bx2 - bx1) - (max(ax2, bx2) - min(ax1, bx1))
        overlapY = abs(ay2 - ay1) + abs(by2 - by1) - (max(ay2, by2) - min(ay1, by1))

        return overlapX > 0 and overlapY > 0
