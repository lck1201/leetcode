# NOTE: think thorough
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arrlen = len(nums)
        k = k % arrlen

        if k==0 or arrlen == 0:
            return None

        nums[:] = nums[-k:] + nums[:arrlen-k]
