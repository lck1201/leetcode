class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True

        seen = set()
        while True:
            n = helper(n)
            if n == 1:
                return True
            if n in seen:
                return False
            else:
                seen.add(n)

def helper(n):
    sum = 0
    while n != 0:
        d = n % 10
        n = n // 10
        sum += d * d
    return sum

re=Solution().isHappy(19)
print(re)