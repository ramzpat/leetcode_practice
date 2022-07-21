# https://leetcode.com/problems/find-duplicate-subtrees/

# Definition for a binary tree node.
from collections import defaultdict
from typing import Dict, List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
      def inOrderTravel(tree:Optional[TreeNode]) -> List[str]:
        if tree == None:
          return []
        return inOrderTravel(tree.left) + [str(tree.val)] + inOrderTravel(tree.right)
      return ",".join(inOrderTravel(self))

class Solution:
  def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
    hashTree:Dict[int, List[TreeNode]] = defaultdict(list)
    def postOrderTravel(tree:Optional[TreeNode]):
      if tree == None:
        return 'n'
      hashString= str(tree.val) + "."  + postOrderTravel(tree.left) + "." + postOrderTravel(tree.right)  
      hashTree[hashString].append(tree)
      return hashString
    postOrderTravel(root)
    return [((list[0])) for list in hashTree.values() if len(list) > 1]
      
s = Solution()
root =TreeNode(1, TreeNode(2,TreeNode(4)), TreeNode(3, TreeNode(2,TreeNode(4)), TreeNode(4)) )
print(s.findDuplicateSubtrees(root))
