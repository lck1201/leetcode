# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        dummpy = tail = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
            tail.next = None  # more secure

        tail.next = l1 or l2

        return dummpy.next

# recursively. This solution is not a tail-recursive, the stack will overflow while the list is too long :)
def mergeTwoLists2(l1, l2):
    if l1 == None:
        return l2
    if l2 == None:
        return l1

    if l1.val < l2.val:
        l1.next = mergeTwoLists2(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists2(l1, l2.next)
        return l2
