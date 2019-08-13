# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head

        maping = dict()
        dummy = Node(None, None, None)
        tail = dummy

        HeadPtr = head
        while HeadPtr:
            newNode = Node(HeadPtr.val, None, None)
            maping[id(HeadPtr)] = newNode
            tail.next = newNode
            tail = tail.next
            tail.next = None
            HeadPtr = HeadPtr.next

        HeadPtr = head
        while HeadPtr:
            if HeadPtr.random:  # if its random ptr is not NULL
                maping[id(HeadPtr)].random = maping[id(HeadPtr.random)]
            else:
                maping[id(HeadPtr)].random = None
            HeadPtr = HeadPtr.next

        return dummy.next

# a1 = Node(0,None,None)
# a2 = Node(0,None,None)
# print(id(a1))
# print(id(a2))
#
