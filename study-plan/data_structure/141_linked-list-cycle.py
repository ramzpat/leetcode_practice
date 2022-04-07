# https://leetcode.com/problems/linked-list-cycle/

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
        tmp = []
        ptr = head
        while(ptr != None):
            if ptr in tmp:
                return True
            tmp.append(ptr)
            ptr = ptr.next

        return False

    def hasCycleOld(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        tmp = []
        ptr = head
        while(ptr != None):
            if ptr in tmp:
                return True
            tmp.append(ptr)
            ptr = ptr.next

        return False
