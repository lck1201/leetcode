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

        result = tail =  ListNode(0)
        while l1 or l2:
            if l2==None or (l1 and l1.val <= l2.val):
                tail.next = ListNode(l1.val)
                l1 = l1.next
                tail = tail.next
            elif l1==None or (l2 and l2.val < l1.val):
                tail.next = ListNode(l2.val)
                l2 = l2.next
                tail = tail.next
            else:
                assert 0

        return result.next


# better iterative
def mergeTwoLists1(l1, l2):
    newHead = cur = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
        cur.next = None # more secure

    cur.next = l1 or l2
    return newHead.next


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
