# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ptr = head
        ret = ListNode()
        ans = ret
        last_max = -101
        while(ptr):
            if (ptr.val > last_max):
                last_max = ptr.val
                ret.next = ListNode(last_max)
                ret = ret.next
            ptr = ptr.next 

        return ans.next 
