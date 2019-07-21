# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head

        ptr = head
        while ptr:
            # CASE 1: if no child, proceed
            if not ptr.child:
                ptr = ptr.next
                continue

            # CASE 2: got child, find the tail of the child and link it to p.next
            childHead = ptr.child
            childTail = childHead
            while childTail.next:
                childTail = childTail.next

            ptrOriginNext= ptr.next

            # subLinkedList head concat
            ptr.next = childHead
            childHead.prev = ptr

            # subLinkedList tail concat
            childTail.next = ptrOriginNext
            if ptrOriginNext:
                ptrOriginNext.prev = childTail

            ptr.child = None

        return head