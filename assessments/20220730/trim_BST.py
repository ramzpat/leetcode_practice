# Definition for a binary tree node.
from typing import Optional


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
  
  def __str__(self):
    def inorder_str(node: Optional[TreeNode]) -> str:
      if node == None:
        return ""
      return inorder_str(node.left) + " " + str(node.val) + " " + inorder_str(node.right)
    return inorder_str(self)

class Solution:
  
  def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
    if root == None:
      return root
    elif root.val < low:
      return self.trimBST(root.right, low, high)
    elif root.val > high:
      return self.trimBST(root.left, low, high)
    else:
      root.left = self.trimBST(root.left, low, high)
      root.right = self.trimBST(root.right, low, high)
      return root

# Test 
s = Solution()
print(s.trimBST(TreeNode(1, TreeNode(0), TreeNode(2)), 1, 2))
print(s.trimBST(TreeNode(1, TreeNode(-1), TreeNode(2)), 0, 0))
print(s.trimBST(TreeNode(3, TreeNode(0, None, TreeNode(2, TreeNode(1))), TreeNode(4)), 1, 3))

