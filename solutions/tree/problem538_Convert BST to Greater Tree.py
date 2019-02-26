# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inOrder(self, node):
        if node:
            self.inOrder(node.right)
            temp = node.val
            node.val += self.accmulate
            self.accmulate += temp
            self.inOrder(node.left)

    def convertBST(self, root: TreeNode) -> 'TreeNode':
        self.accmulate = 0
        self.inOrder(root)

        return root