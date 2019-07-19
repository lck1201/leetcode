# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: 'List[int]', postorder: 'List[int]') -> 'TreeNode':
        if not inorder or not postorder:
            return None

        def buildCore(inorder, postorder):
            if not inorder or not postorder:
                return None
            val = postorder.pop(-1)
            root = TreeNode(val)

            index = inorder.index(val)

            root.left = buildCore(inorder[:index], postorder[:index])
            root.right = buildCore(inorder[index+1:], postorder[index:])
            return root

        return buildCore(inorder, postorder)

# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
#     3
#    / \
#   9  20
#     /  \
#    15   7