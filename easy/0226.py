# https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root == None:
      return root 
    left_side = self.invertTree(root.left)
    right_side = self.invertTree(root.right)
    root.left = right_side
    root.right = left_side
    return root 