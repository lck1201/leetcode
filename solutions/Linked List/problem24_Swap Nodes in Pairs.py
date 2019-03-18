# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: 'ListNode') -> 'ListNode':
        if not head or not head.next:
            return head

        newHead = ListNode(0)
        newTail = newHead
        while head and head.next:
            # extract & dis-connect nodes
            node1 = head
            node2 = head.next
            head = head.next.next

            #insert
            node1.next = None
            node2.next = node1
            newTail.next = node2
            newTail = node1

        newTail.next = head

        return newHead.next