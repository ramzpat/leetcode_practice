# https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        def findPathSum(ptr, currentSum = 0):
            if not(ptr):
                return False
            if not(ptr.left) and not(ptr.right):
                return (currentSum + ptr.val == targetSum)
            return findPathSum(ptr.left, currentSum + ptr.val) or findPathSum(ptr.right, currentSum + ptr.val)
        return findPathSum(root)