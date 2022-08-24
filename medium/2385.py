# https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/

# Definition for a binary tree node.
from collections import defaultdict, deque
from typing import Dict, List, Optional, Set

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
    edges:Dict[int, List[TreeNode]] = defaultdict(list)
    
    def travel(node:Optional[TreeNode], parent:Optional[TreeNode] = None):
      if node == None:
        return

      if parent:
        edges[node.val].append(parent)
      
      travel(node.left, node)
      travel(node.right, node)
      if node.left:
        edges[node.val].append(node.left)
      if node.right:
        edges[node.val].append(node.right)

    travel(root) 

    que = deque([(start, 0)])
    visited:Set[int] = set()
    max_distance = 0
    while len(que) > 0:
      node_val, level = que.popleft()
      if node_val not in visited:
        visited.add(node_val)
        max_distance = max(max_distance, level)
        for t_node in edges[node_val]:
          que.append((t_node.val, level + 1))
    return max_distance
