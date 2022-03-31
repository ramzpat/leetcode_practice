# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/discuss/1612179/Python3-lca

class Solution:
    def getDirections(self, root, startValue, destValue):
        """
        :type root: Optional[TreeNode]
        :type startValue: int
        :type destValue: int
        :rtype: str
        """
        
        def lca(node): 
            """Return lowest common ancestor of start and dest nodes."""
            if not node or node.val in (startValue , destValue): return node 
            left, right = lca(node.left), lca(node.right)
            return node if left and right else left or right
        
        root = lca(root) # only this sub-tree matters
        
        ps = pd = ""
        stack = [(root, "")]
        while stack: 
            node, path = stack.pop()
            if node.val == startValue: ps = path 
            if node.val == destValue: pd = path
            if node.left: stack.append((node.left, path + "L"))
            if node.right: stack.append((node.right, path + "R"))
        return "U"*len(ps) + pd