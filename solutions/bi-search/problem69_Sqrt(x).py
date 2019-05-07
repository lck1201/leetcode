# slower, but more understandable
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1 or x == 0:
            return x

        l = 0
        r = x
        mid = (l + r) / 2
        while abs(mid * mid - x) > 0.001:
            if mid * mid > x:
                r = mid
            elif mid * mid < x:
                l = mid
            mid = (l + r) / 2

        return int(mid)

#Faster
class Solution2():
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1 or x == 0:
            return x

        l = 0
        r = x
        ans = 0
        while True:
            mid = (l + r) / 2
            if ans == mid:  # converve
                break
            if mid * mid > x:
                r = mid
            elif mid * mid < x:
                l = mid
            ans = mid

        return int(ans)
