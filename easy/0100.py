# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

from turtle import st
from typing import Optional 

class Solution:
  def recur_isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    # Base case 1
    if p == None and q == None:
      return True 
    # Base case 2
    if p == None or q == None:
      return False

    return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
  
  def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    
    def check_same_value(p:Optional[TreeNode], q:Optional[TreeNode]) -> bool:
      # Base case 1
      if p == None and q == None:
        return True 
      # Base case 2
      if p == None or q == None:
        return False
      return (p.val == q.val)
    
    stk = [(p, q)]
    while len(stk) > 0:
      (node_a, node_b) = stk.pop()
      if check_same_value(node_a, node_b) == False:
        return False 
        
      if node_a != None and node_b != None:
        stk.append((node_a.left, node_b.left))
        stk.append((node_a.right, node_b.right))

    return True 