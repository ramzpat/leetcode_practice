# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        mergeList = ListNode()
        ptr = mergeList

        ptr1 = list1 
        ptr2 = list2
        while (ptr1 != None) or (ptr2 != None):
            if (ptr1 == None):
                ptr.next = ListNode(ptr2.val)
                ptr = ptr.next 
                ptr2 = ptr2.next
            elif (ptr2 == None):
                ptr.next = ListNode(ptr1.val)
                ptr = ptr.next 
                ptr1 = ptr1.next
            elif (ptr1.val >= ptr2.val):
                ptr.next = ListNode(ptr2.val)
                ptr = ptr.next 
                ptr2 = ptr2.next
            else:
                ptr.next = ListNode(ptr1.val)
                ptr = ptr.next 
                ptr1 = ptr1.next

        return mergeList.next

