class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def linked_list_generator(nums):
    tail = dummy = ListNode(0)
    for x in nums:
        node = ListNode(x)
        tail.next = node
        tail = tail.next

    return dummy.next

def linked_list_display(node):
    pNode = node
    while pNode.next:
        print(pNode.val, end = " -> ")
        pNode = pNode.next
    print(pNode.val, end=' -> NULL')
