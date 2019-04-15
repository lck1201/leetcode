# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest1(self, root: TreeNode, k: int) -> int:
        ans = float('-inf')
        def inorder(node):
            nonlocal k, ans
            if ans != float('-inf'): # already find an answer, skip following operations
                return

            if not node:
                return None

            inorder(node.left)
            k = k - 1
            if k == 0:
                ans = node.val
            inorder(node.right)

        inorder(root)
        return ans

    #iterative
    def kthSmallest2(self, root: TreeNode, k: int) -> int:
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
