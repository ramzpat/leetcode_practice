# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
  def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    # preorder: begin with root node
    # inorder: form a root node, the left side is the left nodes, right side is the right nodes 
    # We need to find a root first. 
    # preorder: root = preorder[0]
    # inorder: root = inorder[j] where inorder[j] == preorder[0] so that inorder[0:j] are for the left tree, inorder[j+1:] are the right tree
    # preorder: for the left, preorder[1:j+1]. for the right, preorder[j+1:] 
    # base case: empty list -> None 

    if len(preorder) == 0:
      return None
    
    # Find the root node in inorder list 
    j = 0
    n = len(inorder)
    while j < n and preorder[0] != inorder[j]:
      j += 1
    
    # find the left tree 
    left_tree = self.buildTree(preorder[1:j+1], inorder[0:j])
    right_tree = self.buildTree(preorder[j+1:], inorder[j+1:])
    return TreeNode(preorder[0], left_tree, right_tree)
