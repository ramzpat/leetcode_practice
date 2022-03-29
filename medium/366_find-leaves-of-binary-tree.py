# https://leetcode.com/problems/find-leaves-of-binary-tree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def arrangeNodeLevel(self, root, dict):
        if ((root.left == None) and (root.right == None)):
            if not (0 in dict):
                dict[0] = []
            dict[0].append(root.val)
            return (0, dict)

        left_level = -1
        right_level = -1
        if (root.left):
            (left_level, dict) = self.arrangeNodeLevel(root.left, dict)
        if (root.right):
            right_level, dict = self.arrangeNodeLevel(root.right, dict)
        deph_level = max(left_level, right_level)+1

        if not (deph_level in dict):
            dict[deph_level] = []
        dict[deph_level].append(root.val)
        return (deph_level, dict)

    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        dict = {}
        max_deph, dict = self.arrangeNodeLevel(root, dict)
        result = []
        for level in range(0, max_deph+1):
            result += [(dict[level])]
        return result

# Test
root = TreeNode(0)
root = TreeNode(0, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
s = Solution()

ret = s.findLeaves(root)
print(ret)