# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        duplicate = None
        newHead = None
        tail = newHead
        while head:
            ptr = head
            head = head.next

            # exclude duplicate nodes
            if ptr.val == duplicate or (ptr.next and ptr.val == ptr.next.val):
                duplicate = ptr.val
                continue

            # only include single nodes
            if not newHead:
                newHead = ptr
                tail = newHead
                tail.next = None
            else:
                tail.next = ptr
                tail = tail.next
                tail.next = None

        return newHead
