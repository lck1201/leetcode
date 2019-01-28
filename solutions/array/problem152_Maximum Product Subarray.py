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

        return result
