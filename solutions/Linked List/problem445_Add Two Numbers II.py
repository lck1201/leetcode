# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# if I don't reverse linked-list,
# then must use stack
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        def reverseLinkedList(node: ListNode) -> ListNode:
            if not node.next:
                return node

            newHead = None
            while node:
                extraction = node
                node = node.next
                extraction.next = newHead
                newHead = extraction

            return newHead

        newl1 = reverseLinkedList(l1)
        newl2 = reverseLinkedList(l2)

        carry = 0
        dummy = cur = ListNode(0)
        while newl1 or newl2 or carry:
            if newl1:
                carry += newl1.val
                newl1 = newl1.next
            if newl2:
                carry += newl2.val
                newl2 = newl2.next
            cur.next = ListNode(carry%10)
            cur = cur.next
            carry //= 10

        return reverseLinkedList(dummy.next)