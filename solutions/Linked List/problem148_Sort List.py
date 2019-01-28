# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# update1: 实现了链表的快排，但是15/16 test case passed，最后一个case很恶心
# 1,2,3 三个数字重复出现，导致分割不均匀，结果超时
# 这题若要过这个case，merge排序更为合适

# update2: 分成了 smaller_list, mid_list, bigger_list，通过所有case
class LinkedList:
    def __init__(self, node):
        if not node:
            self.head = self.tail = None
        else:
            self.head = node
            p = node
            while p.next:
                p = p.next
            self.tail = p

    def push_back(self, node):
        node.next = None
        if not self.is_empty():
            self.tail.next = node
            self.tail = self.tail.next
        else:
            self.head = self.tail = node

    def pop_front(self):
        if not self.is_empty():
            if self.head == self.tail:
                p = self.head
                self.head = None
                self.tail = None
            else:
                p = self.head
                self.head = self.head.next
            p.next = None
            return p
        else:
            return None

    def is_empty(self):
        return (self.head == None) and (self.tail == None)

    def concat(self, linkedlist):
        if self.is_empty():
            self.head = linkedlist.head
            self.tail = linkedlist.tail
        elif linkedlist.is_empty():
            pass
        else:
            self.tail.next = linkedlist.head
            self.tail = linkedlist.tail

        linkedlist = None


def quick_sort(ll):
    if ll.head == ll.tail:
        return ll

    pivot_node = ll.pop_front()

    smaller_list = LinkedList(None)
    mid_list = LinkedList(pivot_node)
    bigger_list = LinkedList(None)

    while not ll.is_empty():
        the_node = ll.pop_front()
        if the_node.val < pivot_node.val:
            smaller_list.push_back(the_node)
        elif the_node.val == pivot_node.val:
            mid_list.push_back(the_node)
        else:
            bigger_list.push_back(the_node)

    smaller_list = quick_sort(smaller_list)
    bigger_list =  quick_sort(bigger_list)

    smaller_list.concat(mid_list)
    smaller_list.concat(bigger_list)

    return smaller_list


class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        ll = LinkedList(head)
        ll = quick_sort(ll)

        return ll.head



# NOTE: ------------merge sort--------------------
def merge(l1, l2):
    l = ListNode(0)
    p = l

    while l1!=None and l2!=None:
        if l1.val < l2.val:
            p.next = l1
            l1 = l1.next
        else:
            p.next = l2
            l2 = l2.next
        p = p.next

    if l1 != None:
        p.next = l1
    if l2 != None:
        p.next = l2

    return l.next

class Solution2:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head

        # step 1. cut the list to two halves
        prev = None
        slow = fast = head

        while fast!=None and fast.next!=None:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None

        # step 2. sort each half
        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        # step 3. merge l1 and l2
        return merge(l1, l2)


# # debug
# l = [6, 2, 3, 7, 10, 11, 100, -5, -123]
# head = ListNode(l[0])
# p = head
# for i in range(1, len(l)):
#     p.next = ListNode(l[i])
#     p = p.next
#
# s = Solution2()
# re = s.sortList(head)
# while re:
#     print(re.val)
#     re = re.next
