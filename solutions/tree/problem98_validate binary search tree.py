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

        prev = float('-inf')
        ans = True

        def inorder(node):
            nonlocal ans, prev
            if not ans:
                return

            if node.left:
                inorder(node.left)

            if node.val <= prev:
                ans = False
                return
            else:
                prev = node.val

            if node.right:
                inorder(node.right)

        inorder(root)
        return ans

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

# 分左右子树去解
def isValidBST(node, minVal=float('-inf'), maxVal=float('inf')):
    if node == None:
        return True
    if node.val >= maxVal or node.val <= minVal:
        return False

    return isValidBST(node.left, minVal, node.val) and isValidBST(node.right, node.val, maxVal)
