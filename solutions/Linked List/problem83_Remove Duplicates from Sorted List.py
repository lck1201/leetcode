# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        newHead = None
        tail = newHead
        while head:
            ptr = head
            ptr.next = None
            head = head.next

            if not newHead:
                newHead = ptr
                tail = newHead
            else:
                if tail.val != ptr.val:
                    tail.next = ptr
                    tail = tail.next

        return newHead

# head = ListNode(1)
# head.next = ListNode(1)
# head.next.next = ListNode(1)
# ans = Solution().deleteDuplicates(head)
# print('---------')
# while ans:
#     print(ans.val)
#     ans = ans.next

