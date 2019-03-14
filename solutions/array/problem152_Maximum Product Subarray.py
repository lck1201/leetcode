class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return

        # NOTE:    result // store the result that is the max we have found so far
        # NOTE:    pmax   // imax/imin stores the max/min product of
        # NOTE:    pmin   // subarray that ends with the current number A[i]
        result = pmax = pmin = nums[0]

        for idx in range(1, len(nums)):
            n = nums[idx]
            # multiplied by a negative makes big number smaller, small number bigger
            # so we redefine the extremums by swapping them
            if n < 0:
                pmax, pmin = pmin, pmax

            # // max/min product for the current number is either the current number itself
            # // or the max/min by the previous number times the current one
            pmax = max(nums[idx], pmax*n)
            pmin = min(nums[idx], pmin*n)


            # // the newly computed max value is a candidate for our global result
            result = max(pmax, result)
            print(pmax, pmin, result)

        return result


class Solution2:
    @staticmethod
    def maxProduct(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return

        pmax = [0 for _ in range(len(nums))]
        pmin = [0 for _ in range(len(nums))]
        result = nums[0]
        pmax[0] = nums[0]
        pmin[0] = nums[0]

        for idx in range(1, len(nums)):
            n = nums[idx]

            pre_max = pmax[idx-1]
            pre_min = pmin[idx-1]
            if n < 0:
                pre_max, pre_min = pre_min, pre_max

            pmax[idx] = max(n, n*pre_max)
            pmin[idx] = min(n, n*pre_min)

            result = max(result, pmax[idx])

        print(pmax)
        print(pmin)
        print(result)
        return result

Solution2.maxProduct([-1, 2, 4, 0, 1])

