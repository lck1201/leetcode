# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def robSub(root, mp):
    if not root:
        return 0
    if id(root) in mp:
        return mp[id(root)]

    val = 0
    if root.left:
        val += robSub(root.left.left, mp) + robSub(root.left.right, mp)

    if root.right:
        val += robSub(root.right.left, mp) + robSub(root.right.right, mp)

    val = max(val + root.val, robSub(root.left, mp) + robSub(root.right, mp))
    mp[id(root)] = val

    return val


class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        mp = dict()
        return robSub(root, mp)

