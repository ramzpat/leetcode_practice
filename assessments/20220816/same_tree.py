# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    stk_tree:List[Tuple[Optional[TreeNode], Optional[TreeNode]]] = [(p, q)]
      
    while len(stk_tree) > 0:
      (node_a, node_b) = stk_tree.pop()
      if node_a == None and node_b == None:
        pass
      elif node_a == None or node_b == None:
        return False
      elif node_a.val != node_b.val:
        return False
      else:
        stk_tree.append((node_a.left, node_b.left))
        stk_tree.append((node_a.right, node_b.right))
    return True 
  
  
        