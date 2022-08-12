# https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Dict, Optional, Set


class Node:
  def __init__(self, val = 0, neighbors = None):
    self.val = val
    self.neighbors = neighbors if neighbors is not None else []

class Solution:
  def cloneGraph(self, node:Node) -> Node:
    # Constraints: 
    # - Node.val is unique for each node
    # - No repeating edges and no self-loops

    visited:Dict[int, Node] = {}
    def deep_clone(node:Node) -> Optional[Node]:
      if not node:
        return None 

      if node.val in visited:
        return visited[node.val]
      visited[node.val] = Node(node.val, [])
      visited[node.val].neighbors = [ deep_clone(neighbor) for neighbor in node.neighbors]
      return visited[node.val]

    return deep_clone(node)