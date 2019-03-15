# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def inorder(self, node):
    #     if not node:
    #         return
    #     self.inorder(node.left)
    #     self.cnt = self.cnt - 1
    #     if self.cnt == 0:
    #         self.ans = node.val
    #         return
    #     self.inorder(node.right)
    #
    # def kthSmallest(self, root: TreeNode, k: int) -> int:
    #     self.ans = 0
    #     self.cnt = k
    #
    #     self.inorder(root)
    #
    #     return self.ans

    #iterative
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.ans = 0
        self.cnt = k

        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k = k - 1
            if k == 0:
                break
            root = root.right

        return root.val
