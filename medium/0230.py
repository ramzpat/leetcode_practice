# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
from operator import index
from re import S
from tracemalloc import start
from typing import Optional


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:

  # Recursive
  # Bad: heap storage 
  def recur_kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    ptr = root
    ans_k = []

    def indexing_until_k(root, start_index = 0) -> int:
      # Return: the largest index
      if root == None:
        return start_index
      
      # We already have an answer
      if len(ans_k) == 1:
        return k
      
      most_left_index = indexing_until_k(root.left, start_index)
      
      # Found the solution
      if most_left_index + 1 == k:
        ans_k.append(root.val)
        return k
      # Continue to search more 
      most_index = indexing_until_k(root.right, most_left_index + 1)
      return most_index
    indexing_until_k(root)
    return ans_k[0]

  # Interation
  # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
  #   current_index = 0
  #   stk = [root]  
    