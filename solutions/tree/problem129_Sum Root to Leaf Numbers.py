# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0

        ans = 0
        def preOrder(node, num):
            nonlocal ans
            if not node.left and not node.right:
                ans += (num * 10 + node.val)
                return

            if node.left:
                preOrder(node.left, node.val + num * 10)
            if node.right:
                preOrder(node.right, node.val + num * 10)

        preOrder(root, 0)
        return ans
