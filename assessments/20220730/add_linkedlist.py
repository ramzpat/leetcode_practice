# Definition for singly-linked list.

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

  def __str__(self):
    return str(self.val) + " " + str(self.next)

from typing import List, Optional, Tuple


class Solution:
  def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    def reverseList(l1:Optional[ListNode], preVal:Optional[int] = None) -> Tuple [Optional[ListNode], Optional[ListNode]]:
      if l1 == None:
        return (None, None)
      elif l1.next == None:
        newNode = ListNode(l1.val)
        return (newNode, newNode) 
      newHead, newLast  = reverseList(l1.next, l1.val)
      newNode = ListNode(l1.val)
      newLast.next = newNode
      return (newHead, newNode)
    
    def addReverseList(l1_r:Optional[ListNode], l2_r:Optional[ListNode], carried:int = 0) -> Optional[ListNode]:
      if l1_r == None and l2_r == None:
        if carried > 0:
          return ListNode(carried)
        else:
          return None
      sum = carried
      nextL1 = l1_r
      nextL2 = l2_r
      # print(sum, nextL1.val, nextL2.val)
      if nextL1 != None:
        sum += nextL1.val
        nextL1 = nextL1.next
      if nextL2 != None:
        sum += nextL2.val
        nextL2 = nextL2.next
      return ListNode(sum%10, addReverseList(nextL1, nextL2, sum//10))

    l1_r,_ = reverseList(l1)
    l2_r,_ = reverseList(l2)
    # Add 
    ans_r = addReverseList(l1_r, l2_r, 0)
    ans, _ = reverseList(ans_r)
    return ans

# Test
s = Solution()
# [7,2,4,3], l2 = [5,6,4]
print(s.addTwoNumbers(ListNode(7, ListNode(2, ListNode(4, ListNode(3)))) , ListNode(5, ListNode(6, ListNode(4)) )) ) 