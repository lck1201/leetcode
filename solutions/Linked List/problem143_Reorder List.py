# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head or not head.next:
            return

        # compute linked-list length
        length = 0
        tPtr = head
        while tPtr:
            length += 1
            tPtr = tPtr.next

        # get head ptr of second part, and break the link
        midStep = int(length/2 + 0.5) - 1
        tail = head
        for _ in range(midStep):
            tail = tail.next

        secondHead = tail.next
        tail.next = None

        # reverse the second part
        newhead = None
        while secondHead:
            extraction = secondHead
            secondHead = secondHead.next
            extraction.next = newhead
            newhead = extraction

        # concat two linked-list
        head1 = head
        tail = dummy = ListNode(0)
        while head1 and newhead:
            tail.next = head1
            head1 = head1.next
            tail = tail.next
            tail.next = None

            tail.next = newhead
            newhead = newhead.next
            tail = tail.next
            tail.next = None

        tail.next = head1 or newhead

        head = dummy.next


from utils import linked_list_generator, linked_list_display
a = [1,2,3,4]
ll = linked_list_generator(a)

Solution().reorderList(ll)
linked_list_display(ll)