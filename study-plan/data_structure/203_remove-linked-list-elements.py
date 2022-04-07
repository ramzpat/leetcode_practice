# https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        ptr = new_head = ListNode()
        ptr_head = head 
        while (ptr_head):
            if (ptr_head.val != val):
                ptr.next = ListNode(ptr_head.val)
                ptr = ptr.next
            ptr_head = ptr_head.next 
        return new_head.next