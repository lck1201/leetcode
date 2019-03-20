# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# see https://leetcode.com/problems/reverse-linked-list-ii/discuss/
#   30666/Simple-Java-solution-with-clear-explanation

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or not head.next or m == n:
            return head

        tempHead = ListNode(0)
        tempHead.next = head

        tail = tempHead
        for _ in range(m - 1):
            tail = tail.next
        # find left ptr, break original link
        newTail = tail.next
        tail.next = None

        ptr2 = newTail
        prev = None
        for i in range(m, n+1):
            pNext = ptr2.next
            ptr2.next = prev
            prev = ptr2
            if i < n:
                ptr2 = pNext
        newHead = ptr2

        tail.next = newHead
        newTail.next = pNext

        return tempHead.next


head = ListNode(1)
ptr = head
for i in range(2, 3):
    ptr.next = ListNode(i)
    ptr = ptr.next

re = Solution().reverseBetween(head, m = 1, n = 2)
while re:
    print(re.val)
    re = re.next