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
        if not head or not head.next:
            return head

        prev = None
        while True:
            pNext = head.next
            head.next = prev

            if not pNext:
                return head

            prev = head
            head = pNext


class Solution2:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        #reverse sub linked-list
        newhead = None
        while head:
            extraction = head
            head = head.next
            extraction.next = newhead
            newhead = extraction

        return head


# recursively, easy to understand, same idea as Solution
class Solution3:
    def reverseList(self, head):
        return self._reverse(head)

    def _reverse(self, cur_node, prev_node=None):
        if not cur_node:
            return prev_node
        next_node = cur_node.next
        cur_node.next = prev_node
        return self._reverse(next_node, cur_node)


# more recursive
class Solution4:
    def reverseList(self, head):
        if not head or not head.next:
            return head

        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return node