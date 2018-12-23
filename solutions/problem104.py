# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def dfs(node):
    if node==None:
        return 0

    return max(dfs(node.left) + 1, dfs(node.right) + 1)

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return dfs(root)
