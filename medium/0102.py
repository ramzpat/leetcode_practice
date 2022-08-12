# https://leetcode.com/problems/binary-tree-level-order-traversal/

from collections import defaultdict
from typing import Dict, List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
  def recur_levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    
    # Key: level, Value: List of values 
    level_ordering:Dict[int, List[int]] = defaultdict(list)
    maxi_level:List[int] = [0] # pass by reference 
    
    def travel_ordering(root:Optional[TreeNode], level:int = 1):
      # base case
      if root == None:
        return 0 
      level_ordering[level].append(root.val)
      maxi_level[0] = max(maxi_level[0], level)
      travel_ordering(root.left, level + 1)
      travel_ordering(root.right, level + 1)
    
    travel_ordering(root)
    return[level_ordering[i] for i in range(1, maxi_level[0]+1)]

  # iteration
  def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    level_ordering:Dict[int, List[int]] = defaultdict(list)
    max_level = 0

    stk = [(root, 1)]
    while len(stk) > 0:
      (node, level) = stk.pop()
      if node != None:
        level_ordering[level].append(node.val)
        stk.append((node.right, level+1))
        stk.append((node.left, level+1))
        max_level = max(max_level, level)
    
    return[level_ordering[i] for i in range(1, max_level+1)]
