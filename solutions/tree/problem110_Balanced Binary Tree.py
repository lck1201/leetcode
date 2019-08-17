# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(node):
            if not node:
                return 0, True

            leftDepth, isLeftBa = dfs(node.left)
            rightDepth, isRightBa = dfs(node.right)

            curDepth = max(leftDepth, rightDepth) + 1

            if not isLeftBa or not isRightBa:
                return curDepth, False
            else:
                return curDepth, abs(leftDepth - rightDepth) <= 1

        _, isB = dfs(root)

        return isB

