# https://leetcode.com/problems/maximum-width-of-binary-tree/

# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val  
    self.left = left
    self.right = right  

class Solution:
  def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0
    
    # bfs 
    # value: (TreeNode, position)
    que = deque([(root, 0)])
    max_width = 0
    while len(que) > 0:
      _, left_most_index = que[0]
      element_cnt = len(que)
      for _ in range(element_cnt):
        node, pos = que.popleft()
        max_width = max(max_width, pos-left_most_index+1)

        # consider next level
        if node.left:
          que.append((node.left, pos * 2))
        if node.right:
          que.append((node.right, pos * 2 + 1))
    return max_width

