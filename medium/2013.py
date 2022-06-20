# https://leetcode.com/problems/detect-squares/

from typing import List
from collections import defaultdict

class DetectSquares:
  def __init__(self):
    self.added_points = defaultdict(lambda: 0)
    self.row_points = defaultdict(lambda: 0)
    self.coln_points = defaultdict(lambda: 0)

  def add(self, point: List[int]) -> None:
    self.added_points[(point[0], point[1])] += 1
    self.row_points[point[0]] += 1
    self.coln_points[point[1]] += 1
  
  def count(self, point: List[int]) -> int:
    count:int = 0 
    if (self.row_points[point[0]] > 0 and self.coln_points[point[1]] > 0):
      # Count left 
      for i in range(0, point[1]):
        if self.added_points[(point[0], i)] > 0: 
          width = (point[1] - i)
          # Count upper
          if (point[0] - width >= 0):
            count += self.added_points[(point[0], i)] * self.added_points[(point[0]-width, i)] * self.added_points[(point[0]-width, point[1])]
          # Count below
          if (point[0] + width <= 1000):
            count += self.added_points[(point[0], i)] * self.added_points[(point[0]+width, i)] * self.added_points[(point[0]+width, point[1])]
      # Count right 
      for i in range(point[1]+1, 1001):
        if self.added_points[(point[0], i)] > 0: 
          width = (i - point[1])
          # Count upper
          if (point[0] - width >= 0):
            count += self.added_points[(point[0], i)] * self.added_points[(point[0]-width, i)] * self.added_points[(point[0]-width, point[1])]
          # Count below
          if (point[0] + width <= 1000):
            count += self.added_points[(point[0], i)] * self.added_points[(point[0]+width, i)] * self.added_points[(point[0]+width, point[1])]
    return count


# Your DetectSquares object will be instantiated and called as such:
obj = DetectSquares()
obj.add([3, 10])
obj.add([11, 2])
obj.add([3, 2])
obj.add([11, 2])
param_2 = obj.count([11, 10])
print(param_2)