# https://leetcode.com/contest/weekly-contest-305/problems/reachable-nodes-with-restrictions/

from collections import defaultdict
from typing import List


class Solution:
  def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
    can_go = defaultdict(list)
    for [x, y] in edges:
      can_go[x].append(y)
      can_go[y].append(x)
    set_restricted = set(restricted)

    stk = [0]
    cnt = 0
    visited = set()
    while len(stk) > 0:
      node = stk.pop()
      if node not in set_restricted and node not in visited:
        visited.add(node)
        cnt += 1  # We can visit this node 
        for next_node in can_go[node]:
          stk.append(next_node)
    
    return cnt 

# 7
# [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]]
# [4,5]

s = Solution()
print(s.reachableNodes(7, [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], [4, 5]))
