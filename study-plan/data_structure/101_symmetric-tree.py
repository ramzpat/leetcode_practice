# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isSame(left, right):
            if (not left and not right):
                return True
            if not left or not right:
                return False 
            if (left.val != right.val):
                return False
            return isSame(left.left, right.right) and isSame(left.right, right.left)
        return isSame(root.left, root.right)