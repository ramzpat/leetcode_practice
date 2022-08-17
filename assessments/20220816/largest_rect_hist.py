from typing import List


class Solution:
  # O(n^2)
  def largestRectangleArea(self, heights: List[int]) -> int:
    n = len(heights)
    max_val = 0
    for i in range(n):
      sum_val = heights[i]
      min_val = heights[i]
      for j in range(i-1, -1, -1):
        min_val = min(heights[j], min_val)
        if min_val * (i-j+1) > sum_val:
          sum_val = min_val * (i-j+1)
      max_val = max(max_val, sum_val)
    return max_val
   