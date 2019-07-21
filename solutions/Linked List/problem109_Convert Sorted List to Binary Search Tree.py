# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head: 'ListNode') -> 'TreeNode':
        if not head:
            return None

        if not head.next:
            return TreeNode(head.val)

        ptr = head
        lenCount = 0
        while ptr:
            lenCount += 1
            ptr = ptr.next

        def dfsBuildTree(sNode, length):
            if length <= 0:
                return None

            leftPart = sNode
            for _ in range(length//2):
                sNode = sNode.next
            root = TreeNode(sNode.val)

            root.left = dfsBuildTree(leftPart, length//2)
            root.right = dfsBuildTree(sNode.next, length - length//2 - 1)

            return root

        return dfsBuildTree(head, lenCount)