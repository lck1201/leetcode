# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def splitListToParts(self, root: 'ListNode', k: int) -> 'List[ListNode]':
        if not root:
            return [None] * k

        lenCount = 0
        ptr = root
        while ptr:
            lenCount += 1
            ptr = ptr.next

        partLen = [lenCount//k] * k
        for i in range(lenCount%k):
            partLen[i] += 1

        ptr = root
        ans = list()
        for i in range(len(partLen)):
            if partLen[i] > 0:
                dummy = ListNode(0)
                tail = dummy
                for j in range(partLen[i]):
                    tail.next = ListNode(ptr.val)
                    ptr = ptr.next
                    tail = tail.next
                    tail.next = None
                ans.append(dummy.next)
            else:
                ans.append(None)

        return ans