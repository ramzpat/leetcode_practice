# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):



    def getDirections(self, root, startValue, destValue):
        """
        :type root: Optional[TreeNode]
        :type startValue: int
        :type destValue: int
        :rtype: str
        """
        
        def findDest(root, foundStart = False, foundDest = False):
            if (foundStart and foundDest):
                return ("", foundStart, foundDest)

            if (root == None):
                return ("", foundStart, foundDest)
            
            if (root.val == destValue):
                foundDest = True
                if (foundStart):
                    return ("", foundStart, foundDest)
                
            if (root.val == startValue):
                foundStart = True
                if (foundDest):
                    return ("", foundStart, foundDest)
            
            if (foundDest and (not foundStart)):
                (ret, foundStart, foundDest) = findDest(root.left, foundStart, foundDest)
                if (foundStart):
                    return (ret + "U", foundStart, foundDest)
                (ret, foundStart, foundDest) = findDest(root.right, foundStart, foundDest)
                if (foundStart):
                    return (ret + "U", foundStart, foundDest)
                return  ("", foundStart, foundDest)

            if (foundStart and (not foundDest)):
                (ret, foundStart, foundDest) = findDest(root.left, foundStart, foundDest)
                if (foundDest):
                    return ("L" + ret, foundStart, foundDest)
                (ret, foundStart, foundDest) = findDest(root.right, foundStart, foundDest)
                if (foundDest):
                    return ("R" + ret, foundStart, foundDest)
                return  ("", foundStart, foundDest)

            if ((not foundDest) and (not foundStart)):
                (l_ret, l_foundStart, l_foundDest) = findDest(root.left, foundStart, foundDest)
                (r_ret, r_foundStart, r_foundDest) = findDest(root.right, foundStart, foundDest)
                ret = ""
                if (l_foundStart and l_foundDest):
                    return (l_ret, l_foundStart, l_foundDest)
                
                if (r_foundStart and r_foundDest):
                    return (r_ret, r_foundStart, r_foundDest)

                if (l_foundStart):
                    ret = l_ret + "U" + ret

                if (r_foundStart):
                    ret = r_ret + "U" + ret 
                
                if (l_foundDest):
                    ret = ret + "L" + l_ret
                
                if (r_foundDest):
                    ret = ret + "R" + r_ret 
                
                return (ret, l_foundStart or r_foundStart, l_foundDest or r_foundDest)  # not found 

            return ("", False, False)  # not found 
        
        ret, _, _ = findDest(root)
        return ret

# Test
root = TreeNode(2, TreeNode(1))
root = TreeNode(5, TreeNode(1, TreeNode(3)), TreeNode(2, TreeNode(6), TreeNode(4)))
s = Solution()

ret = s.getDirections(root, 4, 6)
print(ret)

