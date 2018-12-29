from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        def helper(preorder, inorder):
            if not inorder:
                return None

            # pick up the first element as a root
            root_val = preorder.popleft()
            root = TreeNode(root_val)

            # root splits inorder list
            # into left and right subtrees
            index = inorder.index(root_val)

            # recursion 
            root.left = helper(preorder, inorder[:index])
            root.right = helper(preorder, inorder[index + 1:])
            return root

        return helper(deque(preorder), inorder)
