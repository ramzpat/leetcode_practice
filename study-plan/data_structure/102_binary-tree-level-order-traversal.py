# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        
        def levelTravel(ptr, level = 0):
            if not(ptr):
                return
            if(len(levels) < level+1):
                levels.append([])
            levels[level].append(ptr.val)
            levelTravel(ptr.left, level+1)
            levelTravel(ptr.right, level+1)
        levelTravel(root)
        return levels