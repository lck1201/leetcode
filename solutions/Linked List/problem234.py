# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        count = 0
        p = head
        while p:
            p = p.next
            count += 1

        p = head
        for _ in range(count//2):
            p = p.next

        # if odd, step once more
        if count % 2 == 1:
            p = p.next

        #reverse sub linked-list
        newhead = None
        while p:
            extraction = p
            p = p.next
            extraction.next = newhead
            newhead = extraction

        for _ in range(count//2):
            # print(p.val, head.val)
            if newhead.val != head.val:
                return False
            newhead = newhead.next
            head = head.next

        return True

