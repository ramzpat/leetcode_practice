# https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        def invert(ptr):
            if not(ptr):
                return None
            newPtr = TreeNode(ptr.val)
            newPtr.left = invert(ptr.right)
            newPtr.right = invert(ptr.left)
            return newPtr
        return invert(root)