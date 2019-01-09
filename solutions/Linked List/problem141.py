# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nodeDict = {}
        while head:
            if id(head) not in nodeDict:
                nodeDict[id(head)] = 1
            else:
                return True
            head = head.next

        return False


# runner(2 step) & walker(1 step)
def hasCycle(head):
    try:
        slow = head
        fast = head.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
        return True
    except:
        return False