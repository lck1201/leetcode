# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: 'ListNode', k: int) -> 'ListNode':
        if not head or not head.next or k==0:
            return head

        length = 0
        ptr = head
        while ptr:
            ptr = ptr.next
            length += 1

        # module
        k = k%length
        if k==0:
            return head

        # find newTail
        num_to_break = length - k - 1
        ptr = head
        for _ in range(num_to_break):
            ptr = ptr.next

        # newHead is next to newTail
        newHead = ptr.next
        ptr.next = None #break connection

        # connect newTail and the rest
        ptr = newHead
        for _ in range(k-1):
            ptr = ptr.next

        ptr.next = head

        return newHead

class Solution2:
    def rotateRight(self, head: 'ListNode', k: int) -> 'ListNode':
        if not head or not head.next or k==0:
            return head

        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        tail.next = head

        # module
        k = k%length
        if k!=0:
            # find newTail
            num_to_break = length - k
            for _ in range(num_to_break):
                tail = tail.next

        # newHead is the next to newTail
        newHead = tail.next
        # break connection
        tail.next = None

        return newHead

# Test case
# head = ListNode(1)
# ptr = head
# for i in range(2,6):
#     ptr.next = ListNode(i)
#     ptr = ptr.next
#
# head = Solution2().rotateRight(head, 5)
# while head:
#     print(head.val)
#     head = head.next