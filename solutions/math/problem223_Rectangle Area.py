class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        ax1, ay1, ax2, ay2, bx1, by1, bx2, by2 = A, B, C, D, E, F, G, H

        overlapX = abs(ax2 - ax1) + abs(bx2 - bx1) - (max(ax2, bx2) - min(ax1, bx1))
        overlapY = abs(ay2 - ay1) + abs(by2 - by1) - (max(ay2, by2) - min(ay1, by1))

        twoArea = abs(ax2 - ax1) * abs(ay2 - ay1) + abs(bx2 - bx1)* abs(by2 - by1)
        if overlapX > 0 and overlapY > 0:
            return twoArea - overlapX * overlapY
        else:
            return twoArea


print(Solution().computeArea(A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2))