# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head or not head.next:
            return  head

        tail1 = dummy_less = ListNode(0)
        tail2 = dummy_bigger = ListNode(0)

        ptr = head
        while ptr:
            extract = ptr
            ptr = ptr.next
            extract.next = None

            if extract.val < x:
                tail1.next = extract
                tail1 = tail1.next
            else:
                tail2.next = extract
                tail2 = tail2.next

        tail1.next = dummy_bigger.next
        return dummy_less.next