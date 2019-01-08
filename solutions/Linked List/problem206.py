# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# iteratively
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        pre = None
        while True:
            temp = head.next
            head.next = pre
            pre = head
            if not temp:
                return head
            head = temp

# fake recursively
class Solution2:
    def reverseList(self, head):
        return self._reverse(head)

    def _reverse(self, node, prev=None):
        if not node:
            return prev
        next = node.next
        node.next = prev
        return self._reverse(next, node)

# real recursively
class Solution3:
    def reverseList(self, head):
        if not head or not head.next:
            return head

        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return node

