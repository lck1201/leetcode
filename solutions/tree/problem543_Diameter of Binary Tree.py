# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def dfs(self, node):
        if not node:
            return 0

        leftDepth = self.dfs(node.left)
        rightDepth = self.dfs(node.right)
        self.ans = max(leftDepth + rightDepth + 1, self.ans)

        return max(leftDepth, rightDepth) + 1

    def diameterOfBinaryTree(self, root: TreeNode) -> 'int':
        if not root:
            return 0

        self.ans = 0
        self.dfs(root)
        return self.ans - 1
