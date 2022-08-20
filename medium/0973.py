# https://leetcode.com/problems/k-closest-points-to-origin/

from heapq import heapify
import heapq
from typing import List


class Solution:
  def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    n = len(points)
    if k == n:
      return points
    
    def dist(x:int, y:int) -> int:
      return x*x + y*y
      
    ans = [ (dist(x,y), x, y) for [x,y] in points ]
    return [ [x, y] for (_, x, y) in heapq.nsmallest(k, ans)]
    