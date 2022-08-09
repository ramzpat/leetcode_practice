# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
from typing import Optional, Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
  def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    def travel(head:Optional[ListNode], index:int = 1) -> Tuple[Optional[ListNode], int]:
      if head == None:
        return (head, index-n)
      
      (new_next, tartget_index) = travel(head.next, index + 1)
      if tartget_index == index:
        return (new_next, tartget_index)
      else:
        head.next = new_next
        return (head, tartget_index)

    (new_head, _) = travel(head, 1)
    return new_head
    