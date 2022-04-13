# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def reverseL(ptr, tail = None):
            if not(ptr):
                return tail
            l = ptr.next
            new_tail = ListNode(ptr.val, tail)
            return reverseL(l, new_tail)
        
        def reverseL2(ptr, tail = None):
            if not(ptr):
                return tail
            l = ptr.next
            new_tail = ListNode(ptr.val, tail)
            return reverseL(l, new_tail)
        
        return reverseL(head)

