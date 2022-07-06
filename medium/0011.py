# https://leetcode.com/problems/container-with-most-water/

from typing import List 

class Solution:
  def maxArea(self, height: List[int]) -> int:
    # # Brute force
    # max_area = 0 
    # for i in range(len(height)):
    #   max_area = max([(j-i)*min(height[i], height[j]) for j in range(i+1, len(height))] + [max_area])
    # return max_area
    max_area = 0
    left_index, right_index = 0, len(height)-1
    while(left_index < right_index):      
      max_area = max(max_area, min(height[left_index], height[right_index])*(right_index-left_index))

      # Move inside by moving the less significant height
      if height[left_index] < height[right_index]:
        left_index += 1
      else:
        right_index -= 1
    return max_area
       

s = Solution()
print(s.maxArea(height = [1,8,6,2,5,4,8,3,7]))