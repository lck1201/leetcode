# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def dfs(node):
    if node==None:
        return 0

    left_depth = dfs(node.left)
    right_depth = dfs(node.right)
    return max(left_depth, right_depth) + 1

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return dfs(root)
