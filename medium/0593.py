# https://leetcode.com/problems/valid-square/


from math import sqrt
from typing import Dict, List, Tuple


class Solution:
  def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
    def dis(p1:List[int], p2:List[int]) -> int:
      return ( pow(p1[0]-p2[0], 2) + pow(p1[1]-p2[1], 2) )
    pointList = sorted([(dis(p1, p), tuple(p)) for p in [p2, p3, p4] ])
    # print(pointList)
    # print(dis(pointList[1][1], pointList[2][1]), dis(pointList[0][1], pointList[2][1]))
    return ((pointList[0][0] == pointList[1][0]) and 
            dis(pointList[0][1], p1) == dis(pointList[0][1], pointList[2][1]) and 
            dis(pointList[1][1], p1) == dis(pointList[1][1], pointList[2][1]) and 
            dis(pointList[1][1], pointList[2][1]) == dis(pointList[0][1], pointList[2][1]) and 
            dis(pointList[2][1], p1) == dis(pointList[0][1], pointList[1][1]) and 
            dis(pointList[2][1], p1) > 0)
s = Solution()
print(s.validSquare([7,7], [5,3], [3,5], [1,1]))