# https://leetcode.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not(root):
            return []
        l = [root.val]
        l += self.preorderTraversal(root.left)
        l += self.preorderTraversal(root.right)
        return l