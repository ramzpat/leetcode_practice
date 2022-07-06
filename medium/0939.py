# https://leetcode.com/problems/minimum-area-rectangle/

from typing import List 

class Solution:
  def minAreaRect(self, points: List[List[int]]) -> int:
    seen = set() 
    res = float("inf")
    for [x,y] in points:
      for (x1, y1) in seen:
        if (x1, y) in seen and (x, y1) in seen: 
          area = abs(x1-x) * abs(y1-y)
          if area < res: 
            res = area
      seen.add((x, y))
    return res if res < float('inf') else 0