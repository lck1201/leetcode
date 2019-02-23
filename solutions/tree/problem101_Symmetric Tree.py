# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: 'TreeNode') -> 'bool':
        if not root:
            return True

        leftQ = [root.left]
        rightQ = [root.right]

        while leftQ and rightQ:
            left  = leftQ.pop(0)
            right = rightQ.pop(0)

            if left == None and right == None:
                continue
            if left == None or right == None:
                return False
            if left.val!=right.val:
                return False

            leftQ.append(left.left)
            leftQ.append(left.right)
            rightQ.append(right.right)
            rightQ.append(right.left)

        return True

# recursive, almost the same performance
class Solution2:
    def isSymmetric(self, root: 'TreeNode') -> 'bool':
        if not root:
            return True

        return self.isSymmetricTree(root.left, root.right)

    def isSymmetricTree(self, left, right):
        if not left and not right:
            return True

        if not left or not right or left.val != right.val:
            return False

        return self.isSymmetricTree(left.left, right.right) and self.isSymmetricTree(left.right, right.left)
