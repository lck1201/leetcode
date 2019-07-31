class Solution:
    def majorityElement(self, nums: 'List[int]') -> 'List[int]':
        if not nums:
            return list()

        candi1, candi2, count1, count2 = 1, 0, 0, 0
        for n in nums:
            if n == candi1:
                count1 += 1
            elif n == candi2:
                count2 += 1
            elif count1 == 0:
                candi1, count1 = n, 1
            elif count2 == 0:
                candi2, count2 = n, 1
            else:
                count1 -= 1
                count2 -= 1

        return [n for n in (candi1, candi2) if nums.count(n) > len(nums) // 3]
