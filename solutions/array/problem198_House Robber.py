class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if N == 0:
            return 0
        if N == 1:
            return nums[0]

        table = [-1] * N
        for idx in range(N):
            if idx == 0:
                table[idx] = nums[0]
            elif idx == 1:
                table[idx] = max(nums[0], nums[1])
            else:
                table[idx] = max(table[idx-1], nums[idx]+table[idx-2])

        return max(table[-1], table[-2])

a = [2,7,9,3,1,4]
print(Solution().rob(a))

# In essence, they are the same algorithm
def rob(nums):
    n = len(nums)
    a = b = 0
    for i in range(n):
        if i%2==0:
            a = max(a+nums[i],b)
        else:
            b = max(a, b+nums[i])
    return max(a,b)

print(rob(a))


#Step 2. Recursive (top-down)
# public int rob(int[] nums) {
#     return rob(nums, nums.length - 1);
# }
# private int rob(int[] nums, int i) {
#     if (i < 0) {
#         return 0;
#     }
#     return Math.max(rob(nums, i - 2) + nums[i], rob(nums, i - 1));
# }

# Step 3. Recursive + DP (top-down).
# int[] memo;
# public int rob(int[] nums) {
#     memo = new int[nums.length + 1];
#     Arrays.fill(memo, -1);
#     return rob(nums, nums.length - 1);
# }
#
# private int rob(int[] nums, int i) {
#     if (i < 0) {
#         return 0;
#     }
#     if (memo[i] >= 0) {
#         return memo[i];
#     }
#     int result = Math.max(rob(nums, i - 2) + nums[i], rob(nums, i - 1));
#     memo[i] = result;
#     return result;
# }