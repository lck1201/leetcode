# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        lh = rh = 0
        ln = root
        rn = root
        while ln:
            lh += 1
            ln = ln.left
        while rn:
            rh += 1
            rn = rn.right

        if rh == lh:
            return pow(2, lh) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
