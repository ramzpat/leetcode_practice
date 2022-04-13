# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def maxDepthFn(ptr, level = 0):
            if not(ptr):
                return level
            return max(maxDepthFn(ptr.left), maxDepthFn(ptr.right))+1
        return maxDepthFn(root)