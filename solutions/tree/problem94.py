# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# NOTE: Recursively, common practice
class Solution1:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []

        def helper(node):
            if not node:
                return
            helper(node.left)
            result.append(node.val)
            helper(node.right)

        helper(root)
        return result


# NOTE: Iteratively, need to master
class Solution2:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result, stack = [], []
        while root or len(stack)>0:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right

        return result