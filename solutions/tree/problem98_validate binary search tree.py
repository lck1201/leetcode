# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: 'TreeNode') -> 'bool':
        if not root:
            return True

        self.prev = float('-inf')
        self.ans = True
        self.inorder(root)

        return self.ans

    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)

        if node.val <= self.prev:
            self.ans = False
            return
        else:
            self.prev = node.val

        self.inorder(node.right)

    def isValidBST_iter(self, root: 'TreeNode') -> 'bool':
        stack = []
        prev = float('-inf')
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if prev >= root.val:
                return False
            else:
                prev = root.val
            root = root.right

        return True