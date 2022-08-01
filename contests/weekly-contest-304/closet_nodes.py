# https://leetcode.com/contest/weekly-contest-304/problems/find-closest-node-to-given-two-nodes/
# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/

from collections import defaultdict
from typing import Dict, List, Set, Tuple

class Solution:
  def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:

    travel_cost_1:Dict[int, int] = {node1:0}
    ptr = edges[node1]
    step = 1
    while(ptr != -1 and ptr not in travel_cost_1):
      travel_cost_1[ptr] = step
      ptr = edges[ptr]
      step += 1
      
    travel_cost_2:Dict[int, int] = {node2:0}
    ptr = edges[node2]
    step = 1
    while(ptr != -1 and ptr not in travel_cost_2):
      travel_cost_2[ptr] = step
      ptr = edges[ptr]
      step += 1

    n = len(edges)
    min_index = -1 
    min_val = n + 1
    print(travel_cost_1)
    print(travel_cost_2)
    for i in range(n):
      if (i in travel_cost_1) and (i in travel_cost_2):
        max_distance = max(travel_cost_1[i], travel_cost_2[i])
        if max_distance < min_val:
          min_index = i
          min_val = max_distance

    return min_index
    


s = Solution()

# Input: edges = [2,2,3,-1], node1 = 0, node2 = 1
# Output: 2
print(s.closestMeetingNode(edges = [2,2,3,-1], node1 = 0, node2 = 1))

# Input: edges = [1,2,-1], node1 = 0, node2 = 2
# Output: 2
print(s.closestMeetingNode(edges = [1,2,-1], node1 = 0, node2 = 2))

print(s.closestMeetingNode(edges = [-1,-1,-1], node1 = 0, node2 = 2))

# [4,4,4,5,1,2,2]
# 1
# 1

print(s.closestMeetingNode(edges = [4,4,4,5,1,2,2], node1 = 1, node2 = 1))

# [2,0,0]
# 2, 0
# Out: 0
print(s.closestMeetingNode(edges = [2, 0, 0], node1 = 2, node2 = 0))


# [-1,7,15,15,-1,4,16,2,16,7,11,6,10,4,9,1,14,-1]
# 1, 6
# Out: 7
print(s.closestMeetingNode(edges = [-1,7,15,15,-1,4,16,2,16,7,11,6,10,4,9,1,14,-1], node1 = 1, node2 = 6))

# [4,4,8,-1,9,8,4,4,1,1]
# 5, 6
# Out: 1
print(s.closestMeetingNode(edges = [4,4,8,-1,9,8,4,4,1,1], node1 = 5, node2 = 6))


# [33,24,57,56,45,1,33,61,61,-1,4,69,11,1,44,71,-1,-1,-1,56,7,39,52,47,-1,61,40,42,63,-1,-1,49,-1,-1,53,6,-1,27,-1,14,51,-1,-1,-1,28,-1,8,-1,62,2,33,62,66,45,34,26,79,-1,32,8,56,70,73,6,21,6,0,30,-1,22,52,25,9,68,11,10,6,-1,23,19,2]
# 77 16
# Expect: -1
print(s.closestMeetingNode(edges = [33,24,57,56,45,1,33,61,61,-1,4,69,11,1,44,71,-1,-1,-1,56,7,39,52,47,-1,61,40,42,63,-1,-1,49,-1,-1,53,6,-1,27,-1,14,51,-1,-1,-1,28,-1,8,-1,62,2,33,62,66,45,34,26,79,-1,32,8,56,70,73,6,21,6,0,30,-1,22,52,25,9,68,11,10,6,-1,23,19,2], node1 = 77, node2 = 16))