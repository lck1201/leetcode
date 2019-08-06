# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# brilliant
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = cur =ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry%10)
            cur = cur.next
            carry //=10
        return dummy.next


class MySolution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        re = 0
        flag = 0
        pos = 0
        while True:
            if l1 == None and l2 == None:
                if flag == 1:
                    re = re + (10**pos)
                break
            elif l1 != None and l2 == None:
                the_digit = l1.val
                the_sum = l1.val
                l1 = l1.next
            elif l1 == None and l2 != None:
                the_digit = l2.val
                the_sum = l2.val
                l2 = l2.next
            elif l1 != None and l2 != None:
                the_digit = (l1.val+l2.val)%10
                the_sum = l1.val + l2.val
                l1=l1.next
                l2=l2.next

            re = re + (10**pos)*(the_digit + flag)

            flag = 0
            if the_sum >= 10:
                flag = 1

            pos += 1

        re = str(re)
        int_string_list = [ListNode(int(re[idx])) for idx in range(len(re)-1, -1, -1)]
        for idx in range(len(int_string_list)-1):
            int_string_list[idx].next = int_string_list[idx+1]

        return int_string_list[0]
