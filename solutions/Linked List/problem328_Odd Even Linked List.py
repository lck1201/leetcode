# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        tail_odd = dummy_odd = ListNode(0)
        tail_even = dummy_even = ListNode(0)

        while head:
            tail_odd.next = head
            head = head.next
            tail_odd = tail_odd.next
            tail_odd.next = None

            if not head:
                break

            tail_even.next = head
            head = head.next
            tail_even = tail_even.next
            tail_even.next = None

        dummy_even = dummy_even.next
        tail_odd.next = dummy_even

        return dummy_odd.next

from utils import linked_list_generator, linked_list_display
a = [2,1,3,5,6,4,7]
ll = linked_list_generator(a)

re = Solution().oddEvenList(ll)
linked_list_display(re)