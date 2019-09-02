# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: 'TreeNode') -> 'int':
        if not root:
            return 0

        def dfs(node):
            nonlocal maxValue
            if not node:
                return 0

            left = max(0, dfs(node.left)) # zero means do not include left/right tree, e.g[2,-1,-1]
            right = max(0, dfs(node.right))
            maxValue = max(maxValue, left + right + node.val)
            return max(left, right) + node.val

        maxValue = float('-inf')
        dfs(root)
        return int(maxValue)