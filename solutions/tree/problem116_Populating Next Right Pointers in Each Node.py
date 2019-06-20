"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        if root.left:
            root.left.next = root.right

        if root.next and root.right:
            root.right.next = root.next.left

        self.connect(root.left)
        self.connect(root.right)

        return root


    def connect2(self, root):
        '''
        Brilliant! iterative! Level-order, managed by next pointer
        '''
        while root and root.left:
            next = root.left
            while root:
                root.left.next = root.right
                root.right.next = root.next and root.next.left
                root = root.next
            root = next