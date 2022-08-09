# https://leetcode.com/problems/merge-intervals/

from typing import List

class Solution:
  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    
    # O(n log n)
    sorted_inv = sorted(intervals)
    
    ans = []
    n = len(sorted_inv)
    [start_position, end_position] = sorted_inv[0]
    for i in range(1, n):
      (s, e) = sorted_inv[i]
      if s > end_position: 
        ans.append([start_position, end_position])
        start_position, end_position = s, e 
      else: 
        end_position = max(e, end_position) 
    
    ans.append([start_position, end_position])
    return ans 

# [[1,1]]
# [[2, 2], [1, 1]]
# [[1,2], [2,3]]