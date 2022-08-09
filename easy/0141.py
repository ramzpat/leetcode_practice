# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional, Set


class Solution:
  def hasCycle(self, head: Optional[ListNode]) -> bool:
    visited:Set[ListNode] = set()
    ptr = head 
    while(ptr != None):
      if ptr in visited:
        return True 
      visited.add(ptr)
      ptr = ptr.next   
    return False