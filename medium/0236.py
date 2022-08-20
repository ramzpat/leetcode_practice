# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
from collections import defaultdict
from typing import Dict, Tuple


class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None
  def __str__(self):
    return str(self.val)
  
class Solution:
  def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    
    def travel_path(root:TreeNode, p:TreeNode) -> List[TreeNode]:
      if root == None:
        return []
      if root.val == p.val:
        return [root]
      l_path = travel_path(root.left, p)
      r_path = travel_path(root.right, p)
      if len(l_path) > 0:
        return [root] + l_path
      elif len(r_path) > 0:
        return [root] + r_path
      else:
        return []
    
    p_path = travel_path(root, p)
    q_path = travel_path(root, q)
    i = 0
    n = min(len(p_path), len(q_path))
    while i < n and p_path[i] == q_path[i]:
      i+=1
    return p_path[i-1]
  