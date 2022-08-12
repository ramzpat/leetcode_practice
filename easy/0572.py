# https://leetcode.com/problems/subtree-of-another-tree/

# Definition for a binary tree node.
from optparse import Option
from typing import List, Optional, Set, Tuple


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  # encode solution
  def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    # This must be unique for each tree 
    # str format: Rroot.L(left).R(right)
    def encode_tree(root: Optional[TreeNode]) -> str: 
      if root == None:
        return "n"
      return "R"+str(root.val)+"l"+encode_tree(root.left)+"r"+encode_tree(root.right)
    return encode_tree(subRoot) in encode_tree(root)

  # dfs solution
  def dfs_isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

      # dfs for each node 
      # Time complexity: O(min(V(root_a),V(root_b)) ) where V(X) is the number of nodes in tree X
      def isSameTree(root_a:Optional[TreeNode], root_b:Optional[TreeNode]) -> bool:
        # Base cases
        if root_a == None and root_b == None:
          return True 
        if root_a == None or root_b == None:
          return False

        return (root_a.val == root_b.val) and isSameTree(root_a.left, root_b.left) and isSameTree(root_a.right, root_b.right)

      # Base case
      if root == None and subRoot == None:
        return True

      if root == None or subRoot == None:
        return False 
      
      # From here, we can ensure subRoot is not None 
      # Travel all nodes in the root
      # Time complexity: O(V(root) * V(root))
      ptr_q = [root]
      while len(ptr_q) > 0:
        root_node = ptr_q.pop()

        if root_node != None:
          # Check the current sub-tree
          if root_node.val == subRoot.val and isSameTree(root_node, subRoot):
            return True 

          # if not, we continue to explore the tree (dfs)
          ptr_q.append(root_node.left)
          ptr_q.append(root_node.right)
      # We cannot find the matched subtree 
      return False 
