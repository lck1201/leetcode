class Solution:
    def numberToWords(self, num: int) -> str:
        LESS_THAN_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                        "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        TENS = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        THOUSANDS = ["", "Thousand", "Million", "Billion"]

        def helper(n):
            if n == 0:
                return ""
            elif n < 20:
                return LESS_THAN_20[n] + " "
            elif n < 100:
                return TENS[n//10] + " " + helper(n%10)
            else:
                return LESS_THAN_20[n//100] + ' Hundred ' + helper(n%100)

        if num == 0:
            return "Zero"

        i = 0
        words = ""
        while num > 0:
            if num % 1000 != 0:
                words = helper(num%1000) + THOUSANDS[i] + " " + words

            num //= 1000
            i += 1
        return words.strip()

# re = Solution().numberToWords(132146)
# print(re)