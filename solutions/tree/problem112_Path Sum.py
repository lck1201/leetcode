# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        ans = False
        if not root:
            return ans

        def helper(node, cSum):
            nonlocal ans
            if ans or not node:
                return

            cSum += node.val
            if cSum == sum and not node.left and not node.right:
                ans = True
                return

            helper(node.left, cSum)
            helper(node.right, cSum)

        helper(root, 0)

        return ans