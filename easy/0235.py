# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # recursive
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
      if p.val < root.val and q.val > root.val:
        return root
      if q.val < root.val and p.val > root.val:
        return root
      if p.val == root.val or q.val == root.val:
        return root
      if p.val < root.val and q.val < root.val:
        return self.lowestCommonAncestor(root.left, p, q)
      if p.val > root.val and q.val > root.val:
        return self.lowestCommonAncestor(root.right, p, q)
      raise AssertionError('there is an error')
        