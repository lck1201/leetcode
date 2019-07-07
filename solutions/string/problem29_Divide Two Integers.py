class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            print("enter")
            while dividend >= temp: #actually it's an acceleration, by-default step is 1*divisor
                print(dividend, temp, i, res)
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)


Solution().divide(27,3)