# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
from optparse import Option
from typing import Optional


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def isValidBST(self, root: Optional[TreeNode]) -> bool:
    if root == None:
      return True
    
    def helper(root, lower_bound:Optional[int] = None, upper_bound:Optional[int] = None):
      if root == None:
        return True
      if lower_bound != None and root.val <= lower_bound:
        return False 
      if upper_bound != None and root.val >= upper_bound:
        return False 
      return helper(root.left, lower_bound, root.val) and helper(root.right, root.val, upper_bound)
    
    return helper(root)