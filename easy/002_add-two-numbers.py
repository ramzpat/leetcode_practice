# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum = 0
        head = ListNode(0, None)
        ptr = head
        prev_ptr = None
        while ((sum > 0) or (l1 != None) or (l2 != None)):
            if (l1 != None):
                sum = sum + l1.val
                l1 = l1.next 
            if (l2 != None):
                sum = sum + l2.val
                l2 = l2.next
            ptr.val = sum%10
            next_ptr = ListNode(0, None)
            ptr.next = next_ptr
            prev_ptr = ptr
            ptr = next_ptr
            sum = sum/10
        prev_ptr.next = None
        return head

# Test
# l1 = ListNode(2, ListNode(4, ListNode(3, None)))
# l2 = ListNode(5, ListNode(6, ListNode(4, None)))
# s = Solution()

# ret = s.addTwoNumbers(l1, l2)
# while (ret != None):
#     print(ret.val)
#     ret = ret.next
